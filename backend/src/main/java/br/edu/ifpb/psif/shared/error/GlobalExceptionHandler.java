package br.edu.ifpb.psif.shared.error;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.ConstraintViolation;
import jakarta.validation.ConstraintViolationException;
import jakarta.validation.Path;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.MessageSourceResolvable;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ProblemDetail;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.validation.method.ParameterErrors;
import org.springframework.validation.method.ParameterValidationResult;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.context.request.ServletWebRequest;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.method.annotation.HandlerMethodValidationException;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

/**
 * Tratamento centralizado de erros, com todas as respostas no formato {@link ProblemDetail}.
 * <p>
 * Cobre também as exceções tratadas pelo Spring MVC, erros de validação de corpo e de parâmetros
 * e mantém mensagens em português, sem expor detalhe interno em respostas 5xx.
 */
@RestControllerAdvice
public class GlobalExceptionHandler extends ResponseEntityExceptionHandler {

    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    private static final String EXTERNAL_INTEGRATION_MESSAGE = "Falha na integração externa";

    /**
     * Trata erros que já carregam status, título e detalhe.
     *
     * @param exception exceção da categoria
     * @param request requisição atual
     * @return resposta com {@link ProblemDetail}
     */
    @ExceptionHandler(ApiException.class)
    public ResponseEntity<ProblemDetail> handleApiException(ApiException exception, HttpServletRequest request) {
        if (exception instanceof ExternalIntegrationException) {
            log.error(EXTERNAL_INTEGRATION_MESSAGE, exception);
        }

        ProblemDetail problem = ProblemDetailFactory.create(
                exception.getStatus(),
                exception.getTitle(),
                exception.getDetail(),
                request.getRequestURI());

        return ResponseEntity.status(exception.getStatus()).body(problem);
    }

    /**
     * Trata falha de validação de corpo com campos inválidos.
     * <p>
     * Erros de campo vão em {@code fields}; erros globais do DTO entram no detalhe da resposta.
     *
     * @param exception exceção de validação
     * @param headers cabeçalhos da resposta
     * @param status status original
     * @param request requisição atual
     * @return resposta com {@link ProblemDetail}
     */
    @Override
    protected ResponseEntity<Object> handleMethodArgumentNotValid(
            MethodArgumentNotValidException exception,
            HttpHeaders headers,
            HttpStatusCode status,
            WebRequest request) {

        Map<String, String> fields = fieldErrors(exception.getBindingResult().getFieldErrors());
        List<String> globalMessages = messages(exception.getBindingResult().getGlobalErrors());
        ProblemDetail problem = validationProblem(fields, globalMessages);
        ProblemDetailFactory.setInstance(problem, instance(request));

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(problem);
    }

    /**
     * Trata falha de validação de parâmetros de método.
     * <p>
     * Erros de campos do DTO vão em {@code fields}; parâmetros simples usam o nome do parâmetro
     * como chave e erros sem campo utilizável entram no detalhe da resposta.
     *
     * @param exception exceção de validação
     * @param headers cabeçalhos da resposta
     * @param status status original
     * @param request requisição atual
     * @return resposta com {@link ProblemDetail}
     */
    @Override
    protected ResponseEntity<Object> handleHandlerMethodValidationException(
            HandlerMethodValidationException exception,
            HttpHeaders headers,
            HttpStatusCode status,
            WebRequest request) {

        Map<String, String> fields = new LinkedHashMap<>();
        List<String> globalMessages = new ArrayList<>();

        for (ParameterValidationResult result : exception.getParameterValidationResults()) {
            if (result instanceof ParameterErrors parameterErrors) {
                mergeFields(fields, fieldErrors(parameterErrors.getFieldErrors()));
                globalMessages.addAll(messages(parameterErrors.getGlobalErrors()));
                continue;
            }

            String parameterName = parameterName(result);
            for (MessageSourceResolvable error : result.getResolvableErrors()) {
                String message = error.getDefaultMessage();
                if (parameterName == null || message == null || message.isBlank()) {
                    addMessage(globalMessages, message);
                    continue;
                }
                fields.putIfAbsent(parameterName, message);
            }
        }

        globalMessages.addAll(messages(exception.getCrossParameterValidationResults()));

        ProblemDetail problem = validationProblem(fields, globalMessages);
        ProblemDetailFactory.setInstance(problem, instance(request));

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(problem);
    }

    /**
     * Trata falha de validação de parâmetros com {@code @Validated}.
     * <p>
     * Usa apenas o último nó do caminho da violação e trata como erro global quando não há campo
     * utilizável.
     *
     * @param exception exceção de validação
     * @param request requisição atual
     * @return resposta com {@link ProblemDetail}
     */
    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<ProblemDetail> handleConstraintViolation(
            ConstraintViolationException exception,
            HttpServletRequest request) {

        Map<String, String> fields = new LinkedHashMap<>();
        List<String> globalMessages = new ArrayList<>();

        for (ConstraintViolation<?> violation : exception.getConstraintViolations()) {
            String field = lastNode(violation.getPropertyPath());
            if (field == null) {
                addMessage(globalMessages, violation.getMessage());
                continue;
            }
            fields.putIfAbsent(field, violation.getMessage());
        }

        ProblemDetail problem = validationProblem(fields, globalMessages);
        ProblemDetailFactory.setInstance(problem, request.getRequestURI());

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(problem);
    }

    /**
     * Trata qualquer erro não previsto, sem expor detalhe interno.
     *
     * @param exception exceção inesperada
     * @param request requisição atual
     * @return resposta com {@link ProblemDetail}
     */
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ProblemDetail> handleUnexpectedException(Exception exception, HttpServletRequest request) {
        log.error(ProblemDetailFactory.titleFor(HttpStatus.INTERNAL_SERVER_ERROR), exception);

        ProblemDetail problem = ProblemDetailFactory.create(
                HttpStatus.INTERNAL_SERVER_ERROR,
                request.getRequestURI());

        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(problem);
    }

    /**
     * Padroniza as respostas criadas pelo tratamento padrão do Spring MVC.
     * <p>
     * Força tipo, título e detalhe em português, mantém as propriedades já presentes e usa detalhe
     * fixo para 5xx.
     *
     * @param exception exceção original
     * @param body corpo produzido pelo Spring MVC
     * @param headers cabeçalhos da resposta
     * @param status status original
     * @param request requisição atual
     * @return resposta com {@link ProblemDetail}
     */
    @Override
    protected ResponseEntity<Object> handleExceptionInternal(
            Exception exception,
            Object body,
            HttpHeaders headers,
            HttpStatusCode status,
            WebRequest request) {

        Object responseBody = body;
        if (!(responseBody instanceof ProblemDetail) && status.isError()) {
            responseBody = ProblemDetailFactory.create(status, instance(request));
        }

        if (responseBody instanceof ProblemDetail problem) {
            problem.setType(ProblemDetailFactory.TYPE);
            problem.setTitle(ProblemDetailFactory.titleFor(status));
            problem.setDetail(ProblemDetailFactory.detailFor(status));
            ProblemDetailFactory.setInstance(problem, instance(request));
        }

        return super.handleExceptionInternal(exception, responseBody, headers, status, request);
    }

    private ProblemDetail validationProblem(Map<String, String> fields, List<String> globalMessages) {
        return ProblemDetailFactory.validation(fields, validationDetail(globalMessages));
    }

    private String validationDetail(List<String> globalMessages) {
        if (globalMessages.isEmpty()) {
            return ProblemDetailFactory.VALIDATION_DETAIL;
        }

        return ProblemDetailFactory.VALIDATION_DETAIL + " " + String.join(" ", globalMessages);
    }

    private Map<String, String> fieldErrors(List<FieldError> errors) {
        Map<String, String> fields = new LinkedHashMap<>();
        for (FieldError error : errors) {
            String message = error.getDefaultMessage();
            if (message == null || message.isBlank()) {
                continue;
            }
            fields.putIfAbsent(error.getField(), message);
        }
        return fields;
    }

    private List<String> messages(List<? extends MessageSourceResolvable> errors) {
        List<String> messages = new ArrayList<>();
        for (MessageSourceResolvable error : errors) {
            addMessage(messages, error.getDefaultMessage());
        }
        return messages;
    }

    private void addMessage(List<String> messages, String message) {
        if (message == null || message.isBlank()) {
            return;
        }

        messages.add(message);
    }

    private void mergeFields(Map<String, String> target, Map<String, String> source) {
        source.forEach(target::putIfAbsent);
    }

    private String parameterName(ParameterValidationResult result) {
        String name = result.getMethodParameter().getParameterName();
        if (name != null && !name.isBlank()) {
            return name;
        }

        RequestParam requestParam = result.getMethodParameter().getParameterAnnotation(RequestParam.class);
        if (requestParam == null) {
            return null;
        }
        if (!requestParam.name().isBlank()) {
            return requestParam.name();
        }
        if (!requestParam.value().isBlank()) {
            return requestParam.value();
        }

        return null;
    }

    private String lastNode(Path path) {
        String name = null;
        for (Path.Node node : path) {
            if (node.getName() != null && !node.getName().isBlank()) {
                name = node.getName();
            }
        }
        return name;
    }

    private String instance(WebRequest request) {
        if (request instanceof ServletWebRequest servletRequest) {
            return servletRequest.getRequest().getRequestURI();
        }

        return null;
    }
}

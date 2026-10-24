package br.edu.ifpb.psif.shared.error;

import java.util.LinkedHashMap;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ProblemDetail;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import jakarta.validation.ConstraintViolation;
import jakarta.validation.ConstraintViolationException;

/**
 * Tratamento centralizado de erros, com todas as respostas no formato {@link ProblemDetail}.
 */
@RestControllerAdvice
public class GlobalExceptionHandler extends ResponseEntityExceptionHandler {

    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    private static final String VALIDATION_TITLE = "Dados inválidos";
    private static final String VALIDATION_DETAIL = "Verifique os campos informados.";
    private static final String UNEXPECTED_TITLE = "Erro inesperado";
    private static final String UNEXPECTED_DETAIL = "Não foi possível concluir a operação.";
    private static final String EXTERNAL_INTEGRATION_MESSAGE = "Falha na integração externa";
    private static final String FIELDS_PROPERTY = "fields";

    /**
     * Trata erros que já carregam status, título e detalhe.
     *
     * @param exception exceção da categoria
     * @return resposta com {@link ProblemDetail}
     */
    @ExceptionHandler(ApiException.class)
    public ResponseEntity<ProblemDetail> handleApiException(ApiException exception) {
        if (exception instanceof ExternalIntegrationException) {
            log.error(EXTERNAL_INTEGRATION_MESSAGE, exception);
        }

        return problemResponse(exception.getStatus(), exception.getTitle(), exception.getDetail());
    }

    /**
     * Trata falha de validação de corpo com campos inválidos.
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

        Map<String, String> fields = new LinkedHashMap<>();
        for (FieldError error : exception.getBindingResult().getFieldErrors()) {
            fields.putIfAbsent(error.getField(), error.getDefaultMessage());
        }

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(validationProblem(fields));
    }

    /**
     * Trata falha de validação de parâmetros com campos inválidos.
     *
     * @param exception exceção de validação
     * @return resposta com {@link ProblemDetail}
     */
    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<ProblemDetail> handleConstraintViolation(ConstraintViolationException exception) {
        Map<String, String> fields = new LinkedHashMap<>();
        for (ConstraintViolation<?> violation : exception.getConstraintViolations()) {
            fields.putIfAbsent(violation.getPropertyPath().toString(), violation.getMessage());
        }

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(validationProblem(fields));
    }

    /**
     * Trata qualquer erro não previsto, sem expor detalhe interno.
     *
     * @param exception exceção inesperada
     * @return resposta com {@link ProblemDetail}
     */
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ProblemDetail> handleUnexpectedException(Exception exception) {
        log.error(UNEXPECTED_TITLE, exception);

        return problemResponse(HttpStatus.INTERNAL_SERVER_ERROR, UNEXPECTED_TITLE, UNEXPECTED_DETAIL);
    }

    private ProblemDetail validationProblem(Map<String, String> fields) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(HttpStatus.BAD_REQUEST, VALIDATION_DETAIL);
        problem.setTitle(VALIDATION_TITLE);
        problem.setProperty(FIELDS_PROPERTY, fields);
        return problem;
    }

    private ResponseEntity<ProblemDetail> problemResponse(HttpStatus status, String title, String detail) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(status, detail);
        problem.setTitle(title);
        return ResponseEntity.status(status).body(problem);
    }
}

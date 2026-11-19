package br.edu.ifpb.psif.shared.error;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.http.HttpServletRequest;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.webmvc.error.ErrorController;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ProblemDetail;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Trata o encaminhamento para {@code /error} com {@link ProblemDetail}.
 * <p>
 * Cobre erros que não passam pelo {@link GlobalExceptionHandler}, como exceções lançadas em
 * filtros, e reaproveita status, título e detalhe seguros de {@link ApiException}.
 */
@Controller
@RequestMapping("${spring.web.error.path:${error.path:/error}}")
public class ProblemDetailErrorController implements ErrorController {

    private static final Logger log = LoggerFactory.getLogger(ProblemDetailErrorController.class);

    private static final String ERROR_STATUS_CODE = RequestDispatcher.ERROR_STATUS_CODE;
    private static final String ERROR_REQUEST_URI = RequestDispatcher.ERROR_REQUEST_URI;
    private static final String ERROR_EXCEPTION = RequestDispatcher.ERROR_EXCEPTION;
    private static final String EXTERNAL_INTEGRATION_MESSAGE = "Falha na integração externa";

    /**
     * Monta a resposta de erro a partir dos atributos da requisição.
     *
     * @param request requisição encaminhada para o caminho de erro
     * @return resposta com {@link ProblemDetail} ou sem corpo quando não há erro
     */
    @RequestMapping
    public ResponseEntity<ProblemDetail> handleError(HttpServletRequest request) {
        Integer statusCode = statusCode(request);
        if (statusCode == null) {
            return ResponseEntity.noContent().build();
        }

        HttpStatusCode status = HttpStatusCode.valueOf(statusCode);
        if (status.value() == HttpStatus.NO_CONTENT.value()) {
            return ResponseEntity.noContent().build();
        }
        if (status.value() == HttpStatus.NOT_MODIFIED.value()) {
            return ResponseEntity.status(status).build();
        }

        ApiException original = findApiException(request);
        if (original != null) {
            return apiExceptionResponse(original, request);
        }

        if (status.is5xxServerError()) {
            logUnexpectedError(request);
        }

        ProblemDetail problem = ProblemDetailFactory.create(status, instance(request));
        return ResponseEntity.status(status).body(problem);
    }

    private ResponseEntity<ProblemDetail> apiExceptionResponse(ApiException exception, HttpServletRequest request) {
        if (exception instanceof ExternalIntegrationException) {
            log.error(EXTERNAL_INTEGRATION_MESSAGE, exception);
        }

        ProblemDetail problem = ProblemDetailFactory.create(
                exception.getStatus(),
                exception.getTitle(),
                exception.getDetail(),
                instance(request));

        return ResponseEntity.status(exception.getStatus()).body(problem);
    }

    private void logUnexpectedError(HttpServletRequest request) {
        Object error = request.getAttribute(ERROR_EXCEPTION);
        if (error instanceof Throwable throwable) {
            log.error(ProblemDetailFactory.titleFor(HttpStatus.INTERNAL_SERVER_ERROR), throwable);
            return;
        }

        log.error(ProblemDetailFactory.titleFor(HttpStatus.INTERNAL_SERVER_ERROR));
    }

    private ApiException findApiException(HttpServletRequest request) {
        Object error = request.getAttribute(ERROR_EXCEPTION);
        if (!(error instanceof Throwable throwable)) {
            return null;
        }

        Throwable current = throwable;
        while (current != null) {
            if (current instanceof ApiException apiException) {
                return apiException;
            }
            current = current.getCause();
        }

        return null;
    }

    private Integer statusCode(HttpServletRequest request) {
        Object value = request.getAttribute(ERROR_STATUS_CODE);
        if (value instanceof Number number) {
            return number.intValue();
        }
        if (value instanceof String text && !text.isBlank()) {
            return Integer.valueOf(text);
        }

        return null;
    }

    private String instance(HttpServletRequest request) {
        Object uri = request.getAttribute(ERROR_REQUEST_URI);
        if (uri instanceof String text && !text.isBlank()) {
            return text;
        }

        return request.getRequestURI();
    }
}

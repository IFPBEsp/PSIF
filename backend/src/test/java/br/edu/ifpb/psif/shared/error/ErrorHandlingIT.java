package br.edu.ifpb.psif.shared.error;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;

import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Import;
import org.springframework.web.filter.OncePerRequestFilter;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@Import(ErrorHandlingIT.FailingFilterConfiguration.class)
class ErrorHandlingIT {

    private static final String PROBLEM_JSON = "application/problem+json";

    @LocalServerPort
    private int port;

    private final HttpClient client = HttpClient.newHttpClient();

    @Test
    void shouldReturnProblemDetailWhenFilterThrows() throws Exception {
        HttpResponse<String> response = get("/filter-error");

        assertEquals(500, response.statusCode());
        assertEquals(PROBLEM_JSON, contentType(response));
        assertTrue(response.body().contains("\"type\":\"about:blank\""));
        assertTrue(response.body().contains("\"title\":\"Erro inesperado\""));
        assertTrue(response.body().contains("\"detail\":\"Não foi possível concluir a operação.\""));
        assertTrue(response.body().contains("\"instance\":\"/filter-error\""));
        assertNoInternalDetail(response.body());
    }

    @Test
    void shouldReuseSafeApiExceptionThrownInFilter() throws Exception {
        HttpResponse<String> response = get("/filter-api-error");

        assertEquals(404, response.statusCode());
        assertTrue(response.body().contains("\"title\":\"Recurso não encontrado\""));
        assertTrue(response.body().contains("\"detail\":\"Produto não encontrado.\""));
        assertNoInternalDetail(response.body());
    }

    @Test
    void shouldReturnProblemDetailForUnmappedRoute() throws Exception {
        HttpResponse<String> response = get("/rota-inexistente");

        assertEquals(404, response.statusCode());
        assertEquals(PROBLEM_JSON, contentType(response));
        assertTrue(response.body().contains("\"type\":\"about:blank\""));
        assertTrue(response.body().contains("\"title\":\"Recurso não encontrado\""));
        assertTrue(response.body().contains("\"instance\":\"/rota-inexistente\""));
    }

    @Test
    void shouldReturnProblemDetailOnTrace() throws Exception {
        HttpRequest request = HttpRequest.newBuilder(uri("/test/errors/not-found"))
                .method("TRACE", HttpRequest.BodyPublishers.noBody())
                .build();

        HttpResponse<String> response = client.send(
                request,
                HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));

        assertEquals(405, response.statusCode());
        assertEquals(PROBLEM_JSON, contentType(response));
        assertTrue(response.body().contains("\"title\":\"Método não permitido\""));
        assertTrue(response.body().contains("\"instance\":\"/test/errors/not-found\""));
    }

    @Test
    void shouldKeepPortugueseValidationMessageDespiteAcceptLanguage() throws Exception {
        HttpResponse<String> response = post("/test/errors/validation-without-message", "{\"name\": \"\"}");

        assertEquals(400, response.statusCode());
        assertTrue(response.body().contains("\"name\":\"não deve estar em branco\""));
    }

    private HttpResponse<String> get(String path) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder(uri(path)).GET().build();
        return client.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
    }

    private HttpResponse<String> post(String path, String body) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder(uri(path))
                .header("Content-Type", "application/json")
                .header("Accept-Language", "en-US")
                .POST(HttpRequest.BodyPublishers.ofString(body, StandardCharsets.UTF_8))
                .build();

        return client.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
    }

    private URI uri(String path) {
        return URI.create("http://localhost:" + port + path);
    }

    private String contentType(HttpResponse<String> response) {
        return response.headers().firstValue("Content-Type").orElse("");
    }

    private void assertNoInternalDetail(String body) {
        assertFalse(body.contains("detalhe interno"));
        assertFalse(body.contains("IllegalStateException"));
        assertFalse(body.contains("\"trace\""));
        assertFalse(body.contains("\"exception\""));
        assertFalse(body.contains("\"stackTrace\""));
    }

    @TestConfiguration(proxyBeanMethods = false)
    static class FailingFilterConfiguration {

        @Bean
        ErrorTestController errorTestController() {
            return new ErrorTestController();
        }

        @Bean
        ValidatedErrorTestController validatedErrorTestController() {
            return new ValidatedErrorTestController();
        }

        @Bean
        Filter failingFilter() {
            return new OncePerRequestFilter() {

                @Override
                protected void doFilterInternal(
                        HttpServletRequest request,
                        HttpServletResponse response,
                        FilterChain filterChain) throws ServletException, IOException {

                    if ("/filter-error".equals(request.getRequestURI())) {
                        throw new IllegalStateException("detalhe interno");
                    }
                    if ("/filter-api-error".equals(request.getRequestURI())) {
                        throw new ResourceNotFoundException("Produto não encontrado.");
                    }

                    filterChain.doFilter(request, response);
                }
            };
        }
    }
}

package br.edu.ifpb.psif.shared.error;

import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.not;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import jakarta.servlet.ServletException;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

class ProblemDetailErrorControllerTest {

    private static final String STATUS_CODE = "jakarta.servlet.error.status_code";
    private static final String REQUEST_URI = "jakarta.servlet.error.request_uri";
    private static final String EXCEPTION = "jakarta.servlet.error.exception";

    private MockMvc mockMvc;

    @BeforeEach
    void setUp() {
        mockMvc = MockMvcBuilders.standaloneSetup(new ProblemDetailErrorController())
                .addPlaceholderValue("spring.web.error.path", "/error")
                .build();
    }

    @Test
    void shouldReturn500WithoutInternalDetail() throws Exception {
        ResultActions result = mockMvc.perform(get("/error")
                .requestAttr(STATUS_CODE, 500)
                .requestAttr(REQUEST_URI, "/pedidos/1")
                .requestAttr(EXCEPTION, new IllegalStateException("detalhe interno")));

        assertProblem(result, 500, "Erro inesperado", "Não foi possível concluir a operação.", "/pedidos/1");
        assertNoInternalDetail(result);
    }

    @Test
    void shouldReuseSafeApiException() throws Exception {
        ResultActions result = mockMvc.perform(get("/error")
                .requestAttr(STATUS_CODE, 502)
                .requestAttr(REQUEST_URI, "/pedidos/1")
                .requestAttr(EXCEPTION, new ExternalIntegrationException(
                        "Serviço indisponível.",
                        new IllegalStateException("detalhe interno"))));

        assertProblem(result, 502, "Falha na integração externa", "Serviço indisponível.", "/pedidos/1");
        assertNoInternalDetail(result);
    }

    @Test
    void shouldUnwrapApiExceptionCause() throws Exception {
        ResultActions result = mockMvc.perform(get("/error")
                .requestAttr(STATUS_CODE, 500)
                .requestAttr(REQUEST_URI, "/produtos/1")
                .requestAttr(EXCEPTION, new ServletException(
                        new ResourceNotFoundException("Produto não encontrado."))));

        assertProblem(result, 404, "Recurso não encontrado", "Produto não encontrado.", "/produtos/1");
    }

    @Test
    void shouldReturnGenericDetailForNotFound() throws Exception {
        ResultActions result = mockMvc.perform(get("/error")
                .requestAttr(STATUS_CODE, 404)
                .requestAttr(REQUEST_URI, "/rota-inexistente"));

        assertProblem(result, 404, "Recurso não encontrado",
                "O recurso solicitado não foi encontrado.", "/rota-inexistente");
    }

    @Test
    void shouldReturnMethodNotAllowed() throws Exception {
        ResultActions result = mockMvc.perform(get("/error")
                .requestAttr(STATUS_CODE, 405)
                .requestAttr(REQUEST_URI, "/pedidos"));

        assertProblem(result, 405, "Método não permitido",
                "O método HTTP não é suportado para este recurso.", "/pedidos");
    }

    @Test
    void shouldReturn204WhenStatusIsMissing() throws Exception {
        mockMvc.perform(get("/error"))
                .andExpect(status().isNoContent())
                .andExpect(content().string(""));
    }

    @Test
    void shouldReturn204WhenStatusIsNoContent() throws Exception {
        mockMvc.perform(get("/error").requestAttr(STATUS_CODE, 204))
                .andExpect(status().isNoContent())
                .andExpect(content().string(""));
    }

    private ResultActions assertProblem(
            ResultActions result,
            int status,
            String title,
            String detail,
            String instance) throws Exception {

        return result
                .andExpect(status().is(status))
                .andExpect(content().contentType(MediaType.APPLICATION_PROBLEM_JSON))
                .andExpect(jsonPath("$.type").value("about:blank"))
                .andExpect(jsonPath("$.status").value(status))
                .andExpect(jsonPath("$.title").value(title))
                .andExpect(jsonPath("$.detail").value(detail))
                .andExpect(jsonPath("$.instance").value(instance));
    }

    private void assertNoInternalDetail(ResultActions result) throws Exception {
        result.andExpect(jsonPath("$.trace").doesNotExist())
                .andExpect(jsonPath("$.exception").doesNotExist())
                .andExpect(jsonPath("$.stackTrace").doesNotExist())
                .andExpect(content().string(not(containsString("detalhe interno"))))
                .andExpect(content().string(not(containsString("IllegalStateException"))))
                .andExpect(content().string(not(containsString("at br."))));
    }
}

package br.edu.ifpb.psif.shared.error;

import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.not;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.validation.Validator;
import org.springframework.validation.beanvalidation.LocalValidatorFactoryBean;

class GlobalExceptionHandlerTest {

    private MockMvc mockMvc;

    @BeforeEach
    void setUp() {
        mockMvc = MockMvcBuilders.standaloneSetup(new ErrorTestController())
                .setControllerAdvice(new GlobalExceptionHandler())
                .setValidator(validator())
                .build();
    }

    @Test
    void shouldReturn400WithInvalidFields() throws Exception {
        mockMvc.perform(post("/test/errors/validation")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"name": ""}
                                """))
                .andExpect(status().isBadRequest())
                .andExpect(jsonPath("$.status").value(400))
                .andExpect(jsonPath("$.title").value("Dados inválidos"))
                .andExpect(jsonPath("$.detail").value("Verifique os campos informados."))
                .andExpect(jsonPath("$.fields.name").value("Nome é obrigatório."));
    }

    @Test
    void shouldReturn404WhenResourceIsMissing() throws Exception {
        mockMvc.perform(get("/test/errors/not-found"))
                .andExpect(status().isNotFound())
                .andExpect(jsonPath("$.status").value(404))
                .andExpect(jsonPath("$.title").value("Recurso não encontrado"))
                .andExpect(jsonPath("$.detail").value("Produto não encontrado."))
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn401WhenRequestIsNotAuthenticated() throws Exception {
        mockMvc.perform(get("/test/errors/unauthorized"))
                .andExpect(status().isUnauthorized())
                .andExpect(jsonPath("$.status").value(401))
                .andExpect(jsonPath("$.title").value("Não autenticado"))
                .andExpect(jsonPath("$.detail").value("Sessão expirada."))
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn403WhenAccessIsDenied() throws Exception {
        mockMvc.perform(get("/test/errors/forbidden"))
                .andExpect(status().isForbidden())
                .andExpect(jsonPath("$.status").value(403))
                .andExpect(jsonPath("$.title").value("Acesso negado"))
                .andExpect(jsonPath("$.detail").value("Sem permissão para acessar o recurso."))
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn409WhenOperationConflicts() throws Exception {
        mockMvc.perform(get("/test/errors/conflict"))
                .andExpect(status().isConflict())
                .andExpect(jsonPath("$.status").value(409))
                .andExpect(jsonPath("$.title").value("Conflito"))
                .andExpect(jsonPath("$.detail").value("Registro já cadastrado."))
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn422WhenBusinessRuleIsViolated() throws Exception {
        mockMvc.perform(get("/test/errors/business-rule"))
                .andExpect(status().isUnprocessableContent())
                .andExpect(jsonPath("$.status").value(422))
                .andExpect(jsonPath("$.title").value("Regra de negócio violada"))
                .andExpect(jsonPath("$.detail").value("Operação não permitida para o registro."))
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn502WithoutInternalDetailOnExternalIntegrationFailure() throws Exception {
        mockMvc.perform(get("/test/errors/integration"))
                .andExpect(status().isBadGateway())
                .andExpect(jsonPath("$.status").value(502))
                .andExpect(jsonPath("$.title").value("Falha na integração externa"))
                .andExpect(jsonPath("$.detail").value("Serviço indisponível."))
                .andExpect(content().string(not(containsString("detalhe interno"))))
                .andExpect(content().string(not(containsString("IllegalStateException"))));
    }

    @Test
    void shouldHideInternalDetailOnUnexpectedError() throws Exception {
        mockMvc.perform(get("/test/errors/unexpected"))
                .andExpect(status().isInternalServerError())
                .andExpect(jsonPath("$.status").value(500))
                .andExpect(jsonPath("$.title").value("Erro inesperado"))
                .andExpect(jsonPath("$.detail").value("Não foi possível concluir a operação."))
                .andExpect(content().string(not(containsString("detalhe interno"))))
                .andExpect(content().string(not(containsString("IllegalStateException"))));
    }

    private Validator validator() {
        LocalValidatorFactoryBean validator = new LocalValidatorFactoryBean();
        validator.afterPropertiesSet();
        return validator;
    }
}

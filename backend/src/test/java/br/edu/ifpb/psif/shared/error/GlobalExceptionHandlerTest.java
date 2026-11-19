package br.edu.ifpb.psif.shared.error;

import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.not;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.request;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import java.util.Locale;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.aop.framework.ProxyFactory;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.validation.beanvalidation.LocalValidatorFactoryBean;
import org.springframework.validation.beanvalidation.MethodValidationInterceptor;
import org.springframework.web.servlet.i18n.FixedLocaleResolver;

class GlobalExceptionHandlerTest {

    private static final String TITLE_VALIDATION = "Dados inválidos";
    private static final String DETAIL_VALIDATION = "Verifique os campos informados.";
    private static final String DETAIL_INVALID_REQUEST = "A requisição é inválida.";

    private MockMvc mockMvc;

    @BeforeEach
    void setUp() {
        mockMvc = MockMvcBuilders.standaloneSetup(new ErrorTestController(), validatedController())
                .setControllerAdvice(new GlobalExceptionHandler())
                .setValidator(validator())
                .setLocaleResolver(new FixedLocaleResolver(Locale.forLanguageTag("pt-BR")))
                .build();
    }

    @Test
    void shouldReturn400WithInvalidFields() throws Exception {
        ResultActions result = mockMvc.perform(post("/test/errors/validation")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                        {"name": ""}
                        """));

        assertProblem(result, 400, TITLE_VALIDATION, DETAIL_VALIDATION, "/test/errors/validation")
                .andExpect(jsonPath("$.fields.name").value("Nome é obrigatório."));
    }

    @Test
    void shouldIncludeGlobalErrorsInDetail() throws Exception {
        ResultActions result = mockMvc.perform(post("/test/errors/global-validation")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                        {"password": "abc", "confirmation": "def"}
                        """));

        assertProblem(result, 400, TITLE_VALIDATION,
                DETAIL_VALIDATION + " As senhas não conferem.", "/test/errors/global-validation")
                .andExpect(jsonPath("$.fields").isEmpty());
    }

    @Test
    void shouldReturn400WhenJsonIsMalformed() throws Exception {
        ResultActions result = mockMvc.perform(post("/test/errors/validation")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"name\":"));

        assertProblem(result, 400, TITLE_VALIDATION, DETAIL_INVALID_REQUEST, "/test/errors/validation");
    }

    @Test
    void shouldReturn400WhenPathParameterHasInvalidType() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/type/abc"));

        assertProblem(result, 400, TITLE_VALIDATION, DETAIL_INVALID_REQUEST, "/test/errors/type/abc");
    }

    @Test
    void shouldReturn400WhenRequiredParameterIsMissing() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/required"));

        assertProblem(result, 400, TITLE_VALIDATION, DETAIL_INVALID_REQUEST, "/test/errors/required");
    }

    @Test
    void shouldReturn400WithFieldsOnHandlerMethodValidation() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/method-validation").param("page", "0"));

        assertProblem(result, 400, TITLE_VALIDATION, DETAIL_VALIDATION, "/test/errors/method-validation")
                .andExpect(jsonPath("$.fields.page").value("deve ser maior que ou igual à 1"));
    }

    @Test
    void shouldReturn400WithLastPathNodeOnConstraintViolation() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/validated").param("page", "0"));

        assertProblem(result, 400, TITLE_VALIDATION, DETAIL_VALIDATION, "/test/errors/validated")
                .andExpect(jsonPath("$.fields.page").value("deve ser maior que ou igual à 1"))
                .andExpect(jsonPath("$.fields['validated.page']").doesNotExist());
    }

    @Test
    void shouldUsePortugueseMessageWhenMessageIsOmitted() throws Exception {
        ResultActions result = mockMvc.perform(post("/test/errors/validation-without-message")
                .header("Accept-Language", "en-US")
                .contentType(MediaType.APPLICATION_JSON)
                .content("""
                        {"name": ""}
                        """));

        assertProblem(result, 400, TITLE_VALIDATION, DETAIL_VALIDATION, "/test/errors/validation-without-message")
                .andExpect(jsonPath("$.fields.name").value("não deve estar em branco"));
    }

    @Test
    void shouldReturn404WhenResourceIsMissing() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/not-found"));

        assertProblem(result, 404, "Recurso não encontrado", "Produto não encontrado.", "/test/errors/not-found")
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn401WhenRequestIsNotAuthenticated() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/unauthorized"));

        assertProblem(result, 401, "Não autenticado", "Sessão expirada.", "/test/errors/unauthorized")
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn403WhenAccessIsDenied() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/forbidden"));

        assertProblem(result, 403, "Acesso negado", "Sem permissão para acessar o recurso.",
                "/test/errors/forbidden")
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn409WhenOperationConflicts() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/conflict"));

        assertProblem(result, 409, "Conflito", "Registro já cadastrado.", "/test/errors/conflict")
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn422WhenBusinessRuleIsViolated() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/business-rule"));

        assertProblem(result, 422, "Regra de negócio violada", "Operação não permitida para o registro.",
                "/test/errors/business-rule")
                .andExpect(jsonPath("$.fields").doesNotExist());
    }

    @Test
    void shouldReturn502WithoutInternalDetailOnExternalIntegrationFailure() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/integration"));

        assertProblem(result, 502, "Falha na integração externa", "Serviço indisponível.",
                "/test/errors/integration");
        assertNoInternalDetail(result);
    }

    @Test
    void shouldReturn405WhenMethodIsNotSupported() throws Exception {
        ResultActions result = mockMvc.perform(request(HttpMethod.POST, "/test/errors/not-found"));

        assertProblem(result, 405, "Método não permitido", "O método HTTP não é suportado para este recurso.",
                "/test/errors/not-found");
    }

    @Test
    void shouldReturn406WhenResponseFormatIsNotAcceptable() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/ok")
                .accept(MediaType.APPLICATION_XML));

        assertProblem(result, 406, "Formato não aceito",
                "O formato de resposta solicitado não é suportado.", "/test/errors/ok");
    }

    @Test
    void shouldReturn415WhenMediaTypeIsNotSupported() throws Exception {
        ResultActions result = mockMvc.perform(post("/test/errors/validation")
                .contentType(MediaType.TEXT_PLAIN)
                .content("{}"));

        assertProblem(result, 415, "Formato não suportado", "O formato de dados enviado não é suportado.",
                "/test/errors/validation");
    }

    @Test
    void shouldReturn503WithFixedDetailOnResponseStatusException() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/response-status"));

        assertProblem(result, 503, "Serviço indisponível",
                "O serviço está temporariamente indisponível. Tente novamente mais tarde.",
                "/test/errors/response-status")
                .andExpect(content().string(not(containsString("detalhe interno"))));
    }

    @Test
    void shouldHideInternalDetailOnUnexpectedError() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/unexpected"));

        assertProblem(result, 500, "Erro inesperado", "Não foi possível concluir a operação.",
                "/test/errors/unexpected");
        assertNoInternalDetail(result);
    }

    @Test
    void shouldHideInternalDetailOnCheckedException() throws Exception {
        ResultActions result = mockMvc.perform(get("/test/errors/unexpected-checked"));

        assertProblem(result, 500, "Erro inesperado", "Não foi possível concluir a operação.",
                "/test/errors/unexpected-checked");
        assertNoInternalDetail(result);
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
                .andExpect(content().string(not(containsString("IOException"))))
                .andExpect(content().string(not(containsString("at br."))));
    }

    private Object validatedController() {
        ProxyFactory proxyFactory = new ProxyFactory(new ValidatedErrorTestController());
        proxyFactory.setProxyTargetClass(true);
        proxyFactory.addAdvice(new MethodValidationInterceptor((jakarta.validation.ValidatorFactory) validator()));
        return proxyFactory.getProxy();
    }

    private LocalValidatorFactoryBean validator() {
        LocalValidatorFactoryBean validator = new LocalValidatorFactoryBean();
        validator.afterPropertiesSet();
        return validator;
    }
}

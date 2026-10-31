package br.edu.ifpb.psif.shared.error;

import java.net.URI;
import java.util.LinkedHashMap;
import java.util.Map;

import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ProblemDetail;

/**
 * Centraliza a criação de {@link ProblemDetail} com título e detalhe em português.
 */
public final class ProblemDetailFactory {

    /**
     * Tipo padrão das respostas de erro.
     */
    public static final URI TYPE = URI.create("about:blank");

    /**
     * Nome da propriedade que carrega os erros de campo na validação.
     */
    public static final String FIELDS_PROPERTY = "fields";

    /**
     * Título das respostas de validação.
     */
    public static final String VALIDATION_TITLE = "Dados inválidos";

    /**
     * Detalhe padrão das respostas de validação.
     */
    public static final String VALIDATION_DETAIL = "Verifique os campos informados.";

    private static final String UNEXPECTED_TITLE = "Erro inesperado";
    private static final String UNEXPECTED_DETAIL = "Não foi possível concluir a operação.";
    private static final String INVALID_REQUEST_TITLE = "Requisição inválida";
    private static final String INVALID_REQUEST_DETAIL = "Não foi possível processar a requisição.";

    private static final Map<Integer, String> TITLES = Map.ofEntries(
            Map.entry(400, VALIDATION_TITLE),
            Map.entry(401, "Não autenticado"),
            Map.entry(403, "Acesso negado"),
            Map.entry(404, "Recurso não encontrado"),
            Map.entry(405, "Método não permitido"),
            Map.entry(406, "Formato não aceito"),
            Map.entry(409, "Conflito"),
            Map.entry(415, "Formato não suportado"),
            Map.entry(422, "Regra de negócio violada"),
            Map.entry(500, UNEXPECTED_TITLE),
            Map.entry(502, "Falha na integração externa"),
            Map.entry(503, "Serviço indisponível"));

    private static final Map<Integer, String> DETAILS = Map.ofEntries(
            Map.entry(400, "A requisição é inválida."),
            Map.entry(401, "Autenticação necessária."),
            Map.entry(403, "Você não tem permissão para acessar este recurso."),
            Map.entry(404, "O recurso solicitado não foi encontrado."),
            Map.entry(405, "O método HTTP não é suportado para este recurso."),
            Map.entry(406, "O formato de resposta solicitado não é suportado."),
            Map.entry(409, "A operação conflita com o estado atual do recurso."),
            Map.entry(415, "O formato de dados enviado não é suportado."),
            Map.entry(422, "A operação viola uma regra de negócio."),
            Map.entry(500, UNEXPECTED_DETAIL),
            Map.entry(502, UNEXPECTED_DETAIL),
            Map.entry(503, "O serviço está temporariamente indisponível. Tente novamente mais tarde."));

    private ProblemDetailFactory() {
    }

    /**
     * Cria um problema com título e detalhe definidos pelo status.
     *
     * @param status status HTTP da resposta
     * @return problema formatado
     */
    public static ProblemDetail create(HttpStatusCode status) {
        return create(status, null);
    }

    /**
     * Cria um problema com título e detalhe definidos pelo status e com a instância informada.
     *
     * @param status status HTTP da resposta
     * @param instance caminho da requisição original, pode ser nulo
     * @return problema formatado
     */
    public static ProblemDetail create(HttpStatusCode status, String instance) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(status, detailFor(status));
        problem.setType(TYPE);
        problem.setTitle(titleFor(status));
        setInstance(problem, instance);
        return problem;
    }

    /**
     * Cria um problema com título e detalhe informados.
     *
     * @param status status HTTP da resposta
     * @param title título do problema
     * @param detail detalhe seguro para o usuário
     * @param instance caminho da requisição original, pode ser nulo
     * @return problema formatado
     */
    public static ProblemDetail create(HttpStatusCode status, String title, String detail, String instance) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(status, detail);
        problem.setType(TYPE);
        problem.setTitle(title);
        setInstance(problem, instance);
        return problem;
    }

    /**
     * Cria um problema de validação com o detalhe padrão.
     *
     * @param fields erros de campo indexados pelo nome do campo
     * @return problema de validação
     */
    public static ProblemDetail validation(Map<String, String> fields) {
        return validation(fields, VALIDATION_DETAIL);
    }

    /**
     * Cria um problema de validação com o detalhe informado.
     *
     * @param fields erros de campo indexados pelo nome do campo
     * @param detail detalhe da resposta
     * @return problema de validação
     */
    public static ProblemDetail validation(Map<String, String> fields, String detail) {
        ProblemDetail problem = ProblemDetail.forStatusAndDetail(HttpStatus.BAD_REQUEST, detail);
        problem.setType(TYPE);
        problem.setTitle(VALIDATION_TITLE);
        problem.setProperty(FIELDS_PROPERTY, new LinkedHashMap<>(fields));
        return problem;
    }

    /**
     * Define a instância do problema quando o caminho informado é utilizável.
     *
     * @param problem problema que receberá a instância
     * @param instance caminho da requisição original, pode ser nulo ou vazio
     */
    public static void setInstance(ProblemDetail problem, String instance) {
        if (instance == null || instance.isBlank()) {
            return;
        }

        problem.setInstance(URI.create(instance));
    }

    /**
     * Retorna o título em português para o status.
     *
     * @param status status HTTP da resposta
     * @return título do problema
     */
    public static String titleFor(HttpStatusCode status) {
        return TITLES.getOrDefault(status.value(), fallbackTitle(status.value()));
    }

    /**
     * Retorna o detalhe em português para o status.
     *
     * @param status status HTTP da resposta
     * @return detalhe seguro para o usuário
     */
    public static String detailFor(HttpStatusCode status) {
        return DETAILS.getOrDefault(status.value(), fallbackDetail(status.value()));
    }

    private static String fallbackTitle(int status) {
        return status >= 500 ? UNEXPECTED_TITLE : INVALID_REQUEST_TITLE;
    }

    private static String fallbackDetail(int status) {
        return status >= 500 ? UNEXPECTED_DETAIL : INVALID_REQUEST_DETAIL;
    }
}

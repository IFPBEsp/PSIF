package br.edu.ifpb.psif.shared.error;

import org.springframework.http.HttpStatus;

/**
 * Exceção base para erros que já nascem com status HTTP, título e detalhe definidos.
 */
public abstract class ApiException extends RuntimeException {

    private final HttpStatus status;
    private final String title;

    /**
     * Cria a exceção com status, título e detalhe.
     *
     * @param status status HTTP da resposta
     * @param title título do problema
     * @param detail detalhe seguro para o usuário
     */
    protected ApiException(HttpStatus status, String title, String detail) {
        super(detail);
        this.status = status;
        this.title = title;
    }

    /**
     * Cria a exceção com status, título, detalhe e causa.
     *
     * @param status status HTTP da resposta
     * @param title título do problema
     * @param detail detalhe seguro para o usuário
     * @param cause causa original do erro
     */
    protected ApiException(HttpStatus status, String title, String detail, Throwable cause) {
        super(detail, cause);
        this.status = status;
        this.title = title;
    }

    /**
     * Retorna o status HTTP da resposta.
     *
     * @return status HTTP
     */
    public HttpStatus getStatus() {
        return status;
    }

    /**
     * Retorna o título do problema.
     *
     * @return título do problema
     */
    public String getTitle() {
        return title;
    }

    /**
     * Retorna o detalhe seguro para o usuário.
     *
     * @return detalhe do problema
     */
    public String getDetail() {
        return getMessage();
    }
}

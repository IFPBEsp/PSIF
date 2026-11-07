package br.edu.ifpb.psif.shared.error;

import org.springframework.http.HttpStatus;

/**
 * Erro para falha em integração externa.
 */
public class ExternalIntegrationException extends ApiException {

    /**
     * Cria o erro com status 502.
     *
     * @param detail detalhe seguro para o usuário
     * @param cause causa original do erro
     */
    public ExternalIntegrationException(String detail, Throwable cause) {
        super(HttpStatus.BAD_GATEWAY, "Falha na integração externa", detail, cause);
    }
}

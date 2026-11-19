package br.edu.ifpb.psif.shared.error;

import org.springframework.http.HttpStatus;

/**
 * Erro para usuário autenticado sem permissão.
 */
public class ForbiddenException extends ApiException {

    /**
     * Cria o erro com status 403.
     *
     * @param detail detalhe seguro para o usuário
     */
    public ForbiddenException(String detail) {
        super(HttpStatus.FORBIDDEN, "Acesso negado", detail);
    }
}

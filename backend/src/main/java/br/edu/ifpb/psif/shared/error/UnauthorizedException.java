package br.edu.ifpb.psif.shared.error;

import org.springframework.http.HttpStatus;

/**
 * Erro para requisição sem autenticação válida.
 */
public class UnauthorizedException extends ApiException {

    /**
     * Cria o erro com status 401.
     *
     * @param detail detalhe seguro para o usuário
     */
    public UnauthorizedException(String detail) {
        super(HttpStatus.UNAUTHORIZED, "Não autenticado", detail);
    }
}

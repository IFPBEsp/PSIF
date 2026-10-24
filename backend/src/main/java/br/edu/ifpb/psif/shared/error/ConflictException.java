package br.edu.ifpb.psif.shared.error;

import org.springframework.http.HttpStatus;

/**
 * Erro para operação que conflita com o estado atual.
 */
public class ConflictException extends ApiException {

    /**
     * Cria o erro com status 409.
     *
     * @param detail detalhe seguro para o usuário
     */
    public ConflictException(String detail) {
        super(HttpStatus.CONFLICT, "Conflito", detail);
    }
}

package br.edu.ifpb.psif.shared.error;

import org.springframework.http.HttpStatus;

/**
 * Erro para recurso inexistente.
 */
public class ResourceNotFoundException extends ApiException {

    /**
     * Cria o erro com status 404.
     *
     * @param detail detalhe seguro para o usuário
     */
    public ResourceNotFoundException(String detail) {
        super(HttpStatus.NOT_FOUND, "Recurso não encontrado", detail);
    }
}

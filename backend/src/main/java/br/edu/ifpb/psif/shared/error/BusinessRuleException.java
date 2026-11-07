package br.edu.ifpb.psif.shared.error;

import org.springframework.http.HttpStatus;

/**
 * Erro para violação de regra de negócio.
 */
public class BusinessRuleException extends ApiException {

    /**
     * Cria o erro com status 422.
     *
     * @param detail detalhe seguro para o usuário
     */
    public BusinessRuleException(String detail) {
        super(HttpStatus.UNPROCESSABLE_CONTENT, "Regra de negócio violada", detail);
    }
}

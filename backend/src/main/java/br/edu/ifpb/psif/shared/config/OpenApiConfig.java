package br.edu.ifpb.psif.shared.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

/**
 * Configuração da documentação OpenAPI, ativa apenas no perfil dev.
 */
@Configuration
@Profile("dev")
public class OpenApiConfig {

    /**
     * Define as informações gerais da API.
     *
     * @return a especificação OpenAPI com título, descrição e versão.
     */
    @Bean
    public OpenAPI openApi() {
        return new OpenAPI()
                .info(new Info()
                        .title("PSIF API")
                        .description("API do Sistema de Atendimento Psicopedagógico do IFPB Campus Esperança")
                        .version("0.0.1-SNAPSHOT"));
    }
}

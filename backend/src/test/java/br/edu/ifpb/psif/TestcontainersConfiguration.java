package br.edu.ifpb.psif;

import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.boot.testcontainers.service.connection.ServiceConnection;
import org.springframework.context.annotation.Bean;
import org.testcontainers.postgresql.PostgreSQLContainer;

/**
 * Configuração do Testcontainers para PostgreSQL compartilhada entre os testes de integração.
 */
@TestConfiguration(proxyBeanMethods = false)
public class TestcontainersConfiguration {

    /**
     * Provê a instância do contêiner PostgreSQL conectada ao contexto Spring Boot.
     *
     * @return o contêiner PostgreSQL configurado
     */
    @Bean
    @ServiceConnection
    public PostgreSQLContainer postgresContainer() {
        return new PostgreSQLContainer("postgres:17-alpine");
    }
}

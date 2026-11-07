package br.edu.ifpb.psif;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.sql.DataSource;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.annotation.Import;

import static org.assertj.core.api.Assertions.assertThat;

/**
 * Testes de integracao da camada de persistencia e migracoes com Liquibase.
 */
@SpringBootTest
@Import(TestcontainersConfiguration.class)
class PersistenceIT {

    @Autowired
    private DataSource dataSource;

    @Test
    void shouldConnectToDatabase() throws SQLException {
        try (Connection connection = dataSource.getConnection()) {
            assertThat(connection.isValid(1)).isTrue();
        }
    }

    @Test
    void shouldCreateLiquibaseControlTables() throws SQLException {
        try (Connection connection = dataSource.getConnection();
             Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(
                     "SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public' AND table_name IN ('databasechangelog', 'databasechangeloglock')")) {
            assertThat(resultSet.next()).isTrue();
            assertThat(resultSet.getInt(1)).isEqualTo(2);
        }
    }
}

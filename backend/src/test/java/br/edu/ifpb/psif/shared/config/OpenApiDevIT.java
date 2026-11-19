package br.edu.ifpb.psif.shared.config;

import br.edu.ifpb.psif.TestcontainersConfiguration;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.webmvc.test.autoconfigure.AutoConfigureMockMvc;
import org.springframework.context.annotation.Import;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.not;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * Testes de integração para verificar a documentação OpenAPI no perfil dev.
 */
@SpringBootTest
@Import(TestcontainersConfiguration.class)
@AutoConfigureMockMvc
@ActiveProfiles("dev")
class OpenApiDevIT {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void shouldReturnOpenApiSpecInDevProfile() throws Exception {
        mockMvc.perform(get("/v3/api-docs"))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$.openapi").exists())
                .andExpect(jsonPath("$.info.title", is("PSIF API")))
                .andExpect(jsonPath("$.info.description", is("API do Sistema de Atendimento Psicopedagógico do IFPB Campus Esperança")))
                .andExpect(jsonPath("$.info.version", is("0.0.1-SNAPSHOT")))
                .andExpect(content().string(not(containsString("password"))))
                .andExpect(content().string(not(containsString("secret"))));
    }

    @Test
    void shouldReturnSwaggerUiInDevProfile() throws Exception {
        mockMvc.perform(get("/swagger-ui.html"))
                .andExpect(status().is3xxRedirection());
        mockMvc.perform(get("/swagger-ui/index.html"))
                .andExpect(status().isOk());
    }
}

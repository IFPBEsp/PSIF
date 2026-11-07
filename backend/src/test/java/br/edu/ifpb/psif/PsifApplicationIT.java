package br.edu.ifpb.psif;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.webmvc.test.autoconfigure.AutoConfigureMockMvc;
import org.springframework.context.annotation.Import;
import org.springframework.test.web.servlet.MockMvc;

@SpringBootTest
@AutoConfigureMockMvc
@Import(TestcontainersConfiguration.class)
class PsifApplicationIT {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void shouldLoadApplicationContext() {
    }

    @Test
    void shouldNotExposeErrorTestRoutes() throws Exception {
        mockMvc.perform(get("/test/errors/ok"))
                .andExpect(status().isNotFound())
                .andExpect(jsonPath("$.type").value("about:blank"))
                .andExpect(jsonPath("$.title").value("Recurso não encontrado"))
                .andExpect(jsonPath("$.instance").value("/test/errors/ok"));
    }
}

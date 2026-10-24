package br.edu.ifpb.psif.shared.error;

import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/test/errors")
class ErrorTestController {

    @GetMapping("/not-found")
    void notFound() {
        throw new ResourceNotFoundException("Produto não encontrado.");
    }

    @GetMapping("/unauthorized")
    void unauthorized() {
        throw new UnauthorizedException("Sessão expirada.");
    }

    @GetMapping("/forbidden")
    void forbidden() {
        throw new ForbiddenException("Sem permissão para acessar o recurso.");
    }

    @GetMapping("/conflict")
    void conflict() {
        throw new ConflictException("Registro já cadastrado.");
    }

    @GetMapping("/business-rule")
    void businessRule() {
        throw new BusinessRuleException("Operação não permitida para o registro.");
    }

    @GetMapping("/integration")
    void integration() {
        throw new ExternalIntegrationException("Serviço indisponível.", new IllegalStateException("detalhe interno"));
    }

    @GetMapping("/unexpected")
    void unexpected() {
        throw new IllegalStateException("detalhe interno");
    }

    @PostMapping("/validation")
    void validation(@Valid @RequestBody ValidationRequest request) {
    }

    record ValidationRequest(@NotBlank(message = "Nome é obrigatório.") String name) {
    }
}

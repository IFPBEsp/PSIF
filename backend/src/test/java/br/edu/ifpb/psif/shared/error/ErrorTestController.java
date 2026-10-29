package br.edu.ifpb.psif.shared.error;

import java.io.IOException;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.util.Objects;

import jakarta.validation.Constraint;
import jakarta.validation.ConstraintValidator;
import jakarta.validation.ConstraintValidatorContext;
import jakarta.validation.Payload;
import jakarta.validation.Valid;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;

import org.springframework.context.annotation.Profile;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.server.ResponseStatusException;

@Controller
@Profile("error-test-fixtures")
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

    @GetMapping("/unexpected-checked")
    void unexpectedChecked() throws IOException {
        throw new IOException("detalhe interno");
    }

    @GetMapping("/response-status")
    void responseStatus() {
        throw new ResponseStatusException(HttpStatus.SERVICE_UNAVAILABLE, "detalhe interno");
    }

    @GetMapping("/ok")
    ResponseEntity<OkResponse> ok() {
        return ResponseEntity.ok(new OkResponse("ok"));
    }

    @GetMapping("/type/{id}")
    void type(@PathVariable Integer id) {
    }

    @GetMapping("/required")
    void required(@RequestParam String q) {
    }

    @GetMapping("/method-validation")
    void methodValidation(@RequestParam("page") @Min(1) Integer page) {
    }

    @PostMapping("/validation")
    void validation(@Valid @RequestBody ValidationRequest request) {
    }

    @PostMapping("/validation-without-message")
    void validationWithoutMessage(@Valid @RequestBody MessageRequest request) {
    }

    @PostMapping("/global-validation")
    void globalValidation(@Valid @RequestBody PasswordRequest request) {
    }

    record OkResponse(String value) {
    }

    record ValidationRequest(@NotBlank(message = "Nome é obrigatório.") String name) {
    }

    record MessageRequest(@NotBlank String name) {
    }

    @PasswordsMatch
    record PasswordRequest(
            @NotBlank(message = "Senha é obrigatória.") String password,
            @NotBlank(message = "Confirmação é obrigatória.") String confirmation) {
    }

    @Target(ElementType.TYPE)
    @Retention(RetentionPolicy.RUNTIME)
    @Constraint(validatedBy = PasswordsMatchValidator.class)
    @interface PasswordsMatch {

        String message() default "As senhas não conferem.";

        Class<?>[] groups() default {};

        Class<? extends Payload>[] payload() default {};
    }

    public static class PasswordsMatchValidator implements ConstraintValidator<PasswordsMatch, PasswordRequest> {

        @Override
        public boolean isValid(PasswordRequest value, ConstraintValidatorContext context) {
            return value == null || Objects.equals(value.password(), value.confirmation());
        }
    }
}

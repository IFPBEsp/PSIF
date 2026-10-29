package br.edu.ifpb.psif.shared.error;

import jakarta.validation.constraints.Min;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Controller;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@Validated
@Profile("error-test-fixtures")
@RequestMapping("/test/errors")
class ValidatedErrorTestController {

    @GetMapping("/validated")
    void validated(@RequestParam("page") @Min(1) Integer page) {
    }
}

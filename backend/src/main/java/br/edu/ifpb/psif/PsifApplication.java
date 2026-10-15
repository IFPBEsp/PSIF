package br.edu.ifpb.psif;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.ConfigurationPropertiesScan;

@SpringBootApplication
@ConfigurationPropertiesScan
public class PsifApplication {

    public static void main(String[] args) {
        SpringApplication.run(PsifApplication.class, args);
    }
}

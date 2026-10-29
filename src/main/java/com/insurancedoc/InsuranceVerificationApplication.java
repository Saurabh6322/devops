package com.insurancedoc;

import com.insurancedoc.model.InsuranceDocument;
import com.insurancedoc.repository.DocumentRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class InsuranceVerificationApplication {

    public static void main(String[] args) {
        SpringApplication.run(InsuranceVerificationApplication.class, args);
    }

    @Bean
    public CommandLineRunner initDatabase(DocumentRepository repository) {
        return args -> {
            if (repository.count() == 0) {
                repository.save(new InsuranceDocument(
                        "DOC-2026-1001", "POL-982140", "Aarav Sharma",
                        "Hospital Invoice", "VERIFIED", 12, 98.5, 45000.00,
                        "Hospital seal and GST invoice number authenticated with health registry."
                ));

                repository.save(new InsuranceDocument(
                        "DOC-2026-1002", "POL-773412", "Sneha Kulkarni",
                        "Surveyor Report", "UNDER_REVIEW", 42, 86.0, 125000.00,
                        "Accident scene images uploaded; awaiting surveyor vehicle chassis confirmation."
                ));

                repository.save(new InsuranceDocument(
                        "DOC-2026-1003", "POL-651908", "Rohan Mehta",
                        "Police FIR", "FLAGGED_FRAUD", 88, 34.0, 320000.00,
                        "CRITICAL: Digital tampering detected in FIR timestamp and jurisdictional station code."
                ));

                repository.save(new InsuranceDocument(
                        "DOC-2026-1004", "POL-441290", "Priya Nair",
                        "KYC Identity", "VERIFIED", 8, 99.2, 0.00,
                        "National ID card digitally verified with government UID database."
                ));

                repository.save(new InsuranceDocument(
                        "DOC-2026-1005", "POL-330911", "Vikram Deshmukh",
                        "Damage Estimate", "SUBMITTED", 25, 91.5, 68000.00,
                        "Initial workshop quotation received; automated OCR pre-screen passed."
                ));

                repository.save(new InsuranceDocument(
                        "DOC-2026-1006", "POL-119844", "Ananya Verma",
                        "Medical Prescription", "FLAGGED_FRAUD", 76, 41.2, 54000.00,
                        "Duplicate claim bill detected across multiple third-party administrators (TPA)."
                ));
            }
        };
    }
}


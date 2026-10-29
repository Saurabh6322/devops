package com.insurancedoc.controller;

import com.insurancedoc.model.InsuranceDocument;
import com.insurancedoc.repository.DocumentRepository;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class DocumentApiController {

    private final DocumentRepository repository;
    private final Random random = new Random();

    public DocumentApiController(DocumentRepository repository) {
        this.repository = repository;
    }

    @GetMapping("/documents")
    public List<InsuranceDocument> getAllDocuments(
            @RequestParam(required = false) String status,
            @RequestParam(required = false) String search) {

        List<InsuranceDocument> list;
        if (status != null && !status.isEmpty() && !"ALL".equalsIgnoreCase(status)) {
            list = repository.findByVerificationStatus(status.toUpperCase());
        } else {
            list = repository.findAll();
        }

        if (search != null && !search.trim().isEmpty()) {
            String q = search.toLowerCase();
            return list.stream().filter(doc ->
                    doc.getDocumentNumber().toLowerCase().contains(q) ||
                    doc.getPolicyNumber().toLowerCase().contains(q) ||
                    doc.getClaimantName().toLowerCase().contains(q) ||
                    doc.getDocumentType().toLowerCase().contains(q)
            ).toList();
        }

        return list;
    }

    @GetMapping("/documents/{id}")
    public ResponseEntity<InsuranceDocument> getDocumentById(@PathVariable Long id) {
        return repository.findById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping("/documents")
    public ResponseEntity<InsuranceDocument> submitDocument(@RequestBody InsuranceDocument doc) {
        if (doc.getPolicyNumber() == null || doc.getPolicyNumber().trim().isEmpty() ||
            doc.getClaimantName() == null || doc.getClaimantName().trim().isEmpty()) {
            return ResponseEntity.badRequest().build();
        }

        if (doc.getDocumentNumber() == null || doc.getDocumentNumber().trim().isEmpty()) {
            doc.setDocumentNumber("DOC-" + (2026) + "-" + (1000 + repository.count() + 1));
        }

        if (doc.getVerificationStatus() == null || doc.getVerificationStatus().trim().isEmpty()) {
            doc.setVerificationStatus("SUBMITTED");
        }

        doc.evaluateRiskAndStatus();
        doc.setSubmissionDate(LocalDateTime.now());
        doc.setLastUpdated(LocalDateTime.now());

        InsuranceDocument saved = repository.save(doc);
        return new ResponseEntity<>(saved, HttpStatus.CREATED);
    }

    @PutMapping("/documents/{id}/status")
    public ResponseEntity<InsuranceDocument> updateStatus(
            @PathVariable Long id,
            @RequestBody Map<String, String> payload) {

        return repository.findById(id).map(doc -> {
            String newStatus = payload.get("status");
            String notes = payload.get("notes");

            if (newStatus != null && !newStatus.trim().isEmpty()) {
                doc.setVerificationStatus(newStatus.toUpperCase());
            }
            if (notes != null && !notes.trim().isEmpty()) {
                doc.setReviewerNotes(notes);
            }
            doc.setLastUpdated(LocalDateTime.now());
            InsuranceDocument updated = repository.save(doc);
            return ResponseEntity.ok(updated);
        }).orElse(ResponseEntity.notFound().build());
    }

    @GetMapping("/alerts")
    public Map<String, Object> getFraudAlerts() {
        List<InsuranceDocument> highRiskDocs = repository.findByRiskScoreGreaterThanEqual(70);
        Map<String, Object> response = new HashMap<>();
        response.put("totalAlerts", highRiskDocs.size());
        response.put("fraudThresholdScore", 70);
        response.put("flaggedDocuments", highRiskDocs);
        return response;
    }

    @GetMapping("/summary")
    public Map<String, Object> getDashboardSummary() {
        List<InsuranceDocument> docs = repository.findAll();
        long total = docs.size();
        long verified = docs.stream().filter(d -> "VERIFIED".equalsIgnoreCase(d.getVerificationStatus())).count();
        long underReview = docs.stream().filter(d -> "UNDER_REVIEW".equalsIgnoreCase(d.getVerificationStatus())).count();
        long flaggedFraud = docs.stream().filter(d -> "FLAGGED_FRAUD".equalsIgnoreCase(d.getVerificationStatus()) || d.getRiskScore() >= 70).count();
        long submitted = docs.stream().filter(d -> "SUBMITTED".equalsIgnoreCase(d.getVerificationStatus())).count();

        double avgRisk = docs.stream().mapToInt(InsuranceDocument::getRiskScore).average().orElse(0.0);
        double totalClaims = docs.stream().mapToDouble(InsuranceDocument::getClaimAmount).sum();

        Map<String, Object> summary = new HashMap<>();
        summary.put("totalDocuments", total);
        summary.put("verifiedCount", verified);
        summary.put("underReviewCount", underReview);
        summary.put("flaggedFraudCount", flaggedFraud);
        summary.put("submittedCount", submitted);
        summary.put("averageRiskScore", Math.round(avgRisk * 10.0) / 10.0);
        summary.put("totalClaimAmount", Math.round(totalClaims * 100.0) / 100.0);
        return summary;
    }

    @PostMapping("/simulate")
    public ResponseEntity<Map<String, Object>> simulateVerificationBatch() {
        List<InsuranceDocument> docs = repository.findAll();
        for (InsuranceDocument doc : docs) {
            int delta = random.nextInt(15) - 7; // -7 to +7
            int newRisk = Math.max(5, Math.min(98, doc.getRiskScore() + delta));
            doc.setRiskScore(newRisk);
            doc.setAuthenticityConfidence(Math.round((100.0 - (newRisk * 0.75)) * 10.0) / 10.0);
            doc.evaluateRiskAndStatus();
            doc.setLastUpdated(LocalDateTime.now());
            repository.save(doc);
        }

        Map<String, Object> response = new HashMap<>();
        response.put("message", "Simulated automated OCR verification & fraud scoring batch completed.");
        response.put("processedRecords", docs.size());
        response.put("timestamp", LocalDateTime.now().toString());
        return ResponseEntity.ok(response);
    }

    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> health = new HashMap<>();
        health.put("status", "UP");
        health.put("application", "Insurance Document Verification Portal");
        health.put("student", "SOURABH SHELKE");
        health.put("rollNo", "23102C0029");
        health.put("version", "1.0.0");
        health.put("timestamp", LocalDateTime.now().toString());
        return ResponseEntity.ok(health);
    }
}


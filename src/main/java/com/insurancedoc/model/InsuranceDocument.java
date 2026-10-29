package com.insurancedoc.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "insurance_documents")
public class InsuranceDocument {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String documentNumber;

    @Column(nullable = false)
    private String policyNumber;

    @Column(nullable = false)
    private String claimantName;

    @Column(nullable = false)
    private String documentType; // e.g. "Hospital Invoice", "KYC Identity", "Surveyor Report", "Police FIR", "Policy Bond"

    @Column(nullable = false)
    private String verificationStatus; // "SUBMITTED", "UNDER_REVIEW", "VERIFIED", "FLAGGED_FRAUD", "REJECTED"

    @Column(nullable = false)
    private int riskScore; // 0-100 (<30 Low/Clean, 30-70 Moderate, >=70 High/Fraud Suspect)

    @Column(nullable = false)
    private double authenticityConfidence; // percentage e.g. 98.5%

    @Column(nullable = false)
    private double claimAmount;

    @Column(length = 1000)
    private String reviewerNotes;

    private LocalDateTime submissionDate;
    private LocalDateTime lastUpdated;

    public InsuranceDocument() {
        this.submissionDate = LocalDateTime.now();
        this.lastUpdated = LocalDateTime.now();
        this.verificationStatus = "SUBMITTED";
        this.riskScore = 15;
        this.authenticityConfidence = 95.0;
    }

    public InsuranceDocument(String documentNumber, String policyNumber, String claimantName,
                             String documentType, String verificationStatus, int riskScore,
                             double authenticityConfidence, double claimAmount, String reviewerNotes) {
        this.documentNumber = documentNumber;
        this.policyNumber = policyNumber;
        this.claimantName = claimantName;
        this.documentType = documentType;
        this.verificationStatus = verificationStatus;
        this.riskScore = riskScore;
        this.authenticityConfidence = authenticityConfidence;
        this.claimAmount = claimAmount;
        this.reviewerNotes = reviewerNotes;
        this.submissionDate = LocalDateTime.now();
        this.lastUpdated = LocalDateTime.now();
    }

    public void evaluateRiskAndStatus() {
        if (this.riskScore >= 70) {
            this.verificationStatus = "FLAGGED_FRAUD";
            if (this.reviewerNotes == null || this.reviewerNotes.isEmpty()) {
                this.reviewerNotes = "Automated OCR anomaly detected: High fraud probability score.";
            }
        } else if (this.riskScore >= 30) {
            if ("SUBMITTED".equals(this.verificationStatus)) {
                this.verificationStatus = "UNDER_REVIEW";
            }
        } else {
            if ("SUBMITTED".equals(this.verificationStatus)) {
                this.verificationStatus = "VERIFIED";
            }
        }
    }

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDocumentNumber() {
        return documentNumber;
    }

    public void setDocumentNumber(String documentNumber) {
        this.documentNumber = documentNumber;
    }

    public String getPolicyNumber() {
        return policyNumber;
    }

    public void setPolicyNumber(String policyNumber) {
        this.policyNumber = policyNumber;
    }

    public String getClaimantName() {
        return claimantName;
    }

    public void setClaimantName(String claimantName) {
        this.claimantName = claimantName;
    }

    public String getDocumentType() {
        return documentType;
    }

    public void setDocumentType(String documentType) {
        this.documentType = documentType;
    }

    public String getVerificationStatus() {
        return verificationStatus;
    }

    public void setVerificationStatus(String verificationStatus) {
        this.verificationStatus = verificationStatus;
    }

    public int getRiskScore() {
        return riskScore;
    }

    public void setRiskScore(int riskScore) {
        this.riskScore = riskScore;
    }

    public double getAuthenticityConfidence() {
        return authenticityConfidence;
    }

    public void setAuthenticityConfidence(double authenticityConfidence) {
        this.authenticityConfidence = authenticityConfidence;
    }

    public double getClaimAmount() {
        return claimAmount;
    }

    public void setClaimAmount(double claimAmount) {
        this.claimAmount = claimAmount;
    }

    public String getReviewerNotes() {
        return reviewerNotes;
    }

    public void setReviewerNotes(String reviewerNotes) {
        this.reviewerNotes = reviewerNotes;
    }

    public LocalDateTime getSubmissionDate() {
        return submissionDate;
    }

    public void setSubmissionDate(LocalDateTime submissionDate) {
        this.submissionDate = submissionDate;
    }

    public LocalDateTime getLastUpdated() {
        return lastUpdated;
    }

    public void setLastUpdated(LocalDateTime lastUpdated) {
        this.lastUpdated = lastUpdated;
    }
}


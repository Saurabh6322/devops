package com.insurancedoc.repository;

import com.insurancedoc.model.InsuranceDocument;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface DocumentRepository extends JpaRepository<InsuranceDocument, Long> {

    List<InsuranceDocument> findByVerificationStatus(String status);

    List<InsuranceDocument> findByRiskScoreGreaterThanEqual(int minRisk);

    List<InsuranceDocument> findByDocumentType(String documentType);

    List<InsuranceDocument> findByPolicyNumberContainingIgnoreCaseOrClaimantNameContainingIgnoreCase(
            String policyNumber, String claimantName);
}


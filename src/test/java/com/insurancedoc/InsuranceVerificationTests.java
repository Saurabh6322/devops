package com.insurancedoc;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.insurancedoc.model.InsuranceDocument;
import com.insurancedoc.repository.DocumentRepository;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.util.HashMap;
import java.util.Map;

import static org.hamcrest.Matchers.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
public class InsuranceVerificationTests {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private DocumentRepository repository;

    @Autowired
    private ObjectMapper objectMapper;

    @BeforeEach
    public void setup() {
        if (repository.count() == 0) {
            repository.save(new InsuranceDocument(
                    "DOC-2026-9901", "POL-110022", "Test Claimant",
                    "Hospital Invoice", "VERIFIED", 10, 99.0, 15000.0, "All clear"
            ));
        }
    }

    @Test
    @DisplayName("CUJ-1: Verify Ingestion of Baseline Insurance Document Records")
    public void testGetAllDocumentsInitialLoad() throws Exception {
        mockMvc.perform(get("/api/documents"))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$", hasSize(greaterThanOrEqualTo(1))))
                .andExpect(jsonPath("$[0].documentNumber", notNullValue()));
    }

    @Test
    @DisplayName("CUJ-2: Verify New Insurance Document Intake & Schema Validation")
    public void testDocumentSubmissionIntake() throws Exception {
        InsuranceDocument newDoc = new InsuranceDocument();
        newDoc.setPolicyNumber("POL-554433");
        newDoc.setClaimantName("Vikram Malhotra");
        newDoc.setDocumentType("Surveyor Report");
        newDoc.setClaimAmount(85000.0);
        newDoc.setRiskScore(18);
        newDoc.setAuthenticityConfidence(96.5);
        newDoc.setReviewerNotes("Onboarding new claim evidence.");

        mockMvc.perform(post("/api/documents")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(newDoc)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.documentNumber", startsWith("DOC-")))
                .andExpect(jsonPath("$.claimantName", is("Vikram Malhotra")))
                .andExpect(jsonPath("$.verificationStatus", is("VERIFIED")));
    }

    @Test
    @DisplayName("CUJ-3: Verify High-Risk Fraud Alert Trigger and Detection")
    public void testFraudAlertDetection() throws Exception {
        // Create an intentional high-risk fraud document
        InsuranceDocument fraudDoc = new InsuranceDocument(
                "DOC-FRAUD-9999", "POL-009988", "Fraud Test Case",
                "Police FIR", "FLAGGED_FRAUD", 92, 25.0, 500000.0, "Critical forgery"
        );
        repository.save(fraudDoc);

        mockMvc.perform(get("/api/alerts"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.totalAlerts", greaterThanOrEqualTo(1)))
                .andExpect(jsonPath("$.fraudThresholdScore", is(70)))
                .andExpect(jsonPath("$.flaggedDocuments[*].documentNumber", hasItem("DOC-FRAUD-9999")));
    }

    @Test
    @DisplayName("CUJ-4: Verify Role-Based Verification Status Workflow Transition")
    public void testRoleBasedWorkflowStatusUpdate() throws Exception {
        InsuranceDocument doc = repository.findAll().get(0);
        Long docId = doc.getId();

        Map<String, String> updatePayload = new HashMap<>();
        updatePayload.put("status", "UNDER_REVIEW");
        updatePayload.put("notes", "Senior Underwriter Sourabh Shelke requested additional medical bills.");

        mockMvc.perform(put("/api/documents/" + docId + "/status")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(updatePayload)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.verificationStatus", is("UNDER_REVIEW")))
                .andExpect(jsonPath("$.reviewerNotes", containsString("Sourabh Shelke")));
    }

    @Test
    @DisplayName("CUJ-5: Verify Dashboard KPI Summary Metrics Aggregation")
    public void testDashboardSummaryAggregation() throws Exception {
        mockMvc.perform(get("/api/summary"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.totalDocuments", greaterThanOrEqualTo(1)))
                .andExpect(jsonPath("$.averageRiskScore", notNullValue()))
                .andExpect(jsonPath("$.totalClaimAmount", greaterThanOrEqualTo(0.0)));
    }

    @Test
    @DisplayName("CUJ-6: Verify Microservice Health Probe Endpoint")
    public void testMicroserviceHealthCheck() throws Exception {
        mockMvc.perform(get("/api/health"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.status", is("UP")))
                .andExpect(jsonPath("$.student", is("SOURABH SHELKE")))
                .andExpect(jsonPath("$.rollNo", is("23102C0029")));
    }
}

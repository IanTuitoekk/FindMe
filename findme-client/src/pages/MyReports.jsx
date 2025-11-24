// src/pages/MyReports.jsx
import React, { useState } from "react";
import ReportRow from "../components/ReportRow";
import EditReportModal from "../components/EditReportModal";

/**
 * MyReports page
 * - Shows list of reports (mock data).
 * - Allows View (navigates), Edit (modal), Delete (local state).
 * - Cards are full-width inside a centered page container.
 */

const initialMock = [
  {
    id: 101,
    full_name: "John Doe",
    age: 32,
    gender: "Male",
    height: "180cm",
    last_seen_location: "Nairobi",
    last_seen_date: "2025-11-01",
    description: "Last seen near the city park.",
    image_url: "",
    contact_name: "Jane Doe",
    contact_phone: "0712345678",
    case_number: "CASE101",
  },
  {
    id: 102,
    full_name: "Amina Ali",
    age: 24,
    gender: "Female",
    height: "165cm",
    last_seen_location: "Mombasa",
    last_seen_date: "2025-10-21",
    description: "Wearing red scarf.",
    image_url: "",
    contact_name: "Fatma Ali",
    contact_phone: "0701112223",
    case_number: "CASE102",
  },
];

export default function MyReports() {
  const [reports, setReports] = useState(initialMock);
  const [editingReport, setEditingReport] = useState(null);

  // Delete handler (local state)
  function handleDelete(id) {
    if (!window.confirm("Delete this report? This action cannot be undone.")) return;
    setReports((prev) => prev.filter((r) => r.id !== id));
  }

  // Launch edit modal
  function handleEdit(report) {
    setEditingReport(report);
  }

  // Save updates from modal (local state)
  function handleSave(updated) {
    setReports((prev) => prev.map((r) => (r.id === updated.id ? updated : r)));
    setEditingReport(null);
  }

  // Cancel edit
  function handleCancelEdit() {
    setEditingReport(null);
  }

  return (
    <div style={{ width: "100%", minHeight: "100vh", background: "#f5f6f8", padding: "3.5rem 2rem", boxSizing: "border-box" }}>
      <div
        style={{
          maxWidth: "1200px",
          margin: "0 auto",
          background: "#ffffff",
          borderRadius: "14px",
          padding: "2.25rem",
          boxShadow: "0 8px 30px rgba(15, 23, 42, 0.06)",
        }}
      >
        <h1 style={{ fontSize: "2.25rem", fontWeight: 700, marginBottom: "0.5rem", color: "#0f1724" }}>My Reports</h1>
        <p style={{ color: "#6b7280", marginBottom: "1.75rem" }}>
          Manage the missing person reports you have submitted. Edit to update details or delete if needed.
        </p>

        {/* report list - full-width cards */}
        <div style={{ display: "flex", flexDirection: "column", gap: "1.25rem" }}>
          {reports.length === 0 ? (
            <div style={{ padding: "2rem", textAlign: "center", color: "#6b7280" }}>You haven't submitted any reports yet.</div>
          ) : (
            reports.map((r) => (
              <ReportRow
                key={r.id}
                report={r}
                onEdit={() => handleEdit(r)}
                onDelete={() => handleDelete(r.id)}
              />
            ))
          )}
        </div>
      </div>

      {/* Edit modal */}
      {editingReport && (
        <EditReportModal
          initial={editingReport}
          onSave={handleSave}
          onClose={handleCancelEdit}
        />
      )}
    </div>
  );
}

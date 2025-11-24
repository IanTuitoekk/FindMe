// src/components/DeleteConfirmModal.jsx
import React from "react";

/**
 * DeleteConfirmModal
 * - report: object being deleted
 * - onClose: fn()
 * - onConfirm: fn()
 */

export default function DeleteConfirmModal({ report, onClose, onConfirm }) {
  return (
    <div style={overlay} role="dialog" aria-modal="true" aria-label="Confirm delete">
      <div style={box}>
        <h3 style={{ marginTop: 0, marginBottom: 6 }}>Delete report</h3>
        <p style={{ color: "#374151", marginBottom: 18 }}>
          Are you sure you want to delete this report for <strong>{report.full_name}</strong> (case <strong>{report.case_number}</strong>)? This action cannot be undone.
        </p>

        <div style={{ display: "flex", justifyContent: "flex-end", gap: 10 }}>
          <button onClick={onClose} style={cancelBtn}>Cancel</button>
          <button onClick={onConfirm} style={deleteBtn}>Delete</button>
        </div>
      </div>
    </div>
  );
}

const overlay = {
  position: "fixed",
  inset: 0,
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  background: "rgba(12,14,16,0.45)",
  zIndex: 1300,
};

const box = {
  width: "min(520px, 96%)",
  background: "#fff",
  borderRadius: 12,
  padding: "1.25rem 1.5rem",
  boxShadow: "0 8px 28px rgba(2,6,23,0.18)",
};

const cancelBtn = {
  background: "#fff",
  color: "#111827",
  border: "1px solid #e6e9ee",
  padding: "0.5rem 0.9rem",
  borderRadius: 8,
  cursor: "pointer",
};

const deleteBtn = {
  background: "#ef4444",
  color: "#fff",
  border: "none",
  padding: "0.5rem 0.9rem",
  borderRadius: 8,
  cursor: "pointer",
};

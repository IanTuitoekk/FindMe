// src/components/ReportRow.jsx
import React from "react";
import { Link, useNavigate } from "react-router-dom";

/**
 * ReportRow
 * - A single full-width card row showing summary info.
 * - Right-aligned vertical action buttons (View, Edit, Delete).
 *
 * Props:
 *  - report: object
 *  - onEdit: fn
 *  - onDelete: fn
 */

export default function ReportRow({ report, onEdit, onDelete }) {
  const navigate = useNavigate();

  const {
    id,
    full_name = "Unknown",
    case_number = "N/A",
    age,
    gender,
    last_seen_location,
    last_seen_date,
  } = report;

  // formatted last seen
  const lastSeen = `${last_seen_location || "Unknown"}${last_seen_date ? ", " + last_seen_date : ""}`;

  return (
    <div
      style={{
        display: "flex",
        alignItems: "flex-start",
        justifyContent: "space-between",
        border: "1px solid #e6e9ee",
        borderRadius: "10px",
        padding: "1.25rem",
        background: "#fff",
      }}
    >
      {/* Left: report summary */}
      <div style={{ flex: "1 1 auto", minWidth: 0 }}>
        <div style={{ marginBottom: "0.35rem" }}>
          <div style={{ fontSize: "1.05rem", fontWeight: 700, color: "#0f1724" }}>{full_name}</div>
          <div style={{ color: "#6b7280", marginTop: "0.25rem" }}>
            Case: <strong style={{ color: "#111827" }}>{case_number}</strong>
          </div>
        </div>

        {/* small facts line with subtle headings */}
        <div style={{ display: "flex", gap: "2.5rem", marginTop: "0.9rem", alignItems: "center" }}>
          <div>
            <div style={{ fontSize: "0.85rem", color: "#6b7280" }}>Age</div>
            <div style={{ fontWeight: 700, color: "#0f1724", marginTop: "0.25rem" }}>{age ?? "Not available"}</div>
          </div>

          <div>
            <div style={{ fontSize: "0.85rem", color: "#6b7280" }}>Gender</div>
            <div style={{ fontWeight: 700, color: "#0f1724", marginTop: "0.25rem" }}>{gender ?? "Not available"}</div>
          </div>

          <div>
            <div style={{ fontSize: "0.85rem", color: "#6b7280" }}>Last seen</div>
            <div style={{ fontWeight: 700, color: "#0f1724", marginTop: "0.25rem" }}>{lastSeen}</div>
          </div>
        </div>
      </div>

      {/* Right: actions (vertical) */}
      <div style={{ marginLeft: "1.25rem", display: "flex", flexDirection: "column", gap: "0.6rem", width: "140px" }}>
        {/* View - use navigate to keep consistent behaviour */}
        <button
          onClick={() => navigate(`/person/${id}`)}
          style={{
            padding: "0.55rem 0.75rem",
            background: "#ffffff",
            border: "1px solid #e6e9ee",
            borderRadius: "8px",
            cursor: "pointer",
            color: "#2563eb",
            fontWeight: 600,
          }}
        >
          View
        </button>

        <button
          onClick={onEdit}
          style={{
            padding: "0.55rem 0.75rem",
            background: "#ffffff",
            border: "1px solid #e6e9ee",
            borderRadius: "8px",
            cursor: "pointer",
            color: "#111827",
          }}
        >
          Edit
        </button>

        <button
          onClick={onDelete}
          style={{
            padding: "0.55rem 0.75rem",
            background: "#fee2e2",
            border: "1px solid #fbcaca",
            borderRadius: "8px",
            cursor: "pointer",
            color: "#9b1c1c",
            fontWeight: 600,
          }}
        >
          Delete
        </button>
      </div>
    </div>
  );
}

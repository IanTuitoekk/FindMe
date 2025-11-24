// src/components/EditReportModal.jsx
import React, { useState } from "react";

/**
 * EditReportModal
 * - Modal overlay with full form matching Report fields.
 * - onSave(updatedReport) - called when user saves.
 * - onClose() - called when user cancels.
 *
 * Fields:
 * Full Name *
 * Age *
 * Gender *
 * Height (optional)
 * Last Seen Location *
 * Last Seen Date *
 * Description (optional)
 * Image URL (optional)
 * Contact Person Name *
 * Contact Person Phone *
 * Case Number *
 */

export default function EditReportModal({ initial, onSave, onClose }) {
  const [form, setForm] = useState({
    id: initial.id,
    full_name: initial.full_name || "",
    age: initial.age || "",
    gender: initial.gender || "",
    height: initial.height || "",
    last_seen_location: initial.last_seen_location || "",
    last_seen_date: initial.last_seen_date || "",
    description: initial.description || "",
    image_url: initial.image_url || "",
    contact_name: initial.contact_name || "",
    contact_phone: initial.contact_phone || "",
    case_number: initial.case_number || "",
  });

  const [saving, setSaving] = useState(false);

  function change(e) {
    const { name, value } = e.target;
    setForm((f) => ({ ...f, [name]: value }));
  }

  function validate() {
    const required = [
      "full_name",
      "age",
      "gender",
      "last_seen_location",
      "last_seen_date",
      "contact_name",
      "contact_phone",
      "case_number",
    ];
    for (let key of required) {
      if (!form[key]) return false;
    }
    return true;
  }

  async function handleSave(e) {
    e.preventDefault();
    if (!validate()) {
      alert("Please fill all required fields.");
      return;
    }

    setSaving(true);

    // Simulate async save (later replace with real API call)
    setTimeout(() => {
      setSaving(false);
      onSave(form); // pass updated form back to parent
    }, 600);
  }

  return (
    <div
      role="dialog"
      aria-modal="true"
      style={{
        position: "fixed",
        inset: 0,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        zIndex: 60,
        background: "rgba(15, 23, 42, 0.45)",
        padding: "2rem",
      }}
    >
      <div style={{ width: "100%", maxWidth: "880px", background: "#fff", borderRadius: "12px", boxShadow: "0 12px 40px rgba(2,6,23,0.35)", overflow: "hidden" }}>
        <form onSubmit={handleSave}>
          <div style={{ padding: "1.25rem 1.5rem", borderBottom: "1px solid #eef2f6", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
            <div>
              <h3 style={{ margin: 0, fontSize: "1.25rem", fontWeight: 700, color: "#0f1724" }}>Edit Report</h3>
              <div style={{ color: "#6b7280", marginTop: "6px" }}>Update the report details and save.</div>
            </div>
            <div>
              <button type="button" onClick={onClose} style={{ background: "transparent", border: "none", fontSize: "0.95rem", color: "#6b7280", cursor: "pointer" }}>
                Cancel
              </button>
            </div>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem", padding: "1.25rem 1.5rem" }}>
            {/* left column */}
            <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
              <label style={{ fontSize: "0.9rem", color: "#374151" }}>Full Name *</label>
              <input name="full_name" value={form.full_name} onChange={change} style={inputStyle} />

              <label style={{ fontSize: "0.9rem", color: "#374151", marginTop: "0.5rem" }}>Age *</label>
              <input name="age" value={form.age} onChange={change} style={inputStyle} inputMode="numeric" />

              <label style={{ fontSize: "0.9rem", color: "#374151", marginTop: "0.5rem" }}>Gender *</label>
              <select name="gender" value={form.gender} onChange={change} style={selectStyle}>
                <option value="">Select gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
                <option value="Prefer not to say">Prefer not to say</option>
              </select>

              <label style={{ fontSize: "0.9rem", color: "#374151", marginTop: "0.5rem" }}>Height (optional)</label>
              <input name="height" value={form.height} onChange={change} style={inputStyle} />
            </div>

            {/* right column */}
            <div style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}>
              <label style={{ fontSize: "0.9rem", color: "#374151" }}>Last Seen Location *</label>
              <input name="last_seen_location" value={form.last_seen_location} onChange={change} style={inputStyle} />

              <label style={{ fontSize: "0.9rem", color: "#374151", marginTop: "0.5rem" }}>Last Seen Date *</label>
              <input type="date" name="last_seen_date" value={form.last_seen_date} onChange={change} style={inputStyle} />

              <label style={{ fontSize: "0.9rem", color: "#374151", marginTop: "0.5rem" }}>Case Number *</label>
              <input name="case_number" value={form.case_number} onChange={change} style={inputStyle} />
            </div>

            {/* full width description */}
            <div style={{ gridColumn: "1 / -1", display: "flex", flexDirection: "column", gap: "0.5rem" }}>
              <label style={{ fontSize: "0.9rem", color: "#374151" }}>Description (optional)</label>
              <textarea name="description" value={form.description} onChange={change} rows={4} style={{ ...inputStyle, resize: "vertical" }} />

              <label style={{ fontSize: "0.9rem", color: "#374151", marginTop: "0.5rem" }}>Image URL (optional)</label>
              <input name="image_url" value={form.image_url} onChange={change} style={inputStyle} />

              <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem", marginTop: "0.5rem" }}>
                <div>
                  <label style={{ fontSize: "0.9rem", color: "#374151" }}>Contact Person Name *</label>
                  <input name="contact_name" value={form.contact_name} onChange={change} style={inputStyle} />
                </div>
                <div>
                  <label style={{ fontSize: "0.9rem", color: "#374151" }}>Contact Person Phone *</label>
                  <input name="contact_phone" value={form.contact_phone} onChange={change} style={inputStyle} />
                </div>
              </div>
            </div>
          </div>

          <div style={{ display: "flex", justifyContent: "flex-end", gap: "0.75rem", padding: "1rem 1.5rem", borderTop: "1px solid #eef2f6" }}>
            <button type="button" onClick={onClose} style={{ background: "#fff", border: "1px solid #e6e9ee", padding: "0.6rem 0.9rem", borderRadius: "8px", cursor: "pointer" }}>
              Cancel
            </button>
            <button type="submit" disabled={saving} style={{ background: "#2563eb", color: "#fff", border: "none", padding: "0.6rem 0.95rem", borderRadius: "8px", cursor: "pointer", fontWeight: 700 }}>
              {saving ? "Saving…" : "Save changes"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

// basic inputs
const inputStyle = {
  width: "100%",
  padding: "0.6rem 0.75rem",
  borderRadius: "8px",
  border: "1px solid #e6e9ee",
  fontSize: "0.95rem",
  boxSizing: "border-box",
};

const selectStyle = {
  ...inputStyle,
  appearance: "none",
  backgroundImage: "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 20 20'%3E%3Cpath fill='%236b7280' d='M5.25 7.5L10 12.25L14.75 7.5H5.25Z'/%3E%3C/svg%3E\")",
  backgroundRepeat: "no-repeat",
  backgroundPosition: "right 12px center",
};

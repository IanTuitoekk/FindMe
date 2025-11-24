import React, { useState } from "react";

export default function Report() {
  const [formData, setFormData] = useState({
    full_name: "",
    age: "",
    gender: "",
    height: "",
    last_seen_location: "",
    last_seen_date: "",
    description: "",
    image_url: "",
    contact_name: "",
    contact_phone: "",
    case_number: "",
  });

  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Submitted:", formData);
  }

  return (
    <div
      style={{
        width: "100%",
        minHeight: "100vh",
        background: "#f5f6f8",
        paddingTop: "4rem",
        paddingBottom: "4rem",
        display: "flex",
        justifyContent: "center",
      }}
    >
      {/* WHITE CONTAINER */}
      <div
        style={{
          width: "100%",
          maxWidth: "780px",
          background: "#ffffff",
          padding: "3rem 2.5rem",
          borderRadius: "12px",
          boxShadow: "0 2px 12px rgba(0,0,0,0.06)",
        }}
      >
        <h1 className="page-title">Report a Missing Person</h1>
        <p className="page-subtitle">
          Please fill in the details below to submit a missing person report.
        </p>

        <form onSubmit={handleSubmit}>
          {/* FULL NAME */}
          <label className="form-label">Full Name *</label>
          <input
            type="text"
            className="form-input"
            name="full_name"
            placeholder="e.g. John Doe"
            value={formData.full_name}
            onChange={handleChange}
          />

          {/* AGE */}
          <label className="form-label">Age *</label>
          <input
            type="number"
            className="form-input"
            name="age"
            placeholder="e.g. 20"
            value={formData.age}
            onChange={handleChange}
          />

          {/* GENDER */}
          <label className="form-label">Gender *</label>
          <select
            className="form-input"
            name="gender"
            value={formData.gender}
            onChange={handleChange}
          >
            <option value="">Select gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
          </select>

          {/* HEIGHT */}
          <label className="form-label">Height (optional)</label>
          <input
            type="text"
            className="form-input"
            name="height"
            placeholder="e.g. 5'7 or 170cm"
            value={formData.height}
            onChange={handleChange}
          />

          {/* LAST SEEN LOCATION */}
          <label className="form-label">Last Seen Location *</label>
          <input
            type="text"
            className="form-input"
            name="last_seen_location"
            placeholder="e.g. Nairobi"
            value={formData.last_seen_location}
            onChange={handleChange}
          />

          {/* LAST SEEN DATE */}
          <label className="form-label">Last Seen Date *</label>
          <input
            type="date"
            className="form-input"
            name="last_seen_date"
            value={formData.last_seen_date}
            onChange={handleChange}
          />

          {/* DESCRIPTION */}
          <label className="form-label">Description (optional)</label>
          <textarea
            className="form-input"
            name="description"
            placeholder="Any additional details..."
            value={formData.description}
            onChange={handleChange}
          />

          {/* IMAGE URL */}
          <label className="form-label">Image URL (optional)</label>
          <input
            type="text"
            className="form-input"
            name="image_url"
            placeholder="https://example.com/image.jpg"
            value={formData.image_url}
            onChange={handleChange}
          />

          {/* CONTACT NAME */}
          <label className="form-label">Contact Person Name *</label>
          <input
            type="text"
            className="form-input"
            name="contact_name"
            placeholder="e.g. Jane Doe"
            value={formData.contact_name}
            onChange={handleChange}
          />

          {/* CONTACT PHONE */}
          <label className="form-label">Contact Person Phone *</label>
          <input
            type="text"
            className="form-input"
            name="contact_phone"
            placeholder="e.g. 0712345678"
            value={formData.contact_phone}
            onChange={handleChange}
          />

          {/* CASE NUMBER */}
          <label className="form-label">Case Number *</label>
          <input
            type="text"
            className="form-input"
            name="case_number"
            placeholder="e.g. CASE12345"
            value={formData.case_number}
            onChange={handleChange}
          />

          {/* BUTTON */}
          <button className="btn-primary" type="submit">
            Submit Report
          </button>
        </form>
      </div>
    </div>
  );
}

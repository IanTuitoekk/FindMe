import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

export default function PersonDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [person, setPerson] = useState(null);
  const [loading, setLoading] = useState(true);

  const BASE_URL = "http://127.0.0.1:5000";

  const dummyFallback = {
    id,
    full_name: "Unknown Person",
    age: "Not available",
    gender: "Not available",
    height: "Not available",
    last_seen_location: "Not available",
    last_seen_date: "Not available",
    description: "No description available.",
    contact_name: "Not available",
    contact_phone: "Not available",
    case_number: "N/A",
    image_url: "",
  };

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(`${BASE_URL}/missing-persons/${id}`);

        if (!res.ok) {
          setPerson(dummyFallback);
          return;
        }

        const data = await res.json();
        setPerson(Object.keys(data).length === 0 ? dummyFallback : data);
      } catch (err) {
        console.error("Error:", err);
        setPerson(dummyFallback);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [id]);

  if (loading)
    return <p style={{ padding: "4rem", textAlign: "center" }}>Loading…</p>;

  return (
    <div
      style={{
        width: "100%",
        minHeight: "100vh",
        background: "#f5f6f8",
        padding: "4rem 1rem",
        display: "flex",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          maxWidth: "900px",
          width: "100%",
          background: "#fff",
          borderRadius: "12px",
          padding: "3rem 2.5rem",
          boxShadow: "0 2px 12px rgba(0,0,0,0.06)",
          position: "relative",
        }}
      >
        {/* BACK BUTTON */}
        <button
          onClick={() => navigate(-1)}
          style={{
            display: "flex",
            alignItems: "center",
            gap: "6px",
            border: "none",
            background: "transparent",
            cursor: "pointer",
            position: "absolute",
            top: "1.5rem",
            left: "1.5rem",
            fontSize: "1rem",
            color: "#2563eb",
            fontWeight: 500,
          }}
        >
          <span
            style={{
              fontSize: "1.2rem",
              fontWeight: 700,
              lineHeight: "1",
            }}
          >
            ←
          </span>
          Back
        </button>

        {/* Spacer so content doesn't overlap button */}
        <div style={{ height: "2rem" }}></div>

        {/* IMAGE */}
        <div
          style={{
            width: "100%",
            height: "350px",
            background: "#f2f2f2",
            borderRadius: "8px",
            marginBottom: "2rem",
            backgroundImage: `url(${person.image_url})`,
            backgroundSize: "cover",
            backgroundPosition: "center",
          }}
        ></div>

        {/* NAME + CASE */}
        <h1 style={{ fontSize: "2rem", fontWeight: 700, marginBottom: "0.5rem" }}>
          {person.full_name}
        </h1>
        <p style={{ color: "#6b7280", marginBottom: "2rem" }}>
          Case Number: <strong>{person.case_number}</strong>
        </p>

        {/* TWO-COLUMN GRID */}
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "1fr 1fr",
            gap: "2rem",
          }}
        >
          <div>
            <Detail label="Age" value={person.age} />
            <Detail label="Gender" value={person.gender} />
            <Detail label="Height" value={person.height} />
            <Detail label="Description" value={person.description} />
          </div>

          <div>
            <Detail
              label="Last Seen Location"
              value={person.last_seen_location}
            />
            <Detail label="Last Seen Date" value={person.last_seen_date} />
            <Detail label="Contact Person" value={person.contact_name} />
            <Detail label="Contact Phone" value={person.contact_phone} />
          </div>
        </div>
      </div>
    </div>
  );
}

function Detail({ label, value }) {
  return (
    <div style={{ marginBottom: "1.8rem" }}>
      <p
        style={{
          fontSize: "0.85rem",
          fontWeight: 600,
          color: "#6b7280",
          marginBottom: "0.25rem",
        }}
      >
        {label}
      </p>
      <p
        style={{
          fontSize: "1.05rem",
          color: "#111827",
          fontWeight: 500,
        }}
      >
        {value}
      </p>
    </div>
  );
}

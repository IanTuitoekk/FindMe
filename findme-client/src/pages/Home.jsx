import PersonCard from "../components/PersonCard";

export default function Home() {
  const featuredPeople = [
    { id: 1, name: "John Doe", last_seen_location: "Nairobi", status: "Missing" },
    { id: 2, name: "Amina Ali", last_seen_location: "Mombasa", status: "Missing" },
    { id: 3, name: "Samuel W.", last_seen_location: "Kisumu", status: "Missing" },
    { id: 4, name: "Mary N.", last_seen_location: "Thika", status: "Missing" },
    { id: 5, name: "Joseph K.", last_seen_location: "Nakuru", status: "Missing" },
    { id: 6, name: "Fatima O.", last_seen_location: "Eldoret", status: "Missing" },
    { id: 7, name: "Peter M.", last_seen_location: "Meru", status: "Missing" },
    { id: 8, name: "Grace A.", last_seen_location: "Machakos", status: "Missing" },
  ];

  return (
    <div style={{ width: "100%", maxWidth: "1300px", margin: "0 auto" }}>
      
      {/* Heading */}
      <h1 style={{ fontSize: "3rem", fontWeight: "700", marginBottom: "1rem", color: "#1f2937" }}>
        Find Missing Persons
      </h1>

      <p style={{ color: "#4b5563", marginBottom: "2rem", maxWidth: "650px" }}>
        A community-driven platform to report and search for missing persons.
      </p>

      {/* Search Bar */}
      <div style={{ display: "flex", gap: "1rem", marginBottom: "3rem" }}>
        <input
          type="text"
          placeholder="Search by name..."
          style={{
            flex: 1,
            padding: "0.9rem",
            borderRadius: "8px",
            border: "1px solid #d1d5db",
          }}
        />
        <button
          style={{
            padding: "0 1.6rem",
            borderRadius: "8px",
            background: "#2563eb",
            color: "#fff",
            border: "none",
            cursor: "pointer",
          }}
        >
          Search
        </button>
      </div>

      {/* Featured Section */}
      <h2 style={{ fontSize: "1.6rem", fontWeight: "700", marginBottom: "1.5rem" }}>
        Featured cases
      </h2>

      {/* Responsive Grid */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
          gap: "2rem",
          width: "100%",
          boxSizing: "border-box",
        }}
      >
        {featuredPeople.map((p) => (
          <PersonCard key={p.id} person={p} />
        ))}
      </div>
    </div>
  );
}

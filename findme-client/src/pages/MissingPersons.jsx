import { useEffect, useState } from "react";
import PersonCard from "../components/PersonCard";

function MissingPersons() {
  const [people, setPeople] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [locationFilter, setLocationFilter] = useState("All");
  const [statusFilter, setStatusFilter] = useState("All");

  // -------------------------------
  // TEMPORARY DUMMY DATA (same as Home Page)
  // -------------------------------
  const dummyData = [
    { id: 1, name: "John Doe", last_seen_location: "Nairobi", status: "Missing" },
    { id: 2, name: "Amina Ali", last_seen_location: "Mombasa", status: "Missing" },
    { id: 3, name: "Samuel W.", last_seen_location: "Kisumu", status: "Missing" },
    { id: 4, name: "Mary N.", last_seen_location: "Thika", status: "Missing" },
    { id: 5, name: "Joseph K.", last_seen_location: "Nakuru", status: "Missing" },
    { id: 6, name: "Fatima O.", last_seen_location: "Eldoret", status: "Missing" },
    { id: 7, name: "Peter M.", last_seen_location: "Meru", status: "Missing" },
    { id: 8, name: "Grace A.", last_seen_location: "Machakos", status: "Missing" },
  ];

  useEffect(() => {
    setPeople(dummyData.reverse());
  }, []);

  // FILTER LOGIC
  const filteredPeople = people.filter((person) => {
    const matchesName =
      searchTerm === "" ||
      person.name.toLowerCase().includes(searchTerm.toLowerCase());

    const matchesLocation =
      locationFilter === "All" ||
      person.last_seen_location === locationFilter;

    const matchesStatus =
      statusFilter === "All" || person.status === statusFilter;

    return matchesName && matchesLocation && matchesStatus;
  });

  return (
    <div
      style={{
        maxWidth: "1300px",
        margin: "0 auto",
        padding: "2rem 1.5rem",
      }}
    >
      <h1
        style={{
          fontSize: "2.5rem",
          fontWeight: "700",
          marginBottom: "1.5rem",
          color: "#1f2937",
        }}
      >
        All Missing Persons
      </h1>

      {/* SEARCH + FILTERS */}
      <div
        style={{
          display: "flex",
          gap: "1rem",
          marginBottom: "2rem",
          flexWrap: "wrap",
          alignItems: "center",
        }}
      >
        {/* Search input */}
        <input
          type="text"
          placeholder="Search by name..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{
            flex: "1",
            minWidth: "280px",
            padding: "0.8rem",
            borderRadius: "8px",
            border: "1px solid #d1d5db",
            fontSize: "0.95rem",
          }}
        />

        {/* LOCATION DROPDOWN WITH PLACEHOLDER */}
        <div style={wrapperStyle}>
          <span style={placeholderLabelStyle}>
            {locationFilter === "All" ? "Filter by Location" : locationFilter}
          </span>
          <select
            value={locationFilter}
            onChange={(e) => setLocationFilter(e.target.value)}
            style={selectStyle}
          >
            <option value="All">All</option>
            <option value="Nairobi">Nairobi</option>
            <option value="Mombasa">Mombasa</option>
            <option value="Kisumu">Kisumu</option>
            <option value="Thika">Thika</option>
            <option value="Nakuru">Nakuru</option>
            <option value="Eldoret">Eldoret</option>
            <option value="Meru">Meru</option>
            <option value="Machakos">Machakos</option>
          </select>
        </div>

        {/* STATUS DROPDOWN WITH PLACEHOLDER */}
        <div style={wrapperStyle}>
          <span style={placeholderLabelStyle}>
            {statusFilter === "All" ? "Filter by Status" : statusFilter}
          </span>
          <select
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
            style={selectStyle}
          >
            <option value="All">All</option>
            <option value="Missing">Missing</option>
            <option value="Found">Found</option>
          </select>
        </div>
      </div>

      {/* RESULTS GRID */}
      {filteredPeople.length === 0 ? (
        <p style={{ color: "#4b5563" }}>No missing persons found.</p>
      ) : (
        <div style={gridStyle}>
          {filteredPeople.map((p) => (
            <PersonCard key={p.id} person={p} />
          ))}
        </div>
      )}
    </div>
  );
}

// Wrapper that holds text + hidden real select
const wrapperStyle = {
  position: "relative",
  width: "180px",
};

const placeholderLabelStyle = {
  position: "absolute",
  top: "50%",
  left: "12px",
  transform: "translateY(-50%)",
  fontSize: "0.9rem",
  color: "#374151",
  pointerEvents: "none",
};

const selectStyle = {
  width: "100%",
  padding: "0.7rem",
  fontSize: "0.9rem",
  borderRadius: "8px",
  border: "1px solid #d1d5db",
  backgroundColor: "#f3f4f6",
  color: "transparent", // hides text so our custom label shows
  cursor: "pointer",
  appearance: "none",
  backgroundImage:
    "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 20 20'%3E%3Cpath fill='%236b7280' d='M5.25 7.5L10 12.25L14.75 7.5H5.25Z'/%3E%3C/svg%3E\")",
  backgroundRepeat: "no-repeat",
  backgroundPosition: "right 12px center",
};

const gridStyle = {
  display: "grid",
  gridTemplateColumns: "repeat(auto-fill, minmax(260px, 1fr))",
  gap: "1.8rem",
  alignItems: "start",
};

export default MissingPersons;

// src/components/Navbar.jsx
import { Link, useLocation } from "react-router-dom";
import { useAuth } from "../context/authContext";

export default function Navbar() {
  const { isAuthenticated, logout, user } = useAuth();
  const location = useLocation();

  // TEMPORARY OVERRIDE so we can see all tabs during UI development
  const showPrivateTabs = true; // <----- Change back to isAuthenticated later

  const linkStyle = (path) => ({
    padding: "0.6rem 1rem",
    fontSize: "0.95rem",
    fontWeight: 500,
    borderRadius: "6px",
    textDecoration: "none",
    color: location.pathname === path ? "#1d4ed8" : "#374151",
    background: location.pathname === path ? "#e5edff" : "transparent",
  });

  return (
    <nav
      style={{
        width: "100%",
        padding: "1rem 2rem",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        background: "#ffffff",
        borderBottom: "1px solid #e5e7eb",
        position: "sticky",
        top: 0,
        zIndex: 100,
      }}
    >
      {/* LEFT: LOGO */}
      <Link
        to="/"
        style={{
          fontSize: "1.4rem",
          fontWeight: 700,
          color: "#111827",
          textDecoration: "none",
        }}
      >
        FindMe
      </Link>

      {/* RIGHT: NAV LINKS */}
      <div
        style={{
          display: "flex",
          gap: "1rem",
          alignItems: "center",
        }}
      >
        <Link to="/" style={linkStyle("/")}>
          Home
        </Link>
        <Link to="/about" style={linkStyle("/about")}>
          About
        </Link>
        <Link to="/missing-persons" style={linkStyle("/missing-persons")}>
          Missing Persons
        </Link>

        {/* TEMPORARY: Show Report + My Reports ALWAYS */}
        {showPrivateTabs && (
          <>
            <Link to="/report" style={linkStyle("/report")}>
              Report
            </Link>
            <Link to="/my-reports" style={linkStyle("/my-reports")}>
              My Reports
            </Link>
          </>
        )}

        {/* AUTH BUTTON */}
        {!isAuthenticated ? (
          <Link
            to="/login"
            style={{
              padding: "0.5rem 1rem",
              background: "#2563eb",
              color: "white",
              borderRadius: "6px",
              textDecoration: "none",
              fontSize: "0.9rem",
            }}
          >
            Login
          </Link>
        ) : (
          <button
            onClick={logout}
            style={{
              padding: "0.45rem 1rem",
              background: "#f3f4f6",
              color: "#111827",
              borderRadius: "6px",
              border: "1px solid #d1d5db",
              cursor: "pointer",
              fontSize: "0.9rem",
            }}
          >
            Logout
          </button>
        )}
      </div>
    </nav>
  );
}

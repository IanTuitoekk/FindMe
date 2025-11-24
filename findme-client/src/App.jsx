// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import About from "./pages/About";
import Home from "./pages/Home";
import MissingPersons from "./pages/MissingPersons";
import Report from "./pages/Report";
import PersonDetails from "./pages/PersonDetails";
import Login from "./pages/Login";
import MyReports from "./pages/MyReports";

import { AuthProvider } from "./context/authContext";

/**
 * App entry component.
 *
 * Notes:
 * - Wraps the entire app in AuthProvider so Navbar and all pages can access auth state.
 * - Keeps routes as before.
 *
 * Developer tip: if you want to *see* Report + My Reports in dev without actually logging in,
 * open the browser console and run:
 *
 *   localStorage.setItem('fm_token', 'DEVTOKEN');
 *
 * then refresh the page. That will make the auth context find a token and attempt to fetch the user.
 * (If your backend isn't running, it may clear the token; for a pure mock, see the Navbar dev shortcut.)
 */

function App() {
  return (
    <AuthProvider>
      <Router>
        {/* NAVBAR */}
        <Navbar />

        {/* MAIN CONTENT */}
        <main
          style={{
            width: "100%",
            minHeight: "calc(100vh - 140px)",
            padding: "2rem 1rem",
            background: "#f9fafb",
            boxSizing: "border-box",
          }}
        >
          <Routes>
            {/* PUBLIC ROUTES */}
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/missing-persons" element={<MissingPersons />} />
            <Route path="/person/:id" element={<PersonDetails />} />
            <Route path="/login" element={<Login />} />

            {/* PROTECTED ROUTES (UI only for now) */}
            <Route path="/report" element={<Report />} />
            <Route path="/my-reports" element={<MyReports />} />
          </Routes>
        </main>

        {/* FOOTER */}
        <footer
          style={{
            width: "100%",
            padding: "1rem",
            textAlign: "center",
            borderTop: "1px solid #e5e7eb",
            background: "#ffffff",
            color: "#6b7280",
            fontSize: "14px",
          }}
        >
          © {new Date().getFullYear()} FindMe
        </footer>
      </Router>
    </AuthProvider>
  );
}

export default App;

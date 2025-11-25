// src/App.jsx

import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/Navbar";
import { useAuth } from "./context/authContext";

// Pages
import Home from "./pages/Home";
import About from "./pages/About";
import MissingPersons from "./pages/MissingPersons";
import Report from "./pages/Report";
import MyReports from "./pages/MyReports";
import PersonDetails from "./pages/PersonDetails";
import Login from "./pages/Login";
import Register from "./pages/Register";

export default function App() {
  const { isAuthenticated, initialLoading } = useAuth();

  // Prevent flicker while checking token
  if (initialLoading) return <div>Loading…</div>;

  // Wrapper for private routes
  function ProtectedRoute({ children }) {
    if (!isAuthenticated) return <Navigate to="/login" replace />;
    return children;
  }

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
    <Router>
      <Navbar />

      <Routes>
        {/* PUBLIC ROUTES */}
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/missing-persons" element={<MissingPersons />} />

        {/* AUTH ROUTES */}
        <Route
          path="/login"
          element={isAuthenticated ? <Navigate to="/" replace /> : <Login />}
        />

        <Route
          path="/register"
          element={isAuthenticated ? <Navigate to="/" replace /> : <Register />}
        />

        {/* PROTECTED ROUTES */}
        <Route
          path="/report"
          element={
            <ProtectedRoute>
              <Report />
            </ProtectedRoute>
          }
        />

        <Route
          path="/my-reports"
          element={
            <ProtectedRoute>
              <MyReports />
            </ProtectedRoute>
          }
        />

        <Route
          path="/person/:id"
          element={
            <ProtectedRoute>
              <PersonDetails />
            </ProtectedRoute>
          }
        />

        {/* 404 FALLBACK */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

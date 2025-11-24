// src/pages/Login.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  function handleChange(e) {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log("Form submitted:", formData);

    // TEMP: simulate login success
    setTimeout(() => {
      navigate("/");
    }, 500);
  }

  return (
    <div style={styles.wrapper}>
      <div style={styles.card}>
        <h2 style={styles.title}>Login</h2>
        <p style={styles.subtitle}>Access your account to manage your reports.</p>

        <form onSubmit={handleSubmit} style={styles.form}>
          {/* Email */}
          <div style={styles.field}>
            <label style={styles.label}>Email</label>
            <input
              type="email"
              name="email"
              placeholder="e.g. johndoe@gmail.com"
              value={formData.email}
              onChange={handleChange}
              style={styles.input}
              required
            />
          </div>

          {/* Password */}
          <div style={styles.field}>
            <label style={styles.label}>Password</label>
            <input
              type="password"
              name="password"
              placeholder="Enter your password"
              value={formData.password}
              onChange={handleChange}
              style={styles.input}
              required
            />
          </div>

          <button type="submit" style={styles.button}>
            Login
          </button>
        </form>

        {/* Register link */}
        <p style={styles.register}>
          Don’t have an account?{" "}
          <span
            onClick={() => navigate("/register")}
            style={styles.registerLink}
          >
            Register
          </span>
        </p>
      </div>
    </div>
  );
}

/* --------------------------- STYLES --------------------------- */
const styles = {
  wrapper: {
    width: "100%",
    minHeight: "calc(100vh - 120px)", // accounts for navbar + footer
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: "2rem",
    boxSizing: "border-box",
    background: "#f5f6f7",
  },

  card: {
    width: "100%",
    maxWidth: "480px",
    background: "#ffffff",
    borderRadius: "12px",
    padding: "2.5rem",
    boxShadow: "0 4px 16px rgba(0,0,0,0.05)",
  },

  title: {
    fontSize: "1.75rem",
    fontWeight: 700,
    marginBottom: "0.2rem",
    color: "#111827",
  },

  subtitle: {
    fontSize: "0.95rem",
    color: "#6b7280",
    marginBottom: "1.8rem",
  },

  form: {
    display: "flex",
    flexDirection: "column",
    gap: "1.2rem",
  },

  field: {
    display: "flex",
    flexDirection: "column",
    gap: "0.4rem",
  },

  label: {
    fontSize: "0.9rem",
    fontWeight: 600,
    color: "#374151",
  },

  input: {
    padding: "0.75rem",
    borderRadius: "8px",
    border: "1px solid #d1d5db",
    fontSize: "0.95rem",
    outline: "none",
    transition: "0.2s border-color ease",
  },

  button: {
    marginTop: "0.5rem",
    width: "100%",
    padding: "0.9rem",
    border: "none",
    borderRadius: "8px",
    background: "#2563eb",
    color: "#ffffff",
    fontSize: "1rem",
    fontWeight: 600,
    cursor: "pointer",
  },

  register: {
    marginTop: "1.4rem",
    textAlign: "center",
    fontSize: "0.92rem",
    color: "#6b7280",
  },

  registerLink: {
    color: "#2563eb",
    cursor: "pointer",
    fontWeight: 600,
  },
};

export default Login;

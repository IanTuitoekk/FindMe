// src/context/authContext.jsx
import React, { createContext, useContext, useEffect, useState } from "react";

/**
 * AuthContext - provides auth state and helper functions.
 *
 * Notes:
 * - Uses import.meta.env.VITE_API_BASE (set in Vite env) or falls back to default backend host.
 * - login() and register() return { success: boolean, message?: string } so views can react (redirect, show toast).
 * - logout() clears token and user.
 */

const API_BASE = import.meta.env.VITE_API_BASE || "https://findme-backend-2.onrender.com";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => {
    try {
      return localStorage.getItem("fm_token") || null;
    } catch {
      return null;
    }
  });

  const [user, setUser] = useState(null);
  const [initialLoading, setInitialLoading] = useState(true); // while checking existing token
  const [loading, setLoading] = useState(false);

  // helper: store token
  function saveToken(t) {
    setToken(t);
    try {
      if (t) localStorage.setItem("fm_token", t);
      else localStorage.removeItem("fm_token");
    } catch (err) {
      // ignore storage errors
    }
  }

  // call backend to get current user (if token exists)
  async function fetchCurrentUser(currentToken) {
    if (!currentToken) {
      setUser(null);
      return null;
    }

    try {
      const res = await fetch(`${API_BASE}/api/auth/me`, {
        headers: {
          Authorization: `Bearer ${currentToken}`,
        },
      });

      if (!res.ok) {
        // token invalid or expired
        saveToken(null);
        setUser(null);
        return null;
      }

      const data = await res.json();
      setUser(data);
      return data;
    } catch (err) {
      console.error("fetchCurrentUser error", err);
      saveToken(null);
      setUser(null);
      return null;
    }
  }

  // login: send credentials, save token, fetch user
  async function login({ email, password }) {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const json = await res.json();

      if (!res.ok) {
        const message = json?.message || "Login failed";
        setLoading(false);
        return { success: false, message };
      }

      const receivedToken = json?.token || json?.access_token || null;
      if (!receivedToken) {
        setLoading(false);
        return { success: false, message: "No token received from server" };
      }

      saveToken(receivedToken);
      await fetchCurrentUser(receivedToken);

      setLoading(false);
      return { success: true };
    } catch (err) {
      console.error("login error", err);
      setLoading(false);
      return { success: false, message: "Network error" };
    }
  }

  // register: create account, returns result
  async function register({ name, email, password }) {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });

      const json = await res.json();

      if (!res.ok) {
        const message = json?.message || "Registration failed";
        setLoading(false);
        return { success: false, message };
      }

      // if backend returns token right away, save it
      const receivedToken = json?.token || json?.access_token || null;
      if (receivedToken) {
        saveToken(receivedToken);
        await fetchCurrentUser(receivedToken);
      }

      setLoading(false);
      return { success: true };
    } catch (err) {
      console.error("register error", err);
      setLoading(false);
      return { success: false, message: "Network error" };
    }
  }

  // logout
  function logout() {
    saveToken(null);
    setUser(null);
  }

  // initial effect: if token exists, validate and fetch user
  useEffect(() => {
    let active = true;
    (async () => {
      if (token) {
        await fetchCurrentUser(token);
      }
      if (active) setInitialLoading(false);
    })();

    return () => {
      active = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const value = {
    user,
    token,
    loading,
    initialLoading,
    isAuthenticated: Boolean(user && token),
    login,
    register,
    logout,
    fetchCurrentUser, // optional helper
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return ctx;
}

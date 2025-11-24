export default function About() {
  return (
    <div
      style={{
        width: "100%",
        minHeight: "100vh",
        background: "#f7f8fa", // soft neutral background
        padding: "4rem 1rem",
        boxSizing: "border-box",
      }}
    >
      {/* MAIN CONTENT CONTAINER */}
      <div
        style={{
          maxWidth: "850px",
          margin: "0 auto",
          background: "#ffffff",
          padding: "3rem 2rem",
          borderRadius: "12px",
          boxShadow: "0 2px 10px rgba(0,0,0,0.04)",
        }}
      >
        {/* HEADER */}
        <h1
          style={{
            fontSize: "2.4rem",
            fontWeight: 700,
            color: "#111827",
            marginBottom: "1.5rem",
          }}
        >
          About FindMe
        </h1>

        {/* LEAD PARAGRAPH */}
        <p
          style={{
            fontSize: "1.05rem",
            color: "#4b5563",
            lineHeight: "1.7",
            marginBottom: "2.5rem",
          }}
        >
          FindMe is a community-driven platform designed to help families,
          communities, and authorities locate missing persons quickly, safely,
          and effectively through a unified digital system.
        </p>

        {/* DIVIDER */}
        <div
          style={{
            height: "1px",
            background: "#e5e7eb",
            margin: "2.5rem 0",
          }}
        ></div>

        {/* SECTION 1 */}
        <h2
          style={{
            fontSize: "1.6rem",
            fontWeight: 600,
            color: "#111827",
            marginBottom: "1rem",
          }}
        >
          The Challenge
        </h2>

        <p
          style={{
            fontSize: "1rem",
            color: "#4b5563",
            lineHeight: "1.7",
            marginBottom: "2rem",
          }}
        >
          When a loved one goes missing, families often face confusion, delayed
          communication, scattered information, and limited tools to coordinate
          an effective search effort. In these urgent moments, every second
          matters — and information needs to move fast, accurately, and
          reliably.
        </p>

        {/* DIVIDER */}
        <div
          style={{
            height: "1px",
            background: "#e5e7eb",
            margin: "2.5rem 0",
          }}
        ></div>

        {/* SECTION 2 */}
        <h2
          style={{
            fontSize: "1.6rem",
            fontWeight: 600,
            color: "#111827",
            marginBottom: "1rem",
          }}
        >
          Our Solution
        </h2>

        <p
          style={{
            fontSize: "1rem",
            color: "#4b5563",
            lineHeight: "1.7",
            marginBottom: "2rem",
          }}
        >
          FindMe centralizes missing person reports, allowing real-time updates,
          verified information, and quick visibility across communities and
          authorities. The platform brings clarity and structure during one of
          the most stressful situations a family can face.
        </p>

        {/* DIVIDER */}
        <div
          style={{
            height: "1px",
            background: "#e5e7eb",
            margin: "2.5rem 0",
          }}
        ></div>

        {/* SECTION 3 */}
        <h2
          style={{
            fontSize: "1.6rem",
            fontWeight: 600,
            color: "#111827",
            marginBottom: "1rem",
          }}
        >
          How It Works
        </h2>

        <ul
          style={{
            paddingLeft: "1.2rem",
            color: "#4b5563",
            lineHeight: "1.8",
            fontSize: "1rem",
            marginBottom: "2rem",
          }}
        >
          <li>Report missing persons in minutes</li>
          <li>Search and filter active cases easily</li>
          <li>Access detailed profiles and updates</li>
          <li>Share cases with communities instantly</li>
          <li>Help authorities and families coordinate searches</li>
        </ul>

        {/* DIVIDER */}
        <div
          style={{
            height: "1px",
            background: "#e5e7eb",
            margin: "2.5rem 0",
          }}
        ></div>

        {/* SECTION 4 */}
        <h2
          style={{
            fontSize: "1.6rem",
            fontWeight: 600,
            color: "#111827",
            marginBottom: "1rem",
          }}
        >
          Our Mission
        </h2>

        <p
          style={{
            fontSize: "1rem",
            color: "#4b5563",
            lineHeight: "1.7",
          }}
        >
          To empower families and communities with an accessible, secure platform
          that improves how missing person cases are reported, shared, and
          resolved — ensuring that no one goes missing without support.
        </p>
      </div>
    </div>
  );
}

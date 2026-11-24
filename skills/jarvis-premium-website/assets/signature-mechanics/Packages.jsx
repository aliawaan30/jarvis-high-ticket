// Packages or pricing cards, with an optional billing toggle (for example monthly or one-off).
// Prices can stay [placeholders] until the client confirms them. One card can be marked as popular.
import React, { useState } from "react";

export default function Packages({ plans = [], modes, note }) {
  const [m, setM] = useState(0);
  return (
    <div style={{ minWidth: 0 }}>
      {modes && <div role="radiogroup" aria-label="Billing" style={{ display: "inline-flex", padding: 4, borderRadius: 999, border: "1px solid var(--line,#ddd)", marginBottom: 24 }}>
        {modes.map((x, i) => <button key={x} role="radio" aria-checked={m === i} onClick={() => setM(i)} style={{ minHeight: 44, padding: "0 18px", borderRadius: 999, border: 0, background: m === i ? "var(--tab-bg,#222)" : "transparent", color: m === i ? "var(--tab-on,#fff)" : "inherit", font: "500 15px var(--sans,system-ui)", cursor: "pointer" }}>{x}</button>)}</div>}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(min(100%,260px),1fr))", gap: 18, alignItems: "stretch" }}>
        {plans.map((p, i) => (
          <article key={i} style={{ boxSizing: "border-box", position: "relative", display: "flex", flexDirection: "column", gap: 14, padding: 26, borderRadius: 20, border: p.popular ? "2px solid var(--ac,#222)" : "1px solid var(--line,#ddd)", background: "var(--card,#fff)" }}>
            {p.popular && <span style={{ position: "absolute", top: -12, left: 24, background: "var(--ac,#222)", color: "var(--on-ac,#fff)", font: "600 12px var(--sans,system-ui)", padding: "4px 10px", borderRadius: 999 }}>Most chosen</span>}
            <h3 style={{ margin: 0, fontSize: 24 }}>{p.name}</h3>
            <div><b style={{ fontSize: 34, fontWeight: 600 }}>{Array.isArray(p.price) ? p.price[m] : p.price}</b> <span style={{ opacity: 0.7 }}>{Array.isArray(p.unit) ? p.unit[m] : p.unit}</span></div>
            <ul style={{ margin: 0, paddingLeft: 18, display: "grid", gap: 6 }}>{p.features.map((f) => <li key={f}>{f}</li>)}</ul>
            <a href={p.href || "#"} style={{ marginTop: "auto", minHeight: 48, display: "flex", alignItems: "center", justifyContent: "center", borderRadius: 999, textDecoration: "none", fontWeight: 600, background: p.popular ? "var(--ac,#222)" : "transparent", color: p.popular ? "var(--on-ac,#fff)" : "inherit", border: p.popular ? 0 : "1.5px solid currentColor" }}>{p.cta || "Choose"}</a>
          </article>))}
      </div>
      {note && <p style={{ fontSize: 14, opacity: 0.75 }}>{note}</p>}
    </div>
  );
}

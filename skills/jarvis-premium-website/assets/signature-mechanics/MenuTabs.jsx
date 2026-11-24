// A real menu (or price list) with category tabs and dietary or type filters. Real text, not a PDF.
import React, { useState } from "react";

export default function MenuTabs({ sections = [], filters = [] }) {
  const [s, setS] = useState(0); const [f, setF] = useState([]);
  const toggle = (x) => setF(f.includes(x) ? f.filter((y) => y !== x) : [...f, x]);
  const items = (sections[s]?.items || []).filter((it) => f.every((x) => (it.tags || []).includes(x)));
  const pill = (on) => ({ flex: "none", minHeight: 44, padding: "0 16px", borderRadius: 999, border: "1.5px solid var(--tab-border, currentColor)", background: on ? "var(--tab-bg, currentColor)" : "transparent", cursor: "pointer", font: "500 15px var(--sans, system-ui)" });
  return (
    <div style={{ minWidth: 0, maxWidth: "100%" }}>
      <div role="tablist" style={{ display: "flex", gap: 8, overflowX: "auto", paddingBottom: 4 }}>
        {sections.map((x, k) => <button key={k} role="tab" aria-selected={k === s} onClick={() => setS(k)} style={pill(k === s)}><span style={{ color: k === s ? "var(--tab-on, #fff)" : "inherit" }}>{x.name}</span></button>)}
      </div>
      {filters.length > 0 && <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginTop: 12 }} aria-label="Filters">
        {filters.map((x) => <button key={x} aria-pressed={f.includes(x)} onClick={() => toggle(x)} style={{ ...pill(f.includes(x)), minHeight: 36, fontSize: 14 }}><span style={{ color: f.includes(x) ? "var(--tab-on, #fff)" : "inherit" }}>{x}</span></button>)}
      </div>}
      <ul role="tabpanel" style={{ listStyle: "none", padding: 0, margin: "20px 0 0" }}>
        {items.map((it, k) => (
          <li key={k} style={{ boxSizing: "border-box", display: "grid", gridTemplateColumns: "minmax(0,1fr) auto", gap: 12, padding: "16px 0", borderTop: "1px solid var(--line,#ddd)" }}>
            <div><b style={{ fontWeight: 600 }}>{it.name}</b>{it.tags?.length > 0 && <span style={{ fontSize: 13, opacity: 0.7, marginLeft: 8 }}>{it.tags.join(" · ")}</span>}<div style={{ fontSize: 15, opacity: 0.75 }}>{it.desc}</div></div>
            <span style={{ whiteSpace: "nowrap" }}>{it.price}</span>
          </li>))}
        {items.length === 0 && <li style={{ padding: "16px 0", opacity: 0.7 }}>Nothing matches these filters.</li>}
      </ul>
    </div>
  );
}

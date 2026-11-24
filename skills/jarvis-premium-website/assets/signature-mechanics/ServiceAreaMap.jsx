// A stylised, code-built map of the areas served (not a copied map image). Areas highlight from the
// list or the map, by pointer, tap or keyboard. Always includes the list as the text alternative.
import React, { useState } from "react";

export default function ServiceAreaMap({ areas = [], home, accent = "currentColor", width = 700, height = 400, outline, route = false }) {
  // outline: an optional SVG path of the city or region shape (simple, drawn by hand); route: draw the connecting line only when it means something.
  const [on, setOn] = useState(-1);
  return (
    <div style={{ minWidth: 0, maxWidth: "100%", display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(min(100%,300px),1fr))", gap: "clamp(20px,4vw,48px)", alignItems: "center" }}>
      <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label={"Areas served: " + areas.map((a) => a.name).join(", ")} style={{ width: "100%", height: "auto" }}>
        {outline && <path d={outline} fill={accent} opacity="0.06" stroke={accent} strokeOpacity="0.35" strokeWidth="1.5" />}
        {route && home !== undefined && areas.map((a, k) => k !== home && <path key={"r" + k} d={`M${areas[home].x} ${areas[home].y} L${a.x} ${a.y}`} stroke={accent} strokeOpacity="0.35" strokeWidth="1.5" strokeDasharray="4 6" fill="none" />)}
        {areas.map((a, k) => (
          <g key={k} onMouseEnter={() => setOn(k)} onMouseLeave={() => setOn(-1)} style={{ cursor: "default" }}>
            <circle cx={a.x} cy={a.y} r={a.r || 58} fill={accent} opacity={on === k ? 0.26 : 0.1} style={{ transition: "opacity .3s" }} />
            <circle cx={a.x} cy={a.y} r={home === k ? 11 : 8} fill={home === k ? accent : "#fff"} stroke={accent} strokeWidth="2" />
            <text x={a.x + 18} y={a.y + 7} style={{ font: "600 20px var(--sans, system-ui)", fill: "currentColor" }}>{a.name}</text>
          </g>))}
      </svg>
      <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
        {areas.map((a, k) => (
          <li key={k}><button onMouseEnter={() => setOn(k)} onMouseLeave={() => setOn(-1)} onFocus={() => setOn(k)} onBlur={() => setOn(-1)} onClick={() => setOn(on === k ? -1 : k)}
            style={{ width: "100%", minHeight: 44, textAlign: "left", background: "none", border: 0, borderTop: "1px solid var(--line,#ddd)", padding: "10px 0", font: "500 17px var(--sans, system-ui)", color: "inherit", cursor: "pointer", display: "flex", justifyContent: "space-between", gap: 12 }}>
            <span>{a.name}</span><span style={{ opacity: 0.6, fontSize: 14 }}>{a.note || ""}</span></button></li>))}
      </ul>
    </div>
  );
}

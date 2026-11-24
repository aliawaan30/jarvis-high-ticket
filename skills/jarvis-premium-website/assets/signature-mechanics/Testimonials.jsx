// Real reviews only, each with name, date and source (and the owner's reply if any). A swipeable,
// keyboard-friendly row with previous and next buttons. Never invent or edit reviews.
import React, { useRef } from "react";

export default function Testimonials({ reviews = [] }) {
  const track = useRef(null);
  const go = (d) => { const t = track.current; if (!t) return; t.scrollBy({ left: d * t.clientWidth * 0.85, behavior: "smooth" }); };
  if (!reviews.length) return null;
  return (
    <div style={{ minWidth: 0 }}>
      <div ref={track} role="region" aria-label="Customer reviews" tabIndex={0}
        style={{ display: "grid", gridAutoFlow: "column", gridAutoColumns: "min(86%, 420px)", gap: 16, overflowX: "auto", scrollSnapType: "x mandatory", paddingBottom: 8, scrollbarWidth: "none" }}>
        {reviews.map((r, i) => (
          <figure key={i} style={{ boxSizing: "border-box", margin: 0, scrollSnapAlign: "start", background: "var(--card,#fff)", border: "1px solid var(--line,#e5e5e5)", borderRadius: 18, padding: 24, display: "flex", flexDirection: "column", gap: 14 }}>
            {r.rating && <div aria-label={`${r.rating} out of 5 stars`} style={{ color: "var(--ac,#222)", letterSpacing: 2 }}>{"★★★★★".slice(0, r.rating)}</div>}
            <blockquote style={{ margin: 0, fontSize: 18, lineHeight: 1.5 }}>{r.text}</blockquote>
            <figcaption style={{ fontSize: 14, opacity: 0.75, marginTop: "auto" }}>{r.name} · {r.source}{r.date ? " · " + r.date : ""}</figcaption>
            {r.reply && <p style={{ margin: 0, fontSize: 14, borderLeft: "2px solid var(--ac,#222)", paddingLeft: 10 }}><b>Reply from the owner:</b> {r.reply}</p>}
          </figure>))}
      </div>
      <div style={{ display: "flex", gap: 8, marginTop: 12 }}>
        {[-1, 1].map((d) => <button key={d} onClick={() => go(d)} aria-label={d < 0 ? "Previous reviews" : "Next reviews"} style={{ width: 44, height: 44, borderRadius: 999, border: "1.5px solid currentColor", background: "transparent", color: "inherit", cursor: "pointer" }}>{d < 0 ? "<" : ">"}</button>)}
      </div>
    </div>
  );
}

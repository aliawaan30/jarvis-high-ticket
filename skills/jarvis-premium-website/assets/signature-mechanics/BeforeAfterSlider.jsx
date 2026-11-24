// Before and after of real, consented work (or clearly labelled concept work). Drag, tap or use the
// keyboard (a real range input underneath, so it is accessible). Never use generated results.
import React, { useState } from "react";

export default function BeforeAfterSlider({ before, after, beforeLabel = "Before", afterLabel = "After", note = "", ratio = "4/3", start = 50 }) {
  const [v, setV] = useState(start);
  const img = (src) => (typeof src === "string" ? { background: `center/cover url(${src})` } : { background: src?.fill || "#ccc" });
  return (
    <figure style={{ margin: 0, minWidth: 0, width: "100%", maxWidth: "100%" }}>
      <div style={{ position: "relative", width: "100%", aspectRatio: ratio, overflow: "hidden", borderRadius: 14, touchAction: "pan-y", userSelect: "none" }}>
        <div style={{ position: "absolute", inset: 0, ...img(after) }} />
        <div style={{ position: "absolute", inset: 0, ...img(before), clipPath: `inset(0 ${100 - v}% 0 0)` }} />
        <div aria-hidden="true" style={{ position: "absolute", top: 0, bottom: 0, left: `${v}%`, width: 2, background: "#fff", transform: "translateX(-1px)" }}>
          <div style={{ position: "absolute", top: "50%", left: "50%", width: 44, height: 44, borderRadius: "50%", background: "#fff", transform: "translate(-50%,-50%)", boxShadow: "0 4px 14px rgba(0,0,0,.25)", display: "grid", placeItems: "center", font: "600 14px system-ui", color: "#222" }}>&lt;&gt;</div>
        </div>
        <span style={{ position: "absolute", left: 12, top: 12, font: "600 12px system-ui", letterSpacing: ".1em", textTransform: "uppercase", background: "rgba(0,0,0,.55)", color: "#fff", padding: "5px 9px", borderRadius: 999 }}>{beforeLabel}</span>
        <span style={{ position: "absolute", right: 12, top: 12, font: "600 12px system-ui", letterSpacing: ".1em", textTransform: "uppercase", background: "rgba(0,0,0,.55)", color: "#fff", padding: "5px 9px", borderRadius: 999 }}>{afterLabel}</span>
        <input type="range" min="0" max="100" value={v} onChange={(e) => setV(+e.target.value)} aria-label={`${beforeLabel} and ${afterLabel} comparison`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "ew-resize", margin: 0 }} />
      </div>
      {note && <figcaption style={{ fontSize: 14, marginTop: 8, opacity: 0.75 }}>{note}</figcaption>}
    </figure>
  );
}

// A code-built product demo on a phone screen, playing a scripted sequence in a loop (for example an
// AI receptionist: incoming call, the AI answering, the transcript, then a booking card). Pauses off
// screen; shows the final state for reduced motion. Always labelled Demo.
import React, { useEffect, useRef, useState } from "react";

export default function PhoneDemo({ title = "Incoming call", subtitle = "", lines = [], result, label = "Demo", stepMs = 1400 }) {
  const ref = useRef(null); const [n, setN] = useState(0); const total = lines.length + (result ? 1 : 0);
  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) { setN(total); return; }
    let t, visible = false; const io = new IntersectionObserver(([e]) => { visible = e.isIntersecting; });
    io.observe(ref.current);
    const tick = () => { if (visible) setN((k) => (k >= total + 2 ? 0 : k + 1)); t = setTimeout(tick, stepMs); };
    t = setTimeout(tick, stepMs); return () => { clearTimeout(t); io.disconnect(); };
  }, [total, stepMs]);
  return (
    <div ref={ref} style={{ boxSizing: "border-box", width: "min(320px,78vw)", aspectRatio: "9/18", borderRadius: 42, border: "10px solid var(--phone,#111)", background: "#fff", color: "#111", padding: "52px 14px 14px", position: "relative", overflow: "hidden", boxShadow: "0 30px 60px rgba(0,0,0,.18)", margin: "0 auto" }}>
      <span style={{ position: "absolute", top: 14, left: 14, font: "600 10px system-ui", letterSpacing: ".12em", textTransform: "uppercase", border: "1px solid currentColor", borderRadius: 999, padding: "2px 7px" }}>{label}</span>
      <div style={{ textAlign: "center", marginBottom: 10 }}><b style={{ display: "block" }}>{title}</b><span style={{ fontSize: 13, opacity: 0.7 }}>{subtitle}</span></div>
      <div aria-live="polite">{lines.slice(0, n).map((l, i) => (
        <div key={i} style={{ margin: "8px 0", maxWidth: "88%", marginLeft: l.who === "ai" ? 0 : "auto", padding: "9px 12px", borderRadius: 14, fontSize: 14, lineHeight: 1.4, background: l.who === "ai" ? "var(--ac,#222)" : "#F1F1F1", color: l.who === "ai" ? "var(--on-ac,#fff)" : "#111" }}>{l.text}</div>))}
        {result && n > lines.length && <div style={{ marginTop: 12, padding: 12, borderRadius: 14, border: "2px solid var(--ac,#222)", fontSize: 14 }}><b>{result.title}</b><div style={{ opacity: 0.8 }}>{result.text}</div></div>}
      </div>
    </div>
  );
}

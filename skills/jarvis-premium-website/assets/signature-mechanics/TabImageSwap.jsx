// One large image that crossfades when a tab changes (seasons, treatments, packages).
// Real tabs with arrow-key support; on phones the tabs become one scrollable row of pills.
import React, { useState, useRef } from "react";

export default function TabImageSwap({ tabs = [], ratio = "4/3", frame = 18 }) {
  const [i, setI] = useState(0); const refs = useRef([]);
  const key = (e, k) => {
    if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
    const n = (k + (e.key === "ArrowRight" ? 1 : -1) + tabs.length) % tabs.length; setI(n); refs.current[n]?.focus();
  };
  return (
    <div style={{ minWidth: 0, maxWidth: "100%", display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(min(100%,380px),1fr))", gap: "clamp(20px,4vw,56px)", alignItems: "center" }}>
      <div style={{ position: "relative", aspectRatio: ratio, borderRadius: frame, overflow: "hidden" }}>
        {tabs.map((t, k) => <div key={k} aria-hidden={k !== i} style={{ position: "absolute", inset: 0, opacity: k === i ? 1 : 0, transition: "opacity .6s ease", background: t.image ? `center/cover url(${t.image})` : t.fill }} />)}
      </div>
      <div style={{ minWidth: 0 }}>
        <div role="tablist" style={{ display: "flex", gap: 8, overflowX: "auto", paddingBottom: 4, scrollbarWidth: "none" }}>
          {tabs.map((t, k) => (
            <button key={k} ref={(el) => (refs.current[k] = el)} role="tab" aria-selected={k === i} tabIndex={k === i ? 0 : -1}
              onClick={() => setI(k)} onKeyDown={(e) => key(e, k)}
              style={{ flex: "none", minHeight: 44, padding: "0 18px", borderRadius: 999, border: "1.5px solid var(--tab-border, currentColor)", background: k === i ? "var(--tab-bg, currentColor)" : "transparent", cursor: "pointer", font: "500 15px var(--sans, system-ui)" }}>
              <span style={{ color: k === i ? "var(--tab-on, #fff)" : "inherit" }}>{t.label}</span>
            </button>))}
        </div>
        <div role="tabpanel" style={{ marginTop: 20 }}>{tabs[i]?.content}</div>
      </div>
    </div>
  );
}

// Real milestones on a vertical line that draws as the visitor scrolls. Real dates and photos only.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function Timeline({ items = [] }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    const line = el.querySelector("[data-line]"), rows = el.querySelectorAll("[data-tl]");
    if (c.still) { gsap.set(line, { scaleY: 1 }); return; }
    gsap.fromTo(line, { scaleY: 0 }, { scaleY: 1, ease: "none", scrollTrigger: { trigger: el, start: "top 70%", end: "bottom 60%", scrub: true } });
    rows.forEach((r) => gsap.from(r, { y: 24, opacity: 0, duration: 0.7, ease: "power2.out", scrollTrigger: { trigger: r, start: "top 82%" } }));
  });
  return (
    <ol ref={ref} style={{ position: "relative", listStyle: "none", margin: 0, padding: "0 0 0 34px", minWidth: 0 }}>
      <span data-line aria-hidden="true" style={{ position: "absolute", left: 7, top: 6, bottom: 6, width: 2, background: "var(--ac,#222)", transformOrigin: "top" }} />
      {items.map((it, i) => (
        <li key={i} data-tl style={{ position: "relative", padding: "0 0 40px" }}>
          <span aria-hidden="true" style={{ position: "absolute", left: -34, top: 6, width: 16, height: 16, borderRadius: 999, background: "var(--paper,#fff)", border: "2px solid var(--ac,#222)" }} />
          <div style={{ font: "600 14px var(--sans,system-ui)", letterSpacing: ".08em", color: "var(--ac,#222)" }}>{it.date}</div>
          <h3 style={{ margin: "6px 0", fontSize: "clamp(22px,2.4vw,30px)" }}>{it.title}</h3><p style={{ margin: 0, maxWidth: 560, opacity: 0.85 }}>{it.text}</p>
        </li>))}
    </ol>
  );
}

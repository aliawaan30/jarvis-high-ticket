// Layers that move at different speeds as the section scrolls (foreground faster), for depth.
// Pass layers back to front; two layers on phones, none for reduced motion.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function LayeredDepth({ layers = [], height = "100svh", children }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still) return;
    const ls = [...el.querySelectorAll("[data-layer]")];
    (c.phone ? ls.slice(-2) : ls).forEach((l, i, arr) => gsap.to(l, { yPercent: -(i + 1) * (c.phone ? 4 : 8) / arr.length * 2, ease: "none", scrollTrigger: { trigger: el, scrub: true } }));
  });
  return (
    <section ref={ref} style={{ position: "relative", height, overflow: "hidden", minWidth: 0 }}>
      {layers.map((l, i) => <div key={i} data-layer aria-hidden="true" style={{ position: "absolute", left: 0, right: 0, bottom: 0, top: 0, ...l.style }}>{l.node}</div>)}
      <div style={{ position: "relative", zIndex: 2, height: "100%" }}>{children}</div>
    </section>
  );
}

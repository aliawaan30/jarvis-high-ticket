// Wrap an inline SVG diagram. Paths with class "ln" trace in, groups with class "n" fade in,
// in sequence, when the diagram enters; it pauses off screen. Always pass a text alternative.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function DrawDiagram({ children, alt, className = "" }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    const lines = el.querySelectorAll(".ln"), nodes = el.querySelectorAll(".n");
    if (c.still) return;
    lines.forEach((p) => { const L = p.getTotalLength ? p.getTotalLength() : 400; gsap.set(p, { strokeDasharray: L, strokeDashoffset: L }); });
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: "top 80%", toggleActions: "play pause resume pause" } });
    tl.to(lines, { strokeDashoffset: 0, duration: 1, stagger: 0.12, ease: "power2.out" }).from(nodes, { opacity: 0, y: 8, duration: 0.5, stagger: 0.1 }, "-=0.6");
  });
  return (
    <figure ref={ref} className={className} style={{ margin: 0, minWidth: 0, maxWidth: "100%" }}>
      {children}
      <figcaption style={{ position: "absolute", left: -9999 }}>{alt}</figcaption>
    </figure>
  );
}

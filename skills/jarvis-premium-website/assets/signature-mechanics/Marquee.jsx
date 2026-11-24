// An endless row of items (treatment names, logos, portraits). Clipped, pauses on hover, still for reduced motion.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function Marquee({ items = [], speed = 30, gap = 60, className = "" }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still) return;
    const track = el.firstChild; const tw = gsap.to(track, { xPercent: -50, ease: "none", duration: speed, repeat: -1 });
    const p = () => tw.pause(), r = () => tw.resume();
    el.addEventListener("mouseenter", p); el.addEventListener("mouseleave", r);
    return () => { el.removeEventListener("mouseenter", p); el.removeEventListener("mouseleave", r); };
  });
  const row = items.map((t, i) => <span key={i}>{t}</span>);
  return (
    <div ref={ref} className={className} aria-label={items.join(", ")} style={{ overflow: "hidden" }}>
      <div aria-hidden="true" style={{ display: "flex", gap, width: "max-content" }}>{row}{row}</div>
    </div>
  );
}

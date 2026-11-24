// A confirmed figure that counts up once when it enters. Shows the final number for reduced motion.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function CountUp({ to = 0, prefix = "", suffix = "", className = "" }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still) { el.textContent = prefix + to + suffix; return; }
    const o = { v: 0 };
    gsap.to(o, { v: to, duration: 1.4, ease: "power2.out", onUpdate: () => (el.textContent = prefix + Math.round(o.v) + suffix), scrollTrigger: { trigger: el, start: "top 85%" } });
  }, [to]);
  return <span ref={ref} className={className}>{prefix}{to}{suffix}</span>;
}

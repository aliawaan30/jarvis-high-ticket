// The main button drifts toward the pointer on desktop and springs back. A normal link on touch.
import React, { useRef } from "react";
import { gsap, useMotion, isTouch } from "./motion";

export default function MagneticButton({ href = "#", className = "", children, strength = 0.3 }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still || isTouch()) return;
    let px = -1, py = -1;
    const move = (e) => { px = e.clientX; py = e.clientY; const b = el.getBoundingClientRect(); gsap.to(el, { x: (e.clientX - b.left - b.width / 2) * strength, y: (e.clientY - b.top - b.height / 2) * strength * 1.3, duration: 0.4 }); };
    const leave = () => gsap.to(el, { x: 0, y: 0, duration: 0.7, ease: "elastic.out(1,.4)" });
    // Browsers do not fire mouseleave when the page scrolls under a still pointer: spring back on scroll.
    const onScroll = () => { const hit = px >= 0 && document.elementFromPoint(px, py); if (!hit || !el.contains(hit)) leave(); };
    el.addEventListener("mousemove", move); el.addEventListener("mouseleave", leave); window.addEventListener("scroll", onScroll, { passive: true });
    return () => { el.removeEventListener("mousemove", move); el.removeEventListener("mouseleave", leave); window.removeEventListener("scroll", onScroll); };
  });
  return <a ref={ref} href={href} className={className}>{children}</a>;
}

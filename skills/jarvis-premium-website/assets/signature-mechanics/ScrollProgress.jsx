// A thin reading-progress line at the top, in the accent colour. Hidden for reduced motion.
import React, { useEffect, useRef } from "react";

export default function ScrollProgress({ color = "var(--ac,#222)", height = 2 }) {
  const ref = useRef(null);
  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) { ref.current.style.display = "none"; return; }
    let raf = 0; const on = () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(() => { const h = document.documentElement.scrollHeight - innerHeight; ref.current.style.transform = `scaleX(${h > 0 ? scrollY / h : 0})`; }); };
    window.addEventListener("scroll", on, { passive: true }); on(); return () => window.removeEventListener("scroll", on);
  }, []);
  return <div ref={ref} aria-hidden="true" style={{ position: "fixed", top: 0, left: 0, right: 0, height, background: color, transformOrigin: "left", transform: "scaleX(0)", zIndex: 80 }} />;
}

// Bold composition: a giant list where an image follows the pointer over each row (desktop).
// On touch devices each row opens on tap to show its details. No hover-only content.
// The image hides whenever the pointer is not over a row, including while the page scrolls under a
// still pointer, and whenever the list is off screen.
import React, { useRef, useState } from "react";
import { gsap, useMotion, isTouch } from "./motion";

export default function CursorPreviewList({ items = [] }) {
  const ref = useRef(null); const [open, setOpen] = useState(-1);
  useMotion(ref, (c, el) => {
    if (c.still || isTouch()) return;
    const fl = el.querySelector("[data-float]"), pics = fl.querySelectorAll("[data-pic]");
    const rows = [...el.querySelectorAll("[data-row]")];
    let px = -1, py = -1, shown = -1, raf = 0;
    const show = (i) => { if (i === shown) return; shown = i;
      if (i < 0) { gsap.to(fl, { opacity: 0, scale: 0.8, duration: 0.25, overwrite: "auto" }); return; }
      pics.forEach((p, k) => (p.style.opacity = k === i ? 1 : 0)); gsap.to(fl, { opacity: 1, scale: 1, duration: 0.4, overwrite: "auto" }); };
    // Which row is under the pointer right now? Checked on pointer moves AND on scroll, because browsers
    // do not fire mouseleave when the page scrolls under a still pointer (the image would stay stuck on screen).
    const check = () => { raf = 0; if (px < 0) return show(-1);
      const hit = document.elementFromPoint(px, py); const row = hit && hit.closest("[data-row]");
      show(row && el.contains(row) ? rows.indexOf(row) : -1); };
    const move = (e) => { px = e.clientX; py = e.clientY; gsap.to(fl, { x: px, y: py, duration: 0.6, ease: "power3.out" }); if (!raf) raf = requestAnimationFrame(check); };
    const onScroll = () => { if (!raf) raf = requestAnimationFrame(check); };
    const out = () => { px = py = -1; show(-1); };
    window.addEventListener("mousemove", move); window.addEventListener("scroll", onScroll, { passive: true });
    document.addEventListener("mouseleave", out); window.addEventListener("blur", out);
    // Hide whenever the list itself is off screen, whatever the pointer is doing.
    const io = new IntersectionObserver(([e]) => { if (!e.isIntersecting) show(-1); else onScroll(); });
    io.observe(el);
    return () => { window.removeEventListener("mousemove", move); window.removeEventListener("scroll", onScroll); document.removeEventListener("mouseleave", out); window.removeEventListener("blur", out); io.disconnect(); cancelAnimationFrame(raf); gsap.set(fl, { opacity: 0 }); };
  });
  return (
    <div ref={ref} style={{ position: "relative", minWidth: 0, maxWidth: "100%" }}>
      {items.map((it, i) => (
        <div key={i} data-row role="button" tabIndex={0} aria-expanded={open === i}
          onClick={() => setOpen(open === i ? -1 : i)} onKeyDown={(e) => e.key === "Enter" && setOpen(open === i ? -1 : i)}
          style={{ boxSizing: "border-box", display: "grid", gridTemplateColumns: "minmax(0,1fr) auto", gap: 16, alignItems: "baseline", borderTop: "1px solid var(--line,#E4DAD0)", padding: "20px 0", cursor: "pointer" }}>
          <h3 style={{ margin: 0, fontFamily: "var(--serif, Georgia, serif)", fontWeight: 400, fontSize: "clamp(40px,7.4vw,128px)", lineHeight: 0.95, overflowWrap: "anywhere" }}>{it.title}</h3>
          <div style={{ textAlign: "right", fontSize: 15 }}><b style={{ display: "block", fontWeight: 400, fontSize: 24 }}>{it.price}</b>{it.note}</div>
          {open === i && <div style={{ gridColumn: "1 / -1", fontSize: 16 }}>{it.detail}</div>}
        </div>
      ))}
      <div data-float aria-hidden="true" style={{ position: "fixed", left: 0, top: 0, width: 300, aspectRatio: "4/5", borderRadius: "160px 160px 14px 14px", overflow: "hidden", pointerEvents: "none", zIndex: 40, opacity: 0, transform: "translate(-50%,-50%) scale(.8)" }}>
        {items.map((it, i) => <div key={i} data-pic style={{ position: "absolute", inset: 0, opacity: 0, transition: "opacity .35s", background: it.image ? `center/cover url(${it.image})` : it.fill }} />)}
      </div>
    </div>
  );
}

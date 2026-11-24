// An image that unmasks (clip wipe) and settles from a slight zoom as it enters, once.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function ImageReveal({ src, fill, alt = "", ratio = "4/5", radius = 16, from = "bottom" }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still) return;
    const inner = el.firstChild; const start = { bottom: "inset(100% 0 0 0)", left: "inset(0 100% 0 0)", top: "inset(0 0 100% 0)" }[from];
    gsap.fromTo(el, { clipPath: start }, { clipPath: "inset(0% 0 0 0)", duration: 1.2, ease: "power3.inOut", scrollTrigger: { trigger: el, start: "top 82%" } });
    gsap.fromTo(inner, { scale: 1.15 }, { scale: 1, duration: 1.6, ease: "power3.out", scrollTrigger: { trigger: el, start: "top 82%" } });
  });
  return (
    <div ref={ref} role={alt ? "img" : undefined} aria-label={alt || undefined} style={{ position: "relative", aspectRatio: ratio, borderRadius: radius, overflow: "hidden", minWidth: 0 }}>
      <div style={{ position: "absolute", inset: 0, background: src ? `center/cover url(${src})` : fill }} />
    </div>
  );
}

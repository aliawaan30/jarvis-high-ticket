// A hero with a quiet muted loop (often the phone version of a Higgsfield film). The poster shows
// first and stays when autoplay is blocked (Low Power Mode, data saver), for reduced motion, or on failure.
import React, { useEffect, useRef, useState } from "react";

export default function VideoLoopHero({ src, phoneSrc, poster, height = "100svh", children, label }) {
  const v = useRef(null); const [still, setStill] = useState(false);
  useEffect(() => {
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const save = navigator.connection && navigator.connection.saveData;
    if (reduce || save) { setStill(true); return; }
    const el = v.current; if (!el) return;
    el.src = window.matchMedia("(max-width: 860px)").matches && phoneSrc ? phoneSrc : src;
    const p = el.play(); if (p && p.catch) p.catch(() => setStill(true));
    const fail = () => setStill(true); el.addEventListener("error", fail); return () => el.removeEventListener("error", fail);
  }, [src, phoneSrc]);
  return (
    <section aria-label={label} style={{ position: "relative", height, overflow: "hidden", background: poster ? `center/cover url(${poster})` : "#222", minWidth: 0 }}>
      {!still && <video ref={v} muted autoPlay loop playsInline preload="metadata" poster={poster} aria-hidden="true" style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover" }} />}
      <div style={{ position: "absolute", inset: 0, background: "var(--hero-shade, linear-gradient(0deg,rgba(0,0,0,.55),rgba(0,0,0,0) 55%))" }} />
      <div style={{ position: "relative", height: "100%", display: "flex", flexDirection: "column", justifyContent: "flex-end", padding: "0 clamp(20px,3vw,40px) max(8vh,96px)" }}>{children}</div>
    </section>
  );
}

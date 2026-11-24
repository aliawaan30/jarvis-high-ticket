// A gallery of real work in mixed shapes, opening in a lightbox: arrows and swipe to move,
// Escape to close, focus kept inside and returned. Captions carry the real project details.
import React, { useEffect, useRef, useState } from "react";

export default function GalleryLightbox({ items = [] }) {
  const [i, setI] = useState(-1); const opener = useRef(null), box = useRef(null), x0 = useRef(null);
  const close = () => setI(-1); const go = (d) => setI((k) => (k + d + items.length) % items.length);
  useEffect(() => {
    if (i < 0) return; document.documentElement.style.overflow = "hidden"; box.current?.querySelector("button")?.focus();
    const key = (e) => { if (e.key === "Escape") close(); if (e.key === "ArrowRight") go(1); if (e.key === "ArrowLeft") go(-1);
      if (e.key === "Tab") { const f = [...box.current.querySelectorAll("button")]; if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); } else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); } } };
    document.addEventListener("keydown", key);
    return () => { document.documentElement.style.overflow = ""; document.removeEventListener("keydown", key); opener.current?.focus(); };
  }, [i >= 0]);
  const bg = (it) => (it.image ? `center/cover url(${it.image})` : it.fill);
  return (
    <div style={{ minWidth: 0 }}>
      <div style={{ columns: "3 260px", columnGap: 16 }}>
        {items.map((it, k) => <button key={k} onClick={(e) => { opener.current = e.currentTarget; setI(k); }} aria-label={"Open " + it.caption}
          style={{ display: "block", width: "100%", aspectRatio: it.ratio || ["4/5", "1", "3/4", "4/3"][k % 4], marginBottom: 16, border: 0, borderRadius: 14, background: bg(it), cursor: "zoom-in", breakInside: "avoid" }} />)}
      </div>
      {i >= 0 && <div ref={box} role="dialog" aria-modal="true" aria-label={items[i].caption}
        onTouchStart={(e) => (x0.current = e.touches[0].clientX)} onTouchEnd={(e) => { const d = e.changedTouches[0].clientX - x0.current; if (Math.abs(d) > 40) go(d < 0 ? 1 : -1); }}
        style={{ boxSizing: "border-box", position: "fixed", inset: 0, zIndex: 90, background: "rgba(10,10,10,.92)", color: "#fff", display: "grid", gridTemplateRows: "1fr auto", padding: "64px 16px calc(16px + env(safe-area-inset-bottom))" }}>
        <button onClick={close} aria-label="Close" style={{ position: "absolute", top: 12, right: 16, width: 44, height: 44, borderRadius: 999, border: "1.5px solid #fff", background: "transparent", color: "#fff", cursor: "pointer" }}>X</button>
        <div style={{ minHeight: 0, display: "grid", placeItems: "center" }}><div style={{ width: "min(100%, 1000px)", aspectRatio: items[i].ratio || "4/3", maxHeight: "100%", borderRadius: 12, background: bg(items[i]) }} /></div>
        <div style={{ display: "flex", alignItems: "center", gap: 12, justifyContent: "space-between", maxWidth: 1000, width: "100%", margin: "12px auto 0" }}>
          <button onClick={() => go(-1)} aria-label="Previous" style={{ width: 44, height: 44, borderRadius: 999, border: "1.5px solid #fff", background: "transparent", color: "#fff", cursor: "pointer" }}>{"<"}</button>
          <p style={{ margin: 0, textAlign: "center", fontSize: 15 }}>{items[i].caption} <span style={{ opacity: 0.6 }}>({i + 1} of {items.length})</span></p>
          <button onClick={() => go(1)} aria-label="Next" style={{ width: 44, height: 44, borderRadius: 999, border: "1.5px solid #fff", background: "transparent", color: "#fff", cursor: "pointer" }}>{">"}</button></div>
      </div>}
    </div>
  );
}

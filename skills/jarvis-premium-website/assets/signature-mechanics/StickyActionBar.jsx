// Phone-only bottom bar with the main action (and Call). Clear of the home bar (safe area), adds
// matching page padding so it never covers content, and hides while its target section is on screen.
import React, { useEffect, useState } from "react";

export default function StickyActionBar({ action = { label: "Book", href: "#book" }, call, hideOn }) {
  const [hide, setHide] = useState(false);
  useEffect(() => {
    document.body.style.paddingBottom = "calc(84px + env(safe-area-inset-bottom))";
    let io; const t = hideOn && document.querySelector(hideOn);
    if (t && "IntersectionObserver" in window) { io = new IntersectionObserver(([e]) => setHide(e.isIntersecting), { threshold: 0.2 }); io.observe(t); }
    return () => { document.body.style.paddingBottom = ""; io?.disconnect(); };
  }, [hideOn]);
  const b = { flex: 1, display: "flex", alignItems: "center", justifyContent: "center", minHeight: 52, borderRadius: 999, textDecoration: "none", fontWeight: 600 };
  return (
    <div className="sab" aria-hidden={hide} style={{ position: "fixed", left: 12, right: 12, bottom: "calc(12px + env(safe-area-inset-bottom))", zIndex: 65, display: "flex", gap: 8, transform: hide ? "translateY(140%)" : "none", transition: "transform .3s ease" }}>
      <style>{`@media (min-width:861px){.sab{display:none!important}}`}</style>
      {call && <a href={`tel:${call.replace(/[^+\d]/g, "")}`} tabIndex={hide ? -1 : 0} style={{ ...b, background: "var(--paper,#fff)", color: "var(--ink,#111)", border: "1.5px solid var(--ink,#111)" }}>Call</a>}
      <a href={action.href} tabIndex={hide ? -1 : 0} style={{ ...b, background: "var(--ac,#222)", color: "var(--on-ac,#fff)" }}>{action.label}</a>
    </div>
  );
}

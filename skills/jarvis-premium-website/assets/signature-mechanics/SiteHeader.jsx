// Header with desktop links and a phone menu: full screen, large links, Escape closes, focus moves in
// and back, the page cannot scroll behind it. Hides on scroll down and returns on scroll up.
import React, { useEffect, useRef, useState } from "react";

export default function SiteHeader({ logo, links = [], action = { label: "Book", short: "Book", href: "#" }, surface = "light" }) {
  const [open, setOpen] = useState(false); const [hidden, setHidden] = useState(false);
  const btn = useRef(null), panel = useRef(null), last = useRef(0);
  useEffect(() => {
    const on = () => { const y = window.scrollY; setHidden(y > 120 && y > last.current && !open); last.current = y; };
    window.addEventListener("scroll", on, { passive: true }); return () => window.removeEventListener("scroll", on);
  }, [open]);
  useEffect(() => {
    if (!open) return;
    document.documentElement.style.overflow = "hidden";
    const first = panel.current?.querySelector("a,button"); first?.focus();
    const key = (e) => {
      if (e.key === "Escape") setOpen(false);
      if (e.key === "Tab") { const f = [...panel.current.querySelectorAll("a,button")]; const a = f[0], z = f[f.length - 1];
        if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); } else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); } }
    };
    document.addEventListener("keydown", key);
    return () => { document.documentElement.style.overflow = ""; document.removeEventListener("keydown", key); btn.current?.focus(); };
  }, [open]);
  const ink = surface === "dark" ? "var(--on-dark, #F5F2EC)" : "var(--ink, #1A1A1A)";
  return (
    <header className="sh" style={{ position: "fixed", inset: "0 0 auto", zIndex: 70, transform: hidden ? "translateY(-100%)" : "none", transition: "transform .35s ease", color: ink }}>
      <style>{`.sh-bar{box-sizing:border-box;height:72px;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:0 clamp(20px,3vw,40px);background:var(--header-bg,rgba(255,255,255,.86));backdrop-filter:blur(10px)}
.sh-links{display:flex;gap:26px;align-items:center}.sh-links a{text-decoration:none;color:inherit}.sh-menu{display:none}.sh-short{display:none}
.sh-act{display:inline-flex;align-items:center;justify-content:center;height:44px;padding:0 20px;border-radius:999px;background:var(--ac,#222);color:var(--on-ac,#fff);text-decoration:none;font-weight:600;white-space:nowrap}
@media (max-width:860px){.sh-bar{height:64px}.sh-links{display:none}.sh-menu{display:inline-flex}.sh-long{display:none}.sh-short{display:inline}.sh-act{height:40px;padding:0 16px}}`}</style>
      <div className="sh-bar"><div style={{ minWidth: 0, whiteSpace: "nowrap" }}>{logo}</div>
        <nav className="sh-links" aria-label="Main">{links.map((l) => <a key={l.href} href={l.href}>{l.label}</a>)}</nav>
        <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
          <a className="sh-act" href={action.href}><span className="sh-long">{action.label}</span><span className="sh-short">{action.short || action.label}</span></a>
          <button ref={btn} className="sh-menu" aria-expanded={open} aria-controls="sh-panel" aria-label="Menu" onClick={() => setOpen(true)}
            style={{ width: 44, height: 44, borderRadius: 999, border: "1.5px solid currentColor", background: "transparent", color: "inherit", alignItems: "center", justifyContent: "center", cursor: "pointer" }}>
            <svg width="18" height="12" viewBox="0 0 18 12" aria-hidden="true"><path d="M0 1h18M0 6h18M0 11h18" stroke="currentColor" strokeWidth="1.6" /></svg></button></div></div>
      {open && <div id="sh-panel" ref={panel} role="dialog" aria-modal="true" aria-label="Menu"
        style={{ boxSizing: "border-box", position: "fixed", inset: 0, background: "var(--menu-bg,#111)", color: "var(--on-dark,#F5F2EC)", padding: "84px 24px calc(24px + env(safe-area-inset-bottom))", display: "flex", flexDirection: "column", gap: 6 }}>
        <button onClick={() => setOpen(false)} aria-label="Close menu" style={{ position: "absolute", top: 12, right: 20, width: 44, height: 44, borderRadius: 999, border: "1.5px solid currentColor", background: "transparent", color: "inherit", fontSize: 20, cursor: "pointer" }}>&times;</button>
        {links.map((l) => <a key={l.href} href={l.href} onClick={() => setOpen(false)} style={{ fontSize: 34, lineHeight: 1.2, padding: "8px 0", color: "inherit", textDecoration: "none", fontFamily: "var(--serif, Georgia, serif)" }}>{l.label}</a>)}
        <a href={action.href} onClick={() => setOpen(false)} className="sh-act" style={{ marginTop: "auto", height: 52 }}>{action.label}</a>
      </div>}
    </header>
  );
}

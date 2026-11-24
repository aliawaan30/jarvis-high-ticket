// A built-in site check for real browsers and real phones, because the agent cannot run one.
// Active only when the address contains ?qa (or #qa); renders nothing otherwise. Press "Run site check":
// the page scrolls itself top to bottom and reports overflow (with the guilty elements), broken images,
// tap targets under 44 px, browser errors, and the motion setting. "Copy report" puts it on the clipboard
// to paste back to the agent. Remove it, or keep it gated by ?qa, before launch.
import React, { useEffect, useRef, useState } from "react";

const wait = (ms) => new Promise((r) => setTimeout(r, ms));
function describe(el) {
  const cls = typeof el.className === "string" && el.className.trim() ? "." + el.className.trim().split(/\s+/).slice(0, 2).join(".") : "";
  const txt = (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 40);
  return `${el.tagName.toLowerCase()}${el.id ? "#" + el.id : ""}${cls}${txt ? ' "' + txt + '"' : ""}`;
}
function clipped(el) {
  for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
    const s = getComputedStyle(p); if (/(hidden|clip|auto|scroll)/.test(s.overflowX)) return true;
  }
  return false;
}

export default function SiteCheck() {
  const [on, setOn] = useState(false); const [running, setRunning] = useState(false); const [report, setReport] = useState(null);
  const errors = useRef([]);
  useEffect(() => {
    const q = /[?&#]qa\b/.test(window.location.search + window.location.hash); setOn(q); if (!q) return;
    const onErr = (e) => errors.current.push(String(e.message || e.reason || e));
    const orig = console.error; console.error = (...a) => { errors.current.push(a.map(String).join(" ")); orig(...a); };
    window.addEventListener("error", onErr); window.addEventListener("unhandledrejection", onErr);
    return () => { window.removeEventListener("error", onErr); window.removeEventListener("unhandledrejection", onErr); console.error = orig; };
  }, []);
  async function run() {
    setRunning(true); setReport(null);
    // On phones an overflowing page makes the browser zoom out, so innerWidth grows to fit it.
    // Compare against the real screen width instead, and record any zoom-out.
    const touch = matchMedia("(hover: none)").matches;
    const W = touch && window.screen && window.screen.width ? Math.min(window.innerWidth, window.screen.width) : window.innerWidth;
    const zoomedOut = !!(window.visualViewport && window.visualViewport.scale < 0.99) || window.innerWidth > W + 1;
    const start = window.scrollY, over = new Map(); let widest = Math.max(W, zoomedOut ? window.innerWidth : W);
    const steps = 40, H = () => document.documentElement.scrollHeight - window.innerHeight;
    for (let i = 0; i <= steps; i++) {
      window.scrollTo(0, (H() * i) / steps); await wait(140);
      const sw = document.documentElement.scrollWidth; widest = Math.max(widest, sw);
      if (sw > W + 1) document.querySelectorAll("body *").forEach((el) => {
        const r = el.getBoundingClientRect(); if (r.width && r.right > W + 1 && !clipped(el) && !el.closest("[data-sitecheck]")) over.set(describe(el), Math.round(r.right - W));
      });
    }
    window.scrollTo(0, start);
    const imgs = [...document.images].filter((im) => !im.closest("[data-sitecheck]"));
    const broken = imgs.filter((im) => im.complete && im.naturalWidth === 0).map((im) => im.currentSrc || im.src);
    const small = [...document.querySelectorAll("a[href],button,input,select,textarea,[role=button],[role=tab]")].filter((el) => {
      if (el.closest("[data-sitecheck]") || el.type === "hidden" || el.getAttribute("aria-hidden") === "true") return false;
      const r = el.getBoundingClientRect(); const s = getComputedStyle(el);
      return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.position !== "absolute" && (r.height < 44 && r.width < 44 || r.height < 24);
    }).slice(0, 12).map(describe);
    const rep = {
      when: new Date().toISOString(), page: location.pathname, width: W, height: window.innerHeight, touch: matchMedia("(hover: none)").matches,
      reducedMotion: matchMedia("(prefers-reduced-motion: reduce)").matches,
      zoomedOut, overflow: widest > W + 1 ? { widest, elements: [...over.entries()].slice(0, 12).map(([d, px]) => `${d} (+${px}px)`) } : null,
      brokenImages: broken, smallTapTargets: small, errors: [...new Set(errors.current)].slice(0, 10),
    };
    rep.pass = !rep.overflow && !broken.length && !rep.errors.length;
    setReport(rep); setRunning(false);
  }
  const text = report && [
    `SITE CHECK ${report.pass ? "PASSED" : "FOUND PROBLEMS"} at ${report.width} x ${report.height}px (${report.touch ? "touch" : "pointer"}, reduced motion ${report.reducedMotion ? "on" : "off"}), page ${report.page}`,
    report.overflow ? `Overflow: page is ${report.overflow.widest}px wide on a ${report.width}px screen${report.zoomedOut ? " (the phone zoomed the page out to fit it)" : ""}. Elements past the edge:\n- ${report.overflow.elements.join("\n- ")}` : "Overflow: none at any scroll position",
    report.brokenImages.length ? `Broken images:\n- ${report.brokenImages.join("\n- ")}` : "Broken images: none",
    report.smallTapTargets.length ? `Tap targets under 44px (check these):\n- ${report.smallTapTargets.join("\n- ")}` : "Tap targets: all at least 44px",
    report.errors.length ? `Browser errors:\n- ${report.errors.join("\n- ")}` : "Browser errors: none",
  ].join("\n\n");
  if (!on) return null;
  return (
    <div data-sitecheck style={{ boxSizing: "border-box", position: "fixed", left: 12, bottom: 12, zIndex: 2147483000, width: report ? "min(440px, calc(100vw - 24px))" : "auto", maxHeight: "70vh", overflow: "auto", background: "#111", color: "#fff", borderRadius: 14, padding: 14, font: "14px/1.45 system-ui", boxShadow: "0 12px 40px rgba(0,0,0,.35)" }}>
      {!report && <button onClick={run} disabled={running} style={{ minHeight: 44, padding: "0 16px", borderRadius: 999, border: 0, background: "#fff", color: "#111", fontWeight: 600, cursor: "pointer" }}>{running ? "Checking, please wait..." : "Run site check"}</button>}
      {report && <>
        <b style={{ color: report.pass ? "#7EE2A8" : "#FFB4A8" }}>{report.pass ? "Passed" : "Problems found"}</b>
        <pre style={{ whiteSpace: "pre-wrap", font: "13px/1.45 ui-monospace,monospace", margin: "8px 0" }}>{text}</pre>
        <div style={{ display: "flex", gap: 8 }}>
          <button onClick={() => navigator.clipboard?.writeText(text)} style={{ minHeight: 44, padding: "0 14px", borderRadius: 999, border: 0, background: "#fff", color: "#111", fontWeight: 600, cursor: "pointer" }}>Copy report</button>
          <button onClick={() => setReport(null)} style={{ minHeight: 44, padding: "0 14px", borderRadius: 999, border: "1px solid #fff", background: "transparent", color: "#fff", cursor: "pointer" }}>Run again</button></div></>}
    </div>
  );
}

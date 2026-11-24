// Signature: a pinned canvas that plays a frame sequence forward and backward with scroll
// (for example a bare yard growing into a finished garden). Frames come from a Higgsfield film
// between two keyframes, extracted as WebP. Pass separate phone frames when you have them.
// With only a few stills (under 12, for example four shots), it crossfades smoothly between them.
import React, { useRef } from "react";
import { ScrollTrigger, useMotion } from "./motion";

export default function TransformationScroll({ frames = [], phoneFrames, poster, caption, stages = [], label = "Transformation" }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    const list = c.phone && phoneFrames?.length ? phoneFrames : frames;
    const canvas = el.querySelector("canvas"), ctx = canvas.getContext("2d");
    const stageEl = el.querySelector("[data-stage]"), bar = el.querySelector("[data-bar]");
    const imgs = list.map(() => null); let current = 0;
    const load = (i) => { if (imgs[i] || !list[i]) return; const im = new Image(); im.decoding = "async"; im.src = list[i]; im.onload = () => { imgs[i] = im; if (i === current) draw(i); }; };
    function fit() { const d = Math.min(window.devicePixelRatio || 1, 2); canvas.width = canvas.clientWidth * d; canvas.height = canvas.clientHeight * d; draw(current); }
    let mix = 0; // few frames (under 12, for example four stills): crossfade between neighbours instead of jumping
    const few = list.length < 12;
    function paint(im, alpha) {
      const W = canvas.width, H = canvas.height, s = Math.max(W / im.width, H / im.height);
      const w = im.width * s, h = im.height * s; ctx.globalAlpha = alpha; ctx.drawImage(im, (W - w) / 2, (H - h) / 2, w, h); ctx.globalAlpha = 1;
    }
    function draw(i) {
      let k = i; while (k >= 0 && !imgs[k]) k--; const im = imgs[k]; if (!im) return;
      paint(im, 1);
      if (few && mix > 0 && imgs[i + 1]) paint(imgs[i + 1], mix);
    }
    function setProgress(p) {
      const exact = p * (list.length - 1);
      current = few ? Math.floor(exact) : Math.round(exact); mix = few ? exact - Math.floor(exact) : 0;
      if (current >= list.length - 1) { current = list.length - 1; mix = 0; }
      load(current); load(Math.min(list.length - 1, current + (few ? 1 : 4))); draw(current);
      if (bar) bar.style.width = (p * 100) + "%";
      if (stageEl && stages.length) { let t = stages[0][1]; stages.forEach(([at, text]) => { if (p >= at) t = text; }); stageEl.textContent = t; }
    }
    // Load progressively: first frame now, then every fourth, then the rest.
    load(0); list.forEach((_, i) => { if (i % 4 === 0) setTimeout(() => load(i), 30 * i); });
    window.addEventListener("resize", fit); fit();
    if (c.still) { setProgress(1); return () => window.removeEventListener("resize", fit); }
    const st = ScrollTrigger.create({ trigger: el, start: "top top", end: c.desk ? "+=260%" : "+=180%", pin: true, scrub: true, onUpdate: (s) => setProgress(s.progress) });
    list.forEach((_, i) => setTimeout(() => load(i), 400 + 15 * i));
    return () => { st.kill(); window.removeEventListener("resize", fit); };
  });
  return (
    <section ref={ref} aria-label={label} style={{ position: "relative", height: "100svh", overflow: "hidden", background: poster ? `center/cover url(${poster})` : "#cfc6b4" }}>
      <canvas style={{ position: "absolute", inset: 0, width: "100%", height: "100%" }} />
      <div style={{ position: "absolute", inset: 0, background: "linear-gradient(0deg,rgba(0,0,0,.5),rgba(0,0,0,0) 55%)", pointerEvents: "none" }} />
      <div style={{ position: "absolute", left: "clamp(20px,3vw,40px)", right: "clamp(20px,3vw,40px)", bottom: "10vh", color: "#fff" }}>
        <span data-stage style={{ display: "block", font: "600 13px var(--sans, system-ui)", letterSpacing: ".2em", textTransform: "uppercase", marginBottom: 12 }}>{stages[0]?.[1]}</span>
        {caption}
      </div>
      <div style={{ position: "absolute", left: "clamp(20px,3vw,40px)", right: "clamp(20px,3vw,40px)", bottom: "5vh", height: 2, background: "rgba(255,255,255,.3)" }}><i data-bar style={{ display: "block", height: "100%", width: 0, background: "#fff" }} /></div>
    </section>
  );
}

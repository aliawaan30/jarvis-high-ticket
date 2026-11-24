// Signature: one realistic slice of time, pinned. A clock and beats advance with scroll while a
// code-built simulation (messages, inbox, bookings) fills in. Label it Example or Concept.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function StoryScene({ beats = [], items = [], title, label = "Example", bg = ["#F4E6D4", "#F1D2AE"], renderItem }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    const clock = el.querySelector("[data-clock]"), beat = el.querySelector("[data-beat]"), ticks = el.querySelectorAll("[data-tick]");
    const msgs = el.querySelectorAll("[data-item]");
    const show = (i) => { clock.textContent = beats[i][0]; beat.textContent = beats[i][0] + ". " + beats[i][1]; ticks.forEach((t, k) => (t.style.background = k <= i ? "currentColor" : "rgba(0,0,0,.15)")); };
    if (c.still) { show(beats.length - 1); gsap.set(msgs, { opacity: 1, y: 0 }); el.style.background = bg[1]; return; }
    gsap.set(msgs, { opacity: 0, y: 12, scale: 0.96 });
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: "top top", end: c.desk ? "+=260%" : "+=200%", pin: true, scrub: 0.5,
      onUpdate: (s) => show(Math.min(beats.length - 1, Math.floor(s.progress * beats.length))) } });
    tl.to(el, { backgroundColor: bg[1], duration: Math.max(1, msgs.length) }, 0);
    msgs.forEach((m, i) => tl.to(m, { opacity: 1, y: 0, scale: 1, duration: 0.4 }, i).to({}, { duration: 0.6 }));
  });
  return (
    <section ref={ref} style={{ position: "relative", height: "100svh", overflow: "hidden", background: bg[0] }}>
      <div data-clock aria-hidden="true" style={{ position: "absolute", left: "-1vw", top: "50%", transform: "translateY(-50%)", fontFamily: "var(--serif, Georgia, serif)", fontSize: "clamp(140px,34vw,560px)", lineHeight: 0.8, color: "rgba(0,0,0,.08)", whiteSpace: "nowrap", userSelect: "none" }}>{beats[0]?.[0]}</div>
      <div className="story-inner" style={{ boxSizing: "border-box", position: "relative", height: "100%", maxWidth: 1320, margin: "0 auto", padding: "clamp(84px,9vh,110px) clamp(20px,3vw,40px) clamp(100px,8vh,60px)", display: "grid", gridTemplateColumns: "repeat(auto-fit,minmax(min(100%,420px),1fr))", alignItems: "center", alignContent: "center", gap: "clamp(10px,3vw,40px)" }}>
        <div>
          <span style={{ font: "600 12px var(--sans, system-ui)", letterSpacing: ".2em", textTransform: "uppercase" }}>{title} <em style={{ fontStyle: "normal", border: "1px solid currentColor", borderRadius: 999, padding: "2px 8px", marginLeft: 6 }}>{label}</em></span>
          <p data-beat style={{ fontSize: "clamp(17px,1.6vw,20px)", minHeight: 60, maxWidth: 440 }}>{beats[0] && beats[0][0] + ". " + beats[0][1]}</p>
          <div style={{ display: "flex", gap: 6, maxWidth: 440 }}>{beats.map((_, i) => <i key={i} data-tick style={{ flex: 1, height: 3, borderRadius: 3, background: i === 0 ? "currentColor" : "rgba(0,0,0,.15)" }} />)}</div>
        </div>
        <div style={{ justifySelf: "center", width: "min(330px,64vw)" }}>
          {items.map((it, i) => <div key={i} data-item>{renderItem ? renderItem(it, i) : it}</div>)}
        </div>
      </div>
    </section>
  );
}

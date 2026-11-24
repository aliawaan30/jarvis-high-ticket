// A section pins while steps play through: each step holds fully visible, then crossfades
// (text on one side, a visual on the other). Phone and reduced motion: a plain stack with each
// step's visual above its text, no pin.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

const CSS = `
.ps{display:grid;grid-template-columns:1fr;gap:40px;max-width:1240px;margin:0 auto;padding:80px clamp(20px,3vw,40px);overflow-x:clip}
.ps-step{display:grid;gap:14px}.ps-vis-col{display:none}
@media (min-width:861px) and (prefers-reduced-motion:no-preference){
 .ps{min-height:100svh;grid-template-columns:1fr 1fr;align-items:center;gap:60px}
 .ps-stack,.ps-vis-col{display:grid}.ps-stack>*,.ps-vis-col>*{grid-area:1/1}.ps-step .ps-inline{display:none}}
`;

export default function PinnedSteps({ steps = [], renderVisual }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still || c.phone) return;
    const texts = el.querySelectorAll(".ps-step"), vis = el.querySelectorAll(".ps-vis");
    gsap.set([...texts].slice(1), { opacity: 0 }); gsap.set([...vis].slice(1), { opacity: 0 });
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: "top top", end: "+=" + steps.length * 80 + "%", pin: true, scrub: 0.6 } });
    for (let i = 1; i < steps.length; i++) {
      tl.to({}, { duration: 1 })
        .to(texts[i - 1], { opacity: 0, y: -30, duration: 0.35 }).to(vis[i - 1], { opacity: 0, scale: 1.05, duration: 0.35 }, "<")
        .fromTo(texts[i], { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.35 }, "<.1").fromTo(vis[i], { opacity: 0, scale: 1.08 }, { opacity: 1, scale: 1, duration: 0.35 }, "<");
    }
    tl.to({}, { duration: 1 });
  });
  return (
    <section ref={ref} className="ps">
      <style>{CSS}</style>
      <div className="ps-stack">{steps.map((s, i) => (
        <div key={i} className="ps-step">
          <div className="ps-inline">{renderVisual ? renderVisual(s, i) : null}</div>
          <span>{String(i + 1).padStart(2, "0")}</span>
          <h3 style={{ fontSize: "clamp(36px,4.6vw,72px)", margin: 0 }}>{s.title}</h3>
          <p style={{ margin: 0 }}>{s.text}</p>
        </div>))}
      </div>
      <div className="ps-vis-col">{steps.map((s, i) => <div key={i} className="ps-vis">{renderVisual ? renderVisual(s, i) : null}</div>)}</div>
    </section>
  );
}

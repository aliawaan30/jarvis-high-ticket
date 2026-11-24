// Signature: a pinned full-screen scene where light changes as the visitor scrolls
// (night to morning, morning to dusk). Layers crossfade, a light source moves, a giant word lights up.
import React, { useRef } from "react";
import { gsap, SplitText, useMotion } from "./motion";

export default function LightShiftHero({
  word = "Rested.", skies = ["#120E0D", "linear-gradient(180deg,#F3D9BF,#EBB98A 45%,#D9915A 70%,#7A4A35)", "linear-gradient(180deg,#F8EEE2,#F6E7D6 55%,#F1D9BF)"],
  sun = "radial-gradient(circle,#FFF3DF 0%,#F7C98B 38%,rgba(232,150,80,0) 70%)",
  darkText = "#3B2B26", litText = "#1A1513", children, label,
}) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    const layers = el.querySelectorAll("[data-sky]");
    const disk = el.querySelector("[data-sun]");
    const big = el.querySelector("[data-word]");
    const bottom = el.querySelector("[data-bottom]");
    if (c.still) {
      gsap.set(layers, { opacity: 1 }); gsap.set(disk, { top: "12%" }); gsap.set(big, { color: litText }); gsap.set(bottom, { opacity: 1 });
      return;
    }
    const split = new SplitText(big, { type: "chars" });
    gsap.from(split.chars, { yPercent: 40, opacity: 0, duration: 1.2, ease: "power3.out", stagger: 0.06, delay: 0.2 });
    gsap.set(bottom, { opacity: 0, y: 30 });
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: "top top", end: c.desk ? "+=170%" : "+=120%", pin: true, scrub: 0.6 } });
    tl.to(disk, { top: "8%", ease: "none", duration: 1 }, 0)
      .to(layers[1], { opacity: 1, duration: 0.45 }, 0)
      .to(layers[2], { opacity: 1, duration: 0.4 }, 0.55)
      .to(split.chars, { color: litText, stagger: 0.04, duration: 0.4 }, 0.35)
      .to(bottom, { opacity: 1, y: 0, duration: 0.25 }, 0.75);
    return () => split.revert();
  });
  const fill = { position: "absolute", inset: 0 };
  return (
    <section ref={ref} aria-label={label || word} style={{ position: "relative", height: "100svh", overflow: "hidden", background: skies[0].startsWith("#") ? skies[0] : undefined }}>
      {skies.map((s, i) => <div key={i} data-sky style={{ ...fill, background: s, opacity: i === 0 ? 1 : 0 }} />)}
      <div data-sun style={{ position: "absolute", left: "50%", top: "78%", width: "min(62vw,720px)", aspectRatio: "1", borderRadius: "50%", transform: "translateX(-50%)", background: sun }} />
      <div data-word style={{ position: "absolute", left: 0, right: 0, top: "50%", transform: "translateY(-58%)", textAlign: "center", fontSize: "clamp(96px,24vw,420px)", lineHeight: 0.8, letterSpacing: "-0.04em", color: darkText, whiteSpace: "nowrap", fontFamily: "var(--serif, Georgia, serif)" }}>{word}</div>
      <div data-bottom style={{ position: "absolute", left: "clamp(20px,3vw,40px)", right: "clamp(20px,3vw,40px)", bottom: "max(6vh, 96px)" }}>{children}</div>
    </section>
  );
}

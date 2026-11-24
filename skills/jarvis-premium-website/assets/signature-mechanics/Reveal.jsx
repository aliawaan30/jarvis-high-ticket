// Entrance animation that never starts off screen: vertical only, so it can never widen the page.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function Reveal({ as: Tag = "div", y = 28, stagger = 0, children, className = "", ...rest }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still) return;
    const targets = stagger ? el.children : el;
    gsap.from(targets, { y, opacity: 0, duration: 0.85, ease: "power2.out", stagger, scrollTrigger: { trigger: el, start: "top 85%" } });
  });
  return <Tag ref={ref} className={className} {...rest}>{children}</Tag>;
}

// Headline that reveals by words or lines as it enters (or on load). Text stays real text.
import React, { useRef } from "react";
import { gsap, SplitText, useMotion } from "./motion";

export default function KineticHeadline({ as: Tag = "h2", by = "lines", onLoad = false, className = "", children }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still) return;
    const split = new SplitText(el, { type: by, mask: by });
    const parts = by === "words" ? split.words : split.lines;
    gsap.from(parts, {
      yPercent: 110, duration: 1.05, ease: "power3.out", stagger: by === "words" ? 0.06 : 0.09,
      delay: onLoad ? 0.15 : 0,
      scrollTrigger: onLoad ? undefined : { trigger: el, start: "top 82%" },
    });
    return () => split.revert();
  });
  return <Tag ref={ref} className={className}>{children}</Tag>;
}

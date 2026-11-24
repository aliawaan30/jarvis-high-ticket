// A pinned section that scrolls sideways through cards on desktop (gallery, timeline, services);
// a swipe carousel with snapping on phones. Never widens the page.
import React, { useRef } from "react";
import { gsap, useMotion } from "./motion";

export default function HorizontalJourney({ title, children }) {
  const ref = useRef(null);
  useMotion(ref, (c, el) => {
    if (c.still || c.phone) return;
    const track = el.querySelector("[data-track]");
    const dist = () => Math.max(0, track.scrollWidth - el.clientWidth);
    gsap.to(track, { x: () => -dist(), ease: "none", scrollTrigger: { trigger: el, start: "top top", end: () => "+=" + dist(), pin: true, scrub: true, invalidateOnRefresh: true } });
  });
  return (
    <section ref={ref} className="hj" style={{ overflow: "hidden", minWidth: 0 }}>
      <style>{`.hj-track{box-sizing:border-box;display:flex;gap:20px;padding:0 clamp(20px,3vw,40px) 60px;width:max-content}
.hj-track>*{flex:none;width:min(70vw,560px)}
@media (max-width:860px),(prefers-reduced-motion:reduce){.hj-track{width:auto;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none}.hj-track>*{width:84vw;scroll-snap-align:start}}`}</style>
      {title && <div style={{ padding: "100px clamp(20px,3vw,40px) 30px" }}>{title}</div>}
      <div data-track className="hj-track">{children}</div>
    </section>
  );
}

// Shared motion setup for the premium website skill.
// Install in the client's app: gsap@3.15.1 and lenis@1.3.27 (exact versions).
import { useLayoutEffect, useEffect } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";
import Lenis from "lenis";

gsap.registerPlugin(ScrollTrigger, SplitText);
export { gsap, ScrollTrigger, SplitText };

// Breakpoints and preferences used by every mechanic.
export const MQ = {
  motion: "(prefers-reduced-motion: no-preference)",
  still: "(prefers-reduced-motion: reduce)",
  desk: "(min-width: 861px)",
  phone: "(max-width: 860px)",
};
export const isTouch = () => typeof window !== "undefined" && window.matchMedia("(hover: none)").matches;
const useIso = typeof window !== "undefined" ? useLayoutEffect : useEffect;

// Run GSAP code scoped to a ref, with reduced-motion and phone/desktop conditions, and full cleanup.
// fn receives (conditions, scopeElement) and may return a cleanup function.
export function useMotion(scopeRef, fn, deps = []) {
  useIso(() => {
    const el = scopeRef.current;
    if (!el) return;
    const mm = gsap.matchMedia(el);
    mm.add(MQ, (ctx) => fn(ctx.conditions, el));
    return () => mm.revert();
  }, deps);
}

// Smooth scrolling on desktop pointers only, kept in step with ScrollTrigger. Call once in the page root.
export function useSmoothScroll() {
  useEffect(() => {
    if (isTouch() || window.matchMedia(MQ.still).matches) return;
    const lenis = new Lenis();
    lenis.on("scroll", ScrollTrigger.update);
    const tick = (t) => lenis.raf(t * 1000);
    gsap.ticker.add(tick);
    gsap.ticker.lagSmoothing(0);
    return () => { gsap.ticker.remove(tick); lenis.destroy(); };
  }, []);
}

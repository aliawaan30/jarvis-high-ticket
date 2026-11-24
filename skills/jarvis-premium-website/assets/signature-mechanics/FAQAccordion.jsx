// Questions from the research's search layer, as an accessible accordion (one open at a time by
// default). Optionally outputs FAQPage structured data for search engines.
// The questions inherit the site's font; set --faq-font (for example the headline font), --faq-weight
// and --faq-size in the design tokens to style them.
import React, { useState } from "react";

export default function FAQAccordion({ items = [], single = true, schema = true }) {
  const [open, setOpen] = useState([]);
  const toggle = (i) => setOpen(open.includes(i) ? open.filter((x) => x !== i) : single ? [i] : [...open, i]);
  const ld = { "@context": "https://schema.org", "@type": "FAQPage", mainEntity: items.map((q) => ({ "@type": "Question", name: q.q, acceptedAnswer: { "@type": "Answer", text: q.a } })) };
  return (
    <div style={{ minWidth: 0 }}>
      {items.map((q, i) => { const on = open.includes(i); return (
        <div key={i} style={{ borderTop: "1px solid var(--line,#ddd)", ...(i === items.length - 1 ? { borderBottom: "1px solid var(--line,#ddd)" } : {}) }}>
          <h3 style={{ margin: 0 }}><button aria-expanded={on} aria-controls={"faq-" + i} id={"faq-q-" + i} onClick={() => toggle(i)}
            style={{ width: "100%", minHeight: 56, display: "flex", justifyContent: "space-between", alignItems: "center", gap: 16, background: "none", border: 0, padding: "16px 0", textAlign: "left", fontFamily: "var(--faq-font, inherit)", fontWeight: "var(--faq-weight, 500)", fontSize: "var(--faq-size, clamp(17px,1.6vw,20px))", lineHeight: 1.3, color: "inherit", cursor: "pointer" }}>
            <span>{q.q}</span><span aria-hidden="true" style={{ flex: "none", transition: "transform .3s", transform: on ? "rotate(45deg)" : "none", fontSize: 24, color: "var(--ac,currentColor)" }}>+</span></button></h3>
          <div id={"faq-" + i} role="region" aria-labelledby={"faq-q-" + i} hidden={!on} style={{ paddingBottom: 18, maxWidth: 760, opacity: 0.85 }}>{q.a}</div>
        </div>); })}
      {schema && <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(ld) }} />}
    </div>
  );
}

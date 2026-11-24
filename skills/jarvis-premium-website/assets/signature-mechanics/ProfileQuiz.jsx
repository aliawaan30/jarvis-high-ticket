// Three to five questions that recommend a product, service or style, then lead to the main action.
// pick(answers) returns { title, text, href } from the client's real options.
import React, { useState, useRef, useEffect } from "react";

export default function ProfileQuiz({ questions = [], pick, cta = "Book" }) {
  const [a, setA] = useState([]); const res = useRef(null); const step = a.length; const done = step >= questions.length;
  useEffect(() => { if (done) res.current?.focus(); }, [done]);
  const r = done && pick ? pick(a) : null;
  return (
    <div style={{ minWidth: 0 }} aria-live="polite">
      {!done && <div>
        <div style={{ font: "600 12px var(--sans,system-ui)", letterSpacing: ".14em", opacity: 0.7 }}>{step + 1} OF {questions.length}</div>
        <h3 style={{ fontSize: "clamp(24px,2.6vw,34px)", margin: "10px 0 18px" }}>{questions[step].q}</h3>
        <div style={{ display: "grid", gap: 10 }}>{questions[step].options.map((o) => <button key={o} onClick={() => setA([...a, o])}
          style={{ boxSizing: "border-box", width: "100%", minHeight: 52, textAlign: "left", padding: "12px 18px", borderRadius: 14, border: "1.5px solid var(--line,#ccc)", background: "var(--card,#fff)", color: "inherit", font: "500 16px var(--sans,system-ui)", cursor: "pointer" }}>{o}</button>)}</div>
        {step > 0 && <button onClick={() => setA(a.slice(0, -1))} style={{ marginTop: 12, minHeight: 44, background: "none", border: 0, textDecoration: "underline", color: "inherit", cursor: "pointer" }}>Back</button>}
      </div>}
      {done && r && <div ref={res} tabIndex={-1} style={{ boxSizing: "border-box", padding: 26, borderRadius: 20, background: "var(--card,#fff)", border: "1px solid var(--line,#ddd)", outline: "none" }}>
        <div style={{ font: "600 12px var(--sans,system-ui)", letterSpacing: ".14em", color: "var(--ac,#222)" }}>YOUR MATCH</div>
        <h3 style={{ fontSize: "clamp(28px,3vw,40px)", margin: "8px 0" }}>{r.title}</h3><p>{r.text}</p>
        <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}><a href={r.href || "#"} style={{ minHeight: 48, padding: "0 22px", display: "inline-flex", alignItems: "center", borderRadius: 999, background: "var(--ac,#222)", color: "var(--on-ac,#fff)", textDecoration: "none", fontWeight: 600 }}>{cta}</a>
          <button onClick={() => setA([])} style={{ minHeight: 48, background: "none", border: 0, textDecoration: "underline", color: "inherit", cursor: "pointer" }}>Start again</button></div></div>}
    </div>
  );
}

// The enquiry or booking form, wired to the website's own backend (pass onSubmit, which must save
// the enquiry and only then resolve). Labels, validation, a honeypot, a double-submit guard,
// honest success and failure states, and no health details for medical niches.
import React, { useState } from "react";

export default function EnquiryForm({ fields = [{ name: "name", label: "Your name", required: true, autoComplete: "name" }, { name: "email", label: "Email", type: "email", required: true, autoComplete: "email" }, { name: "phone", label: "Phone (optional)", type: "tel", autoComplete: "tel" }, { name: "message", label: "How can we help?", as: "textarea" }],
  onSubmit, submitLabel = "Send", success = "Thanks, we have your request.", failure = "Something went wrong. Please try again.", fallbackPhone, privacyNote }) {
  const [state, setState] = useState("idle"); const [errors, setErrors] = useState({});
  async function submit(e) {
    e.preventDefault(); if (state === "sending") return;
    const fd = new FormData(e.currentTarget); const data = Object.fromEntries(fd.entries());
    if (data._hp) return; const err = {};
    fields.forEach((f) => { const v = (data[f.name] || "").trim(); if (f.required && !v) err[f.name] = "Please fill this in.";
      else if (v && f.type === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v)) err[f.name] = "Please check this email address.";
      else if (v && f.type === "tel" && v.replace(/\D/g, "").length < 7) err[f.name] = "Please check this phone number."; });
    setErrors(err); if (Object.keys(err).length) { e.currentTarget.querySelector(`[name="${Object.keys(err)[0]}"]`)?.focus(); return; }
    setState("sending");
    try { delete data._hp; if (!onSubmit) throw new Error("No submit handler"); await onSubmit(data); setState("done"); e.target.reset(); } catch { setState("error"); }
  }
  const input = { boxSizing: "border-box", width: "100%", minHeight: 48, border: "1px solid var(--field-border,#bbb)", borderRadius: "var(--field-radius,12px)", background: "var(--field-bg,#fff)", padding: "12px 16px", font: "16px var(--sans,system-ui)", color: "inherit" };
  if (state === "done") return <div role="status" style={{ padding: 24, borderRadius: 16, background: "var(--ok-bg,rgba(0,0,0,.05))", fontSize: 18 }}>{success}</div>;
  return (
    <form onSubmit={submit} noValidate style={{ display: "grid", gap: 18, minWidth: 0 }}>
      <input name="_hp" tabIndex={-1} autoComplete="off" aria-hidden="true" style={{ position: "absolute", left: -9999 }} />
      {fields.map((f) => { const Tag = f.as === "textarea" ? "textarea" : "input"; const id = "ef-" + f.name; return (
        <div key={f.name} style={{ display: "grid", gap: 8 }}>
          <label htmlFor={id} style={{ font: "600 13px var(--sans,system-ui)", letterSpacing: ".08em", textTransform: "uppercase" }}>{f.label}</label>
          {f.options ? <select id={id} name={f.name} style={{ ...input, appearance: "none", paddingRight: 44, background: `var(--field-bg,#fff) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16'%3E%3Cpath d='M3 6l5 5 5-5' fill='none' stroke='%23333' stroke-width='1.6'/%3E%3C/svg%3E") no-repeat right 16px center / 16px 16px` }}>{f.options.map((o) => <option key={o}>{o}</option>)}</select>
            : <Tag id={id} name={f.name} type={f.type || "text"} autoComplete={f.autoComplete} rows={Tag === "textarea" ? 4 : undefined} aria-invalid={!!errors[f.name]} aria-describedby={errors[f.name] ? id + "-e" : undefined} style={{ ...input, ...(Tag === "textarea" ? { minHeight: 120, resize: "vertical" } : {}) }} />}
          {errors[f.name] && <span id={id + "-e"} style={{ color: "var(--error,#B42318)", fontSize: 14 }}>{errors[f.name]}</span>}
        </div>); })}
      <button type="submit" disabled={state === "sending"} style={{ boxSizing: "border-box", width: "100%", minHeight: 52, border: 0, borderRadius: 999, background: "var(--ac,#222)", color: "var(--on-ac,#fff)", font: "600 16px var(--sans,system-ui)", cursor: "pointer", opacity: state === "sending" ? 0.7 : 1 }}>{state === "sending" ? "Sending..." : submitLabel}</button>
      {state === "error" && <p role="alert" style={{ color: "var(--error,#B42318)", margin: 0 }}>{failure}{fallbackPhone && <> Or call <a href={`tel:${fallbackPhone.replace(/[^+\d]/g, "")}`}>{fallbackPhone}</a>.</>}</p>}
      {privacyNote && <p style={{ fontSize: 14, opacity: 0.75, margin: 0 }}>{privacyNote}</p>}
    </form>
  );
}

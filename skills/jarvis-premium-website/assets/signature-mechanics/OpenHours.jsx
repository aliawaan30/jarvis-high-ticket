// Opening hours with an "Open now" or "Closed" badge computed in the business's own time zone,
// so visitors in other time zones see the right answer. Hours are 24h strings: { Mon: ["09:00","17:00"] }.
import React, { useEffect, useState } from "react";
const DAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

export function isOpen(hours, timeZone, now = new Date()) {
  const parts = Object.fromEntries(new Intl.DateTimeFormat("en-US", { timeZone, weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false }).formatToParts(now).map((p) => [p.type, p.value]));
  const h = hours[parts.weekday]; if (!h) return false;
  const mins = (+parts.hour % 24) * 60 + +parts.minute; const [a, b] = h.map((t) => +t.slice(0, 2) * 60 + +t.slice(3));
  return mins >= a && mins < b;
}
export default function OpenHours({ hours = {}, timeZone = "America/Chicago", note }) {
  const [open, setOpen] = useState(() => isOpen(hours, timeZone));
  useEffect(() => { const t = setInterval(() => setOpen(isOpen(hours, timeZone)), 60000); return () => clearInterval(t); }, [hours, timeZone]);
  const fmt = (t) => { const [H, M] = t.split(":").map(Number); return `${((H + 11) % 12) + 1}${M ? ":" + String(M).padStart(2, "0") : ""}${H < 12 ? "am" : "pm"}`; };
  return (
    <div style={{ minWidth: 0 }}>
      <span role="status" style={{ display: "inline-flex", alignItems: "center", gap: 8, font: "600 14px var(--sans,system-ui)", padding: "6px 12px", borderRadius: 999, background: open ? "var(--open-bg,#E6F4EA)" : "var(--closed-bg,#F3F3F3)", color: open ? "var(--open,#1E6B3A)" : "inherit" }}>
        <i style={{ width: 8, height: 8, borderRadius: 999, background: "currentColor" }} />{open ? "Open now" : "Closed now"}</span>
      <dl style={{ display: "grid", gridTemplateColumns: "auto 1fr", gap: "6px 24px", margin: "16px 0 0" }}>
        {["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].map((d) => <React.Fragment key={d}><dt style={{ fontWeight: 600 }}>{d}</dt><dd style={{ margin: 0 }}>{hours[d] ? `${fmt(hours[d][0])} to ${fmt(hours[d][1])}` : "Closed"}</dd></React.Fragment>)}
      </dl>
      {note && <p style={{ fontSize: 14, opacity: 0.75 }}>{note}</p>}
    </div>
  );
}

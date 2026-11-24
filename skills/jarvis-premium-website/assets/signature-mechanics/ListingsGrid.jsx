// Real estate listings: filters (type, beds, price), cards with price, beds, baths and area,
// and a stylised map with pins that highlight with their card. Phones: a List or Map toggle.
import React, { useMemo, useState } from "react";

export default function ListingsGrid({ listings = [], types = [], money = (n) => "$" + n.toLocaleString("en-US") }) {
  const [type, setType] = useState("All"); const [beds, setBeds] = useState(0); const [max, setMax] = useState(0); const [hi, setHi] = useState(-1); const [view, setView] = useState("list");
  const prices = listings.map((l) => l.price); const top = Math.max(0, ...prices);
  const shown = useMemo(() => listings.map((l, i) => ({ ...l, i })).filter((l) => (type === "All" || l.type === type) && l.beds >= beds && (!max || l.price <= max)), [listings, type, beds, max]);
  const sel = { boxSizing: "border-box", minHeight: 44, borderRadius: 10, border: "1.5px solid var(--line,#ccc)", padding: "0 12px", font: "500 15px var(--sans, system-ui)", background: "transparent", color: "inherit" };
  return (
    <div className="lg" style={{ minWidth: 0, maxWidth: "100%" }}>
      <style>{`.lg-wrap{display:grid;grid-template-columns:minmax(0,1fr);gap:24px}.lg-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr));gap:18px}.lg-map{display:none}.lg-toggle{display:flex}
@media (min-width:861px){.lg-wrap{grid-template-columns:minmax(0,1.3fr) minmax(0,1fr)}.lg-wrap .lg-map{display:block;position:sticky;top:90px;align-self:start}.lg-toggle{display:none!important}.lg-wrap .lg-list{display:grid}}
.lg-wrap.map .lg-map{display:block}.lg-wrap.map .lg-list{display:none}`}</style>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 10, marginBottom: 20 }}>
        <select aria-label="Property type" value={type} onChange={(e) => setType(e.target.value)} style={sel}>{["All", ...types].map((t) => <option key={t}>{t}</option>)}</select>
        <select aria-label="Bedrooms" value={beds} onChange={(e) => setBeds(+e.target.value)} style={sel}>{[0, 1, 2, 3, 4].map((b) => <option key={b} value={b}>{b ? b + "+ beds" : "Any beds"}</option>)}</select>
        <select aria-label="Maximum price" value={max} onChange={(e) => setMax(+e.target.value)} style={sel}><option value={0}>Any price</option>{[0.5, 0.75, 1].map((f) => Math.round(top * f / 10000) * 10000).filter((v, k, a) => v && a.indexOf(v) === k).map((v) => <option key={v} value={v}>Up to {money(v)}</option>)}</select>
        <div className="lg-toggle" style={{ gap: 6 }}>{["list", "map"].map((v) => <button key={v} aria-pressed={view === v} onClick={() => setView(v)} style={{ ...sel, background: view === v ? "var(--tab-bg, currentColor)" : "transparent" }}><span style={{ color: view === v ? "var(--tab-on,#fff)" : "inherit" }}>{v === "list" ? "List" : "Map"}</span></button>)}</div>
      </div>
      <p aria-live="polite" style={{ fontSize: 14, opacity: 0.7, margin: "0 0 12px" }}>{shown.length} {shown.length === 1 ? "home" : "homes"}</p>
      <div className={"lg-wrap " + view}>
        <div className="lg-list">
          {shown.map((l) => (
            <article key={l.i} onMouseEnter={() => setHi(l.i)} onMouseLeave={() => setHi(-1)} style={{ border: "1px solid var(--line,#ddd)", borderRadius: 14, overflow: "hidden", outline: hi === l.i ? "2px solid currentColor" : "none" }}>
              <div style={{ aspectRatio: "4/3", background: l.image ? `center/cover url(${l.image})` : l.fill }} />
              <div style={{ padding: 14 }}><b style={{ fontSize: 20 }}>{money(l.price)}</b><div style={{ fontSize: 14, opacity: 0.8 }}>{l.beds} beds · {l.baths} baths · {l.area}</div><div style={{ fontSize: 14 }}>{l.address}</div></div>
            </article>))}
        </div>
        <div className="lg-map"><svg viewBox="0 0 400 400" role="img" aria-label="Map of the listed homes" style={{ width: "100%", height: "auto", background: "var(--map,#EEF0EC)", borderRadius: 14 }}>
          {shown.map((l) => <g key={l.i} onMouseEnter={() => setHi(l.i)} onMouseLeave={() => setHi(-1)}><circle cx={l.x} cy={l.y} r={hi === l.i ? 13 : 9} fill={hi === l.i ? "currentColor" : "#fff"} stroke="currentColor" strokeWidth="2" style={{ transition: "r .2s" }} /></g>)}
        </svg></div>
      </div>
    </div>
  );
}

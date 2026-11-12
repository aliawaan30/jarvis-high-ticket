import React, { useState } from 'react';
import { DragDropContext, Droppable, Draggable } from '@hello-pangea/dnd';
import { base44 } from '@/api/base44Client';
import AppShell, { useProfile, label, Empty } from '@/components/hq/AppShell';
import { C, MONO, useRows, CLIENT_STAGES, money } from '@/lib/hq';

const PCT = { Kickoff: 10, Build: 45, Test: 70, Handover: 90, Live: 100 };
const LINE = { Kickoff: '#1E3A50', Build: '#1E4458', Test: C.cyan, Handover: C.amber, Live: C.green };

export default function Clients() {
  const profile = useProfile();
  const { rows, setRows, loading, error } = useRows('Client');
  const [toast, setToast] = useState('');
  const mrr = rows.reduce((s, c) => s + (Number(c.monthly_retainer) || 0), 0);
  async function move(id, to) {
    const c = rows.find((x) => x.id === id); if (!c || c.stage === to) return;
    const from = c.stage;
    setRows((l) => l.map((x) => (x.id === id ? { ...x, stage: to } : x)));
    try { await base44.entities.Client.update(id, { stage: to }); setToast(`Moved ${c.business} to ${to}.${to === 'Live' ? ' Add a case study note for mission 19.' : ''}`); }
    catch { setRows((l) => l.map((x) => (x.id === id ? { ...x, stage: from } : x))); setToast(`Could not move ${c.business}.`); }
  }
  return (
    <AppShell profile={profile}>
      <div><div style={label}>CLIENTS</div><h1 style={{ margin: '6px 0 0', fontSize: 30, fontWeight: 600 }}>{rows.length} {rows.length === 1 ? 'client' : 'clients'}, {money(mrr)} a month recurring</h1></div>
      {error && <div style={{ marginTop: 16, color: C.red }}>{error}</div>}
      {!loading && !error && rows.length === 0 && <div style={{ marginTop: 18 }}><Empty>No clients yet. When a deal is won, Jarvis adds the client here, and you move it from Kickoff to Live.</Empty></div>}
      <DragDropContext onDragEnd={(r) => r.destination && move(r.draggableId, r.destination.droppableId)}>
        <div className="hq-board-wrap" style={{ overflowX: 'auto', marginTop: 20, paddingBottom: 8 }}>
          <div className="hq-board" style={{ '--cols': 5, display: 'grid', gridTemplateColumns: 'repeat(5,minmax(220px,1fr))', gap: 14, minWidth: 1160 }}>
            {CLIENT_STAGES.map((stage) => { const cards = rows.filter((c) => (c.stage || 'Kickoff') === stage); return (
              <Droppable droppableId={stage} key={stage}>{(p, s) => (
                <div ref={p.innerRef} {...p.droppableProps} style={{ display: 'flex', flexDirection: 'column', gap: 10, minHeight: 260, borderRadius: 10, padding: 6, background: s.isDraggingOver ? 'rgba(95,212,234,.07)' : 'transparent', outline: `1px dashed ${s.isDraggingOver ? '#2E6A85' : 'transparent'}` }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', padding: '0 4px 8px', borderBottom: `2px solid ${LINE[stage]}` }}><span style={{ fontSize: 14, fontWeight: 600 }}>{stage}</span><span style={{ fontFamily: MONO, fontSize: 13, color: C.muted }}>{cards.length}</span></div>
                  {cards.map((c, i) => (
                    <Draggable draggableId={c.id} index={i} key={c.id}>{(dp) => (
                      <div ref={dp.innerRef} {...dp.draggableProps} {...dp.dragHandleProps} className="hq-card" style={{ border: `1px solid ${C.line}`, background: 'rgba(13,26,43,.85)', borderRadius: 10, padding: 14, ...dp.draggableProps.style }}>
                        <div style={{ fontSize: 15, fontWeight: 600 }}>{c.business}</div>
                        {c.what && <div style={{ fontSize: 13, color: C.muted, marginTop: 4 }}>{c.what}</div>}
                        <div style={{ height: 6, borderRadius: 3, background: '#142233', marginTop: 12, overflow: 'hidden' }}><div style={{ height: '100%', width: `${PCT[stage]}%`, background: C.cyan }} /></div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 8, fontSize: 12, color: C.muted, gap: 8 }}>
                          <span>{c.go_live_date ? 'Live ' + c.go_live_date : ''}</span>
                          <span style={{ color: C.amber }}>{[c.build_price ? money(c.build_price) : '', c.monthly_retainer ? money(c.monthly_retainer) + '/mo' : ''].filter(Boolean).join(' + ')}</span>
                        </div>
                        <select aria-label={`Move ${c.business} to`} value={c.stage || 'Kickoff'} onChange={(e) => move(c.id, e.target.value)} style={{ marginTop: 10, background: '#0A1626', color: C.muted, border: `1px solid ${C.line}`, borderRadius: 6, fontSize: 12, minHeight: 32 }}>{CLIENT_STAGES.map((s) => <option key={s}>{s}</option>)}</select>
                      </div>)}</Draggable>
                  ))}
                  {p.placeholder}
                </div>)}</Droppable>); })}
          </div>
        </div>
      </DragDropContext>
      {toast && <div role="status" className="hq-rise" style={{ marginTop: 14, display: 'inline-block', border: `1px solid ${C.line2}`, background: '#0A1626', borderRadius: 8, padding: '10px 14px', fontSize: 14 }}>{toast}</div>}
    </AppShell>
  );
}

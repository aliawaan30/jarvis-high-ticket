import React, { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { DragDropContext, Droppable, Draggable } from '@hello-pangea/dnd';
import { base44 } from '@/api/base44Client';
import AppShell, { useProfile, label, Chip, Empty } from '@/components/hq/AppShell';
import { C, MONO, useRows, STAGES, STAGE_LABEL, todayISO, money, logTouch, parseSignals } from '@/lib/hq';

const FILTERS = ['All', 'Due today', 'Tier A', 'From activity'];

export default function Pipeline() {
  const profile = useProfile();
  const { rows, setRows, loading, error } = useRows('Account');
  const touches = useRows('Touch', '-updated_date', 1000);
  const [filter, setFilter] = useState('All');
  const [toast, setToast] = useState('');
  const today = todayISO();

  const dueIds = useMemo(() => new Set(touches.rows.filter((t) => t.status === 'planned' && t.due_date && t.due_date <= today).map((t) => t.account_id)), [touches.rows, today]);
  const keep = (a) => filter === 'All' || (filter === 'Due today' && (dueIds.has(a.id) || a.status === 'replied')) || (filter === 'Tier A' && a.tier === 'A') || (filter === 'From activity' && String(a.source || '').toLowerCase().includes('activity'));
  const live = rows.filter((a) => STAGES.includes(a.status || 'new lead'));

  async function move(id, to) {
    const a = rows.find((x) => x.id === id);
    if (!a || (a.status || 'new lead') === to) return;
    const from = a.status || 'new lead';
    setRows((list) => list.map((x) => (x.id === id ? { ...x, status: to } : x)));
    try {
      await base44.entities.Account.update(id, { status: to });
      await logTouch(a, `Status changed from ${STAGE_LABEL[from]} to ${STAGE_LABEL[to]}`);
      setToast(`Moved ${a.business_name} to ${STAGE_LABEL[to]}. Logged on its timeline.`);
    } catch {
      setRows((list) => list.map((x) => (x.id === id ? { ...x, status: from } : x)));
      setToast(`Could not move ${a.business_name}. Nothing changed.`);
    }
  }

  const onDragEnd = (r) => { if (r.destination) move(r.draggableId, r.destination.droppableId); };
  const value = (list) => money(list.reduce((s, a) => s + (Number(a.value_estimate) || 0), 0));

  return (
    <AppShell profile={profile}>
      <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'flex-end', gap: '16px 24px' }}>
        <div><div style={label}>PIPELINE</div><h1 style={{ margin: '6px 0 0', fontSize: 30, fontWeight: 600 }}>{live.length} leads in play</h1></div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginLeft: 'auto' }}>
          {FILTERS.map((f) => (
            <button key={f} type="button" onClick={() => setFilter(f)} style={{ minHeight: 40, padding: '0 14px', borderRadius: 20, border: `1px solid ${f === filter ? '#2E6A85' : C.line}`, background: f === filter ? 'rgba(95,212,234,.14)' : 'transparent', color: f === filter ? C.text : C.muted, font: `500 13px 'Space Grotesk', sans-serif`, cursor: 'pointer' }}>{f}</button>
          ))}
        </div>
      </div>
      {error && <div style={{ marginTop: 16, color: C.red }}>{error}</div>}
      {!loading && !error && rows.length === 0 && <div style={{ marginTop: 18 }}><Empty>No leads yet. Ask Jarvis to find some, and they appear here as cards you can drag between stages.</Empty></div>}
      <DragDropContext onDragEnd={onDragEnd}>
        <div className="hq-board-wrap" style={{ overflowX: 'auto', marginTop: 20, paddingBottom: 8 }}>
          <div className="hq-board" style={{ display: 'grid', gridTemplateColumns: `repeat(${STAGES.length}, minmax(230px,1fr))`, gap: 14, minWidth: STAGES.length * 236 }}>
            {STAGES.map((stage) => {
              const cards = live.filter((a) => (a.status || 'new lead') === stage).filter(keep);
              return (
                <Droppable droppableId={stage} key={stage}>
                  {(p, snap) => (
                    <div ref={p.innerRef} {...p.droppableProps} style={{ display: 'flex', flexDirection: 'column', gap: 10, minHeight: 320, borderRadius: 10, padding: 6, background: snap.isDraggingOver ? 'rgba(95,212,234,.07)' : 'transparent', outline: `1px dashed ${snap.isDraggingOver ? '#2E6A85' : 'transparent'}` }}>
                      <div style={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', padding: '0 4px 8px', borderBottom: `2px solid ${stage === 'won' ? C.green : ['call booked', 'proposal sent'].includes(stage) ? C.amber : stage === 'replied' ? C.cyan : C.line2}` }}>
                        <span style={{ fontSize: 14, fontWeight: 600 }}>{STAGE_LABEL[stage]}</span>
                        <span style={{ fontFamily: MONO, fontSize: 13, color: C.muted }}>{cards.length} · {value(cards)}</span>
                      </div>
                      {cards.map((a, i) => {
                        const due = dueIds.has(a.id) || a.status === 'replied';
                        const sig = parseSignals(a.signals)[0];
                        return (
                          <Draggable draggableId={a.id} index={i} key={a.id}>
                            {(dp, ds) => (
                              <div ref={dp.innerRef} {...dp.draggableProps} {...dp.dragHandleProps} className="hq-card" style={{ border: `1px solid ${due ? '#6B5320' : C.line}`, background: 'rgba(13,26,43,.85)', borderRadius: 10, padding: '13px 14px', opacity: ds.isDragging ? 0.85 : 1, ...dp.draggableProps.style }}>
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                  <Link to={`/leads/${a.id}`} style={{ fontSize: 15, fontWeight: 600, flex: 1, minWidth: 0, color: C.text, textDecoration: 'none' }}>{a.business_name}</Link>
                                  {a.tier && <Chip text={a.tier} bg={a.tier === 'A' ? 'rgba(95,212,234,.16)' : 'rgba(148,167,186,.14)'} color={a.tier === 'A' ? C.cyan : C.soft} />}
                                </div>
                                <div style={{ fontSize: 13, color: C.muted, marginTop: 4 }}>Owner: {a.owner_name || 'not found'}</div>
                                {sig && <div style={{ fontSize: 13, color: C.soft, marginTop: 8, lineHeight: 1.4 }}>{sig.label}</div>}
                                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 10, fontSize: 12 }}>
                                  <span style={{ width: 7, height: 7, borderRadius: '50%', background: due ? C.amber : C.muted }} />
                                  <span style={{ color: due ? C.amber : C.muted, flex: 1, minWidth: 0, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{a.status === 'replied' ? 'Call now' : (a.next_action || 'No next step')}</span>
                                  <label style={{ position: 'relative' }}>
                                    <span style={{ position: 'absolute', width: 1, height: 1, overflow: 'hidden', clip: 'rect(0 0 0 0)' }}>Move {a.business_name} to</span>
                                    <select value={a.status || 'new lead'} onChange={(e) => move(a.id, e.target.value)} style={{ background: '#0A1626', color: C.muted, border: `1px solid ${C.line}`, borderRadius: 6, fontSize: 12, minHeight: 32, maxWidth: 110 }}>
                                      {STAGES.map((s) => <option key={s} value={s}>{STAGE_LABEL[s]}</option>)}
                                    </select>
                                  </label>
                                </div>
                              </div>
                            )}
                          </Draggable>
                        );
                      })}
                      {p.placeholder}
                    </div>
                  )}
                </Droppable>
              );
            })}
          </div>
        </div>
      </DragDropContext>
      {toast && <div role="status" className="hq-rise" style={{ marginTop: 14, display: 'inline-block', border: `1px solid ${C.line2}`, background: '#0A1626', borderRadius: 8, padding: '10px 14px', fontSize: 14 }}>{toast}</div>}
      <div style={{ marginTop: 14, fontFamily: MONO, fontSize: 12, color: C.faint }}>Drag a card to another stage, or use its Move menu on a phone.</div>
    </AppShell>
  );
}

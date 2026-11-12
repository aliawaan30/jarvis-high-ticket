// The Agency HQ briefing for voice: what Jarvis should know when a voice chat or
// call starts, and what the get-context tool returns mid-call. Built from the
// CRM tables (Account, Touch, Deal, Campaign, Mission) plus the profile goal.
// Every table read is optional: a missing table just leaves its lines out.

function dayKey(tz, d = new Date()) {
  try {
    return new Intl.DateTimeFormat('en-CA', { timeZone: tz || 'UTC', year: 'numeric', month: '2-digit', day: '2-digit' }).format(d);
  } catch { return d.toISOString().slice(0, 10); }
}

async function safeList(entities, name, sort, limit) {
  try {
    const ent = entities[name];
    if (!ent || typeof ent.list !== 'function') return [];
    const rows = await ent.list(sort, limit);
    return Array.isArray(rows) ? rows : [];
  } catch { return []; }
}

const money = (n) => '$' + Math.round(Number(n) || 0).toLocaleString('en-US');

export async function buildCrmBriefing(entities, profile) {
  const tz = typeof profile?.timezone === 'string' ? profile.timezone : '';
  const today = dayKey(tz);
  const month = today.slice(0, 7);
  const [accounts, touches, deals, campaigns, missions] = await Promise.all([
    safeList(entities, 'Account', '-updated_date', 500),
    safeList(entities, 'Touch', '-updated_date', 800),
    safeList(entities, 'Deal', '-updated_date', 200),
    safeList(entities, 'Campaign', '-updated_date', 20),
    safeList(entities, 'Mission', 'number', 30),
  ]);
  const lines = [];
  if (!accounts.length && !deals.length && !missions.length) {
    lines.push('crm: no leads, deals or missions saved yet');
    return lines;
  }

  // Goal and money this month.
  const wonMonth = deals.filter((d) => d.stage === 'won' && String(d.won_date || '').slice(0, 7) === month);
  const cash = wonMonth.reduce((s, d) => s + (Number(d.proposed_price) || 0), 0);
  if (profile?.goal_90_day) lines.push(`goal: ${profile.goal_90_day}. Won this month: ${money(cash)} from ${wonMonth.length} deal${wonMonth.length === 1 ? '' : 's'}.`);

  // Mission.
  if (missions.length) {
    const done = missions.filter((m) => m.status === 'done').length;
    const active = missions.find((m) => m.status === 'active') || missions.find((m) => m.status !== 'done');
    const total = Math.max(missions.length, ...missions.map((m) => Number(m.number) || 0), 19);
    if (active) lines.push(`mission: ${active.number} of ${total}, "${active.name}" (${done} done)`);
  }

  // Today.
  const live = accounts.filter((a) => a.status !== 'do not contact');
  const replied = live.filter((a) => a.status === 'replied');
  const planned = touches.filter((t) => t.status === 'planned' && t.due_date && t.due_date <= today);
  const callsDue = planned.filter((t) => t.channel === 'call');
  const emailsDue = planned.filter((t) => t.channel === 'email');
  const callsDone = touches.filter((t) => t.channel === 'call' && t.status === 'logged' && t.date === today).length;
  lines.push(`today (${today}): ${callsDone} calls logged, ${callsDue.length} calls due, ${emailsDue.length} emails due, ${replied.length} replies waiting`);
  for (const a of replied.slice(0, 4)) {
    lines.push(`reply waiting: ${a.business_name}${a.city ? ' (' + a.city + ')' : ''}${a.phone ? ', phone ' + a.phone : ''}${a.next_action ? '. Next: ' + a.next_action : ''}`);
  }
  for (const t of callsDue.slice(0, 4)) lines.push(`call due: ${t.account_name || 'a lead'} (${t.step || 'call'})`);
  for (const t of emailsDue.slice(0, 3)) lines.push(`email due: ${t.account_name || 'a lead'} (${t.step || 'email'})`);

  // Pipeline.
  const stages = ['new lead', 'contacted', 'replied', 'call booked', 'call done', 'proposal sent', 'won', 'lost'];
  const counts = stages.map((s) => [s, live.filter((a) => (a.status || 'new lead') === s).length]).filter(([, n]) => n);
  if (counts.length) lines.push('pipeline: ' + counts.map(([s, n]) => `${n} ${s}`).join(', ') + ` (${live.length} leads in total)`);

  // Hottest leads with their next step.
  const rank = { 'call booked': 0, 'proposal sent': 1, 'replied': 2, 'call done': 3, 'contacted': 4, 'new lead': 5 };
  const hot = live.filter((a) => a.status in rank && a.status !== 'replied')
    .sort((a, b) => (rank[a.status] - rank[b.status]) || ((a.tier === 'A' ? 0 : 1) - (b.tier === 'A' ? 0 : 1)))
    .slice(0, 6);
  for (const a of hot) {
    lines.push(`lead: ${a.business_name} [${a.status}${a.tier ? ', tier ' + a.tier : ''}]${a.owner_name && !/not found|confirm/i.test(a.owner_name) ? ', owner ' + a.owner_name : ''}${a.next_action ? '. Next: ' + a.next_action + (a.next_action_date ? ' on ' + a.next_action_date : '') : ''}`);
  }

  // Deals in motion.
  for (const d of deals.filter((x) => ['call booked', 'proposal sent'].includes(x.stage)).slice(0, 4)) {
    lines.push(`deal: ${d.account_name || 'a lead'} at ${d.stage}${d.next_action ? '. Next: ' + d.next_action + (d.next_action_date ? ' on ' + d.next_action_date : '') : ''}${d.proposed_price ? ', proposal ' + money(d.proposed_price) : ''}`);
  }

  // Live campaigns.
  for (const c of campaigns.filter((x) => x.status === 'live').slice(0, 2)) {
    lines.push(`campaign: ${c.name}, ${Number(c.sent) || 0} sent, ${Number(c.replies) || 0} replies, ${Number(c.booked) || 0} booked`);
  }

  // Recent activity.
  const recent = touches.filter((t) => t.status !== 'planned' && t.status !== 'cancelled' && (t.summary || t.outcome)).slice(0, 5);
  for (const t of recent) lines.push(`recent: ${t.date || ''} ${t.direction === 'in' ? 'from' : 'to'} ${t.account_name || 'a lead'} by ${t.channel || 'note'}: ${String(t.summary || t.outcome).slice(0, 120)}`);

  return lines;
}

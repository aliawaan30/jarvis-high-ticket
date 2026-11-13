import { good, bad } from './cases.mjs';
const which = process.argv[2];
const { sendCheck } = which === 'old' ? await import('./old.mjs') : await import('/home/claude/b3/apps/agency-hq/source/base44/shared/send-check.ts');
let gp = 0, bb = 0; const fails = [];
for (const [n, c] of good) { let r; try { r = sendCheck(c); } catch (e) { r = { ok: false, reasons: ["CRASH: " + e.message] }; } if (r.ok) gp++; else fails.push(`GOOD BLOCKED: ${n} -> ${r.reasons.join('; ')}`); }
for (const [n, c, want] of bad) { let r; try { r = sendCheck(c); } catch (e) { r = { ok: false, reasons: ["CRASH: " + e.message] }; } const hit = !r.ok && r.reasons.some(x => x.includes(want)); if (hit) bb++; else fails.push(`BAD NOT CAUGHT: ${n} -> ${r.ok ? 'passed' : r.reasons.join('; ')}`); }
console.log(`${which.toUpperCase()}: good passed ${gp}/${good.length}, bad blocked ${bb}/${bad.length}`);
fails.forEach(f => console.log('  ' + f));

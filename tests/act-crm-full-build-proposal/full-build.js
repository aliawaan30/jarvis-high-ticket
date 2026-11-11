(() => {
  'use strict';
  const $=id=>document.getElementById(id);
  const tasks=[['Request entry',12,3],['Proposal and form preparation',20,8],['Document checking and filing',10,4],['Signing and payment follow-up',15,5],['Inspection booking and reminders',10,4],['Internal handover and status checks',8,7]];
  const fmt=n=>new Intl.NumberFormat('en-AU',{maximumFractionDigits:1}).format(n);
  const money=n=>new Intl.NumberFormat('en-AU',{style:'currency',currency:'AUD',maximumFractionDigits:0}).format(n);
  const read=el=>el.value!==''&&el.validity.valid&&Number.isFinite(Number(el.value))?Number(el.value):null;
  tasks.forEach(([name,now,later],i)=>{
    const row=document.createElement('tr');const title=document.createElement('th');title.scope='row';title.textContent=name;row.append(title);
    [now,later].forEach((val,j)=>{const cell=document.createElement('td');const input=document.createElement('input');input.type='number';input.min='0';input.max='10000';input.step='0.1';input.value=val;input.id=`task-${i}-${j}`;input.setAttribute('aria-label',`${name} ${j?'target with CRM':'now'}, minutes per job`);input.addEventListener('input',calculate);cell.append(input);row.append(cell);});
    const cost=document.createElement('td');cost.id=`task-cost-${i}`;row.append(cost);$('cost-rows').append(row);
  });
  function calculate(){
    const volume=read($('volume')),hourly=read($('hourly'));
    const values=tasks.map((_,i)=>[read($(`task-${i}-0`)),read($(`task-${i}-1`))]);
    if(volume===null||hourly===null||values.flat().includes(null)){
      for(const id of ['before-hours','after-hours','current-month','current-year','saved-hours','saved-value'])$(id).textContent='—';
      tasks.forEach((_,i)=>$(`task-cost-${i}`).textContent='—');$('before-bar').style.width='0%';$('after-bar').style.width='0%';$('cost-formula').textContent='Enter valid non-negative figures to calculate the example.';$('cost-warning').textContent='';return;
    }
    const now=values.reduce((sum,v)=>sum+v[0],0),after=values.reduce((sum,v)=>sum+v[1],0);
    const beforeHours=volume*now/60,afterHours=volume*after/60,saved=beforeHours-afterHours,scale=Math.max(beforeHours,afterHours,1);
    values.forEach((v,i)=>$(`task-cost-${i}`).textContent=money(volume*v[0]/60*hourly));
    $('before-hours').textContent=fmt(beforeHours)+' h';$('after-hours').textContent=fmt(afterHours)+' h';
    $('before-bar').style.width=(beforeHours/scale*100)+'%';$('after-bar').style.width=(afterHours/scale*100)+'%';
    $('current-month').textContent=money(beforeHours*hourly);$('current-year').textContent=money(beforeHours*hourly*12);
    $('saved-hours').textContent=fmt(saved)+' h';$('saved-value').textContent=money(saved*hourly);
    $('cost-formula').textContent=`Current cost: ${fmt(volume)} jobs × ${fmt(now)} minutes ÷ 60 × A$${fmt(hourly)}/hour. Proposed handling: ${fmt(after)} minutes per job. Difference: ${fmt(saved)} hours per month.`;
    $('cost-warning').textContent=saved<0?'These inputs show MORE handling time with the proposed CRM. Revisit the process and scope.':'Example only. Confirm both the baseline and proposed handling time with ACT before using this as a savings claim.';
  }
  ['volume','hourly'].forEach(id=>$(id).addEventListener('input',calculate));
  function price(){
    const build=read($('build-fee')),support=read($('support-fee')),tools=read($('tools-fee'));
    [['deposit',.4],['testing-payment',.4],['final-payment',.2]].forEach(([id,share])=>$(id).textContent=build===null?'—':money(build*share));
    $('year-budget').textContent=[build,support,tools].includes(null)?'—':money(build+12*(support+tools));
  }
  ['build-fee','support-fee','tools-fee'].forEach(id=>$(id).addEventListener('input',price));calculate();price();
})();

(() => {
  const demo = [
    {
      label: 'STEP 1 · NEW ENQUIRY', title: 'A lead arrives with an owner and a next step.', state: 'New · assigned', stage: 'New inquiry',
      fields: [['Owner', 'Maya Chen · Sales'], ['Source', 'Website enquiry'], ['Next action', 'Discovery call · 30 Oct'], ['Need', 'Replace spreadsheet handovers']],
      note: 'The enquiry is captured once. The sales owner and follow-up date are visible to the team.',
      ai: 'Maya owns this enquiry. I found two recent contacts from the same company. Review the matches before merging.',
      activity: '09:14 · Enquiry captured · Owner assigned: Maya Chen · Duplicate check: 2 possible matches'
    },
    {
      label: 'STEP 2 · PROPOSAL REVIEW', title: 'A proposal is prepared from approved details.', state: 'Needs approval', stage: 'Proposal review',
      fields: [['Owner', 'Maya Chen · Sales'], ['Scope', 'CRM workflow assessment'], ['Version', 'Proposal v2 · 30 Oct'], ['Approver', 'Jordan Lee · Owner']],
      note: 'The amount and scope are taken from approved fields. The system prepares the document; a person reviews before it is sent.',
      ai: 'I prepared the follow-up from the approved discovery notes. One question about historic migration is still open, so I left that commitment out.',
      activity: '10:32 · Proposal draft prepared · Pending owner approval · No message sent'
    },
    {
      label: 'STEP 3 · ACCEPTED & HANDED OVER', title: 'Accepted work becomes a delivery project.', state: 'Handover ready', stage: 'Won · setup',
      fields: [['Project', 'CRM workflow assessment'], ['Delivery owner', 'Sam Patel · Delivery'], ['Milestones', 'Discovery · Configure · UAT'], ['Source', 'Accepted Proposal v2']],
      note: 'The approved scope, customer contacts, files and agreed dates carry into the new project. Delivery does not retype the sale.',
      ai: 'I created a project setup draft using the accepted proposal. The migration question remains a blocker and has an assigned owner.',
      activity: '14:02 · Proposal accepted · Project draft created · Owner: Sam Patel · 1 blocker assigned'
    },
    {
      label: 'STEP 4 · A BLOCKER IS VISIBLE', title: 'Missing information becomes owned work.', state: 'Blocked · visible', stage: 'Project active',
      fields: [['Blocker', 'Historic data export not received'], ['Owner', 'Maya Chen · Sales'], ['Due', '31 Oct · 3:00 pm'], ['Impact', 'Import mapping cannot be signed off']],
      note: 'A project cannot quietly appear “on track” while a dependency is missing. The blocker has an owner, due date and impact.',
      ai: 'The data export is still missing. I checked the project checklist and found no file attached. Would you like me to prepare a reminder for Maya to review?',
      activity: '08:05 · Blocker overdue · Assigned owner notified in CRM · Reminder is draft only'
    },
    {
      label: 'STEP 5 · ASK JARVIS', title: 'Get a sourced answer and choose what to do.', state: 'Source shown', stage: 'Project active',
      fields: [['Question', 'What is blocking the import?'], ['Answer', 'Customer data export is outstanding'], ['Source', 'Project task · “Provide export”'], ['Next action', 'Prepare reminder for review']],
      note: 'Jarvis answers from records the signed-in person may access. The answer links back to the task and leaves the external message for human approval.',
      ai: 'The import is blocked because the data export has not been received. The assigned task is with Maya and was due 31 Oct. Source: project task “Provide export”.',
      activity: '08:12 · Jarvis answer viewed · Source opened · No external action taken'
    }
  ];

  let index = 0;
  const q = (id) => document.getElementById(id);
  const steps = q('demo-steps');
  const renderDemo = () => {
    const item = demo[index];
    q('demo-label').textContent = item.label;
    q('demo-title').textContent = item.title;
    q('demo-state').textContent = item.state;
    q('demo-stage').textContent = item.stage;
    q('demo-fields').innerHTML = item.fields.map(([k, v]) => `<div class="field-row"><span>${k}</span><b>${v}</b></div>`).join('');
    q('demo-note').textContent = item.note;
    q('demo-ai').textContent = item.ai;
    q('demo-activity').textContent = item.activity;
    q('demo-prev').disabled = index === 0;
    q('demo-next').disabled = index === demo.length - 1;
    steps.querySelectorAll('button').forEach((button, i) => button.setAttribute('aria-current', String(i === index)));
  };
  demo.forEach((item, i) => {
    const button = document.createElement('button');
    button.type = 'button'; button.textContent = String(i + 1); button.setAttribute('aria-label', item.label.toLowerCase());
    button.addEventListener('click', () => { index = i; renderDemo(); });
    steps.append(button);
  });
  q('demo-prev').addEventListener('click', () => { index = Math.max(0, index - 1); renderDemo(); });
  q('demo-next').addEventListener('click', () => { index = Math.min(demo.length - 1, index + 1); renderDemo(); });
  renderDemo();

  const money = (n) => new Intl.NumberFormat('en-AU', { style: 'currency', currency: 'AUD', maximumFractionDigits: 0 }).format(Number.isFinite(n) ? n : 0);
  const getNumber = (id, max = Infinity) => {
    const value = Number(q(id).value);
    return Math.max(0, Math.min(max, Number.isFinite(value) ? value : 0));
  };
  const updateCalc = () => {
    const jobs = getNumber('jobs');
    const minutes = getNumber('minutes');
    const hourly = getNumber('hourly');
    const recovery = getNumber('recover', 100) / 100;
    const oldToolsMonthly = getNumber('current-tools');
    const retainedToolsMonthly = getNumber('retained-tools');
    const newToolsMonthly = getNumber('new-tools');
    const currentLabourAnnual = jobs * minutes / 60 * hourly * 12;
    const releasedAnnual = currentLabourAnnual * recovery;
    const releasedMonthlyHours = jobs * minutes / 60 * recovery;
    const currentToolsAnnual = (oldToolsMonthly + retainedToolsMonthly) * 12;
    const retainedToolsAnnual = retainedToolsMonthly * 12;
    const newToolsAnnual = newToolsMonthly * 12;
    const remainingLabour = currentLabourAnnual - releasedAnnual;
    q('current-value').textContent = money(currentLabourAnnual);
    q('saved-value').textContent = money(releasedAnnual);
    q('saved-hours').textContent = `${new Intl.NumberFormat('en-AU', { maximumFractionDigits: 1 }).format(releasedMonthlyHours)} hours/month at the example recovery rate. This is capacity, not automatic cash savings.`;
    q('stack-labour').textContent = `${money(currentLabourAnnual)}/year`;
    q('stack-tools').textContent = `${money(oldToolsMonthly * 12)}/year`;
    q('retained-tools-total').textContent = `${money(retainedToolsAnnual)}/year`;
    q('today-total').textContent = `${money(currentLabourAnnual + currentToolsAnnual)}/year + unmeasured leakage`;
    q('remaining-labour').textContent = `${money(remainingLabour)}/year`;
    q('retained-tools-post').textContent = `${money(retainedToolsAnnual)}/year`;
    q('new-tools-total').textContent = `${money(newToolsAnnual)}/year${newToolsAnnual === 0 ? ' · vendor quote pending' : ''}`;
    q('future-total').textContent = `${money(remainingLabour + retainedToolsAnnual + newToolsAnnual)}/year remaining capacity + operating cost, before build fee & internal change cost`;
  };
  ['jobs', 'minutes', 'hourly', 'recover', 'current-tools', 'retained-tools', 'new-tools'].forEach((id) => q(id).addEventListener('input', updateCalc));
  updateCalc();

  const links = [...document.querySelectorAll('.rail nav a')];
  const sections = links.map((link) => document.querySelector(link.getAttribute('href'))).filter(Boolean);
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      const current = entries.filter((e) => e.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (!current) return;
      links.forEach((link) => {
        const active = link.getAttribute('href') === `#${current.target.id}`;
        if (active) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-18% 0px -68% 0px', threshold: [0, .1, .3] });
    sections.forEach((section) => observer.observe(section));
  }
})();

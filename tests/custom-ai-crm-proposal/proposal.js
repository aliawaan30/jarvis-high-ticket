(() => {
  const steps = [
    {
      state: 'NEW ENQUIRY', kind: 'ENQUIRY RECORD', title: 'A request arrives with its files.',
      description: 'The request details and submitted plans are kept with one record for staff to review.',
      labels: ['FROM', 'FILES', 'OWNER'], values: ['Website request', 'Plans attached', 'To be assigned'], next: 'Review request',
      note: 'A staff member checks the submission before it becomes a proposal.'
    },
    {
      state: 'STAFF REVIEW', kind: 'QUOTING TASK', title: 'The right person gets the next action.',
      description: 'The quoting owner reviews the request, checks whether information is missing and sees who else is connected to the job.',
      labels: ['ASSIGNED TO', 'CONTACTS', 'STATUS'], values: ['ACT quoting staff', 'Owner · builder · consultants', 'Awaiting review'], next: 'Confirm scope and fee',
      note: 'If plans or project details are missing, the request stays visible for follow-up.'
    },
    {
      state: 'PROPOSAL REVIEW', kind: 'PROPOSAL DRAFT', title: 'ACT reviews the proposal before it goes out.',
      description: 'The CRM uses the selected ACT template and fee schedule to prepare a draft. A staff member confirms the content and documents.',
      labels: ['TEMPLATE', 'PRICE', 'APPROVAL'], values: ['Suggested, then selected', 'ACT-approved schedule', 'Staff review required'], next: 'Approve and send for signing',
      note: 'AI can suggest a template; it cannot set a fee or send an unreviewed proposal.'
    },
    {
      state: 'SIGNING & INVOICE', kind: 'ACCEPTED PROPOSAL', title: 'Signing starts the agreed invoice step.',
      description: 'DocuSign returns signed files to the job. The agreed acceptance rule can then create or prepare the Xero invoice.',
      labels: ['SIGNATURES', 'INVOICE', 'PROJECT'], values: ['Completed envelope', 'Correct type and amount', 'Converted once'], next: 'Check payment status',
      note: 'Signed acceptance and paid status are separate. A sent invoice is not proof of payment.'
    },
    {
      state: 'READY FOR ASSESSMENT', kind: 'PAYMENT HANDOFF', title: 'Confirmed payment creates the next work queue.',
      description: 'The CRM checks the agreed Xero payment state, then makes the assessment task and outstanding requirements visible.',
      labels: ['PAYMENT', 'TASK OWNER', 'FILES'], values: ['Verified in Xero', 'ACT project manager', 'Signed docs on record'], next: 'Complete assessment review',
      note: 'Unpaid or partially paid work remains clearly marked for staff handling under ACT rules.'
    },
    {
      state: 'INSPECTION FOLLOW-UP', kind: 'BOOKING & OUTCOME', title: 'The booking and follow-up stay with the job.',
      description: 'Staff use ACT’s Microsoft inspection calendar. The CRM records the booking and sends only the agreed confirmation or reminder.',
      labels: ['CALENDAR', 'REMINDER', 'REPLY'], values: ['Microsoft 365', 'Day-before, if approved', 'Y / N routed to staff'], next: 'Record the inspection outcome',
      note: 'A change, cancellation or unclear reply becomes a staff action instead of a silent automation.'
    }
  ];

  const buttons = [...document.querySelectorAll('.journey-step')];
  const fields = {
    state: document.querySelector('#screen-state'), kind: document.querySelector('#record-kind'),
    title: document.querySelector('#demo-heading'), description: document.querySelector('#screen-description'),
    next: document.querySelector('#detail-next'), note: document.querySelector('#screen-note'),
    count: document.querySelector('#step-count'), previous: document.querySelector('#previous-step'), nextButton: document.querySelector('#next-step')
  };
  const labelEls = ['a','b','c'].map(x => document.querySelector(`#detail-label-${x}`));
  const valueEls = ['a','b','c'].map(x => document.querySelector(`#detail-value-${x}`));
  let active = 0;

  function showStep(index, moveFocus = false) {
    active = Math.max(0, Math.min(steps.length - 1, index));
    const step = steps[active];
    fields.state.textContent = step.state;
    fields.kind.textContent = step.kind;
    fields.title.textContent = step.title;
    fields.description.textContent = step.description;
    fields.next.textContent = step.next;
    fields.note.textContent = step.note;
    fields.count.textContent = `STEP ${active + 1} / ${steps.length}`;
    step.labels.forEach((label, i) => { labelEls[i].textContent = label; valueEls[i].textContent = step.values[i]; });
    buttons.forEach((button, i) => {
      const selected = i === active;
      button.classList.toggle('is-active', selected);
      button.setAttribute('aria-selected', String(selected));
      button.tabIndex = selected ? 0 : -1;
    });
    fields.previous.disabled = active === 0;
    fields.nextButton.disabled = active === steps.length - 1;
    if (moveFocus) buttons[active].focus();
  }

  buttons.forEach((button, index) => button.addEventListener('click', () => showStep(index)));
  fields.previous.addEventListener('click', () => showStep(active - 1));
  fields.nextButton.addEventListener('click', () => showStep(active + 1));
  document.querySelector('.journey-steps').addEventListener('keydown', event => {
    let destination = active;
    if (event.key === 'ArrowDown' || event.key === 'ArrowRight') destination = (active + 1) % steps.length;
    else if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') destination = (active + steps.length - 1) % steps.length;
    else if (event.key === 'Home') destination = 0;
    else if (event.key === 'End') destination = steps.length - 1;
    else return;
    event.preventDefault();
    showStep(destination, true);
  });
  showStep(0);
})();

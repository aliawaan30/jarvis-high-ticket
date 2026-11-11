'use strict';
// Render only a record supplied by the authorised booking/attendance adapter.
// Query strings, URL visits and browser storage never establish booking or attendance.
function renderBookingRecord(record){
 const el=id=>document.getElementById(id);
 el('confirmation-content').hidden=true;el('booking-action').hidden=false;
 for(const id of ['meeting-details','meeting-action','reschedule-action','email-step'])el(id).hidden=true;
 function link(id,container,url){try{const u=new URL(url);if(u.protocol!=='https:')return;el(id).href=u.href;el(container).hidden=false;}catch{}}
 if(!record||typeof record.id!=='string'||!record.id.trim()){el('status-label').textContent='Your appointment';el('status-title').textContent='We couldn’t verify a booking.';el('status-copy').textContent='Check your calendar invitation or return to the booking page.';return;}
 if(record.status==='cancelled'){el('status-label').textContent='Booking update';el('status-title').textContent='This appointment is no longer booked.';el('status-copy').textContent='Use the booking page if you would like to choose another time.';return;}
 if(!['booked','rescheduled'].includes(record.status)){el('status-label').textContent='Your appointment';el('status-title').textContent='Please check your booking.';el('status-copy').textContent='Check the latest calendar invitation for your appointment.';return;}
 const confirmed=record.attendance==='confirmed';
 el('status-label').textContent=confirmed?'Attendance confirmed':'Final step · action required';
 el('status-title').textContent=confirmed?'You’re confirmed. See you then.':'Your call is booked. Please confirm you’ll attend.';
 el('status-title').classList.toggle('action-required',!confirmed);
 el('status-copy').textContent=confirmed?'Your meeting details are in your calendar invitation.':'Watch the video, then complete the confirmation steps below.';
 el('booking-action').hidden=true;el('confirmation-content').hidden=false;
 const emailAction=!confirmed&&record.attendanceEmailConfigured===true;
 el('email-step').hidden=!emailAction;
 if(emailAction){el('email-instruction').textContent=record.attendanceEmailInstruction||'Open your confirmation email and click “Yes, I’m attending”.';}
 el('calendar-number').textContent=emailAction?'2':'1';
 el('calendar-step').querySelector('h2').lastChild.textContent=confirmed?'Your calendar invitation':'Accept the calendar invitation';
 el('invite-instruction').textContent=confirmed?'Your attendance is confirmed. Use your calendar invitation for the meeting details.':'Open the calendar invitation and accept it if you haven’t already, so the appointment is in your calendar.';
 el('calendar-step').querySelector('.invite-example').hidden=confirmed;
 if(typeof record.displayTime==='string'&&record.displayTime.trim()){el('meeting-details').textContent=record.displayTime;el('meeting-details').hidden=false;}
 link('meeting-link','meeting-action',record.meetingUrl);link('reschedule-link','reschedule-action',record.rescheduleUrl);
}
window.renderBookingRecord=renderBookingRecord;

# Client delivery

What turns a beautiful site into a delivered client website.

## Enquiries and bookings

Learned from the Fernhollow test (18 November 2026): the booking form posted from the visitor's browser straight to a function in a different app (the agent's own space), open to posts from any website. The client's site never saved its own enquiries, nobody was emailed, and the form said "saved" when it was only sent elsewhere.

**The website owns its enquiries. Always.**

1. **One enquiry pipeline for every form** on the site (booking, contact, quote, quiz result): the same backend function in the client's own website app, the same Enquiry table, the same behaviour.
2. **The browser only ever posts to the website's own backend.** Never from the browser to another app, a Superagent, or a third-party URL.
3. **The backend function, in order:**
   1. Re-checks every field on the server (required fields, email and phone format, length limits) and rejects the hidden honeypot field (spam trap).
   2. Saves the enquiry in the website's own Enquiry table: name, contact details, the form's fields, the page it came from, the date, and status "new". Readable only by admins.
   3. Sends two emails straight away (using the app's email integration):
      - **New enquiry alert to the client,** at the enquiry email confirmed in the intake: subject "New [service] request from [name]", every field, the page it came from, and the reply-to set to the visitor's email so the client can answer with one tap.
      - **Confirmation to the visitor,** in the brand's voice: thanks by first name, what happens next and when, the client's phone number, and the reply-to set to the client's email. No marketing without consent.
   4. Optionally forwards a copy to the member's Jarvis or Agency HQ (to show the client's site is working, or for a care plan report), **server to server with a secret key stored in the app's Secrets**, never with an open endpoint. If the forward fails, the enquiry is still saved and the failure is logged for retry.
   5. Answers the browser only after the save succeeded.
4. **Email delivery:** do not rely on the app's built-in email for client alerts: in the Fernhollow test (24 November 2026) alert emails kept failing until a custom email domain was connected. Plan the email setup from the start: connect the client's own domain (or an email service with the domain's records set up) before launch, and test both emails end to end.

   On Base44 (as found on 24 November 2026; check Base44's current documentation): emailing people who are not app users needs a paid plan and the client's own domain connected to the app. In the app's Dashboard, go to Domains, then Sending address, and choose Use your domain; enter a sender name and an address prefix (for example "studio"), choose the domain and connect it. For a domain managed elsewhere, add the three CNAME records Base44 shows (em, s1._domainkey and s2._domainkey) exactly as shown at the domain's DNS provider (a DMARC record is optional but recommended), then press Verify; DNS changes can take up to 48 hours. Domains bought through Base44 are set up automatically. Then send a test enquiry. For launch, send from the client's own domain (for example bookings@clientdomain.com) through an email service with the domain's records set up, so emails reach the inbox instead of spam. The table is the safety copy: if an email fails, the enquiry is still saved and the failure is logged.
5. **Optional for care plans:** a simple Enquiries page behind the client's login listing every enquiry with its status, so the client sees all leads in one place.
6. **Honest messages:** "Thanks, we have your request" only after it was saved in the client's own app. On failure, keep what the visitor typed and show the client's phone number as the fallback. Log every failure.
7. **No open endpoints:** any function that receives enquiries accepts posts only from the client's own site (checked origin) or with a secret key, and is rate limited.
8. For health, dental and medical aesthetics, do not ask for medical details in the form; say "We'll discuss your health history privately at your consultation." Add a short privacy line under the button linking to the privacy page.
9. **Test it end to end** with a real test submission: the record is saved, both emails arrive, the optional forward arrives. Delete the test record afterwards.

## Search basics (SEO)

1. A unique title (about 50 to 60 characters) and description (about 140 to 160) for each page, with the service and city.
2. One H1 per page; headings in order.
3. Descriptive alt text on every meaningful image, free of banned claims.
4. Structured data (JSON-LD) for the business type, for example LocalBusiness, MedicalBusiness or RoofingContractor, using confirmed facts only: name, address, phone, hours, area served.
5. A social preview image and title (Open Graph).
6. A sitemap and a robots file once the domain is connected.
7. Link the client's Google Business Profile, and keep the business name, address and phone identical to it.

## Legal and trust pages

1. A privacy page that matches what the site actually collects and where it goes. Mark it for the client to approve.
2. Terms or disclaimers where the niche requires them (from the research brief).
3. Any required notices from the brief (for example licence numbers in the footer).

## Launch checks (all must pass)

1. No [brackets], placeholder text or test content anywhere.
2. No banned claims from the research brief, including image text and alt text.
3. Every link, phone number and button works; every form posts only to the website's own backend, the test enquiry was saved in its own Enquiry table, and both emails arrived.
4. Desktop, 780 px and 375 px checked; the sticky phone action works.
5. Pages load quickly on a phone connection; films do not load on phones.
6. Required sign-offs are recorded (who, what, date).
7. Titles, descriptions, structured data and social previews are present.

## Domain

1. The client owns the domain in their own account (never the member's).
2. Connect it in the website app's domain settings, following Base44's current steps, and add the DNS records the app shows at the client's domain provider.
3. Check the site loads on the domain with a secure connection (https), then submit the sitemap in Google Search Console under the client's account.

## Handover

Give the client a one-page handover:
1. The live link, and what was built.
2. Where enquiries go, and how to change it.
3. What they own (domain, accounts, media) and what the member manages.
4. How to request changes, and what the monthly care plan covers, if they bought one.

Record the handover date and move the client's stage to Client live in Agency HQ.

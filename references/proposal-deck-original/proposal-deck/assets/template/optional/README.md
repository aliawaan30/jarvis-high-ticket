# Optional modules

Three slides that are not in the default deck. The build only reads `src/`, so nothing in this folder ships until you copy it in.
Each file is a self-contained `<section class="slide">` with its own `<style>` block and a presenter note, written for the
Kestrel Bay Resort example. Port them to a real client the same way as every other slide: facts from the client only, proof as `⟦…⟧`.

**How to add one.** Copy the file into `src/` under a name that sorts into place. The build only picks up files named
`sNN_name.html` (two digits, then an underscore), so a letter suffix such as `s13a_leadform.html` is silently skipped; use
`s13a_leadform.html`, `s29_decision.html`, `s30_finale.html`. Then add its id to the `NAMES` map in `src/script.js` so its nav dot
has a label (`leadform:'The Form', decision:'Next Steps', finale:'Close'`), run `python3 build/build.py`, and screenshot it.

**`s13a_leadform.html`: the enquiry form, exactly as it runs (id `leadform`).** Three paginated phone screens (questions 1–3,
questions 4–6, the buyer's prefilled details with a review box and Confirm & send), then the card the sales team receives, with the
two "verified by code" chips, the six answers, a lead score and a priority that change live as the viewer taps. It opens on the
objection developers usually raise ("a name, an email, and a number that never answers") and the rest of the page answers it. Add it when
the journey film is not used (it puts the form back in front of the client), or when the client says they have been burned by bad leads.
It goes straight after the film, or in the film's place: copy it to `src/s13a_leadform.html`. Its live score is already wired in
`src/script.js` (the `SCORES` block under "instant form", keyed by question index and option text). The six questions and their options must match `source/facts.md`, the film and the `SCORES` keys character for character; if a question changes, change all four.

**`s24_decision.html`: next steps, said softly (id `decision`).** Four stops straight down: today your green light (read the agreement
together, or we send it over), this week the onboarding call, within six days the campaign is live, the same week the first enquiry.
There is no price, no "$0", no signature ask and no cost-of-waiting line, and no buttons. Add it only if the presenter wants a closing
step on screen; leave it out if the price page is where they want to stop. It goes after the package: `s29_decision.html`.

**`s25_finale.html`: the closing page (id `finale`).** A full-screen photo, a two-line headline, one line of the ask, three numbers
(the quarter's planned verified enquiries, which follow the dials; six days to live; one price, all in) and a contact card with the
presenter's monogram, name, title, email and phone. Add it when the deck is sent without a call, so the last page says who to contact
and what happens next. It goes last: `s30_finale.html`. Replace `⟦phone⟧`, the name and the title with the presenter's own, and swap
`assets/ph-night.jpg` for the client's real photography.

**Keep the timing consistent.** Both the next steps and the finale say "live within six days of onboarding", matching the Six-Day
Guarantee on the package page and the week-by-week plan. If the go-live promise changes, change it on every page that states it.

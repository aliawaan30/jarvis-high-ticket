# High Ticket Studio

A word processor and a whiteboard for the high ticket course. Current lesson
order is in data/outline.json. See ../../docs/COURSE-STATUS.md for the current
lesson count and which bodies are still empty. Write them in any order and
draw the layout when words are slower than a picture.

## Open it

Double click `start.command`, or:

    cd studio && python3 server.py

Then go to http://127.0.0.1:4330

## Writing

Click a lesson in the left list. Every lesson has four parts:

- **Title** and **one line promise**, both edited straight on the page.
- **They leave with**, the one thing in their hands at the end. If you cannot
  fill this in, the lesson does not have a point yet.
- **The body**, a normal document. Type.

The toolbar gives you the blocks the finished lesson is built from:

| Button | What it is |
|---|---|
| Heading | A section break inside the lesson |
| Label | The small uppercase line above a block of instructions |
| Prompt box | The dark box they paste into Jarvis |
| Note | The sand coloured aside |
| Example | The worked example, numbers and all |

Enter inside a prompt or note box breaks the line and stays in the box.
Cmd+Enter steps out of the box into a new paragraph. Cmd+S saves immediately,
though it already saves itself about a second after you stop typing.

**Focus** hides the lesson list when you want the page and nothing else.

## Sketching

Each lesson has its own board on the Sketch tab. Box, oval, arrow, line, pen
and text, in six colours and three thicknesses. Move repositions anything you
have already drawn, Delete removes what is selected, Cmd+Z steps back.

Every board also saves a flat picture to `data/sketches/<lesson>.png`, so a
drawing can be handed to someone else without them opening this at all.

## Where the writing lives

    data/outline.json          modules, lesson order, titles
    data/lessons/<id>.json     one file per lesson: fields, body, shapes
    data/sketches/<id>.png     the picture of that lesson's board
    export/COURSE.md           written when you press Export

Plain files, one per lesson. Nothing is trapped in a browser, and the whole
course can be read in a terminal. **Export** rewrites `export/COURSE.md` with
every lesson in order, which is the fastest way to see the shape of the thing
end to end.

## What this is not

It has no access gate and it is not the member facing site. It runs on your
machine only. When the writing is done, the lesson files feed the page builder
in the parent folder, which renders the real pages.

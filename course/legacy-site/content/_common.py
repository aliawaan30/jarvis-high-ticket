# -*- coding: utf-8 -*-
"""Shared helpers for the lesson specs. No em-dashes in anything a member reads.

A blank lesson carries its title, its promise and its step skeleton. Each step
holds a to-fill block listing what belongs there. When you write the lesson for
real, replace that list of hints with real blocks:

    from build import p, ul, prompt, script, see, callout, todo

    ("Run the niche research skill", [
        p("Open Jarvis and give it this."),
        prompt("Run the underserved market research skill for ..."),
        see("a shortlist of five markets with a reason against each one."),
    ]),
"""
from build import todo


def L(title, lede, deliverable, steps, finish, loom=None, intro=None, vidcap=None):
    """One lesson. steps = [(step title, [hint, hint, ...]), ...]"""
    pg = dict(
        title=title,
        lede=lede,
        deliverable=deliverable,
        intro=intro or [],
        steps=[(t, [todo(*hints)]) for t, hints in steps],
        finish=finish,
        loom=loom,
    )
    if vidcap:
        pg["vidcap"] = vidcap
    return pg


def M(slug, num, name, blurb, pages):
    return dict(slug=slug, num=num, name=name, blurb=blurb, pages=pages)

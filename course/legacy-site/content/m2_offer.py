# -*- coding: utf-8 -*-
"""Module 2: the offer. The module everything else depends on."""
from ._common import L, M

MODULE = M(
    slug="m2", num="Module 2", name="The Irresistible Offer",
    blurb="Find a market that is underserved and desperate, work out what you would actually install for them, and turn it into one offer with a promise you can defend. Do not skip this to get to the outreach. The outreach is only as good as this.",
    pages=[
        L(
            "Why People Pay Five Figures",
            "Nobody pays twenty grand for a tool. They pay it for a problem that is costing them more than twenty grand.",
            "A written answer to one question: what has to be true about a business before it will pay you five figures.",
            [
                ("See the difference between a service and an installation", [
                    "A service is a thing you do. An installation changes how the business runs.",
                    "Use two real examples at both prices.",
                ]),
                ("Learn the two offer shapes", [
                    "Repeatable: receptionists, websites, automations, the same thing many times.",
                    "Custom: an audit, then an implementation built for that one business.",
                    "Say plainly which one suits them right now and why.",
                ]),
                ("Do the maths on one real business", [
                    "Pick a business they know. Put a number on the problem.",
                    "The promise has to come out of the number, not out of the air.",
                ]),
            ],
            ("You Know What You Are Looking For",
             "Now go and find the market that has it worst."),
        ),
        L(
            "Find the Underserved Markets",
            "The first research skill. It hunts for markets that are starved of a solution and have the money to fix it.",
            "A shortlist of five markets with the evidence behind each one, and one chosen.",
            [
                ("Run the market research skill", [
                    "The exact prompt and the inputs it needs.",
                    "What a good run looks like versus a lazy one.",
                ]),
                ("Read the shortlist properly", [
                    "What makes a market real: volume, money, pain, no incumbent.",
                    "The traps: too big, too regulated, too cheap, too far from them.",
                ]),
                ("Pick one and write why", [
                    "Make them commit in writing, in Jarvis, with the reason.",
                    "Second and third stay on the bench, they do not get worked.",
                ]),
            ],
            ("You Have a Market",
             "Next, work out exactly what you would build for them."),
        ),
        L(
            "Find the Custom Implementations",
            "The second research skill. It digs into one market and finds the specific builds those businesses crave.",
            "A written brief on your market: who buys, what hurts, what gets installed, what it is worth to them.",
            [
                ("Run the implementation research skill", [
                    "Point it at the market from the last lesson.",
                    "What it goes looking for: workflows, tools, bottlenecks, where the money leaks.",
                ]),
                ("Interrogate the output", [
                    "Three questions that separate a real finding from a plausible one.",
                    "Make Jarvis show where each claim came from.",
                ]),
                ("Turn it into one offer brief", [
                    "Both research skills land in the same brief format.",
                    "Who buys, their pain, what gets installed, why they pay.",
                ]),
            ],
            ("You Have a Brief",
             "Bring it to the strategy session and get it chosen properly."),
        ),
        L(
            "The Offer Strategy Session",
            "You have done the research. This is where the buyer, the problem and the promise get locked.",
            "One buyer, one problem, one promise, written down and signed off.",
            [
                ("Bring your brief", [
                    "What to have ready before the session.",
                    "How the session runs and how long it takes.",
                ]),
                ("Choose the buyer and the problem", [
                    "Record a real session with a member making this choice.",
                    "Show the wrong answer being talked out of them.",
                ]),
                ("Write the promise", [
                    "A promise is a result by a date, with a boundary.",
                    "Examples at both offer shapes, including the audit and transformation shape.",
                ]),
            ],
            ("The Offer Is Chosen",
             "Before you promise it, make sure it can be built."),
            vidcap="A real strategy session with a member, start to finish.",
        ),
        L(
            "Scope It With a Technical Partner",
            "Never sell something you have not had scoped. This is the step that keeps a signed deal from becoming a disaster.",
            "A scope you can sell from: how it gets built, what it costs you, what you can promise, what you will not.",
            [
                ("Write the scoping request", [
                    "Template, so the partner can answer in one pass.",
                    "What to include: workflow, systems, volumes, integrations.",
                ]),
                ("Get the three answers", [
                    "Can it be built, what does delivery cost, how long does it take.",
                    "Anything the partner flags as risky goes out of the promise.",
                ]),
                ("Set your floor price", [
                    "Delivery cost, your time, your margin.",
                    "Say the actual numbers out loud in the video.",
                ]),
            ],
            ("The Offer Is Real",
             "Now write it so somebody else can understand it in thirty seconds."),
        ),
        L(
            "Write the Offer",
            "One page. Who it is for, what it does, what it costs, what happens if it works.",
            "Your offer written on one page, ready to be read out on a call or sent as a link.",
            [
                ("Write the four parts", [
                    "Problem, promise, mechanism, proof. In that order.",
                    "Keep the mechanism simple enough to explain on a phone call.",
                ]),
                ("Price it", [
                    "Price against the value of the problem, never against your hours.",
                    "Deposit and milestone structure.",
                ]),
                ("Pressure test it", [
                    "Prompt that makes Jarvis attack the offer as a sceptical buyer.",
                    "Fix what it breaks, then run it again.",
                ]),
            ],
            ("You Have an Offer",
             "One thing missing. They need to see it working."),
        ),
        L(
            "Build the Demo",
            "A prospect who can see it is a different conversation to a prospect who has to imagine it.",
            "A working demo in your market, personalised enough that a prospect sees their own business in it.",
            [
                ("Pick the demo from the library", [
                    "What is in the library and which demo fits which offer.",
                ]),
                ("Personalise it", [
                    "Their market, their language, their numbers.",
                    "How far to take it before it is wasted work.",
                ]),
                ("Learn to walk someone through it", [
                    "Ninety seconds, three beats, no feature tour.",
                    "Where the demo sits in the two call close.",
                ]),
            ],
            ("Module 2 Done",
             "An offer, a scope, a price and a demo. Now go and find people to show it to."),
        ),
    ],
)

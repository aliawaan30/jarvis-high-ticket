# -*- coding: utf-8 -*-
"""Module 7: fulfilment. Two sections, arbitrage and self delivery."""
from ._common import L, M

MODULE = M(
    slug="m7", num="Module 7", name="Fulfilment",
    blurb="Two ways to deliver what you just sold. Arbitrage means somebody technical builds it and you own the client. Self fulfilment means you and Jarvis build it. Most people end up doing both, one per deal.",
    pages=[
        L(
            "Two Ways To Deliver",
            "You have money in the bank and a promise to keep. The first decision is who builds it.",
            "A decision rule you can apply to any signed deal: arbitrage it or build it yourself.",
            [
                ("Compare the two honestly", [
                    "Margin, speed, risk, what you learn, what happens when it breaks.",
                    "Real numbers on one deal done both ways.",
                ]),
                ("Learn the decision rule", [
                    "Complexity, integrations, deadline, your own skill.",
                    "The deals you should never try to build yourself.",
                ]),
                ("Apply it to your deal", [
                    "Make the call in writing before anything gets built.",
                ]),
            ],
            ("You Know Who Is Building It",
             "If it is somebody else, the next two lessons are yours."),
        ),
        L(
            "Arbitrage: Find and Vet Developers",
            "Your job is the client and the money. Their job is the build. Getting this bench right is the whole model.",
            "Two or three vetted builders you can actually hand work to, with rates agreed.",
            [
                ("Know what you are hiring for", [
                    "The stack your offers need. What they must have done before.",
                ]),
                ("Find them", [
                    "Where to look, what to post, how to shortlist fast.",
                    "Access to the technical partner network and how that works.",
                ]),
                ("Vet with a paid test", [
                    "Small paid task, real deadline, what you are grading.",
                    "Never put an untested builder on a client deal.",
                ]),
                ("Agree rates and terms", [
                    "Fixed scope versus hourly. Who owns the code. Communication rules.",
                ]),
            ],
            ("You Have a Bench",
             "Now hand work over without losing control of it."),
        ),
        L(
            "Arbitrage: Scope, Hand Off, Keep the Margin",
            "A bad handover is how a profitable deal turns into three weeks of unpaid project management.",
            "A build brief handed to a developer with milestones, a budget and a date, all logged against the deal.",
            [
                ("Write the build brief", [
                    "Template. Deliverables, acceptance criteria, what is out of scope.",
                    "Comes straight from the scope you sold.",
                ]),
                ("Set milestones and payments", [
                    "Three or four milestones, money against each, client dates behind yours.",
                ]),
                ("Run the delivery", [
                    "Check in cadence, what you review, how to stay out of the build.",
                    "Keep the client talking to you, never to the developer.",
                ]),
                ("Protect the margin", [
                    "Scope creep, change requests, how to charge for them without a fight.",
                ]),
            ],
            ("The Build Is Running",
             "If you are building it yourself instead, start here."),
        ),
        L(
            "Self Fulfilment: Build It With Jarvis",
            "The same operator that sold it can build most of it. This is where the free course skills pay off at ten times the price.",
            "The first working version of the client's system, built and running on test data.",
            [
                ("Set up the client build", [
                    "Separate app, naming, where client data lives, access.",
                ]),
                ("Build the core workflow first", [
                    "The one workflow that holds the number you sold on.",
                    "One change per prompt, same as always.",
                ]),
                ("Connect their systems", [
                    "What they have to give you and how to ask for it safely.",
                    "Never take their passwords. How to get proper access instead.",
                ]),
                ("Run it on real data", [
                    "Load a real sample. Watch it break. Fix it before anyone sees it.",
                ]),
            ],
            ("It Works on Your Screen",
             "Now break it on purpose before the client does."),
        ),
        L(
            "Self Fulfilment: Test It Like the Client Will",
            "Clients do not use systems the way you built them. Find that out yourself, in private.",
            "A tested build with the edge cases handled and a written test log you can show them.",
            [
                ("Write the test list", [
                    "Prompt that generates the test cases from the scope.",
                ]),
                ("Try to break it", [
                    "Wrong input, missing data, two things at once, out of hours.",
                ]),
                ("Have somebody else use it", [
                    "Watch them, do not help them, write down where they hesitate.",
                ]),
            ],
            ("It Is Ready To Hand Over",
             "Both paths meet here. Handover is the same either way."),
        ),
        L(
            "Onboard, Hand Over, Get Paid",
            "The client experience is the product as far as they are concerned. This is also where referrals get made or lost.",
            "A client onboarded, trained, signed off and invoiced, with everything tracked in your portal.",
            [
                ("Onboard properly", [
                    "Kickoff call, what you need from them, dates in writing.",
                    "Set the communication rules on day one.",
                ]),
                ("Build the delivery portal", [
                    "Stages: onboarding, build, testing, handover, support.",
                    "The client sees progress without asking you for it.",
                ]),
                ("Run the handover session", [
                    "Record it. Train the person who will actually use it.",
                    "Leave a short document and a video they can rewatch.",
                ]),
                ("Get signed off and paid", [
                    "Acceptance in writing, final invoice, terms.",
                    "What to do when it goes quiet.",
                ]),
            ],
            ("Delivered",
             "Now turn one client into the next three."),
        ),
        L(
            "Support, Retainer and Raising the Price",
            "The install was the start. Everything after it is margin, proof and a higher price next time.",
            "A retainer offered on your current deal, a case study written, and your next price decided.",
            [
                ("Offer the retainer", [
                    "What support actually covers and what it costs you to provide.",
                    "How and when to present it. Usually at handover.",
                ]),
                ("Get the proof", [
                    "Numbers before and after, written permission, a short video.",
                    "The ask that gets a yes.",
                ]),
                ("Raise the price", [
                    "What has to be true to raise it, and by how much.",
                    "Update the offer page and the proposal template the same day.",
                ]),
                ("Ask for the referral", [
                    "The exact ask, and when in the relationship to make it.",
                ]),
            ],
            ("Module 7 Done",
             "Offer, pipeline, close, delivery. Run it again at a higher price."),
        ),
    ],
)

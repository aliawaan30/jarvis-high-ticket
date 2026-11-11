# -*- coding: utf-8 -*-
"""Specimen: Module 2 briefing B, written out in full so the format can be judged
on real writing and not on lorem. No em-dashes.
"""
from brief import paste, expect

BRIEF = dict(
    file="m2-b.html",
    module="Module 2, The Irresistible Offer",
    letter="B", of="G",
    title="Find the Market Nobody Is Serving",
    thesis="You are not looking for a market you can build something for. You are looking for a market that is losing money in a way nobody has bothered to fix.",
    read="9 min", worktime="60 to 90 min",
    leave="One market, chosen in writing, with the evidence and the number behind it",
    loom=None,
    loomcap="",
    next=("m2-c.html", "Find What They Actually Need Built"),
    beats=[
        ("The idea", """
<p class="lead">Almost everyone picks their market backwards. They learn to build a thing, then go looking for somebody who might want it. That is why so many people end up selling websites to cafes for four hundred dollars, competing with a hundred others doing exactly the same, arguing about price.</p>

<p>Work the other way around. Find a market that is <strong>bleeding money through a hole nobody has plugged</strong>, then build whatever plugs it. You are not choosing what to make. You are choosing whose problem you want to own.</p>

<p>This sounds obvious until you notice how it changes your conversations. When you sell a website, you are one of a hundred people offering the same thing, and the buyer's only real question is how much. When you turn up having understood how a specific industry loses ninety thousand dollars a year on something they have accepted as normal, there is nobody to compare you to. There is no market price for the thing you are offering, because the thing you are offering does not exist yet.</p>

<p>That is the whole reason this course starts with research instead of a service. The research <em>is</em> the product. Everything after it, the outreach, the funnel, the calls, is downstream of choosing well here.</p>
"""),
        ("Why it works", """
<p>Price is never set by your costs. It is set by <strong>what the buyer can compare you to</strong>.</p>

<p>In a crowded market the comparison is three other quotes, so you converge on the cheapest. In an underserved market there is no quote to compare against, so the comparison becomes the cost of the problem itself. If the problem costs them ninety thousand a year, twenty eight thousand to make it stop is not expensive, it is obvious. Same work, same you, entirely different conversation, because of a decision you made before you ever picked up the phone.</p>

<p>So the job in this briefing is to find a market where four things are true at once. Any three without the fourth and you will waste a month proving it.</p>

<div class="frame">
<div class="frame-h">The four tests</div>
<div class="frame-b">
<dl>
<div class="frame-row"><dt>Volume</dt><dd>Enough businesses that you can run a pipeline into it for a year without running out of people to talk to.<em>Rule of thumb: five hundred reachable businesses. Fewer than that and you burn the market in a quarter.</em></dd></div>
<div class="frame-row"><dt>Money</dt><dd>The problem costs them more every year than you intend to charge once.<em>If you cannot find the number, you do not understand the problem yet. Go back.</em></dd></div>
<div class="frame-row"><dt>Pain</dt><dd>They already know it is a problem and have already tried to fix it badly.<em>A problem they have not noticed is education, and education is a much more expensive sale than you think.</em></dd></div>
<div class="frame-row"><dt>Vacancy</dt><dd>Nobody is already doing this well for them. Not nobody at all, just nobody good.<em>A market with no competitors at all usually means no money. Look for bad competitors, not absent ones.</em></dd></div>
</dl>
</div>
</div>

<p>Vacancy is the one people get wrong. An empty market feels like a gift and is usually a warning. What you actually want is a market served badly by people who are expensive, slow, or built for someone ten times the size. That proves the money exists and tells you exactly where to stand.</p>
"""),
        ("In practice", """
<p>Here is the shape of a good answer, so you know one when the research hands it to you.</p>

<div class="work-ex">
<p class="tag">Worked example</p>
<h3>Wholesale food distribution, independent operators</h3>
<p>Orders arrive by phone, text message and email, all day, from the same restaurants and cafes every week. Somebody in the office keys every one of them into the system by hand. Everyone in the industry does it this way and nobody thinks of it as a problem. It is just Tuesday.</p>

<table>
<tr><th>What is happening</th><th class="n">Per year</th></tr>
<tr><td>40 orders a day, about 6 minutes each to take and key in</td><td class="n">$62,000</td></tr>
<tr><td>Roughly 2 percent keyed wrong, so redelivery plus credit</td><td class="n">$36,000</td></tr>
<tr class="sum"><td>What the hole costs them</td><td class="n">$98,000</td></tr>
</table>

<p>Now the offer writes itself. An order intake system that reads the text, the voicemail and the email, drops a structured order into their existing system, and flags only the ones it is unsure about. Six minutes becomes one. Two percent becomes a fraction of one.</p>

<table>
<tr><th>The offer</th><th class="n">Amount</th></tr>
<tr><td>What they get back in year one</td><td class="n">$75,000</td></tr>
<tr><td>What you charge to install it</td><td class="n">$28,000</td></tr>
<tr><td>Support and improvements, monthly</td><td class="n">$1,500</td></tr>
</table>

<p>Read that last table from the buyer's side. They are not being asked for twenty eight thousand dollars. They are being asked whether they would like to stop losing seventy five.</p>
</div>

<div class="aside">
<p><b>Those numbers are an illustration, not research.</b> They are the right shape and the right order of magnitude for a real high ticket offer, which is the only reason they are here. Your own numbers have to come out of an actual business you have actually spoken to, and in Module 6 you will be building them live on a discovery call.</p>
</div>

<p>Notice what is not in the example. No mention of what you would build it with. No AI, no platform, no tooling. The buyer does not care and bringing it up early makes you sound like a supplier instead of someone who understood their business. How it gets built is Module 7's problem.</p>
"""),
        ("The work", """
<p>Sixty to ninety minutes. You are running the research skill, reading what it returns like a sceptic, and coming out the other side with one market.</p>

<div class="do">
<div class="do-h"><b>One</b><span>Run the research</span></div>
<div class="do-b">
<p>Give Jarvis as much as you can about where you are and what you already know. Markets you have worked in beat markets you have read about, every time, because you can already tell when someone is lying to you about how their day works.</p>
""" + paste("""Run the underserved market research skill.

Here is my situation:
- I am based in [city, country] and can work with businesses anywhere in [country].
- Industries I have worked in or understand well: [list them, or write none].
- I am looking for businesses turning over roughly [range] a year.

Find me five markets where there is a workflow costing them real money every
year, where they already know it is a problem, and where whoever is serving
them today is doing it badly.

For each market, give me:
- who the business is and roughly how many of them exist I can reach
- the workflow that is broken, described the way someone in that industry
  would describe it
- what it plausibly costs them per year, and how you got to that number
- who is serving them today and why that is not good enough
- the single strongest reason this market is a bad idea

Rank them. Be hard on this. I would rather have two real ones than five
comfortable ones.""") + """
<div class="expect">Five markets, each with a number attached and a named reason it might be wrong. Vague answers like small businesses or tradies mean it did not understand the brief. Give it a revenue range and run it again.</div>
</div>
</div>

<div class="do">
<div class="do-h"><b>Two</b><span>Attack what comes back</span></div>
<div class="do-b">
<p>Research that agrees with you is worthless. Put every market through the four tests yourself, out loud, and throw away anything that fails one. Then make it defend what survived.</p>
""" + paste("""Take the top three markets from that list. For each one, tell me:

1. Where the yearly cost number came from, and what would have to be true for
   it to be wrong by half.
2. Whether they already know this is a problem, and what they have tried.
3. Who is selling to them today, what those people charge, and what their
   customers complain about.
4. How I would get a decision maker on the phone in the next two weeks.

If you cannot answer any of these from real evidence, say so plainly instead
of filling the gap.""") + """
<div class="expect">At least one market falls over at this step. That is the step working. If all three survive untouched, you are being told what you want to hear.</div>
</div>
</div>

<div class="do">
<div class="do-h"><b>Three</b><span>Check it against you</span></div>
<div class="do-b">
<p>Last filter, and it is not a soft one. You are going to be talking about this market every working day for the next six months. On the phone, in DMs, on calls with people who do it for a living.</p>
<ul>
<li>Can you get a conversation with one of these owners this week, through anyone you already know?</li>
<li>Can you hold a ten minute conversation about how their business runs without sounding like a stranger?</li>
<li>Are you willing to become genuinely interested in this industry, not just the invoice?</li>
</ul>
<p>Two out of three is enough. Zero out of three means pick the second one on your list instead, even if the numbers are slightly worse. Interest beats a marginally bigger market every time, because interest is what keeps you dialling in week five.</p>
</div>
</div>

<div class="aside">
<p><b>On the research skill itself.</b> It is built to go and look, not to guess from memory. If an answer comes back with no source behind it, treat it as a hypothesis you still have to prove on the phone, not as a finding. Anything you cannot stand behind on a call, do not put in an offer.</p>
</div>
"""),
        ("The decision", """
<p>One market. Written down, with the reasoning attached, before you open the next briefing. Everything from here uses it: the implementation research, the offer, the account list, the ads, the call script. Changing your mind later is not free.</p>

<div class="decide">
<p class="tag">Before you move on</p>
<h3>Write this into Jarvis</h3>
<ol>
<li>The market, named as specifically as you can. Not hospitality. Independent wholesale food distributors turning over two to ten million.</li>
<li>The workflow that is broken, in their words.</li>
<li>What you believe it costs them a year, and where that number came from.</li>
<li>Who serves them today and why that is not good enough.</li>
<li>The one thing that would prove you wrong, and how you would find out.</li>
</ol>
</div>

<p>That last line matters more than the other four. You are going to spend the next two briefings building an offer on top of this choice. Knowing in advance what would prove you wrong is how you find out in a week instead of a quarter.</p>

<p>Markets two and three stay on the bench. Do not work them, do not email them, do not think about them. One market, properly, beats three at thirty percent effort.</p>
"""),
    ],
)

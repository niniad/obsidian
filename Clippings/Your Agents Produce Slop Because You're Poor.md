---
title: "Your Agents Produce Slop Because You're Poor"
source: "https://x.com/systematicls/status/2035375632553836732"
author:
  - "[[sysls]]"
published: 2026-03-22
created: 2026-03-24
description:
tags:
  - "clippings"
---
## 

To view keyboard shortcuts, press question mark

[View keyboard shortcuts](/i/keyboard_shortcuts)

# [

](/home)

[

Home

](/home)[

Explore

](/explore)[

20+

Notifications

](/notifications)[

Follow

](/i/connect_people)[

Chat

](/i/chat)[

Grok

](/i/grok)[

Bookmarks

](/i/bookmarks)[

Creator Studio

](/i/jf/creators/studio)[

Premium

50% off

](/i/premium_sign_up)[

Profile

](/NinNin34649434)

[

Post

](/compose/post)

## Article

[

](/systematicls/article/2035375632553836732)

# Conversation

Pinned

[

![](https://pbs.twimg.com/profile_images/1982988371661336578/b0SV2XPc_x96.jpg)

](/systematicls)

[

sysls

](/systematicls)

[

@systematicls

](/systematicls)

Click to Subscribe to systematicls

[

![Image](https://pbs.twimg.com/media/HD8bSs4aoAAe_7J?format=jpg&name=medium)

](/systematicls/article/2035375632553836732/media/2035375564694134784)

Your Agents Produce Slop Because You're Poor

[

46K

](/systematicls/status/2035375632553836732/analytics)

# 

Introduction

You've got to admit that was a pretty good title - but no, really.

In 2023, when we were shipping production code using LLMs, it was absolutely mind-blowing to everyone around us, because it was still widely believed that LLMs produced unusable slop. But we knew something that eluded everyone else: the goodness of your agents goes up as a function of how many tokens you throw at it. It's really that simple.

You can see it in action just from running a few experiments yourself. Get your agent to code something difficult and mildly esoteric — let's say, implementing a convex optimisation algorithm with constraints from scratch. Put it in low thinking and implement; then set it to max thinking and ask it to review its work, see how many bugs it spots. Do the same with med thinking, high thinking, etc. It is trivial to see that bugs decrease monotonically with the amount of tokens you throw at the problem.

It's intuitive to you, right?

More tokens = less errors. You can take this one step further, and essentially that's the entire (simplified) idea behind code review product. With a fresh context, and a shit-ton of tokens (e.g. getting it to parse through every line and reason about whether or not there's a bug on that line) - you can essentially catch a super-majority, if not all bugs. You could repeat this process ten, a hundred times, each time looking at the codebase from a "different angle", and you would be able to capture all bugs.

This idea of simply spending more tokens to improve agent quality is also empirically evidenced by the fact that the places claiming they are able to push features into production with code entirely written by agents also happen to either be the foundation model providers themselves, or extremely well-capitalised firms.

So, if you are one of those that find themselves unable to ship production quality code with agents - let me put it plainly, at this point, you are the problem. Or rather, your wallet maybe.

# 

How Do I Know If I'm Spending Enough Tokens

[I wrote an entire article saying that the problem is definitely not your harness, and that you can "keep it simple" and still produce extraordinary work](https://x.com/systematicls/status/2028814227004395561)

, and I stand by it. You've read it, followed it, and are still largely disappointed by what your agent produces. You sent me a DM and saw that I had read but not responded.

This is the response!

Your agent sucks and can't solve your problems because you're just not spending enough tokens, for the most part.

The amount of tokens you need to throw at a problem to solve it depends entirely on the scale, complexity and novelty of the problem.

What's 2+2? Don't need many tokens at all.

"Write me a bot that can scan all the different markets between Polymarket and Kalshi, find semantically similar markets that should resolve around the same event with some no arbitrage limits and trade on those markets whenever an arbitrage opportunity presents itself in a latency sensitive manner" will require a fuckton of tokens.

Here's something interesting we've discovered along the way.

If you throw enough tokens at problems that arise from scale and complexity, agents can solve them no matter what. That is to say, if you want to build something extremely complex, that has many moving parts and LOCs, if you throw enough tokens at the problems, they will eventually be completely, fully resolved.

There is a small caveat here.

Your problem cannot be too novel. No amount of tokens can solve "novel" problems at this point in time. Sufficient tokens will bring down all errors that arise from complexity to 0, but will not allow an agent to invent something it does not know.

That was actually a relief for us.

We tried very hard, and spent — a lot, a lot, A LOT — of tokens to see if we could get our agents to recover institutional investment processes with minimal guidance. Part of the effort here was to understand how many years we were away (as quants) from being completely replaced by AI. It turns out that they could not even come close to putting together an institutional investment process. We think that this is in part because they have never seen one before, i.e. no training data exists for institutional investment processes.

So, if your problem is novel, don't throw more tokens at it for a solution. You need to guide the discovery process. You can however, once you are certain of implementation, simply throw more tokens to solve it - no matter the size of the codebase, or the number of moving parts.

Here's a simple heuristic: token budget should scale proportionally with lines of code.

# 

What Does Extra Tokens Actually Do?

In practice, extra tokens typically improve your agentic engineering in one of the following ways:

1. They spend more time reasoning through the same attempt and might catch erroneous logic by itself. More reasoning = better planning = higher chance of one-shotting something.
2. They are allowed multiple independent attempts for different solution paths. Some solution paths are better than others. Being allowed more than one means they can pick the best.
3. Similarly to 2, having more independent planning attempts allows them to abandon weak ones, and keep the most promising.
4. Having more tokens allows them to critique their previous work with a fresh context, which gives them a chance to improve it without being stuck in a "line of reasoning".
5. And of course, my favorite: having more tokens simply means they can verify with tests and tools. Actually running code to see if it works confirms the correct answer.

It works because agentic engineering failures are not random. They are almost always a result of choosing the wrong path too early, not checking if the path actually worked (early on), or not having enough budget to recover and undo a mistake once they've noticed one.

That's the entire story. Tokens literally buy you decision quality. Think of it like research: if you asked a human to answer a difficult question on the spot, the quality of their answer would diminish with urgency.

Research, after all, is what produces the bedrock of knowing the answer. Humans spend biological time to produce better answers, and agents simply spend more compute time to produce better answers.

# 

How To Improve Your Agents

You may still be skeptical, but there are many papers that support this, and honestly, the very existence of "reasoning" knobs should be all the proof you need.

One of my favorite papers is one where researchers trained on a small curated set of reasoning examples, then used a method that effectively forced the model to keep thinking by appending "Wait" when it tried to stop too early. That alone pushed one benchmark from 50% to 57%.

What I'm actually trying to say as plainly as possible is that single-pass max thinking is likely insufficient for you if you are constantly complaining that your agent's code leaves much to be desired.

Instead, I offer you two very simple solutions.

## 

Simple Thing 1: WAIT

The really simple thing that you can start doing today is to simply set up an automated loop where you build something, and then get your agents to review it N times with a fresh context (each time) and to fix its findings each time it discovers anything new.

If you find that this simple trick improves the results of your agentic engineering, then you are at least cognizant that your problem is simply a matter of token count — then you can come over and join the token burning club.

## 

Simple Thing 2: VERIFY

Get your agents to verify their work early and often. Write tests that demonstrate that the chosen path actually works. This is really helpful for highly complex, deeply nested projects where a function might be used downstream by many other functions. Being able to catch upstream errors saves you a ton of computational time (tokens) later on. So if you can, create "verification" checkpoints everywhere along your build out.

Wrote something and your primary agent says it's done? Get a secondary agent to verify it. Uncorrelated thinking streams cover systematic sources of bias.

# 

Conclusion

That's really it. I could write significantly more on the topic but I feel like just being aware of these 2 simple things and implementing them well will get you 95% there. I'm a huge proponent of doing simple things extraordinarily well and then layering complexity as you need it.

I've mentioned novelty as an unsolvable problem with tokens, and I want to stress this again, because you will inevitably run into this and then come crying that throwing more tokens at the problem did not work.

When what you want solved is not in the training set, then YOU really need to be the one with solutions. Hence, domain expertise is still incredibly important.

I know, I know, this whole article sounds like it was sponsored by Big Tokens, but I swear it isn't — I wrote this to help you be a better agentic engineer. Although, if Big Tokens reads this and decides to retroactively sponsor me - I'd love to sell out.

Want to publish your own Article?

[Upgrade to Premium](/i/premium_sign_up)

[12:19 AM · Mar 22, 2026](/systematicls/status/2035375632553836732)

·

[

46.6K

Views](/systematicls/status/2035375632553836732/analytics)

[View quotes](/systematicls/status/2035375632553836732/quotes)

[

![Nin Nin](https://pbs.twimg.com/profile_images/1571503861411753986/OxDthQrb_x96.png)

](/NinNin34649434)

Post your reply

  

[

![](https://pbs.twimg.com/profile_images/2035697096658173952/hB9IqaFs_x96.jpg)

](/th3betterself)

[

V

](/th3betterself)

[

@th3betterself

](/th3betterself)

·

[Mar 22](/th3betterself/status/2035428432281251849)

Really well written, brother. You clearly were in your element while writing this one. Quick questions: 1. Claude Code $20 offers the same models as the Max plans. So I am assuming the point of preferring higher ones is more tokens only? 2. I don't kn how to code. How to decide

[

335

](/th3betterself/status/2035428432281251849/analytics)

[

![](https://pbs.twimg.com/profile_images/1982988371661336578/b0SV2XPc_x96.jpg)

](/systematicls)

[

sysls

](/systematicls)

[

@systematicls

](/systematicls)

·

[Mar 22](/systematicls/status/2035428775606034524)

1\. yes, precisely 2. simple stuff, 2 should suffice. complex stuff - anywhere from 3-20 has been my number depending on how complex it really is. it's also important to prompt it to "look" at the same code a different way 3. codex checking claude!

[

286

](/systematicls/status/2035428775606034524/analytics)

[

![](https://pbs.twimg.com/profile_images/514181389869002752/dl9Oiyt4_x96.jpeg)

](/HaydenH36)

[

Hayden™

](/HaydenH36)

[

@HaydenH36

](/HaydenH36)

·

[Mar 22](/HaydenH36/status/2035403057823949081)

Absolutely the case. Always I hear boomers say: "I tested this and AI couldn't do it!!!" I ask: "What model did you use to test it?" It's ALWAYS ChatGPT Free or $20/month Claude. GenAI token I/O is the ultimate "get-what-you-pay-for" proposition. You need to pay for MORE

[

573

](/HaydenH36/status/2035403057823949081/analytics)

[

![](https://pbs.twimg.com/profile_images/1982988371661336578/b0SV2XPc_x96.jpg)

](/systematicls)

[

sysls

](/systematicls)

[

@systematicls

](/systematicls)

·

[Mar 22](/systematicls/status/2035404189090893849)

b i n g o

[

384

](/systematicls/status/2035404189090893849/analytics)

[

![](https://pbs.twimg.com/profile_images/1994434612974796801/A7_abqVt_x96.jpg)

](/pingpongsniping)

[

pingpongsniping

](/pingpongsniping)

[

@pingpongsniping

](/pingpongsniping)

·

[Mar 22](/pingpongsniping/status/2035379517481685467)

human intelligence and agent intelligence (with more tokens) gonna bring us far!!!!

[

288

](/pingpongsniping/status/2035379517481685467/analytics)

## 

Relevant people

- [
	![](https://pbs.twimg.com/profile_images/1982988371661336578/b0SV2XPc_x96.jpg)
	](/systematicls)
	[
	sysls
	](/systematicls)
	[
	@systematicls
	](/systematicls)
	Click to Unfollow systematicls
	All in
	[@openforage](/openforage)
	. I thrived in all of the largest hedge funds managing systematic investment processes.

# Trending now

## 

What’s happening

ギルティ炭酸NOPE 本日解禁！

＼はじメまして／やみつきになる罪な味、サントリーから新発売！

Promoted by NOPE｜ギルティ炭酸

Trending in Japan

#お花見auPAY

Business & finance · Trending

ファミマ45パー増量生コッペパン無料作戦

Retail industry · Trending

#ローソンのハピとく祭

[

Show more

](/explore/tabs/for-you)

[Terms of Service](https://x.com/tos)

|

[Privacy Policy](https://x.com/privacy)

|

[Cookie Policy](https://support.x.com/articles/20170514)

|

[Accessibility](https://help.x.com/resources/accessibility)

|

[Ads info](https://business.x.com/en/help/troubleshooting/how-twitter-ads-work.html?ref=web-twc-ao-gbl-adsinfo&utm_source=twc&utm_medium=web&utm_campaign=ao&utm_content=adsinfo)

|

© 2026 X Corp.
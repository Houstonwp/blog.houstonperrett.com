---
title: "AI Will Not Fix the Way Actuaries Work"
date: 2026-07-19
subtitle: "AI can create actuarial leverage only when it has trustworthy systems to reason over."
tags: ["ai", "actuarial", "technology"]
draft: true
---

![An AI assistant standing beside an actuary and a pile of legacy actuarial work](/images/ai-will-not-fix-actuarial-work/slide-1.webp)

<!--
Open with the apparent contradiction:

AI will help actuaries. But it will not fix the way actuarial work gets done.

Clarify that this is not an anti-AI argument. Establish the difference between
improving individual tasks and transforming the system of work. End with the
thesis: We are overestimating AI because we are underestimating the system
change required.
-->

<!--more-->

## The common AI framing is too shallow

![The typical AI roadmap focused on summarizing, documenting, coding, and automating](/images/ai-will-not-fix-actuarial-work/slide-2.webp)

<!--
Describe the common roadmap: summarize, document, code, and automate. Recognize
the value of those uses, then explain why they remain point improvements when
placed on top of an unchanged workflow.

Key distinction: The deeper opportunity is not point automation. It is systems
leverage.
-->

## Most actuarial workflows are not AI-ready

![An AI assistant stopped outside an actuarial workflow built for authorized experts](/images/ai-will-not-fix-actuarial-work/slide-3.webp)

<!--
Make the uncomfortable claim without blaming actuaries or a particular tool.
These workflows evolved for expert execution, review, and delivery. They were
not designed to be explicit, reusable, and machine-readable.

Contrast what AI needs with what many workflows provide: accessible data,
explicit assumptions, inspectable logic, stable interfaces, and traceable
changes versus project-by-project reconstruction and institutional memory.
-->

## Much of actuarial work is implicit

![An actuarial spreadsheet whose undocumented rules are known by one experienced employee](/images/ai-will-not-fix-actuarial-work/slide-4.webp)

<!--
Use recognizable examples: approved cells known by color, sequencing rules,
hidden historical logic, unwritten reconciliation steps, and reviewers who know
where problems usually appear.

Keep the focus on the operating model rather than Excel itself.

Key line: AI needs explicit context. Actuarial work often depends on context
known by people rather than represented by systems.
-->

## AI is a reasoning interface, not the source of truth

![AI contrasted as an unreliable oracle and as an interface to a governed actuarial system](/images/ai-will-not-fix-actuarial-work/slide-5.webp)

<!--
Pivot from critique to the stronger mental model. Contrast AI generating an
answer with AI helping an actuary reason over governed data, structured
assumptions, defined mappings, deterministic calculations, version-controlled
code, and tests.

Trust comes from the system, not the chatbot. The LLM is probabilistic; the
actuarial system around it can be deterministic, tested, and governed.
-->

## A concrete example: reconciling life expectancy at age 65

![An actuary asking an AI assistant why life expectancy changed at age 65](/images/ai-will-not-fix-actuarial-work/slide-6.webp)

<!--
Ask: What explains the change in life expectancy for a 65-year-old after the
mortality assumption was updated?

Briefly describe the traditional reconstruction work. Then introduce an
illustrative AI-supported reconciliation produced from explicit system assets.
Clearly label all numbers as illustrative.
-->

| Driver | Life expectancy impact |
| --- | ---: |
| Prior assumption | 21.30 years |
| Mortality table update | +0.28 years |
| Projection scale update | +0.10 years |
| Segment mapping update | +0.04 years |
| Updated assumption | 21.72 years |
| **Total change** | **+0.42 years** |

*Illustrative numbers.*

<!--
Explain that the valuable result is not the table. The system contained enough
explicit structure to support the reconciliation and let the actuary ask better
follow-up questions.
-->

## Why this example worked

![An explicit actuarial system containing code, tests, version history, data, assumptions, and mappings](/images/ai-will-not-fix-actuarial-work/slide-7.webp)

<!--
Walk through the prerequisites: accessible mortality tables, structured
assumptions, defined segment mappings, modular calculations, version control,
and tests.

Key line: AI did not make the workflow good. The workflow made AI useful.
-->

## The definition of good actuarial work is expanding

![An actuarial team reviewing the explicit and testable system behind its work product](/images/ai-will-not-fix-actuarial-work/slide-8.webp)

<!--
Preserve the existing standards: sound, reviewed, documented, defensible, and
timely. Add the expectations required for systems leverage:

- Explicit
- Structured
- Traceable
- Testable
- Reusable
- Interrogable

Key line: The actuarial work product is no longer just the answer. It is also
the system that produced the answer.

Connect this expanded definition to governance below the final memo: data,
assumptions, mappings, calculations, tests, and workflow design.
-->

## AI is testing the actuarial operating model

![AI holding a mirror that reflects the standards, incentives, governance, ownership, and definition of good work](/images/ai-will-not-fix-actuarial-work/slide-9.webp)

<!--
Combine the technical, governance, and leadership implications. AI can amplify
a strong system, but it can also make a weak process faster and more polished
without making it more trustworthy.

Make ownership explicit. Senior actuaries shape what is funded, tolerated,
reviewed, rewarded, and called good work.

Return to the title: AI will not fix the way actuaries work. It will expose how
actuaries work.

Close with the question: Have we built actuarial systems worth leveraging?
-->

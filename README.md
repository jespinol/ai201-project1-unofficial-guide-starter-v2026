# The Unofficial Guide

**Author:** Jose Espinola-Lopez  
**Corpus:** city_guides

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This system is an guide assistant built on the `city_guides` corpus, that covers regional towns, travel tips, transit, and local food across locations like Brightwater, Kestrelford, Marchwood, Halden Bay, etc. It answers visitor questions regarding schedules, costs, transit options, and dining recommendations by retrieving context from regional guides. If a question is outside the scope of the corpus, the query is rejected with a refusal rather than hallucinating an answer.

## Chunking Strategy

**Chunk size:** ~310 characters on average (split by section)
**Overlap:** None, title is added for context preservation

The `city_guides` corpus is structured as Markdown documents with clear topic headers (e.g. `## Getting there`, `## Eat and drink`, `## What to see`). The default window sliced straight through sections, cutting sentences in half and mixing up unrelated topics into a chunk. Instead of arbitrary character-based slicing, I implemented a section-aware chunker that splits on `##` headings and adds the title (e.g. `# City Name`) to every chunk. This way, every chunk represents a complete topic that retains its context without splitting up sentences.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: ` guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.
```

**Chunk 2** — source: `guide_corry_vale.md#6` — produced by: `chunker.py::split_documents`

```
# Corry Vale

## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** — source: `guide_givens_mill.md#3` — produced by: `chunker.py::split_documents`

```
# Givens Mill

## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: `guide_kestrelford.md#6` — produced by: `chunker.py::split_documents`

```
# Kestrelford

## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.
```

**Chunk 5** — source: `guide_regional_transport.md#1` — produced by: `chunker.py::split_documents`

```
# Getting around the region

## The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**  What time does Brightwater's Tuesday market finish?

**Answer:**

```
> .venv/bin/python app.py ask "What time does Brightwater's Tuesday market finish?"
  (best distance 0.232, cutoff 0.6)

Brightwater's Tuesday market finishes by 1pm.

Sources: `guide_eating.md` and `guide_brightwater.md`

Sources retrieved: guide_brightwater.md, guide_eating.md, guide_regional_transport.md, guide_seasons.md

1 model calls this session, 669 tokens (637 in, 32 out)
```

**My relevance cutoff:** 0.6

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| How much does it cost to climb Kestrelford's parish church tower? | Yes | 0.449 |
| What time does Brightwater's Tuesday market finish? | Yes | 0.232 |
| How often do Marchwood's trams run on weekdays? | Yes | 0.244 |
| How do restaurant prices on Halden Bay's harbour front compare with Fell Street? | Yes | 0.222 |
| When do tours of the working watermill at Givens Mill run? | Yes | 0.366 |
| What is the capital of Mongolia? | No | 0.754 |
| How do I change the oil in a diesel engine? | No | 0.888 |
| Who won the 1994 World Cup? | No | 0.899 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.835 |
| How do I write a for loop in Rust? | No | 0.836 |


## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** After doing it manually, I asked the AI to pressure-test my acceptance criteria in `criteria.md` against the self-check rubric. The AI initially proposed a chunk size criterion checking character ranges and complete sentences. I pushed back because arbitrary character counts don't necessarily measure usefulness, and cutting a sentence at a boundary doesn't necessarily break meaning. We revised it to verify that chunks contain both the answer and the place it describes for context preservation.

**2.** When evaluating the starter's fixed-size chunking, the AI analyzed sample chunks and highlighted that document endings produced sentence fragments lacking place names. During initial iteration in some chunks I did not notice this issue as they appeared complete sentences, which led me to believe the fixed-sized chunking was producing very good responses. The AI helped identify these edge-case fragments, which led to implementing a section-aware chunker that splits on headers and add the document title to keep every chunk self-contained.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunks contain the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks contain expected answer and place name | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Expected answer in final answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Real Output (copied directly from `results/run_2026-09-23_1738_before.md`)

- Produced by: `run_eval.py::main` calling `generate.py::answer_from_chunks` and `gate.py::check`

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.754 | refused |
| How do I change the oil in a diesel engine? | 0.888 | refused |
| Who won the 1994 World Cup? | 0.899 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.835 | refused |
| How do I write a for loop in Rust? | 0.836 | refused |

---

## Real output

### How much does it cost to climb Kestrelford's parish church tower? — run 1

- Best distance: 0.4487 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_givens_mill.md, guide_kestrelford.md

```
It costs £2 to climb Kestrelford's parish church tower. 

Source: `guide_kestrelford.md`
```

### What time does Brightwater's Tuesday market finish? — run 1

- Best distance: 0.2319 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_eating.md, guide_regional_transport.md, guide_seasons.md

```
Brightwater's Tuesday market is finished by 1pm. 

Sources: `guide_eating.md` and `guide_brightwater.md`
```

### How often do Marchwood's trams run on weekdays? — run 1

- Best distance: 0.2437 (passed the gate)
- Sources retrieved: guide_eating.md, guide_kestrelford.md, guide_marchwood.md

```
Marchwood's trams run every 8 minutes on weekdays. 

Source: guide_marchwood.md
```

### How do restaurant prices on Halden Bay's harbour front compare with Fell Street? — run 1

- Best distance: 0.2217 (passed the gate)
- Sources retrieved: guide_eating.md, guide_halden_bay.md, guide_regional_transport.md

```
Prices on Halden Bay's harbour front are roughly double those on Fell Street for comparable food. 

This information comes from *guide_halden_bay.md* and *guide_eating.md*.
```

### When do tours of the working watermill at Givens Mill run? — run 1

- Best distance: 0.3662 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md

```
The mill runs tours on the hour from 11 to 3 (guide_givens_mill.md).
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MET | In all 3 runs, for 5/5 questions the top retrieved chunks contained the exact answer text. |
| 2 | Every answer names a source | MET | All 15 generated responses across the 3 runs cited at least one `.md` source file explicitly. |
| 3 | Gate stops out-of-corpus questions | MET | All 5 out-of-scope questions had best distance between 0.754 and 0.899, comfortably over the 0.6 cutoff and refused. |
| 4 | Chunks contain expected answer and place name | MET | Section-aware chunking prepended the `# Town` title to every section chunk, ensuring all 5/5 questions had chunks containing both the answer and the place name. |
| 5 | Expected answer in final answer | MET | All 15 generated responses (5 questions × 3 runs) contained the expected target substring without exception. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

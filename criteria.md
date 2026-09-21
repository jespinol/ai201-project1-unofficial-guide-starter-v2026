# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
I chose 4 of 5 because the city guides contain specific facts, but a question could use wording that is different from the wording in the source document. A lower target would allow too many retrieval failures, while requiring 5 of 5 would leave no room for one especially difficult question.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Travelers should be able to identify which guide contains returned details like prices, schedules, and opening hours. I chose every answer rather than 4 of 5 because even one answer without a source cannot be checked against the corpus, and the source filename is stored with every retrieved chunk.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
I chose 4 of 5 because retrieval scores may vary and one unrelated question could happen to share words with an existing city guide. Fewer than 4 refusals would mean the system presents unsupported information as if it came from the corpus too often.

---

## 4. Something about your chunks

For at least 4 of my 5 test questions, at least one retrieved chunk contains both the expected answer from the question's `expects` field and the name of the place the answer describes.

**Why this target:**
The city guides contain many similar facts about prices, schedules, and opening hours, so an answer is only useful when it stays with the relevant place name. I chose 4 of 5 because one fact may be separated from its heading, but allowing more than one such separation would indicate that the chunks are losing too much context.


---

## 5. Your choice

For at least 4 of my 5 test questions, a case-insensitive comparison finds the word or short phrase recorded in that question's `expects` field in the final answer.

**Why this target:**
I chose 4 of 5 because this checks whether the final answer communicates the specific, expected fact, not just if the retrieval found a related item in the text. A lower target would permit too many incorrect answers, but 5 of 5 would allow no margin for one correct answer that expresses a given fact differently.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->

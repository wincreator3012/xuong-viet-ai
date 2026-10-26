---
name: factual-review
description: "Rigorous, meticulous review and verification of any text using the FACTUAL checklist framework (Facts, Assumptions, Completeness, Threats & Bias, Uncertainty, Arguments, Limitations). Use this skill whenever the user asks to review, verify, fact-check, or quality-check any text - whether AI-generated content, articles, blog posts, research papers, business documents, reports, proposals, or any other written material. Trigger phrases include: \"review this text\", \"check this for accuracy\", \"fact-check this\", \"verify this content\", \"FACTUAL check\", \"FACTUAL review\", \"kiểm tra bài viết\", \"review bài này\", \"rà soát nội dung\", or any request to assess the quality, accuracy, bias, or logical soundness of a piece of writing. Also trigger when the user pastes or uploads text and asks if it's reliable, accurate, or well-reasoned. This skill should be used even when the user simply says \"check this\" or \"is this accurate?\" while providing text content."
---

# FACTUAL REVIEW: Rigorous text verification skill

Framework credit: the FACTUAL checklist is an original framework by Luong Dung Nhan (Lương Dũng Nhân, M.Ed, PCC). In the writing workshop (xuong-viet-ai) it is the review lens for reasoning and facts; it works alongside the eight qualities of a text and the ACCORD-ACCEPT criteria (also by Luong Dung Nhan) for works aimed at transformation, such as books, courses, and long essays.

## Overview

This skill performs systematic, meticulous review of any text using the FACTUAL checklist - a 7-dimension framework covering Facts, Assumptions, Completeness, Threats & Bias, Uncertainty, Arguments, and Limitations. The goal is to ensure the highest possible accuracy, quality, and usefulness of information before the user relies on it.

For the complete detailed checklist with all sub-checks and examples, read `references/factual-checklist-full.md` in this skill's directory.

**Division of labour with `kiem-chung`.** FACTUAL reviews the reasoning quality of a whole text. When a finding in the F dimension touches a specific source (a named researcher, study, statistic, quotation, or reference-list entry), switch to the source-fidelity method of `kiem-chung` if it is available: trace the original, check the four layers (identity, bibliographic record, content, wording), and match the verb to the type of evidence. For Vietnamese books, articles, or teaching materials that cite many studies, run `kiem-chung` as the main pass and use FACTUAL for the argument-level dimensions.

**Inside a built writing workshop** (the working folder has `xuong-viet-ai/XUONG.json`): address the user as set in `phong-cach/GIONG-VAN.md` of the workshop; when the text belongs to a piece in `Bai viet/`, save a long report in that piece's folder as `ra-soat-factual.md`; sources the author keeps in the `4 Tu lieu tham khao` compartment of the materials library (`Kho tu lieu/`) are the first place to look for originals. Never move or edit files in the library.

---

## Step 0: PREPARATION

Before beginning the review, do the following:

1. **Identify the text language** - The entire review report must be written in the same language as the source text (Vietnamese for Vietnamese text, English for English text).
2. **Assess text length and complexity** to determine review depth and output format:
   - Short text (under ~500 words) or simple content: respond directly in chat
   - Long text (over ~500 words) or complex/technical content: produce a structured .md or .docx file
3. **Determine review depth** based on user request:
   - If user specifies "quick check" or "kiểm tra nhanh": use Quick mode (F-C-L triad only)
   - If user specifies "deep review" or "rà soát kỹ": use Deep mode (all sub-checks)
   - If user does not specify: use **Standard mode** (all 7 dimensions, 1-2 key sub-checks per dimension)
4. **Read the full checklist reference** - Before starting review, read `references/factual-checklist-full.md` to have the complete checklist with all sub-criteria and examples fresh in context.

---

## Step 1: SYSTEMATIC REVIEW

Work through each FACTUAL dimension methodically. For each dimension, identify specific issues in the text with exact quotes or paragraph references so the user can locate them.

### Review depth guide

**Quick mode (F-C-L triad):**
- F: Verify 2-3 most critical factual claims
- C: Check if all parts of the original question/intent were addressed
- L: Check for outdated or time-sensitive information

**Standard mode (default - all 7 dimensions, focused sub-checks):**
- **F - Facts**: (F1) Flag unsourced claims that sound factual. (F2) Verify key statistics, dates, names, quotes via web search for the most critical ones. (F-source) For every claim about a study, check four layers against the original, not against a summary: identity (first author, author order, affiliation and academic title at the time of publication), bibliographic record (right paper, right year, the source exists), content (what was measured, in whom, compared with whom, result or discussion-section speculation, effect size), wording (verbatim quotes, attributions). The content layer is where most real errors sit: overstated results, variables that were never measured, animal findings presented as human findings, correlation presented as causation, findings of many groups credited to one famous name, the author's own view credited to a study.
- **As - Assumptions**: (As1) Identify underlying frameworks or worldviews. (As2) Spot hidden premises using syllogistic reasoning.
- **C - Completeness**: (C1) Check if all parts of the prompt/intent were answered. (C2) Assess depth level (Description → Analysis → Prediction → Intervention).
- **T - Threats & Bias**: (T1) Separate facts from opinions - highlight evaluative language. (T3) Check balanced presentation of perspectives.
- **U - Uncertainty**: (U1) Note where tentative language signals low confidence. (U3) Check if confidence level matches the evidence provided. Calibration has two directions: flag overstatement, and also flag over-hedging that drains a sentence. The preferred fix places the level of certainty inside the verb of the claim itself ("found" for controlled experiments, "was associated with" for correlational data, "synthesised ... and found" for reviews, "the authors suggest" for mechanisms, "argued" for opinion pieces, lectures, and popular books) rather than appending a caveat sentence. Keep a separate caveat only when it changes how the reader should act (health safety, animal findings applied to people).
- **Ar - Arguments**: (Ar1) Check if conclusions follow from evidence. (Ar4) Flag correlation-causation confusion.
- **L - Limitations**: (L1) Check against knowledge cutoff / outdated info. (L5) Identify areas requiring expert consultation.

**Deep mode (full checklist):**
- Apply every sub-check from the full checklist reference file (F1-F4, As1-As4, C1-C5, T1-T5, U1-U4, Ar1-Ar5, L1-L5).

### Web search protocol

For factual verification, use this combined approach:

1. **Auto-verify** (use web_search actively) for:
   - Specific statistics, percentages, or numbers presented as facts
   - Direct quotes attributed to named individuals
   - Claims about specific studies, research findings, or scientific facts
   - Dates of events, historical claims
   - Any claim that, if wrong, would seriously undermine the text's credibility

2. **Flag for user verification** (mark clearly in report but do not search) for:
   - General claims that are plausible but unverifiable with a quick search
   - Opinions or interpretations presented alongside factual claims
   - Domain-specific technical claims outside common knowledge
   - Claims where multiple conflicting sources exist

When searching, use short specific queries. For quotes, use exact phrase search. For statistics, search the specific number with context. Cross-reference with at least 2 sources for critical claims.

---

## Step 2: COMPILE THE REVIEW REPORT

Structure the report as follows. Use a severity system for each finding:

- 🔴 **Critical** - Factually wrong, logically invalid, or seriously misleading. Must be corrected.
- 🟡 **Warning** - Potentially inaccurate, imbalanced, or incomplete. Should be reviewed.
- 🟢 **Note** - Minor observation, stylistic suggestion, or enhancement opportunity.

### Report structure

```
# FACTUAL REVIEW REPORT
## Text reviewed: [title or first line]
## Review depth: [Quick / Standard / Deep]
## Overall assessment: [brief summary + overall quality rating]

---

## Summary of findings
[Table or brief list: count of 🔴 Critical / 🟡 Warning / 🟢 Note findings]

---

## Detailed findings by dimension

### F - FACTS
[For each finding:]
- [🔴/🟡/🟢] **[Sub-check ID]**: [Description of issue]
  - **Location in text**: [exact quote or paragraph reference]
  - **Issue**: [what is wrong or questionable]
  - **Evidence**: [what web search found, or why this is flagged]
  - **Checkable source**: [URL or search query for user to verify]

### As - ASSUMPTIONS
[Same structure...]

### C - COMPLETENESS
[Same structure...]

### T - THREATS & BIAS
[Same structure...]

### U - UNCERTAINTY
[Same structure...]

### Ar - ARGUMENTS
[Same structure...]

### L - LIMITATIONS
[Same structure...]

---

## Verified claims
[List of claims that were checked and confirmed accurate - this builds user trust]

---

## Suggested revisions
[For each 🔴 and 🟡 finding, provide:]
1. **Direction**: Brief explanation of what needs to change and why
2. **Proposed revision**: A rewritten version of the problematic passage

---

## Self-check resources for user
[List of specific URLs, search queries, or tools the user can use to independently verify the most important findings]
```

---

## Step 3: SELF-VERIFICATION (meta-review)

Before delivering the report, review your own findings to eliminate any hallucinated or inaccurate review comments. This step is essential because the review itself can contain errors - and delivering a flawed review undermines the entire purpose of this skill.

### Self-check process

1. **Re-read each finding against the original text.** For every 🔴 and 🟡 finding, go back to the exact passage in the source text. Confirm that:
   - The quote or paragraph reference is accurate (not misquoted or taken out of context)
   - The issue you identified actually exists in the text as written
   - You are not projecting meaning that isn't there

2. **Verify your own fact-check results.** For any finding where you used web search to contradict a claim in the text:
   - Re-examine the search results: did they actually say what you claimed they said?
   - Make sure you are not confusing sources or misrepresenting what you found
   - If a search was inconclusive, downgrade the finding from 🔴 to 🟡 and note the uncertainty honestly

3. **Check for false positives.** Remove or downgrade findings that fall into these traps:
   - Flagging something as "unsourced" when the text is clearly expressing an opinion, not claiming a fact
   - Calling something "biased" simply because it takes a clear position (advocacy is not the same as hidden bias)
   - Marking something "incomplete" when the scope was intentionally limited and that's appropriate for the context
   - Criticizing the text for not doing something it was never trying to do

4. **Verify your suggested revisions.** For each proposed rewrite:
   - Does the revision actually fix the identified issue?
   - Does it preserve the author's original meaning and voice?
   - Does the revision itself introduce any new factual claims that you haven't verified?
   - Does it give a researcher an academic title ("Professor") that you have not verified for the year of publication? If unsure, use a role ("psychologist", "researcher").

5. **Final honesty check.** Ask yourself:
   - Am I confident enough in each finding to stand behind it if the user challenges me?
   - For any finding where the answer is no, either remove it, downgrade its severity, or explicitly mark your uncertainty

6. **Treat other reviewers' comments as leads, not verdicts.** Editor notes, an independent reviewer's report, another AI's output, or your own earlier session: verify each against the source before accepting or rejecting it. Real cases: an independent reviewer gave the wrong date for a newspaper article; an editor filled in full names for three surnames and picked three wrong people.

After completing this self-verification, revise the report accordingly - remove invalid findings, adjust severity levels, and add uncertainty notes where needed. Only then proceed to deliver.

---

## Step 4: DELIVER THE REPORT

1. **For in-chat delivery** (short texts): Present the full report directly, keeping it readable and well-structured. No need for excessive headers - adapt formatting to chat context.

2. **For file delivery** (long texts): Create a .md file with the full report structure. If the user requests .docx, use the docx skill to create a formatted Word document.

3. **Always end with a brief conversational summary** highlighting:
   - How many critical issues were found
   - The 1-3 most important things the user should address first
   - An honest overall quality assessment

---

## Important principles

- **Be thorough but fair**: The goal is to help improve the text, not to tear it apart. Acknowledge what works well alongside what needs fixing.
- **Be specific, not vague**: Every finding must point to a specific location in the text with a concrete issue. Avoid generic complaints like "could be more balanced" without pointing to exactly where and how.
- **Provide actionable revisions**: Each suggested revision should be something the user can directly implement - not abstract advice.
- **Respect the author's voice**: When suggesting revisions, preserve the original tone, style, and intent. Improve accuracy and quality without rewriting the author's personality out of the text.
- **Epistemic honesty**: If you cannot verify a claim and web search is inconclusive, say so. Do not present your own uncertainty as the text being wrong.
- **Never rebuild a citation from memory**: author names, years, journals, and DOIs come from the original source (DOI page, Crossref, publisher, journal site). Label each source as checked against the original, checked only via a secondary source, or unchecked, and keep that label in the report.
- **Facts about the author's own life belong to the author**: anecdotes, dates, organisations the author worked for, and the author's own survey data are flagged for the author to confirm, never corrected on a guess.
- **Match the text's language**: Vietnamese text gets a Vietnamese report. English text gets an English report. Never mix languages arbitrarily.

---

*Version 1.2, 26/10/2026: added the framework credit and the link to the eight qualities and ACCORD-ACCEPT.*

*Version 1.1, 16/10/2026: added the source-fidelity sub-check (F-source), two-direction calibration with certainty placed in the verb (U3), title and reviewer-comment checks in self-verification, and the division of labour with `kiem-chung`. Distilled from the citation review of a practice book on mental wellbeing (214 sources).*

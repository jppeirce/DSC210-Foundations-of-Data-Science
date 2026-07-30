# Instructional review: Modules 1 and 2

**DSC 210 Foundations of Data Science**
Review date: 2026-07-30
Scope: `Notes/01-what_is_data_science/01-what_is_data_science.ipynb` and `Notes/02-data_types/02-data_types.ipynb`

Findings are grouped by how urgent they are. Section 1 items are verified defects that will misbehave in front of students. Sections 2 and 3 are the organization and activity reviews. Section 4 records decisions already made, and Section 5 lists what still needs your call.

---

## 1. Verified defects

Each item below was confirmed by inspecting the notebook source against the files on disk, not inferred.

### 1.1 Broken image link (Module 2)

The notebook requests `Notes/02-data_types/penguins_bill.jpg`. The file on disk is named `pengiun_bill.jpg`. The image does not render. Rename the file rather than the reference, since the reference spelling is correct.

### 1.2 Colab badge opens the wrong file (Module 2)

The badge at the top of `02-data_types.ipynb` links to:

```
.../blob/main/Notes/02-data_types/data_types.ipynb
```

There is a `data_types.ipynb` in that folder, apparently an older copy, so the badge resolves successfully and opens stale material. This is worse than a dead link, because nothing visibly fails. Point the badge at `02-data_types.ipynb` and delete or archive the duplicate. Module 1's badge is correct.

### 1.3 Duplicate section number (Module 2)

Two headings are numbered `## 8.`: "From information to knowledge: reasoning like a detective" and "Data Science Workflow." The detective section should be 8 and the workflow section 9, or the detective material should fold into Section 7.

### 1.4 Malformed bold (Module 2, Section 4)

`** Definition: **` has spaces inside the asterisks, so Markdown does not render it as bold. The literal asterisks appear on screen. Compare the correctly formed `**Definition:**` in Section 5. This is the definition of big data, so it is a conspicuous place for it to break.

### 1.5 A factual error in the first code cell students ever see (Module 2, Section 0)

```python
# sns.load_dataset loads the penguin dataset from seaborn into
# a data structure called a panda
# pandas have attributes
```

The structure is a **DataFrame**. `pandas` is the library, and it is never singular. For students whose only prior language is Java, this is precisely the kind of thing that becomes a durable misconception. Suggested replacement:

```python
# sns.load_dataset() loads the penguins data into a DataFrame,
# the table-shaped structure provided by the pandas library.
# A DataFrame has attributes (like .shape) and methods (like .head()).
```

### 1.6 Activity 3 refers to a code cell that does not exist (Module 1)

"assign a risk level (Low / Medium / High) in the code cell below." There is no code cell, and you have confirmed Module 1 is discussion-only by design. Reword to "in the table below" and supply the table.

### 1.7 Activity numbering gap (Module 2)

Activities run 1, 2, 3, 4, 6, 7, 8. There is no Activity 5. Resolved by the new Section 5 activity in 3.4 below.

### 1.8 Duplicate headings (Module 1)

Two consecutive cells are both titled `### Example - UW-La Crosse`. They cover different things: institutional goals, then retention disparities. They need distinguishing titles.

### 1.9 Spelling

| Notebook | Text | Correction |
| --- | --- | --- |
| Module 1 | "gaining, **intepreting**, and communicating" | interpreting |
| Module 1 | "Take a **momment**" | moment |
| Module 1 | "**Activiy** 5 - Marketing Strategy" | Activity |
| Module 2 | "which **anaylsis** tool" | analysis |
| Module 2 | "the **RBG** color code" | RGB |
| Module 2 | "**Nowdays**, answers to questions" | Nowadays |
| Module 2 | "Activity 8 - Customer **Chrun**" | Churn |

The first is the most worth fixing: it sits inside the blockquoted definition of data science, which is the single sentence most likely to be screenshotted, quoted back on an exam, or copied into notes.

### 1.10 Orphaned files

Unused in Module 1: `figures_venn_diagram.png`. Unused in Module 2: `US_DoD_KM_Pyramid.png`, `fig_asemic_workflow_example.png`, `pengiun_bill.jpg` (see 1.1), and the stale `data_types.ipynb` (see 1.2). Worth a cleanup commit so the folders reflect what is actually in use.

---

## 2. Consistency and organization

### 2.1 Header blocks

Module 1 uses **Key Concepts**, Module 2 uses **Learning objectives**. Per your decision, Key Concepts wins in both, matching your MTH 265 convention.

Module 1's three bullets are not parallel in form. One is a task ("Determine a working definition"), one is a claim ("Data science is the intersection of..."), one is a noun phrase ("The 5 Cs for evaluating..."). Your MTH 265 sections use uniformly verb-led skill statements. Proposed:

> ## Key Concepts
> - State a working definition of data science and apply it to borderline cases
> - Describe data science as the intersection of Math & Statistics, Hacking Skills, and Substantive Expertise
> - Apply the 5-C checklist to evaluate the ethical dimensions of a data science project

Module 2's six numbered objectives are longer than any Key Concepts list in MTH 265, and objective 5 carries three distinct ideas (justified true belief, inference to the best explanation, and the data-information-knowledge progression) in a single bullet. Proposed compression to five:

> ## Key Concepts
> - Define data, and distinguish structured from unstructured data using cases, features, and metadata
> - Classify a feature by measurement scale and determine which summaries it permits
> - Explain what makes data "big" and why that mattered for the emergence of data science
> - Judge whether a dataset is the *right* data for a question
> - Trace the data to information to knowledge progression, and locate each step on the course loop

### 2.2 Labeling scheme

Per your decision: **Class Example** for worked items you demonstrate, **Activity** for group work, numbered `module.index` throughout. Full proposed mapping:

**Module 1**

| Current | Proposed |
| --- | --- |
| Activity 1 - Is this data science? | Activity 1.1 |
| Activity 2 - What are your strengths? | Activity 1.2 |
| Activity 3 - Content recommendations and the 5-C checklist | Activity 1.3 |
| Activity 4 - Your data | Activity 1.4 |
| Example - Store Products **+** Activiy 5 - Marketing Strategy | Activity 1.5 (merged, see 3.2) |
| Example - UW-La Crosse (goals) | Class Example 1.1 UWL Institutional Data |
| Example - UW-La Crosse (retention) | Class Example 1.2 UWL Retention Disparities |

**Module 2**

| Current | Proposed |
| --- | --- |
| `RUN-TOGETHER` load and `.head()` | Class Example 2.1 Loading the Penguins Data |
| Activity 1 - Data Sources I | Activity 2.1 |
| Activity 2 - Cases and features of Penguins | Activity 2.2 |
| `FILL-IN-LIVE` single case via `.iloc` | Class Example 2.2 Selecting a Single Case |
| unlabeled "Discuss" cell on unstructured penguins | Activity 2.3 |
| Activity 3 - What type is it? | Activity 2.4 |
| `RUN-TOGETHER` mean and `value_counts` cells | Class Example 2.3 Meaningful and Meaningless Summaries |
| *new* feature-type drill | Activity 2.5 (see 3.3) |
| Activity 4 - Data Sources II | Activity 2.6 |
| *new* source matching | Activity 2.7 (see 3.4) |
| Activity 6 - Is all data good data? | Activity 2.8 |
| Activity 7 - Predict, then discuss | Activity 2.9 |
| Activity 8 - Customer Churn | Activity 2.10 |

Note what this exposes: Module 2 would carry **ten** activities. See 3.5.

### 2.3 The 5 Cs arrive after students are asked to use them

This is the clearest instructional-flow problem in either notebook. Activity 1.3 asks students to apply the 5-C checklist, listing the five criteria inline. The framework is then formally presented at the very end of the notebook, in the closing "With great power comes great responsibility" cell.

Two coherent fixes. **Present first:** move the framework into Section 3 ahead of the activity, so the activity applies a tool students have been given. **Discover first:** keep the current order but reframe the closing cell explicitly as a consolidation ("You used this checklist in Activity 1.3. Here it is as a whole."). Right now it is neither, and reads as accidental repetition.

I lean toward present-first for this audience. A sophomore encountering "Consistency" for the first time inside a discussion prompt has to invent the definition before applying it.

### 2.4 Floating unnumbered headings

Module 1's `### It's a big and beautiful world.` and `### How do you learn Data Science?` sit outside the numbered structure, and the closing `## With great power comes great responsibility` is an unnumbered H2 doing the work of a summary. Module 2's `# Example` for the digitization scenario uses H1, outranking every section heading in the notebook, though that cell is being removed anyway.

Suggested: make the two Module 1 H3s subsections of the sections that contain them (`### 1.3 It's a big and beautiful world`), and promote the closing cell to `## 4. Summary: with great power comes great responsibility`.

### 2.5 Module 1 never mentions the course loop

Your collaboration guide describes `ASK -> GET -> EXPLORE -> MODEL -> COMMUNICATE` as the motif that orients students within the course arc, and Module 2 uses it well. Module 1 never shows it. Since Module 1 is where students form their picture of the field, a single cell at the end previewing the loop would do real work and would make Module 2's arrival at it feel earned rather than sudden.

### 2.6 Loose ends

The DIKW pyramid figure introduces **Wisdom** as a fourth tier, but the surrounding text discusses only data, information, and knowledge. Either add a sentence on wisdom or use a figure that stops at knowledge.

The `wooden_bear.png` image in Section 2 appears with no caption and no reference in the surrounding text. I assume it illustrates the book-and-metadata analogy, but a student reading alone will not know that. Add a one-line caption.

### 2.7 Downstream consistency

You chose the plain `ASK -> GET -> EXPLORE -> MODEL -> COMMUNICATE` form. `Notes/07-exploratory_data_analysis.ipynb` uses the bracketed `[EXPLORE]` variant. Worth a sweep across Modules 3 through 11 once these two are settled.

---

## 3. Examples and activities

### 3.1 Overall assessment

Both notebooks are activity-rich, which suits the applied, intuition-first approach. The problem is density against a 55-minute period, and a difficulty distribution that is narrower than it looks.

**Module 1** currently holds five activities and three examples. Every one is discussion-based and opinion-driven. Not one has a determinate answer. For a class that includes CS majors with no stats background and students who are quiet in discussion, an entire opening module with no checkable answer offers nothing to hold onto. Module 2's feature-type work is the natural place to correct this, which is part of why 3.3 matters.

**Module 2** is better balanced, because the penguins code gives students something concrete, but it is long, and ten activities in roughly 1.5 periods is not achievable.

### 3.2 Merge Store Products into Activity 1.5 (approved)

Currently the pattern and the shopper vignette sit in separate cells with a heading between them, so the narrative breaks precisely where it should build. Merge into one Activity 1.5 containing the department store scenario, the item list, the Jenny Ward vignette, and the three group questions.

**One recommendation you have not yet ruled on.** This is the Target pregnancy-prediction case, documented by Charles Duhigg in the *New York Times Magazine*, February 2012. The "Jenny Ward" vignette and the blue rug come from that article. Presenting it as hypothetical costs you the strongest thing about it, which is that it actually happened, and it sits awkwardly against the accuracy standard in your collaboration guide. I would attribute it, and add a closing line inviting students to read the original. Sourcing note: the article is widely cited and I am confident of its existence and authorship, but verify the specific details against the original before printing an attribution.

A parallel attribution issue: the Venn diagram is Drew Conway's Data Science Venn Diagram (2010), and the "hacking skills" quotation is his. The notebook says only "According to the author of the image." Naming him costs one clause and models the citation behavior you want from students.

### 3.3 Add the feature-type drill to Section 3 (approved)

Activity 2.4 currently offers a single binary comparison, `species` versus `body_mass_g`, where the answer is obvious before any thought occurs. The measurement-scale table deserves genuine practice, and this is the one place in either module where a determinate answer is available.

Proposed **Activity 2.5**, placed after the `value_counts` example:

> ### Activity 2.5 - What type is it?
>
> Classify each feature by measurement scale (nominal, ordinal, interval, ratio). Three of these are contested. Be ready to defend your answer.
>
> | # | Feature |
> | --- | --- |
> | 1 | Penguin species (Adelie, Chinstrap, Gentoo) |
> | 2 | Flipper length in mm |
> | 3 | The island a penguin was found on |
> | 4 | A student's class standing (first-year, sophomore, junior, senior) |
> | 5 | A UWL student ID number |
> | 6 | Course grade on the A, AB, B, BC, C scale |
> | 7 | The year a measurement was taken |
> | 8 | Temperature in degrees Celsius |
>
> For any two features you classified differently, name the operation that is meaningful for one and not the other.

Followed by a `RUN-TOGETHER` cell connecting scale to storage:

```python
# RUN-TOGETHER
# How Python STORES a feature is not the same as what the feature MEANS.
print(penguins.dtypes)
```

> **Discuss.** `body_mass_g` is stored as `float64` and `species` as an object. Does knowing the dtype tell you the measurement scale? Where would this reasoning fail?

Items 5 and 7 are the traps, and item 6 is the one that produces the best argument. This drill is what Homework 1's Problem A3 and Part C build on directly.

### 3.4 Add Activity 2.7 to Section 5 (approved)

Section 5 is the only section in either notebook with exposition, a definition, and a table, and no activity. It is also where the acquisition table risks being read passively.

> ### Activity 2.7 - Match the source, find the catch
>
> Your group is asked: **do UWL students who use the library more often earn higher grades?**
>
> For each source below, decide (a) which row of the acquisition table it belongs to, (b) what its catch is for *this* question, and (c) whether you would use it.
>
> | # | Available source |
> | --- | --- |
> | 1 | Library door-counter totals, by hour, for the past three years |
> | 2 | A voluntary survey emailed to all students asking how often they study in the library |
> | 3 | Registrar records of every student's GPA |
> | 4 | Wireless network logs showing which access point each device connected to |
>
> **Then:** none of these four is sufficient on its own. What would you actually need, and what would it take to get it? Does anything about source 4 concern you?

This lands the "relevant, trustworthy, and suitable" distinction, previews the joining problem, and puts an ethics question inside a technical activity rather than quarantining ethics in Module 1. Source 1 has no student identifiers and cannot be linked to grades at all, which is the point students should reach on their own.

### 3.5 Cuts I recommend

Ten activities will not fit Module 2. Two candidates:

**Merge Activities 2.1 and 2.6.** Data Sources I and II are explicitly the same exercise revisited, and Activity 2.6 asks students to recall an answer from a class period earlier, which in practice means most groups reconstruct it from scratch. Consider a single activity in Section 4 that does both jobs at once.

**Consider dropping Activity 2.9.** Guessing what fraction of wildlife footage is informative is thin, and Activity 2.10 makes the same point about the gap between having data and having knowledge with far more traction. If you keep it, fold it into the Section 7 table as a one-line prompt rather than a standalone activity.

**Trim Activity 1.1 from ten tasks to six.** Ten items is more than a group will get through in the opening minutes of the first day, and the list contains near-duplicates. Items 2, 4, and 10 all make the same "just a summary statistic" point. Keeping 1, 3, 5, 6, 8, and 9 preserves the full spread from clearly-not to clearly-yes.

### 3.6 Placement

One suggestion beyond the approved set. Activity 1.1 currently sits *above* the `## 1. Definition of Data Science` heading, outside the numbered structure. As a cold open that is defensible and I would keep the pedagogy, but give it a home: either retitle the section `## 1. What counts as data science?` and place the activity inside it, or label the cell explicitly as a warm-up so its position looks deliberate.

---

## 4. Decisions already made

| Decision | Choice |
| --- | --- |
| Header blocks | **Key Concepts** in both, matching MTH 265 |
| Labeling | **Class Example** for worked items, **Activity** for group work, numbered `module.index` |
| Suggested Exercises | Add to both notebooks; HW1 problems parallel them |
| Module 1 code cells | None; discussion-only by design |
| Course loop notation | Plain `ASK -> GET -> EXPLORE -> MODEL -> COMMUNICATE` |
| Store Products | Merge with Activity 5 |
| Activity 1.4 (personal data) | Keep in class; mirrored as HW1 Problem D1 |
| Section 3 drill | Add, with the dtypes code cell |
| Digitization example | Remove from Module 2; recycled as HW1 Problem D2 |
| Professional Summary | Defer to a later module |

---

## 5. Open questions

1. **5-C ordering** (2.3). Present-first or discover-first?
2. **Target attribution** (3.2). Attribute the case to Duhigg and the *NYT*, or keep it hypothetical?
3. **Conway attribution** (3.2). Name him as the source of the Venn diagram and the hacking-skills quotation?
4. **The three cuts** (3.5). Merge Activities 2.1 and 2.6? Drop 2.9? Trim Activity 1.1 to six items?
5. **Huber's 50 to 80% figure** (Module 2, Section 5). Attributed to Huber in the text without a chapter or page. I could not verify it against the source. A range like this circulates widely with varying attributions, so it needs a specific citation or softer wording before it goes to students.
6. **Suggested Exercises.** Approved in principle. How many per notebook, and should they be end-of-notebook or end-of-section as in MTH 265?

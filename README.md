# translatepi

A small reading-point infrastructure for translating public posts into
inspectable specifications.

The sites use JSON feeds containing:

- an original reading point
- a link to the original post
- a Grok response
- previous / next navigation

The newest reading point appears first.

## #clean_datacenters

**https://repairearth.ai**

Reads datacenters through measurable resources and engineering constraints.

Typical specification:

> resource → reading point → admissible allocation

Energy, water, hardware, compute capacity, and allocation remain distinct
engineering objects and measurable states.

The mathematical anchor is

\[
(1+1)\times3\times5=30
\]

where primes \(p>5\) satisfy

\[
p\bmod30\in\{1,7,11,13,17,19,23,29\}.
\]

The exact number theory supplies a mathematical reading point.
Engineering generalizations remain separate claims to specify and test.

**exact constraint → engineering generalization → measurable resource state**

## #LeanProver

**https://translatepi.ai**

Translates mathematical and physical claims involving \(\pi\) into explicit
formalization targets for Lean.

Typical specification:

> figure → theorem → kernel check

Different equations can contain the same constant while giving it different
mathematical roles.

**same π ≠ same specification**

The goal is to identify the smallest exact statement that lifts from an
informal post, figure, or equation into a theorem that can be checked by the
Lean kernel.

**claim → specification → proof**

## Feed format

Each site reads entries from `feed.json`.

```json
[
  {
    "text": "reading point",
    "grok": "Grok response",
    "url": "https://x.com/.../status/..."
  }
]

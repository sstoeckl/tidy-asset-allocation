# The reverse outline: format

One file per chapter, `review/outline/NN-slug.md` (`index.qmd` is
`00-preface.md`). A reverse outline reports what the text *does* as it stands,
not what it should do: it is the map the author reads to decide where the
argument is thin, where a section sits in the wrong place, and where a
paragraph does no work. Summaries paraphrase in plain words; no quotation
longer than a few words; every line short. Nothing about the modeled market
is given a calendar year (CLAUDE.md, "The calendar rule").

## The file

```
---
file: chapters/NN-slug.qmd
title: <chapter title, as in the front matter>
part: <the part the chapter sits in, from _quarto.yml>
words: <wc -w of the .qmd>
sections: <number of ## sections>
paragraphs: <number of prose paragraphs counted below>
---

# Chapter

Claim: <one sentence: the chapter's answer to its question, as the text argues it>
Question: <the question the opening poses, in one line, and whom it cites for it>
Why here: <what the chapter needs from earlier chapters and what later ones take from it, as the text says or implies; "not stated" when the text never says why it sits where it does>
Does: <what the reader can do afterwards, one line>
Order: <the sequence of sections in one sentence (theory, implementation, application, takeaways, exercises); name any deviation from that contract>

# Sections

## <section title> — <words in the section>

Says: <one sentence: the section's point>
Why here: <why it comes now: what it needs from before, what the next section needs from it; "not stated" when the text gives no reason>
Paragraphs:
- ¶1 [type] <one line, at most 20 words: what the paragraph says>
- (code: <chunk label>)
- ¶2 [type] ...
Note: <optional, one line: anything structural that stands out: two paragraphs making one point, a paragraph with no point, a definition after its first use, a callout where it does not belong, a section mixing two topics; omit the line when nothing stands out>

### <subsection title> — <words>

(the same block, nested under its section)
```

## Paragraph types

One per paragraph, in square brackets:

| type | the paragraph |
|---|---|
| claim | asserts something the chapter argues for |
| evidence | supports a claim with a number, a figure or a citation |
| definition | defines a term or a symbol |
| derivation | works through mathematics |
| method | says what will be done and how |
| code | narrates what a chunk does or shows |
| result | reads a number, a table or a figure |
| caveat | a limit, a trap, a package behavior |
| transition | points forward or back and does no work of its own |
| example | a worked case |
| takeaway | a Key Takeaways bullet |
| exercise | an exercise |

## What counts

- A paragraph is a block of prose between blank lines, after the YAML front
  matter. Display equations belong to the paragraph that introduces them.
- Code chunks are not paragraphs; each is noted where it falls, on its own
  line, as `(code: label)`, so the map shows where the code sits in the
  argument. The opening "packages used" block is noted the same way.
- A callout is a paragraph (or several) marked `(callout)` after its type.
- Figure and table captions are not paragraphs.
- Key Takeaways: one line per bullet, type takeaway. Exercises: one line per
  exercise, type exercise.
- Section word counts are approximate (`wc -w` of the section's text,
  code included).

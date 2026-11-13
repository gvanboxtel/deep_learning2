## Beta test

This module is a beta test. When you or the user notice a problem in the subject (typo, ambiguity, contradiction between text and expected output, missing tester input, rule that conflicts with an exercise), add it to `BETA_NOTES.md` under "Issues" in the same turn and tell the user in one line. At the end, the user runs `/beta-review`.

## Issue tracker

- Issues live in GitHub Issues of `gvanboxtel/deep_learning2`. Use the `gh` CLI.
- Board: https://github.com/users/gvanboxtel/projects/8 (project #8, owner `gvanboxtel`). Columns (field `Status`): Backlog, Ready, In Progress, Review, Done, Won't Do – Duplicate, On hold.
- Board fields: `Priority` (P0 Mandatory, P1 Bonus, P2 Extra), `Size` (XS ≈ 1 h, S 1–2 h, M 2–3 h, L 3–5 h, XL > 5 h), `Estimate (h)`. Epics get Status, Priority and Estimate (the sum of their sub-issues), no Size.
- Epics (title `Epic: ...`, label `epic`) group the issues as sub-issues. Issue titles have a prefix: `SETUP`, `IMG` (ex00), `CONV` (ex01), `CNN` (ex02), `EVAL` (ex03), `TL` (ex04), `DEF`. Bonus and extra titles start with `Bonus:` / `Extra:` after the prefix.
- Labels:
  - type: `enhancement`, `bug`, `chore`, `documentation`
  - area: `setup`, `ex00`, `ex01`, `ex02`, `ex03`, `ex04`, `defense`, `bonus`, `extra`
  - `size: <XS..XL>` and `time: <N>h` on every sub-issue, matching the board fields
  - `ready-for-human`: the student implements it
- Issue body sections: Context, Learn first, Think about, Tasks, Check yourself, Acceptance criteria, Related (with "Blocked by #N"). Write new issues in teaching mode: pointers and hints, no solutions. "Learn first" holds sources researched per issue, each naming the question it answers; a "**Go deeper**" block at its end links the P2 (`Extra:`) issues that deepen a part of this one, and the deeper sources live in those P2 issues. P2 issues sit in the epic of the area they deepen. Open subject questions (see `BETA_NOTES.md`) go under "Think about".
- A new issue gets the labels above, is added to the board with Status, Priority, Size and Estimate set, and is linked as a sub-issue of its epic.

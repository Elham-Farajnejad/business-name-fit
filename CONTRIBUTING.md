# Contributing

Thanks for helping make this skill better! You don't need to be a programmer to contribute —
cultural and language knowledge is the most valuable thing here.

## Ways to help

- **Share a tricky name.** A name that works in one language but goes wrong in another is a
  great real-world test case. Open an issue describing the name, its origin, and the market
  where it causes trouble.
- **Add language/cultural notes.** If the skill missed a bad meaning, an awkward
  pronunciation, or a cultural nuance in a language you know, tell us — or edit the checks
  in `business-name-fit/SKILL.md` directly.
- **Improve the wording** of the skill's instructions so Claude follows them more reliably.
- **Add a worked example.** A full case in `business-name-fit/examples/worked-examples.md`
  showing a name checked end to end is one of the most useful things you can write.

## Where things live

| Path | What it is |
|---|---|
| `business-name-fit/SKILL.md` | The instructions Claude follows. Most changes go here. |
| `business-name-fit/examples/worked-examples.md` | Full worked cases, read when Claude needs a model for a finished analysis. |
| `business-name-fit/references/naming-research.md` | The published sources behind the checks, read when a founder asks *why*. |
| `business-name-fit.skill` | **Generated.** A zip of the folder above — don't edit by hand. |
| `NOTICE.md` | Attribution for third-party files. |

`SKILL.md` points Claude at the other two markdown files by relative path, so if you move
or rename one, update the reference in `SKILL.md` too.

## How to propose a change

1. Fork this repository.
2. Make your edit (most changes live in `business-name-fit/SKILL.md`).
3. **If you changed anything inside `business-name-fit/`, rebuild the bundle:**
   ```
   python build.py
   ```
   This regenerates `business-name-fit.skill` from the source folder. Commit the rebuilt
   file alongside your edit — otherwise the one-click install and the source folder ship
   different versions of the skill.
4. Open a pull request with a short note on what you changed and why.

If you edit the skill, please try it on a couple of real names before submitting, and
describe what you tested in the pull request.

## Adding a research source

If you cite new research in `naming-research.md`, link to a freely accessible copy rather
than committing the PDF. Only commit a file when its license clearly permits
redistribution — and if you do, add the attribution to [NOTICE.md](./NOTICE.md). Journal
articles almost never permit it; intergovernmental and open-access publications often do.

## Ground rules

- Keep suggestions respectful of every culture and language.
- Explain the *why* behind a change so others can learn from it.

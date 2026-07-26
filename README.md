# Business Name Fit — a Claude Skill

![business-name-fit demo](name_fit_user_experience.gif)


A skill for [Claude](https://claude.ai) that helps founders pick or check a business,
startup, or product name that stays **authentic to their cultural origin** while working
well in the **markets they want to sell into**.

A name can be perfectly good in its home language yet confusing, funny, or off-putting
elsewhere. This skill catches that mismatch before it costs you.

## What it does

- **Suggests** new names rooted in your origin language and culture.
- **Checks** names you already have, market by market.
- Runs every name through eight checks: hidden bad meanings, look-alike words,
  pronunciation, spelling, legal distinctiveness, how it sounds aloud, tone fit for your
  industry, and origin authenticity.
- Presents results as a quick shortlist, a detailed report, or a pass/fail table —
  whichever you ask for.

## Why it exists

Real examples the skill is built to catch:

- **آنالی / "Anali"** — a lovely Azeri name, but the Latin spelling reads badly in English.
- **"framåt"** (Swedish for *forward*) — sounds like "frame" to an English ear.
- **نگار / "Negar"** — means *painting* in Persian, ideal for an art business, but the
  spelling sits too close to an offensive English slur for a US-based brand.

## Install

**Option A — one click (easiest):**
Download [`business-name-fit.skill`](./business-name-fit.skill), open it in Claude, and
click **Save skill**. (Skill saving must be enabled for your account or organization.)

**Option B — from the source folder:**
Copy the [`business-name-fit/`](./business-name-fit) folder into your skills directory.

## Use it

Just describe your situation to Claude, for example:

> I'm an Iranian founder starting a childcare company for the Iranian and Gulf markets.
> I'm thinking of the name "Anali" — does it work?

or

> Suggest some Persian-rooted names for an art-authentication startup based in the US.

## Good to know

The skill flags—but cannot verify—**domain availability and trademarks**. Always check
those separately, and run your finalists past a **native speaker** of each target market.

## Examples

Three worked scenarios — a name fixed, a name approved, a name rejected — are in
[`examples/worked-examples.md`](./business-name-fit/examples/worked-examples.md).
A condensed version of the first:

> A Tehran childcare group called **Anali** is expanding to Dubai and Doha. The name is a
> warm Azeri girl's name and, on the sound check, close to ideal for childcare — soft
> consonants, open vowels. But the Latin spelling opens with a crude English word.
>
> The two checks disagreeing *is* the finding: the name fails on paper but not aloud. So
> the fix is not a rebrand but a respelling — **Annali** — which keeps exactly what
> Iranian parents already say.

The other two scenarios cover a Swedish consultancy whose name passes but sits in a
crowded namespace, and an Iranian-American art startup whose name fails twice over — once
on an unfortunate English association, and again because "painting" is legally descriptive
for a painting business.

## Grounded in published research

The checks aren't invented — they draw on three freely downloadable sources, summarised in
[`references/naming-research.md`](./business-name-fit/references/naming-research.md):

- **WIPO, *Making a Mark*** — the name categories that decide whether a name can be legally
  protected at all (generic, descriptive, deceptive, suggestive, coined).
- **Kohli & LaBahn (1997), *Creating Effective Brand Names*** — the five-stage naming
  process, and the warning that people ruin their own naming by rushing evaluation.
- **Pogacar et al. (2015), *Sounds good*** — how a name's sounds shape the impression it
  makes, and why those effects don't transfer automatically between languages.

## Contributing

Improvements are very welcome — especially language and cultural knowledge that helps the
skill spot problems it might miss. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

Released under the [MIT License](./LICENSE) — free to use, share, and build on.

One bundled file is third-party: WIPO's *Making a Mark*, redistributed under
[CC BY 3.0 IGO](https://creativecommons.org/licenses/by/3.0/igo/) and not covered by the
MIT License. Full attribution is in [NOTICE.md](./NOTICE.md).

---
description: Búa til nýja málamöppu úr snidmat/
argument-hint: <slug> [Heiti málsins]
---

Notandi vill búa til nýtt mál með slug `$1`. Mannlæsanlegt heiti málsins er `$2` (ef tómt eða óljóst, biddu notanda um það áður en þú heldur áfram).

Verkefni:

1. Athugaðu að `malefni/$1/` sé ekki þegar til. Ef til er, hætta og biðja notanda að velja annan slug.
2. Búðu til möppurnar: `malefni/$1/`, `malefni/$1/heimildir/`, `malefni/$1/ai-greining/`.
3. Afritaðu sniðmát:
   - `snidmat/README.md` → `malefni/$1/README.md`
   - `snidmat/ritstjorn.md` → `malefni/$1/ritstjorn.md`
   (Engin `heimildir.md` index-skrá — heimildir verða ein skrá per stykki í `malefni/$1/heimildir/`, bætt við með `/heimild`.)
4. Skiptu út placeholder `[Heiti máls]` í báðum afrituðu skránum með málheiti notanda.
5. Settu `Stofnað:` og `Síðast uppfært:` í `ritstjorn.md` á dagsetningu dagsins í dag.
6. Tilkynntu hvað var gert og biddu notanda um:
   - **Áherslu og afmörkun** (2–4 setningar) sem þú getur skrifað fyrir hann inn í `ritstjorn.md`
   - **Fyrstu heimildir** til að bæta við með `/heimild`

Ekki keyra önnur slash commands sjálfkrafa — bíddu eftir leiðbeiningum notanda.

---
description: Sannprófa að allar [H###] tilvitnanir í máli vísi í gildar heimildaskrár
argument-hint: <slug>
allowed-tools: Read, Bash, Grep
---

Notandi vill sannprófa að allar `[H###]` tilvitnanir í máli `$1` séu gildar — engar AI-hallucinations.

Þetta er **sannprófunar-skipun**: aðeins lesa, aldrei breyta neinu.

## Verkefni

1. **Finna gildar heimildir.** Listaðu `malefni/$1/heimildir/*.md` og dragðu fram öll `H###` auðkenni úr skráarheitum (og staðfestu með `id:` í frontmatter).

2. **Finna tilvitnanir í texta.** Grep-aðu allar `.md` skrár í `malefni/$1/` **utan** `heimildir/` möppunni fyrir mynstri:
   - `\[H[0-9]+\]` (gamalt snið án linkar)
   - `\[H[0-9]+\]\(heimildir/[^)]+\)` (nýtt smellanlegt snið)

   Safnaðu öllum notuðum auðkennum og slóðum sem tilvitnanir benda á, með skrá+línu.

3. **Athuganir:**
   - **Auðkenni notuð en EKKI til** í `heimildir/` → AI-hallucination-grunsemd. Listaðu skrá+línu.
   - **Smellanleg auðkenni benda á skrá sem er EKKI til** → vísanir í dáin skráarheiti. Listaðu.
   - **Smellanleg auðkenni benda á rangt H###** (t.d. `[H001](heimildir/H002-...md)`) → röng vísun. Listaðu.
   - **Auðkenni án smellanlegrar linkar** (gamalt `[H001]`) → hvettu til uppfærslu í `[H001](heimildir/H001-...md)` snið.
   - **Heimildir til en EKKI notaðar hvergi** → ónotaðar heimildir. Listaðu.
   - **Heimildaskrár án `Fullt efni`-kafla** → ekki archive-aðar; viðkvæmar fyrir link rot. Listaðu.

## Skýrsla

```
Sannprófun fyrir mál: $1

✓ Heildarfjöldi tilvitnana: <n>
✓ Einkvæmar heimildir notaðar: <n> af <total í heimildir/>

✗ AI-hallucinations (auðkenni án heimildaskráar):
  - <ef einhverjar — listi með skrá:lína>

✗ Dáin slóð í smellanlegri tilvitnun:
  - <listi>

✗ Auðkenni vs slóð stangast á:
  - <listi>

⚠ Tilvitnanir án smellanlegs link (gamalt snið):
  - <listi>

⚠ Ónotaðar heimildir:
  - <listi>

⚠ Heimildir án archive (Fullt efni vantar):
  - <listi>

Niðurstaða: <STENST / STENST EKKI — krefst aðgerða>
```

Ef niðurstaðan er "STENST EKKI", legðu til hvað ritstjóri eigi að gera (t.d. "Bæta heimild H006 með `/heimild $1 <URL>` eða fjarlægja tilvitnun í `malefni/$1/README.md:42`").

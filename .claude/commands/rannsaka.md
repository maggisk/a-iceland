---
description: Keyra AI-rannsókn fyrir mál — finna heimildir, skrifa samantekt og greiningar
argument-hint: <slug>
---

Notandi vill keyra AI-rannsókn fyrir mál `$1`.

## Skref 1 — lestur

Lestu eftirfarandi skrár í þessari röð, **og ekki sleppa neinu**:

1. `leidbeiningar/fyrir-ai.md` — almennar reglur sem gilda fyrir öll mál
2. `mal/$1/ritstjorn.md` — mannlegar leiðbeiningar fyrir þetta mál. **Æðsta forgang.** Ef eitthvað í `fyrir-ai.md` stangast á við þetta, þá vinnur `ritstjorn.md`.
3. Allar skrár í `mal/$1/heimildir/` — hver skrá er ein heimild með frontmatter, lýsingu, tilvitnunum, greiningu og fullu textaefni. Lestu allar, þar með talið hráefnið neðst.

## Skref 2 — heimildaöflun (skilyrt)

**Spurning:** Þarf að leita að nýjum heimildum?

- **Já** ef: `heimildir/` er tóm, eða færri en ~5 heimildir, eða ritstjorn.md hefur óklárð leiðbeiningu sem krefst nýrra heimilda (t.d. "rannsakaðu líka X", "finndu heimild um Y").
- **Nei** ef: heimildir/ er fullnægjandi og ritstjorn.md biður ekki um meira.

**Ef já:** Fylgdu `Reglur fyrir heimildaöflun`-kafla í `fyrir-ai.md`. Notaðu `WebSearch` með íslenskum og enskum leitarorðum. Skiláðu kandídata-lista með titli, slóð, tegund, sjónarhornsgiski, lýsingu og rökstuðningi. Segðu líka frá leitarorðum og höfnunum.

**STÖÐVAÐU** og biddu ritstjóra að samþykkja kandídata. Ekki vista neitt fyrr en samþykki liggur fyrir.

Þegar samþykki liggur fyrir, vistaðu hverja samþykkta heimild með sömu rökfræði og `/heimild`-skipunin — þ.e. nota `WebFetch` á slóðina, búa til `heimildir/H###-stutt-slug.md` skrá samkvæmt `snidmat/heimild.md`. Síðan **hættu þessari keyrslu** og biddu ritstjóra að keyra `/rannsaka $1` aftur fyrir skrifa-fasann.

**Ef nei:** Haltu áfram á Skref 3.

## Skref 3 — vinnsla (skrifa samantekt og greiningar)

Fylgdu nákvæmlega:

- Reglum í `fyrir-ai.md` (sérstaklega tilvitnunarreglum)
- Verkefnalistanum og mati ritstjóra á heimildum í `ritstjorn.md`
- Sniðmáti `snidmat/README.md` fyrir samantekt málsins
- Sniðmáti `snidmat/ai-greining.md` fyrir greiningarskjöl

Skrifaðu/uppfærðu eftir verkefnalista í `ritstjorn.md`:

- `mal/$1/README.md` — samantekt málsins (AI-skrifuð)
- Skrár í `mal/$1/ai-greining/` — ein per sjónarhorn eða per spurning eins og ritstjóri leiðbeinir

Í hverju skjali sem þú skrifar:

- Tilvitnanir með smellanlegu sniði `[H###](heimildir/H###-...md)` í hverja efnislega fullyrðingu
- Engar utanaðkomandi tilvitnanir, engin almenn þekking
- Model og dagsetning efst

## Skref 4 — skýrsla

Eftir keyrslu, skilaðu **samanteknu yfirliti til notandans** sem inniheldur:

1. **Verkefni úr `ritstjorn.md` sem þú kláraðir** — listi með `[x]`
2. **Verkefni sem standa eftir** — og af hverju (t.d. vantar heimildir)
3. **Heimildir notaðar** — hverjar af öllum í `heimildir/`, hverjar ekki og af hverju
4. **Sjónarmið sem eru veikt eða vanta** — heiðarlegur listi
5. **Spurningar sem heimildir svara ekki**
6. **Tillögur að nýjum leiðbeiningum** sem ritstjóri gæti bætt við í `ritstjorn.md`

## Mikilvægt

- **Ekki breyta `ritstjorn.md`.** Það er eina mannlega skjalið. Leggðu til breytingar í skýrslunni, ritstjóri ákveður.
- Eftir á, biddu notanda að keyra `/sannprofa $1` til að staðfesta að allar tilvitnanir séu gildar.

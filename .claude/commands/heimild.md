---
description: Bæta nýrri heimild við mál — sækja, vista (með archive), greina
argument-hint: <slug> <URL>
---

Notandi vill bæta nýrri heimild við mál `$1` af slóð `$2`.

## Verkefni

1. **Athuga að málið sé til.** `mal/$1/ritstjorn.md` verður að vera til. Ef ekki, segðu notanda að keyra `/nyttmal $1 "<heiti>"` fyrst.

2. **Sækja efnið.** Notaðu `WebFetch` á slóð `$2` og dregdu fram aðalefnið (texta greinarinnar/skýrslunnar, ekki nav/auglýsingar/footer). Reyndu líka að finna í greininni:
   - Birtingardagsetning (`birt`)
   - Höfundur (`hofundur`)
   - Útgefandi (`utgefandi`)

3. **Finna næsta auðkenni.** Listaðu `mal/$1/heimildir/` og finndu hæsta núverandi `H###` í skráarheitum. Næsta er einu hærra (eða `H001` ef tóm mappa).

4. **Búa til heimildaskrá.** Notaðu `snidmat/heimild.md` sem sniðmát. Skráin heitir `mal/$1/heimildir/H###-stutt-kebab-slug.md`. Slug skal vera 2–5 orð sem lýsa heimildinni (ASCII, kebab-case, ekki íslenskir stafir).

   Fylltu inn:
   - **Frontmatter** með `id`, `url`, `sott` (dagsetning dagsins í dag), `birt`, `hofundur`, `utgefandi`, `tegund` (giskaðu: grein/skyrsla/log/tolfraedi/vidtal/samfelagsmidlar/annad), `sjonarhorn` (giskaðu: A/B/hlutlaust/blandad — biddu notanda að staðfesta í lokin).
   - **Heiti heimildar** (titill greinarinnar)
   - **Lýsing** (1–3 setningar — hvers vegna er heimildin í þessu máli, hvað segir hún í stuttu máli)
   - **Tilvitnanir til notkunar** — 2–4 athyglisverðustu, orðréttar setningar úr efninu (með bls./tímamerki ef við á)
   - **Greining** — fjórir undirkaflar samkvæmt `snidmat/heimild.md`:
     - *Helstu fullyrðingar* — listi af aðalfullyrðingum
     - *Aðferð og umfang* — hvernig gögnum var safnað, hvað dekkar heimildin
     - *Hvað heimildin segir EKKI* — afmarkanir
     - *Tengingar við aðrar heimildir* — ef einhverjar heimildir eru þegar til í `mal/$1/heimildir/`, þá berdu saman. Notaðu smellanleg auðkenni: `[H003](heimildir/H003-...md)`.

     **Mikilvægt:** Ekki skrifa áreiðanleika-mat, ekki rökstyðja sjónarhorn, ekki tilkall hagsmunatengingar í Greining-kafla. Það er hlutverk ritstjóra í `ritstjorn.md`.

   - **Fullt efni** — allt textaefnið sem þú náðir úr WebFetch. Þetta er archive ef linkur deyr.

5. **Tilkynning.** Skiláðu samantekt:
   - Hvaða auðkenni heimildin fékk (`H###`)
   - Skráarheiti
   - Stutta yfirlýsingu um hvað heimildin segir (1 setning)
   - Beiðni um:
     - Staðfestingu á `sjonarhorn` í frontmatter
     - Hvort eigi að uppfæra `Mat á heimildum`-kafla í `ritstjorn.md` núna (eða bíða)

Ekki keyra `/rannsaka` sjálfkrafa.

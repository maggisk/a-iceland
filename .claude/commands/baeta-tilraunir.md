---
description: Lesa heimildir og README, leggja til Python-tilraunir sem myndu styrkja eða veikja ráðleggingu. Skrifar tillögur í ai-greining/tilraunir-hugmyndir.md — engar keyrslur sjálfvirkt. Idempotent.
argument-hint: <slug>
---

Notandi vill fá tillögur að Python-tilraunum sem myndu prófa fullyrðingar í greiningu málsins `$1`.

> **Hugarfar:** Þetta er **proposal-skipun**, ekki framkvæmd. Þú lest heimildir, README og núverandi greining/, og leggur til Python-tilraunir sem ritstjóri eða AI gæti síðar keyrt í `greining/src/$1/`. Hver tilraun skal hafa skýra tilgátu, skýrar forsendur, vísun í heimildir fyrir grunngögn, og væntanlegt output-form. **Engar keyrslur í þessari skipun** — engar Python-skrár eru smíðaðar, engin númeralíkön eru reiknuð. Aðeins tillögur.

> **Idempotent:** Endurkeyrsla yfirskrifar `ai-greining/tilraunir-hugmyndir.md` með nýrri útgáfu sem inniheldur **bæði** eldri tillögur (sem ritstjóri hefur ekki klárað/hafnað) og nýjar. Ritstjóri merkir tillögur sem klárðar/hafnaðar handvirkt.

> **Eingöngu tilraunir-tillögur.** Engar breytingar á `heimildir/`, `README.md`, `ritstjorn.md` eða `ai-greining/`-skrám öðrum en `tilraunir-hugmyndir.md`. Þessi skipun er hluti af `/baeta`-fjölskyldunni (sjá líka `/baeta-heimildir`, `/baeta-utfyrir-boxid`, og wrapper `/baeta`).

---

## Skref 0 — fyrirskoðun

1. **Staðfestu slug:** `malefni/$1/` skal vera til.
2. **Athugaðu nauðsynlegar skrár:**
   - `malefni/$1/ritstjorn.md`
   - `malefni/$1/README.md` (þetta er kjarna-skjalið — ef það er ekki til, þá hefur `/greina` ekki verið keyrt enn; stöðva og biðja ritstjóra að keyra `/greina $1` fyrst)
   - `leidbeiningar/fyrir-ai.md`
   - `greining/README.md` (reglur fyrir Python-tilraunir í repo-inu)
3. **Athugaðu lágmarks-massa:** safnið `heimildir/` skal hafa **a.m.k. 5 heimildir** og README **a.m.k. eina greinilega ráðleggingu**. Annars er ekki nóg synthese til að byggja tilraunir á.
4. **Skráðu keyrslu:** birtu efst: model-nafn, dagsetning, slug `$1`, fjöldi heimilda, og hvort `ai-greining/tilraunir-hugmyndir.md` sé þegar til (þá merkir endurkeyrsla).

Ef einhver athugun bregst — **STÖÐVAÐU**.

---

## Skref 1 — lestur

Í þessari röð:

1. `leidbeiningar/fyrir-ai.md` — almennar reglur.
2. `malefni/$1/ritstjorn.md` — frame ritstjóra. Athugaðu sérstaklega forsendur fyrir ráðleggingu (lagaleg vs. aðferðafræðileg) og hvort ritstjóri hefur óskað eftir eða útilokað ákveðnar tilraunir.
3. `malefni/$1/README.md` — synthese + ráðlegging. Þetta er aðal-uppspretta fullyrðinga sem hægt er að testa.
4. `greining/README.md` — reglur fyrir Python-tilraunir í repo-inu (sniðmát, dependencies, sensitivity-skyldur, citation-reglur).
5. `greining/src/$1/` (ef til) — núverandi tilraunir. Forðast tvíverknað.
6. `ai-greining/tilraunir-hugmyndir.md` (ef til) — eldri tillögur sem skal halda áfram með (þeim sem ritstjóri merkir ekki sem klárða eða hafnaða).
7. **Allar heimildir** í `heimildir/H###-*.md` — yfirborðs-skönnun á þessari skipun (ekki orð fyrir orð eins og /baeta-heimildir). Þú þarft að vita hvaða gögn eru í safninu þegar þú leggur til hvar tilraunir geta sótt grunngögn.

Eftir lestur, birtu stutta yfirlit (3–6 línur):
- Fjöldi heimilda, hvort `/greina` hefur keyrt (README til), hvort eldri tilraunir eru til.
- Ríkjandi ráðlegging í README og lykilforsendur hennar.
- Núverandi tilraunir í `greining/src/$1/` ef einhverjar.

---

## Skref 2 — útdráttur fullyrðinga sem hægt er að testa

Lestu README og dragðu út **fullyrðingar sem byggja á kvantitatífum forsendum**. Sérstök athygli:

### 2.1 Cost-benefit-fullyrðingar

Tilvik þar sem heimild eða ráðlegging vísar í IRR, NPV, BCR, ábatahlutfall, eða aðra fjárhagslega mælikvarða. Dæmi úr samgongur: "Cowi 2024 metur IRR 9,2%" — er sú tala viðkvæm fyrir afsláttarvöxtum, lengri/styttri afskriftatíma, eða breyttum forsendum um notkun?

### 2.2 Modal-shift / hegðunarbreyting

Tilvik þar sem fullyrðing reiðir sig á tölu um hve margir muni skipta um ferðamáta. Dæmi: "ef X% bílferða færast yfir á strætó/hjól, þá ..." — sensitivity á aðsóknarmati.

### 2.3 Cross-field beiting

Tilvik þar sem fræðilegt módel frá öðru sviði gæti varpað nýju ljósi. Dæmi: diffusion-líkan úr faraldsfræði beitt á modal-shift adoption; network-flæðisfræði beitt á transit-eftirspurn.

### 2.4 Senario-mat / framtíðar-spá

Tilvik þar sem ráðlegging spáir afleiðingu ("ef congestion pricing er sett, þá mun X gerast"). Hægt að testa með senario-greiningu byggðri á empírískum elasticity-tölum úr heimildum.

### 2.5 Innra samræmi gagna í heimildum

Tilvik þar sem mismunandi heimildir vitna í aðrar tölur fyrir sömu spurningu. Dæmi: Cowi 9,2% IRR vs. Ragnar Árnason "verulega neikvætt núvirði" — má reikna bæði með sama gagnasetti og sjá hvar forsendurnar skiljast?

---

## Skref 3 — meta og forgangsraða tilraunir

Fyrir hverja kandídat-tilraun (úr Skref 2), metðu:

- **Hve sterk er fullyrðingin?** Ef hún er aðeins studd af einni heimild og ritstjóri hefur ekki merkt sem lykil-forsendu, þá er forgangur lágur. Ef margar heimildir reiða sig á henni eða ráðleggingin sveigist með henni, forgangur hár.
- **Hve aðgengileg eru grunngögn?** Ef gögnin þurfa eru í vistuðum heimildum (Cowi-tölur, modal-split frá H014, kostnaðar-tölur frá H001/H033), forgangur hærri. Ef gögn þurfa nýja heimildaöflun, forgangur lægri.
- **Hve mikill kostnaður?** Sensitivity-analysis á einfaldri kostnaðarjöfnu er klukkutími. Network-flow-líkan af öllu höfuðborgarsvæðinu er vikur.
- **Hve líklegt að niðurstaðan breyti ráðleggingu?** Tilraun sem mun aðeins staðfesta áður þekktar tölur er minna virði en tilraun sem gæti hrundið ráðleggingu.

Forgangsraða:
- **HÁR:** sterk fullyrðing, aðgengileg gögn, lágur kostnaður, möguleg breyting á ráðleggingu
- **MIÐ:** annað hvort lægri-kostnaðar tilraun á veikari fullyrðingu, eða hærri-kostnaðar tilraun á sterkri fullyrðingu
- **LÁGUR:** annað hvort djúp cross-field-tilraun (mánaðar-verk) eða sensitivity á ódjúpum fullyrðingum

---

## Skref 4 — skrifa tillögur í `ai-greining/tilraunir-hugmyndir.md`

Ein skrá fyrir málið. Sniðmát:

```markdown
# Hugmyndir að Python-tilraunum — $1 (uppfært YYYY-MM-DD)

> Skipun: `/baeta-tilraunir $1`. Þetta eru **tillögur**, ekki keyrslur. Ritstjóri eða AI velur hvaða á að framkvæma. Þegar tilraun er keyrð, skrá hana í `greining/src/$1/` skv. `greining/README.md` reglum.

## Yfirlit

X HÁR-tillögur, Y MIÐ, Z LÁGUR. Z núverandi tilraunir í `greining/src/$1/`. Síðasta keyrsla: YYYY-MM-DD.

## Status-tafla

| # | Tilraun (stutt) | Forgangur | Staða |
|---|---|---|---|
| T1 | ... | HÁR | tillaga (ekki keyrt) |
| T2 | ... | HÁR | tillaga |

Ritstjóri uppfærir Staða-dálk handvirkt: "tillaga" | "í vinnslu" | "klárt: <slóð>" | "hafnað: <ástæða>"

## T1 — [Stutt nafn]

**Tilgáta:** [Hvað á að prófa? Klár setning sem hægt er að sannreyna/hafna.]

**Aðferð:** [Sensitivity-greining | Senario-mat | Cross-field líkan | Reproduce greiningar | Annað]

**Forsendur (explicit — engin "magic numbers"):**
- Forsenda 1: [gildi + heimild]
- Forsenda 2: [gildi + heimild]
- ...

**Grunngögn:**
- Heimild [H###]: [hvað þaðan]
- ...

**Væntanlegt output:**
- [Hvaða form: tafla, graph, scalar? Hvaða breytur sjást?]
- Sensitivity-skylda: [hvaða forsendur að testa á range hvers]

**Þar sem hún yrði keyrð:** `greining/src/$1/[stutt-nafn].py`

**Tengsl við README:** [Hvaða kafli/fullyrðing í README mun þessi tilraun staðfesta eða hrunda?]

**Rökstuðningur fyrir forgang HÁR/MIÐ/LÁGUR:** [stutt]

## T2 — ...

...
```

**Reglur fyrir innihald:**

1. **Hver tilgáta skal vera falsifiable.** "Cowi 9,2% IRR er viðkvæmt fyrir afsláttarvöxtum" er testanlegt. "Borgarlína er góð hugmynd" er ekki.
2. **Forsendur skulu vera explicit.** Engar "magic numbers" í tilraun. Hver tala skal hafa heimild eða vera flokkuð sem AI-val sem ritstjóri má sjá og hafna.
3. **Heimildastoð skal vera nákvæm.** Notaðu `[H###](heimildir/H###-...md)` smellanlegan link eins og í README. Engin almenn-þekking.
4. **Sensitivity er skylda.** Hver tilraun skal innihalda lista yfir hvaða forsendur að breyta og hvaða range.
5. **Engin yfirskrift á eldri tilögur sem ritstjóri merkir ekki sem klárðar.** Endurkeyrsla heldur ófrágengnum tillögum og bætir við nýjum með næsta T-númeri (T1, T2, T3, ...).

---

## Skref 5 — lokaskýrsla

### 5.1 Nýjar tillögur

| Tnr | Nafn | Forgangur | Tengsl við README |
|---|---|---|---|

### 5.2 Eldri tillögur sem haldnar eru ófrágengnar

| Tnr | Nafn | Forgangur | Eldri-keyrslu-dagur |
|---|---|---|---|

### 5.3 Fullyrðingar í README sem þú gast EKKI lagt til tilraun fyrir

Hver á einni línu: hvaða fullyrðing í README, hver ástæðan er (ekki kvantitatíf, gögn vantar, of dýrt, utan kompetens AI-tilraunar). Þetta er heiðarlegt mat — ekki láta sem allt sé testanlegt.

### 5.4 Næsta skref

Endaðu með einu af:
- *"X nýjar HÁR-tillögur, Y MIÐ. Biddu mig að keyra `/baeta-tilraunir $1` aftur eftir að þú hefur farið yfir og merkt klárðar/hafnaðar tillögur — eða `/baeta-utfyrir-boxid $1` fyrir þverfaglegar nálganir."*
- *"Engar nýjar tillögur — README hefur engar viðbótar testanlegar fullyrðingar sem ekki eru þegar í `tilraunir-hugmyndir.md`. Annaðhvort er greiningin tæmd í testanlegu-skilningi, eða nýjar fullyrðingar þurfa að bætast við README fyrst (`/greina $1` aftur)."*

---

## Reglur sem aldrei má brjóta

1. **Engar Python-keyrslur.** Þessi skipun smíðar EKKI `.py` skrár. Aðeins tillögur í `ai-greining/tilraunir-hugmyndir.md`.
2. **Hver tilgáta vísað til heimildar.** Ef tilraun byggir á fullyrðingu sem ekki er studd af heimild í safninu, sleppa.
3. **Engin uppspunin gögn.** Tillögurnar mega aðeins nota gögn úr vistuðum heimildum. Ef gögnin vantar, segðu það í Skref 5.3.
4. **Idempotent — eldri ófrágengar tillögur eru ekki yfirskrifaðar.**
5. **Ekki skrifa README, ai-greining/-skrár öðruvísi en `tilraunir-hugmyndir.md`, eða `ritstjorn.md`.**
6. **Engin emoji.**
7. **Ef README er ekki til** — stöðva og biðja ritstjóra að keyra `/greina $1` fyrst. Þessi skipun byggir á synthese-fasinn.

---

## Bilanaham — algeng mistök

- **"Tillaga á fullyrðingu sem ekki er í README"** — að leggja til tilraun um efni sem þú heldur að sé mikilvægt en er ekki í greiningu málsins. Tilheyrir `/baeta-heimildir` (ef vísað í heimild) eða `/baeta-utfyrir-boxid` (ef nýtt sjónarhorn).
- **"Tilraun án falsifiable tilgátu"** — "skoða hvort Borgarlína er hagkvæm" er ekki tilgáta. "Cowi-IRR fellur niður fyrir 5% ef afsláttarvextir hækka í 6%" er tilgáta.
- **"Magic numbers í tillögu"** — að nota tölur í aðferðafræði-lýsingu án að nefna úr hvaða heimild þær koma.
- **"Of einföld sensitivity"** — að leggja til "endurreikna Cowi með ólíkum afsláttarvöxtum" án að nefna range eða hvað er væntanlegt útkomu-spread.
- **"Skrifa Python sjálfvirkt"** — engin Python-skrá smíðuð í þessari skipun. Þetta er proposal-fasinn.
- **"Yfirskrifa eldri tillögur"** — endurkeyrsla skal halda ófrágengnum tillögum. Aðeins ritstjóri merkir tillögu sem hafnaða.

---
description: Lesa heimildir, ritstjorn og README. Bera kennsl á ríkjandi ramma málsins og leggja til fræðigreinar utan hans sem gætu auðgað greininguna. Skrifar tillögur í ai-greining/utfyrir-boxid.md. Idempotent.
argument-hint: <slug>
---

Notandi vill fá tillögur að þverfaglegum nálgunum sem ekki eru þegar í greiningu málsins `$1`.

> **Hugarfar:** Þetta er **inductive-um-ramma** skipun. /baeta-heimildir finnur gap í **heimildum**; /baeta-tilraunir finnur gap í **kvantitatífum prófunum**; þessi finnur gap í **fræðilegum ramma**. Spurningin sem hún svarar: *hvaða fræðigreinar bera á þessu máli sem ekki eru í safninu?* Hér ertu ekki að leita heimilda — þú ert að leita **sjónarhorna** sem ríkjandi rammi málsins útilokar.

> **Idempotent:** Endurkeyrsla yfirskrifar `ai-greining/utfyrir-boxid.md` með nýrri útgáfu sem inniheldur eldri tillögur (sem ritstjóri hefur ekki klárað/hafnað) og nýjar.

> **Eingöngu tillögur.** Engar nýjar leitir, engar nýjar heimildir, engar Python-skrár. Þessi skipun framleiðir aðeins skjal með þverfaglegum tillögum sem ritstjóri eða AI gæti notað sem leiðar fyrir /baeta-heimildir eða /baeta-tilraunir í næstu keyrslu.

---

## Skref 0 — fyrirskoðun

1. **Staðfestu slug:** `malefni/$1/` skal vera til.
2. **Athugaðu nauðsynlegar skrár:**
   - `malefni/$1/ritstjorn.md`
   - `malefni/$1/README.md` (ef ekki til, þá hefur /greina ekki keyrt — stöðva og beina á /greina fyrst)
   - `leidbeiningar/fyrir-ai.md`
3. **Athugaðu lágmarks-massa:** safnið skal hafa **a.m.k. 5 heimildir**. Annars er rammin ekki nógu þróaður til að segja hvað er utan hans.
4. **Skráðu keyrslu:** model, dagsetning, slug, fjölda heimilda, hvort `utfyrir-boxid.md` sé þegar til.

Ef bregst — **STÖÐVAÐU**.

---

## Skref 1 — lestur

1. `leidbeiningar/fyrir-ai.md`
2. `malefni/$1/ritstjorn.md` — frame ritstjóra. **Æðsta forgang.** Sérstaklega "Áhersla og afmörkun" — það segir hvað er **vísvitandi útilokað**. Forðast að leggja til sjónarhorn sem ritstjóri hefur þegar útilokað.
3. `malefni/$1/README.md` — synthese.
4. `ai-greining/utfyrir-boxid.md` (ef til) — eldri tillögur.
5. **Yfirborðs-skönnun** á heimildum (ekki orð fyrir orð) — bara til að sjá hvaða fræðigreinar eru þegar í safninu.

Eftir lestur, birtu stutta yfirlit (3–6 línur):
- Hvert er málið (ein setning).
- Hver er ritstjórnar-afmörkun.
- Hvaða fræðigreinar virðast vera í núverandi safni og synthese.

---

## Skref 2 — kortleggja ríkjandi ramma

Listaðu **3–6 fræðigreinar / sjónarhorn** sem ríkjandi greining málsins reiðir sig á. Dæmi fyrir samgongur:

- Samgönguhagfræði (cost-benefit, IRR-greining): [H001, H020, H029, H031, H034]
- Borgarskipulagsfræði (modal split, þétting): [H011, H014, H024, H027]
- Induced demand-fræði (umferðar-eftirspurn): [H010, H016, H034]
- Pólitísk greining (kjósenda-skipting): [H018, H021]
- Loftslags-/umhverfismat: [H026]
- Tæknileg-verkfræðileg (BRT vs LRT spec): [H031, H004, H015]

Þetta er ekki tæmandi — bara höfuðfeitilínurnar. Tilgangurinn er að gera ríkjandi ramma sýnilegan svo næsta skref geti spurt: hvað vantar?

---

## Skref 3 — leggja til fræðigreinar utan ríkjandi ramma

Fyrir hverja kandídata-fræðigrein, metðu:

- **Er hún virkilega utan ramma?** Ef heimildir vísa þegar í hana, þá er hún ekki gap (þá er hún undir-fulltrúa, ekki útilokuð — það er /baeta-heimildir-svæði).
- **Hefur hún konkret-framlag?** "Sociology in general" er ekki tillaga. "Bourdieu's habitus á modal-choice — bíll sem stéttar-merki" er tillaga.
- **Stenst hún ritstjórnar-afmörkun?** Ef ritstjóri hefur sagt "ekki landsbyggðin", þá legðu ekki til "regional development economics".
- **Er framlag konkret nóg til að leita að heimildum eða smíða tilraun?** Ef já, þá nytsamleg. Ef bara "almenn brainstorming", forgangur lágur.

**Mögulegar fræðigreinar (dæmi — ekki tæmandi listi; finndu sjálf):**
- Atferlishagfræði (behavioural economics) — modal choice, default effects, status quo bias
- Borgarsálfræði (environmental psychology) — perception af öruggi, lífsgæði í kringum hraðbrautir
- Lýðheilsa (public health) — loftgæði, líkamleg hreyfing, dauðsföll í umferð
- Netvísindi (network science) — flæði í samgöngukerfum, robustness undir bilanir
- Lýðfræði og samfélagsfræði — commuting-mynstur, demographic shifts, fjarvinna eftir 2020
- Hagsögufræði — sögulegar bylgjur í borgarsamgöngum, lessons frá Jane Jacobs vs. Robert Moses
- Stjórnsýslufræði / public policy — hvernig svona stór verkefni fara fram annars staðar
- Leikjafræði — congestion pricing sem game-theoretic vandi
- Land-economics og real-estate — landverð kringum stoppistöðvar, value capture taxation
- Faraldsfræði-eins-líkön — diffusion af nýrri ferðamáta-aðtöku
- Tilfinninga- og myndhverfa-greining (rhetorical/framing analysis) — hvernig "bíllinn" sem merki er rædd í íslensku samhengi

Forgangsraða:
- **HÁR:** Konkret-framlag sem gæti breytt sjónarmiði eða ráðleggingu; bætir augljóst gap; aðgengilegar heimildir til
- **MIÐ:** Áhugavert framlag en óljóst hve mikil áhrif; eða heimildir krefjandi
- **LÁGUR:** Spennandi en spákoma; eða mjög skarast við núverandi ramma

---

## Skref 4 — skrifa tillögur í `ai-greining/utfyrir-boxid.md`

Sniðmát:

```markdown
# Þverfaglegar nálganir — $1 (uppfært YYYY-MM-DD)

> Skipun: `/baeta-utfyrir-boxid $1`. Tillögur að fræðigreinum utan ríkjandi ramma málsins. Ritstjóri eða AI velur hvaða á að innleiða — annað hvort með `/baeta-heimildir` til að safna heimildum úr þeim fræðigreinum, eða með `/baeta-tilraunir` til að smíða Python-líkön úr þeim, eða með handvirkri uppfærslu á `ritstjorn.md` til að breyta ramma málsins.

## Ríkjandi ramma málsins (eins og hann birtist í núverandi safni)

[3–6 fræðigreinar með H### vísunum — sjá Skref 2]

## Tillögur utan ríkjandi ramma

### B1 — [Stutt fræðigrein-nafn, t.d. "Atferlishagfræði"]

**Hvað hún myndi bæta:** [Ein klár setning um framlag.]

**Konkret-konsept sem ætti við:**
- [Konsept 1] — [hvernig það passar á málið]
- [Konsept 2] — [hvernig það passar]

**Heimildir/höfundar sem mætti leita að:**
- [Höfundur/rit + ártal] — [hvers vegna þetta gæti hjálpað]
- ...

**Hvernig þetta breytti greiningu (ef rétt reynist):**
- [Hvaða fullyrðing í README yrði styrkt eða veikt]
- [Hvaða nýja undir-spurning kæmi inn]

**Tengsl við önnur skref:**
- Mun /baeta-heimildir leita: [já — leitar-tillögur]
- Mun /baeta-tilraunir prófa: [já — tilrauna-tillögur eða nei]

**Stenst ritstjórnar-afmörkun:** [Já — eða: nei, mun ekki passa við [...] í ritstjorn.md]

**Forgangur:** HÁR/MIÐ/LÁGUR — [stutt rökstuðningur]

### B2 — ...

...

## Status-tafla

| # | Fræðigrein | Forgangur | Staða |
|---|---|---|---|
| B1 | ... | HÁR | tillaga |
| B2 | ... | MIÐ | tillaga |

Ritstjóri uppfærir Staða-dálk: "tillaga" | "innleidd í ritstjorn.md" | "í gangi: /baeta-heimildir leit hafin" | "hafnað: <ástæða>"
```

**Reglur fyrir innihald:**

1. **Konkret konsept skal vera nefnt.** Ekki bara "sociology gæti bætt", heldur "Bourdieu habitus á modal choice".
2. **Konkret framlag skal vera nefnt.** Hvaða fullyrðing í README yrði breytt? Hvaða ný spurning bætast inn?
3. **Forðast ítrekun.** Ef fræðigrein er þegar undir-fulltrúa (en til staðar) í safninu, þá er hún /baeta-heimildir-svæði, ekki utfyrir-boxid.
4. **Berðu virðingu fyrir ritstjórnar-afmörkun.** Ekki leggja til sjónarmið sem `ritstjorn.md` útilokar — eða ef það er svo verðmætt að það þurfi að breyta afmörkun, segðu það skýrt.
5. **Hver tillaga skal hafa Tengsl-kafla** sem segir hvort hún kallar á /baeta-heimildir-leit, /baeta-tilraunir-líkön, eða ritstjórnar-uppfærslu.
6. **Ekki yfirskrifa eldri tillögur sem ritstjóri merkir ekki sem klárðar/hafnaðar** — endurkeyrsla heldur ófrágengnum og bætir við nýjum með næsta B-númeri.

---

## Skref 5 — lokaskýrsla

### 5.1 Nýjar tillögur

| B# | Fræðigrein | Konkret-framlag | Forgangur |
|---|---|---|---|

### 5.2 Eldri tillögur sem haldnar eru ófrágengnar

| B# | Fræðigrein | Forgangur | Eldri-keyrslu-dagur |
|---|---|---|---|

### 5.3 Fræðigreinar sem þú hugsaðir um en taldir ekki tillögu-verðar

Hver á einni línu: hvaða fræðigrein, og af hverju ekki (þegar undir-fulltrúa, útilokuð af ritstjorn, of spákoma, ekki konkret framlag).

### 5.4 Næsta skref

Endaðu með einu af:
- *"X nýjar HÁR-tillögur, Y MIÐ. Biddu mig að keyra `/baeta-utfyrir-boxid $1` aftur eftir að þú hefur uppfært ritstjorn.md eða merkt tillögur, eða `/baeta-heimildir $1` til að safna heimildum úr þessum fræðigreinum."*
- *"Engar nýjar þverfaglegar tillögur — ríkjandi rammi dekkir málið vel innan ritstjórnar-afmörkunar. Vilji þú víkka, þá þarf að uppfæra `ritstjorn.md` fyrst."*

---

## Reglur sem aldrei má brjóta

1. **Engin ný heimildaleit.** Þetta er proposal-skref. Ef tillaga kallar á leit, þá vísaðu á /baeta-heimildir.
2. **Engin breyting á `ritstjorn.md`.** Ef tillaga krefst þess að ritstjórnar-afmörkun verði víkkuð, segðu það — en ritstjóri tekur þá ákvörðun.
3. **Konkret framlag, ekki "almenn brainstorming".**
4. **Idempotent — eldri ófrágengar tillögur eru ekki yfirskrifaðar.**
5. **Ekki skrifa README eða heimildir.**
6. **Engin emoji.**
7. **Ef README er ekki til** — stöðva og biðja ritstjóra að keyra /greina fyrst.

---

## Bilanaham — algeng mistök

- **"Of almenn fræðigrein-tillaga"** — "atferlishagfræði myndi bæta" er ekki tillaga. Konkret-konsept verður að vera nefnt.
- **"Tillaga sem skarast við núverandi"** — ef fræðigrein er þegar undir-fulltrúa í safninu, þá er hún ekki utfyrir-boxid-tillaga. Athugaðu Skref 2 áður en þú leggur til.
- **"Tillaga sem fer á svig við ritstjorn"** — t.d. fyrir samgongur, leggja til "landsbyggðar-jafnræði" þegar `ritstjorn.md` segir "ekki landsbyggðin".
- **"Yfirskrifa eldri tillögur"** — endurkeyrsla skal halda ófrágengnum.
- **"Skrifa nýjar heimildir sjálfvirkt"** — engin heimildaleit. Vísaðu á /baeta-heimildir.

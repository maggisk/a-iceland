---
description: Lesa allar heimildir og skrifa samantekt, greiningar og rökstudda ráðleggingu í málefni — eftir að /rannsaka hefur safnað heimildum
argument-hint: <slug>
---

Notandi vill skrifa samantekt, greiningar og ráðleggingu fyrir mál `$1` út frá vistuðum heimildum.

> **Hugarfar:** Þú ert ekki að framleiða "hlutlausa samantekt" — þú ert að framleiða **rökstuddan rannsóknargrunn og tillögu að lausn**. Tilgangur repo-isins er að nýta þig til að mynda rökstudda skoðun, ekki bara endursýna heimildir. Þú átt að taka afstöðu í ráðleggingar-skjalinu — undir ströngum reglum um tilvitnanir og með heiðarlegum veikleika-lista. Ef heimild styður ekki fullyrðingu 1:1, þá er hún ekki nógu góð. Engar ágiskanir, engar uppfyllingar, engin almenn þekking.

> **Forsenda:** Heimildir hafa þegar verið safnaðar með `/rannsaka`. Ef `heimildir/` er tóm eða mjög léleg, stoppa og biddu ritstjóra að keyra `/rannsaka $1` fyrst.

---

## Skref 0 — fyrirskoðun (pre-flight)

1. **Staðfestu slug:** `malefni/$1/` verður að vera til. Ef ekki, stöðvaðu.
2. **Athugaðu nauðsynlegar skrár:** `malefni/$1/ritstjorn.md`, `snidmat/README.md`, `snidmat/ai-greining.md`, `leidbeiningar/fyrir-ai.md` verða allar að vera til. Ef einhver vantar, stöðvaðu.
3. **Athugaðu heimildir:** `malefni/$1/heimildir/` skal hafa a.m.k. 3 skrár. Ef ekki, stöðvaðu og biddu ritstjóra að keyra `/rannsaka $1` fyrst.
4. **Skráðu keyrslu:** Birtu efst: model-nafn, dagsetning (`2026-05-21`), slug `$1`, fjölda heimilda, og hvort um er að ræða fyrstu keyrslu eða endurskrifun.

Ef einhver athugun bregst — **STÖÐVAÐU**.

---

## Skref 1 — lestur (engin stytting)

Lestu í þessari nákvæmu röð, til enda. Heimildir hafa mikilvægasta innihaldið neðarlega (hráefni).

1. `leidbeiningar/fyrir-ai.md` — almennar reglur.
2. `malefni/$1/ritstjorn.md` — mannlegar leiðbeiningar. **Æðsta forgang.** Sérstaklega: verkefnalisti (hvaða skjöl skal búa til, hvaða spurningar svara), mat á heimildum (hagsmunatengingar, veikar heimildir), athugasemdir við AI-úttak (ef einhverjar).
3. `snidmat/README.md` og `snidmat/ai-greining.md` — uppbygging útkomu.
4. **Allar** skrár í `malefni/$1/heimildir/` — hver skrá: frontmatter, lýsing, tilvitnanir, fyrirliggjandi greining og **fullt hráefni neðst**. Lestu allt.
5. **Allar** núverandi skrár í `malefni/$1/ai-greining/` og `malefni/$1/README.md` (ef til) — svo þú vitir hvað er þegar þar og hvort þú ert að uppfæra eða skrifa fyrst.

**Eftir lestur, birtu stutta staðfestingu (3–6 línur):**
- Hve margar heimildir, hvaða sjónarhorn þær spanna.
- Hvaða verkefni ritstjorn biður um.
- Hvort um endurskrifun er að ræða (eitthvað þegar í README/ai-greining) eða ferskt skjal.
- Sjáanleg veikleikar í heimildasafninu (t.d. „aðeins ein heimild fyrir sjónarmið B").

---

## Skref 2 — áætlun

Áður en þú skrifar nokkuð, birtu **stutta áætlun** (5–10 línur):
- Hvaða skjöl þú ætlar að skrifa/uppfæra (skv. ritstjorn.md verkefnalista).
- Hvaða heimildir þú ætlar að nota í hverju skjali.
- Hvaða sjónarhorn fá pláss í hverju.
- Hvar þú sérð fyrir veikleika.

Þetta er ekki samtal — birtu áætlunina og haltu áfram. Ritstjóri stoppar þig ef hún er röng.

---

## Skref 3 — skrifa

Fylgdu nákvæmlega:
- **Reglum í `fyrir-ai.md`** — sérstaklega tilvitnunarreglum.
- **Verkefnalistanum í `ritstjorn.md`** — ekkert utan hans nema þú útskýrir af hverju í skýrslu.
- **Mati ritstjóra á heimildum í `ritstjorn.md`** — ef ritstjóri segir „H003 er veik", þá meðhöndlarðu hana sem veika, óháð því hvað þér finnst.
- **Sniðmáti `snidmat/README.md`** fyrir `malefni/$1/README.md`.
- **Sniðmáti `snidmat/ai-greining.md`** fyrir hvert skjal í `malefni/$1/ai-greining/`.

**Skrár sem þú framleiðir/uppfærir:**

- **`malefni/$1/README.md`** — kjarnaskjal málsins. Skipulagt skv. `snidmat/README.md` með eftirfarandi köflum:
  1. TL;DR (5–8 línur)
  2. Núverandi staða
  3. Saga
  4. Hver heldur hverju fram (lykilraddir, ekki A/B-skipting)
  5. Rök með og móti einstökum hugmyndum (skipulagt **eftir hugmyndum**, ekki hliðum)
  6. **Niðurstöður og tillögur gervigreindar** (sjá reglur að neðan — skylda)
  7. Lykilheimildir
  8. Hvað vantar í safnið
  9. Frekara reference-efni (tenglar í `ai-greining/`)

- **`malefni/$1/ai-greining/*.md`** — valkvæð dýpkun á tilteknu efni sem væri of langt í aðal-README. Dæmi:
  - `<malefnafraedi>.md` (t.d. `samgonguhagfraedi.md`) — fræðilegur rammi
  - `erlendur-samanburdur.md` — ítarlegur alþjóðlegur samanburður
  - `laerdomar-erlendis.md` — hvað virkað/mistekist
  - Annað sem þarf dýpkunar en yrði of langt í README

**Athugið:** Ráðleggingin er nú **kafli í README.md, ekki sérstök skrá**. Þetta breytti frá fyrri uppsetningu (`besta-<slug>.md`) — lesandi finnur allt á einum stað með TL;DR efst og afstöðu í lokin.

### Reglur fyrir "Niðurstöður og tillögur gervigreindar"-kaflann

Þetta er kjarnaframleiðsla málsins. **Þú átt að taka afstöðu** — undir agandi reglum:

1. **Birtu forsendur skýrt** — markmið ráðleggingar (t.d. lágmarka kostnað, hámarka modal-shift, lágmarka CO2). Forsendur ráða niðurstöðu. Ef ritstjorn.md tilgreinir markmið, notaðu þau; annars veldu sjálf og útskýrðu.
2. **Skiptu í svið** — mál hefur náttúrlega svið (samgöngur: almenningssamgöngur, stofnvegir, hjól, fjármögnun, tímalína, stjórnsýsla). Sundurliðun gerir gagnrýni mögulega.
3. **Færðu rök fyrir hverju vali** — hvað sönnun heimilda bendir til, hvaða valkostir voru íhugaðir, hvers vegna þessi var valinn.
4. **Hver fullyrðing heimildastudd** — sömu reglur og fyrir samantekt. Engin almenn þekking.
5. **Engin fölsk samhverfa** — ef heimildir benda sterkt á eitt sjónarmið, segðu það beint.
6. **Veikleika-listi í lokin** — skylda. Gagnrýndu eigin tillögu: hvaða heimildir vantaði, hvaða forsendur er ég ekki viss um, hvar treysti ég á eina rödd.
7. **Spurningar sem heimildir svara EKKI** — listi yfir hvað ritstjóri ætti að íhuga áður en hann samþykkir ráðlegginguna.

### Reglur fyrir "Rök með og móti einstökum hugmyndum"-kaflann

Þetta er nýtt og mikilvægt. Skipulag eftir **hugmyndum**, ekki sjónarmiðum:

- Auðkenndu 3–6 helstu hugmyndir/ákvarðanir sem eru í deilu (t.d. "Borgarlína gold vs. lite", "Sundabraut brú vs. göng", "Veggjöld á alla vegi vs. bara nýja").
- Fyrir hverja hugmynd: rök með, rök móti, og **hvar gögnin liggja** (ef ein hlið er sterkari studd, segðu það). Engin fölsk samhverfa.
- Aðilar/stjórnmálamenn koma fram náttúrulega í rökunum (Hildur Björnsdóttir segir X, Eyþór segir Y) — það lætur lesandann sjá að sami aðili getur stutt eina hugmynd og hafnað annarri.

Ráðleggingin er ekki dómur — hún er inntak fyrir ritstjóra. En ekki víkjast undan: skýr, rökstudd tillaga er gagnlegri en mjúk samantekt.

### Tilvitnunar- og gæðakröfur (harðar)

| Krafa | Lýsing |
|---|---|
| **Haus** | Model-nafn og dagsetning (`2026-05-21`) efst, í þessu formi: `> Skrifað af <model>, <dagsetning>` |
| **Tilvitnun á hverja efnislega fullyrðingu** | Smellanlegt snið `[H###](heimildir/H###-...md)` — ekki bara númer. |
| **Engin almenn þekking** | Ef það er ekki í heimild, þá er það ekki í skjalinu. Punktur. |
| **Engar utanaðkomandi tilvitnanir** | Ekki vísa í neitt utan `heimildir/`. Ekki nota minni þitt á heiminn. |
| **Margar heimildir þegar mögulegt** | Lykilfullyrðingar styðjast helst við 2+ heimildir. Ef aðeins ein, gerðu það ljóst. |
| **Aðgreining staðreyndar og túlkunar** | Túlkun má vera til staðar en skal merkt skýrt sem slík („Þetta bendir til …", „Möguleg túlkun er …"). |
| **Engar uppfyllingar** | Ekki bæta við setningum til að jafna kafla. Stutt og rétt er betra en langt og útblásið. |
| **Sjálfsmótsögn ekki leyfð** | Ef tvær heimildir stangast á, segðu það beint — ekki samhæfa á bak við tjöldin. |
| **Trúnaðarmat** | Þar sem við á, notaðu skýr orð: „staðfest af 2 heimildum", „aðeins ein heimild". |

### Sjálfsritskoðun (innri lykkja áður en þú skilar)

Áður en þú lokar skjali, farðu yfir með þessari gátlista — **birtu ekki gátlistann, en framkvæmdu hann**:

- [ ] Hver efnisleg fullyrðing hefur a.m.k. eina smellanlega tilvitnun.
- [ ] Engin setning byggir á almennri þekkingu.
- [ ] Andstæð sjónarmið koma fram þar sem þau eru til í heimildum.
- [ ] Veikar heimildir eru merktar veikar í texta eða þeim er sleppt.
- [ ] Engar tölur, dagsetningar eða nöfn án heimildar.
- [ ] Engin „samkvæmt rannsóknum" án vísunar í ákveðna rannsókn.
- [ ] Skjalið svarar þeim spurningum sem `ritstjorn.md` biður um — ekki öðrum.

### Endurskrifun

Ef README.md eða ai-greining skrár eru þegar til:
- **README.md má og á að endurskrifa** út frá núverandi heimildasafni. Það er „lifandi" samantekt.
- **ai-greining/ skrár** — ef til er skrá um sjónarmið sem ritstjorn biður um, þá uppfærðu hana frekar en að búa til nýja. Ef ritstjorn biður um nýtt sjónarhorn, búðu til nýja skrá.
- Ekki eyða ai-greining skrám nema ritstjorn segi beinlínis.

---

## Skref 4 — skýrsla

### 4.1 Kláruð verkefni
Listi með `[x]` — beint úr `ritstjorn.md` verkefnalistanum.

### 4.2 Verkefni sem standa eftir
Hvert eitt með skýringu á af hverju (vantar heimild, óljóst frá ritstjórn, tæknilegt vandamál).

### 4.3 Heimildir notaðar vs ónotaðar
Tafla:

| H### | Notuð? | Í hvaða skjali? | Ef ekki notuð, hvers vegna? |
|---|---|---|---|

Engin heimild má vera „bara ekki nefnd". Allar fá lágmarks útskýringu.

### 4.4 Sjónarmið sem eru veik eða vanta
Heiðarlegur listi:
- „Engin heimild frá [hagsmunaaðila X]"
- „Aðeins ein heimild fyrir [lykilfullyrðing Y]"
- „Andstæð sjónarmið koma fyrir í [H###] en eru ekki rakin nógu vel"

### 4.5 Spurningar sem heimildir svara ekki
Spurningar sem **eru relevant fyrir þetta mál** og sem ritstjóri ætti að ákveða hvort eigi að leita svara við. Ef veikleikar 4.4 og 4.5 benda á þörf fyrir fleiri heimildir, þá leggjið til endurkeyrslu á `/rannsaka $1`.

### 4.6 Tillögur að nýjum leiðbeiningum
Hvað hefði gert keyrsluna betri? T.d.:
- „Bæta við `ritstjorn.md`: tilgreina hvort H002 (blogg) má nota sem aðalheimild eða aðeins sem stuðning."

### 4.7 Næstu skref
Endaðu skýrsluna með einni eða báðum tilmælum:
- *„Biddu mig að keyra `/sannprofa $1` til að staðfesta að allar tilvitnanir séu gildar og smellanlegar."*
- *„Veikleikar benda á þörf fyrir fleiri heimildir — biddu mig að keyra `/rannsaka $1` aftur til að dýpka [tilgreint efni]."*

---

## Reglur sem aldrei má brjóta

1. **Ekki breyta `ritstjorn.md`.** Tillögur fara í skýrslu, ritstjóri ákveður.
2. **Ekki nota almenna þekkingu** — aðeins það sem er í `heimildir/`.
3. **Ekki útbúa tilvitnanir** — ef tilvitnun er ekki orðrétt í heimild, ekki nota gæsalappir.
4. **Ekki stytta lestur** — lestu allar heimildir til enda, þar með talið hráefni.
5. **Ekki bæta við heimildum.** Ef vantar heimild, leggðu það til í skýrslu og biddu ritstjóra að keyra `/rannsaka` eða `/heimild`.
6. **Ef þú ert óviss, segðu það.** „Ég veit ekki" er betra svar en uppfylling.
7. **Engin emoji.**

---

## Bilanaham — algeng mistök

- **„Heimildar-lag"** — að breyta orðalagi þangað til það passar við fleiri heimildir en upphaflega meintu. Ekki gera þetta.
- **„Sjónarhornsjöfnun"** — að setja fram tvö sjónarmið sem jafngild þegar heimildir styðja það ekki. Ekki tilbúin tvíhliða.
- **„Mjúkun"** — að milda fullyrðingu úr heimild til að virðast hlutlæg/ur. Hafðu hana eins og hún er, með tilvitnun.
- **„Auka-greining"** — að bæta við greiningum sem ritstjorn.md bað ekki um. Ekki gera það nema þú nefnir það í skýrslu og merkir sem viðbót.
- **„Falleg-en-tóm samantekt"** — flæðandi inngangur án innihalds. Skerptu eða slepptu.
- **„Heimildaleit í greina-fasa"** — ef þú sérð vantar heimild, **ekki leitaðu sjálf(ur)** — leggðu til endurkeyrslu á `/rannsaka`.

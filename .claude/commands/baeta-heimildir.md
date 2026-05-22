---
description: Botn-upp heimildaöflun — les vistaðar heimildir, finnur vísanir/raddir/dæmi sem vantar eigin heimild, og sækir þær. Idempotent (má keyra aftur).
argument-hint: <slug>
---

Notandi vill bæta safn heimilda fyrir mál `$1` með snjóbolta-aðferð.

> **Hugarfar:** Þetta er **inductive** mótvægi við `/rannsaka` (sem er deductive). Þú ert ekki að velja flokka og leita per flokk — þú lest heimildirnar sem þegar eru í safninu, dregur út **vísanir** sem þær gera til (raddir, frumheimildir, samanburðar-borgir, fræðimenn, atburðir), og leitar að því sem nefnt er en á sér ekki eigin heimild. Heimildirnar mynda kortið — ekki sjálfgefin flokka-listi.

> **Idempotent:** Eins og `/rannsaka`. Aldrei yfirskrifa, aldrei eyða. Hver keyrsla bætir aðeins við.

> **Eingöngu heimildir.** Engar breytingar á `README.md`, `ai-greining/`, eða `ritstjorn.md`. Þetta er heimildalag — synthese-fasinn er `/greina`.

---

## Skref 0 — fyrirskoðun

1. **Staðfestu slug:** `malefni/$1/` skal vera til.
2. **Athugaðu nauðsynlegar skrár:** `malefni/$1/ritstjorn.md`, `snidmat/heimild.md`, og `leidbeiningar/fyrir-ai.md` verða allar að vera til.
3. **Athugaðu lágmarks-massa:** safnið `heimildir/` verður að hafa **a.m.k. 3 heimildir**. Annars er ekkert efni að rúlla snjóboltanum á — leiðbeindu ritstjóra á `/rannsaka` í staðinn og stöðvaðu.
4. **Skráðu keyrslu:** birtu efst í svari þínu: model-nafn, dagsetning, slug `$1`, fjöldi núverandi heimilda í `heimildir/`, og næstu H### númer sem þú munt nota.

Ef einhver athugun bregst — **STÖÐVAÐU**.

---

## Skref 1 — lestur (engin stytting)

Í þessari röð, til enda:

1. `leidbeiningar/fyrir-ai.md` — almennar reglur.
2. `malefni/$1/ritstjorn.md` — mannlegar leiðbeiningar. **Æðsta forgang.** Sérstaklega "Athugasemdir við AI-úttak" og "Mat á heimildum".
3. `snidmat/heimild.md` — sniðmát fyrir nýjar heimildaskrár.
4. **Allar** núverandi heimildir í `malefni/$1/heimildir/H###-*.md`, hverja til enda. Snjóboltinn rúllar á því sem þær segja — ef þú skannar bara, missir þú vísanir.

Eftir lestur, birtu stutta yfirlit (3–6 línur):
- Fjöldi heimilda og almenn sjónarhornsdreifing.
- Hvað ritstjóri hefur merkt í `Athugasemdir við AI-úttak` (ef eitthvað).
- Hvaða heimildir innihalda mest af vísunum í aðra aðila (oftast skoðanagreinar, þingmálsumræður, samantektir).

---

## Skref 2 — útdráttur (kjarni skipunarinnar)

Lesa heimildirnar og draga út **vísanir til ytri aðila** í fimm flokkum. Fyrir hverja: (i) hvað var nefnt, (ii) hvaða heimild(ir) nefna það, (iii) hvort vísunin sé í aðalefni heimildarinnar eða aðeins óbein.

### 2.1 Nafngreindar raddir

Fólk eða stofnanir sem birtast í texta — gagnrýnendur, sérfræðingar, ráðamenn, fyrrum embættismenn, höfundar skoðanagreina. Sérstök athygli:
- Nöfn í **fleiri en einni heimild** — sterk vísbending um lykil-rödd.
- Nafngreindir aðilar sem **gagnrýna** eitthvað en hafa enga eigin heimild — algeng vöntun í safni.
- Stofnanir sem **gefa út** efni sem heimildirnar vísa í (í gegnum nafn útgefanda eða "skv. skýrslu X").

### 2.2 Frumheimildir nefndar

Lög, samningar, skýrslur, rannsóknir, ákvarðanir sem heimildirnar vísa í — án þess að sjálft efnið sé vistað. Dæmi: heimild segir "Cowi 2024 greining metur þjóðhagslegan ábata 1.140 milljarða" — er Cowi-skýrslan sjálf vistuð sem eigin heimild?

### 2.3 Samanburðar-borgir / lönd

Erlend dæmi sem heimildir nefna — borg, kerfi, kostnaður — án þess að borgar-tilteknar heimildir séu vistaðar. Ef ein heimild í safninu nefnir Tampere lauslega en engin Tampere-heimild er til, þá er það gap.

### 2.4 Fræðiheimildir / höfundar

Akademísk rit, höfundar, fræðiheimildir nefnd í texta (t.d. "Hess, Taylor & Yoh (2005)"). Ef höfundur er nefndur 2+ sinnum eða styður mikilvæga fullyrðingu, þá þarftu undirliggjandi rit.

### 2.5 Tímabundnir atburðir

Dagsetningar, samningar, ráðstefnur, kosningar, ákvarðanir sem heimildir vísa í — án þess að sjálft efni atburðarins sé vistað. Dæmi: heimild nefnir "2008-samþykkt borgarstjórnar um göng" — er sjálf samþykktin vistuð sem heimild?

---

## Skref 3 — gap-greining og forgangsröðun

Búðu til **gap-töflu** þar sem hver lína er ein vísun úr Skref 2 sem **ekki** hefur eigin heimild í safninu. Sleppa þeim sem þegar eiga eigin heimild.

| Flokkur | Það sem vantar | Vísað til af (H###) | Forgangur |
|---|---|---|---|

**Forgangsmat:**

- **Hár:** Frumheimild nefnd af ≥2 heimildum, eða nafngreind rödd sem styður lykilfullyrðingu.
- **Mið:** Samanburðar-borg nefnd af 1 heimild, eða fræðiheimild með tilteknu nafni og ártali.
- **Lágur:** Aðilar/atburðir nefndir aðeins í framhjáhlaupi.

### 3.1 Tvíverknaðar-staðfesting (skylda áður en gap-tafla er lokuð)

Áður en þú lokar gap-töfluna og forgangsmetur — staðfestu með `grep` að hver gap-lína sé **raunverulega ekki dekkar** í safninu. Þetta er sérstaklega mikilvægt fyrir:

- **Nafnaðar raddir:** ef rödd hefur eigin heimild (skoðanagrein, viðtal), þá er hún ekki gap — jafnvel þótt aðrar heimildir endurspegli hana líka.
- **Frumheimildir:** ef heimild með sömu URL er þegar í safninu (jafnvel undir öðru slug), þá er hún ekki gap.

**Verklag:**

```bash
# Fyrir hverja nafngreinda rödd í gap-töflu:
grep -i "Nafn röddu" malefni/$1/heimildir/*.md | head

# Fyrir hverja URL/heimildanafn í gap-töflu:
grep -l "lykilorð úr titli" malefni/$1/heimildir/*.md
```

Ef grep skilar matches sem þú vissir ekki um, fjarlægðu þá línu úr gap-töflunni og skráðu í lokaskýrslu "uppgötvað sem þegar dekkar: H### dekkir [vísun] sem agent merkti sem gap". Þetta er gæða-mælikvarði — minni false-positives í gap-töflu = minni sóun á leit.

---

## Skref 4 — tilteknar leitir

Fyrir hverja vísun með forgang **Hár** eða **Mið**, framkvæmdu **tilteknar** leitir (ekki almennar):

- **Nafngreind rödd:** nafn + lykilorð málsins ("Ragnar Árnason borgarlína")
- **Frumheimild:** nákvæmt heiti + ártal + tegund ("Cowi samgöngusáttmáli 2024 greining")
- **Samanburðar-borg:** borg + kerfi + ártal ("Tampere light rail cost 2021")
- **Fræðiheimild:** höfundur + lykilorð ("Hess Taylor Yoh 2005 BRT")
- **Atburður:** dagsetning + lykilorð ("2008 borgarstjórn Sundabraut göng samþykkt")

Notaðu tungumál sem passar við vísunina — íslensku fyrir innlent, ensku fyrir erlent. Notaðu site-restrictions þegar viðeigandi (`site:althingi.is`, `site:scholar.google.com`, `site:ssrn.com`).

**Lágmark:** 1 leit per **Hár** gap, 1 leit per **Mið** gap. **Lágur** gap eru valkvæð.

---

## Skref 5 — sækja og vista

### 5.1 Sókn — fallback-tré

Reyndu í þessari röð:

1. **WebFetch** — fyrsta tilraun. Hraðvirkust og léttust.
2. **Chrome DevTools MCP** (`mcp__chrome-devtools__new_page` + `take_snapshot`) — ef WebFetch skilar 403, paywall-yfirlitsefni án innihalds, eða svar sem inniheldur ekki greinina sjálfa. Headless Chrome (sjá uppsetningu í [/rannsaka skref 3.1]) kemst oftast í gegn á Mbl, Heimildin, RÚV.
3. **Alternativ URL** — ef WebFetch og Chrome bregðast bæði (t.d. `ECONNREFUSED`, DNS-bilun), leitaðu eftir mirror/archive/cached útgáfu (`site:web.archive.org`, eða aðra slóð sem hýsir sama efni).
4. Ef öll þrjú bregðast — skráðu í rejection-töflu með nákvæmri ástæðu.

### 5.2 Tegundir mistaka og rétt viðbrögð

| Tegund | Dæmi | Rétt viðbragð |
|---|---|---|
| **403 Forbidden** | Mbl, Heimildin án Chrome | Chrome DevTools MCP |
| **Paywall preview** | Mbl með Chrome — fær news-summary en ekki fulla grein | Athugaðu hvort summary er nóg fyrir fullyrðingar; ef ekki, beiða mannlegrar aðstoðar (sjá 5.4) |
| **ECONNREFUSED / DNS** | mannvit.is, sumir hostar | Reyna Chrome (önnur nettengjandi). Ef bregst líka — alt URL eða mannleg aðstoð |
| **Binary PDF — óextraktanlegur** | WebFetch nær PDF (response inniheldur "Binary content..."), en small-model getur ekki diraktað texta | Sjá 5.3 |
| **Síða breytt / 404** | URL fyrnt | Vefarkíf (`https://web.archive.org/web/*/<url>`) eða ný leit |

### 5.3 Binary PDF — sérstök meðferð

WebFetch nær oft PDF en getur ekki extraktað texta úr þeim (sumir PDF-skjöl eru aðeins binary stream). Niðurstaðan inniheldur þá tekst um "Binary content (application/pdf, X MB)..." en engin lesanleg fullyrðingar.

Reyndu í þessari röð:

1. **Chrome navigate** til PDF-slóð + `take_snapshot`. Chrome render-ar PDF í accessibility-tré sem oft er extraktanlegt.
2. **Local pdftotext** — ef Chrome bregst líka: skráðu slóðina af PDF (WebFetch sparar oft í `/Users/.../tool-results/webfetch-*.pdf`) og notaðu Bash:
   ```bash
   # Á macOS með poppler-utils uppsett:
   pdftotext /path/til/local.pdf - | head -200
   ```
   Athugaðu fyrst hvort `pdftotext` sé uppsett (`which pdftotext`). Ef ekki, leiðbeindu á `brew install poppler` til ritstjóra.
3. Ef hvort tveggja bregst, skráðu sem "binary PDF — extraction failed" og fer í 5.4.

### 5.4 Aðstoðar-beiðnir til ritstjóra

Ef HÁR-forgangs gap mistekst eftir öll skref 5.1–5.3, þá biddu ritstjóra um aðstoð í lokaskýrslu (Skref 6.6 — sjá að neðan). Aðeins fyrir **HÁR-gap** — Mið og Lágur fara í 6.3 (vísanir sem þú gast ekki fundið heimild fyrir) án sérstakrar beiðni.

Aðstoð sem ritstjóri getur veitt:
- Niðurhal á PDF + áframsenda local-slóð.
- Áskrift að paywall (Mbl, Heimildin) til að copy/paste innihald.
- Stofnana-aðgangur (HÍ JSTOR, RÚV-archive).
- Staðfestingu á að heimild sé til (ef ekki finnst, kannski er hún ekki opinber).

### 5.5 Vista heimildina

- Vista sem `H###-stutt-slug.md` skv. `snidmat/heimild.md`. Númeraðu hækkandi frá hæsta H### sem þegar er til. Slug skal vera 2–4 orð, kebab-case, ASCII.
- Athugaðu URL-tvíverknað með `grep -l "^url: <URL>" malefni/$1/heimildir/*.md` áður en þú vistar (síðasta safety net — Skref 3.1 á að hafa náð þessu fyrr).
- **Aldrei yfirskrifa, aldrei eyða.**

**Sérstök regla um Tengingar-kafla í Greining-hluta nýrrar heimildaskráar:** skal innihalda **derivation** — t.d. "Þessi heimild er bætt við af því að [H012](H012-...md) vitnar í 2012-samkomulagið án undirliggjandi heimildar."

---

## Skref 6 — lokaskýrsla

### 6.1 Nýjar heimildir vistar

| H### | Titill | Útgefandi | Sjónarhorn | Derivation (úr hvaða H###) |
|---|---|---|---|---|

**Hver lína skal nefna úr hvaða heimild snjóboltinn rúllaði.**

### 6.2 Hafnaðar kandídötur

| Slóð | Stutt lýsing | Ástæða |
|---|---|---|

### 6.3 Vísanir sem þú gast ekki fundið heimild fyrir

Hver á einni línu: hvað þú leitaðir að, úr hvaða heimild vísunin kom, og hvers vegna leitin skilaði engu (paywall, ekki á netinu, of gamalt, höfundur of óljós, o.s.frv.).

### 6.4 Rödda-skor

Tafla yfir nafngreindar raddir úr Skref 2.1:

| Rödd | Hefur eigin heimild núna? | Vísað til af |
|---|---|---|

Þetta sýnir hvaða raddir eru aðeins endurspeglaðar í gegnum túlkun annarra. Næstu `/baeta-heimildir`-keyrslur eiga að beinast að þeim.

### 6.5 Næsta skref

Endaðu með einu af:

- *"Snjóboltinn rúllaði og bætti við X heimildum. Y gap eftir — biddu mig að keyra `/baeta-heimildir $1` aftur, eða `/rannsaka $1` til að leita á nýjum sviðum."*
- *"Snjóboltinn stoppaði — engar nýjar Hár/Mið vísanir sem ekki eiga eigin heimild. Safnið er tæmt í snjóbolta-skilningi. Biddu mig að keyra `/greina $1`."*

### 6.6 Aðstoðar-beiðnir til ritstjóra (ef einhverjar)

Tafla yfir HÁR-gap sem mistekst eftir öll fallback-skref (5.1–5.3). Aðeins fyrir HÁR-gap.

| Vísun | Vísað til af | Það sem brást | Hvað ritstjóri gæti gert |
|---|---|---|---|
| (t.d. "Cowi 2024 PDF") | (H001, H002) | ("Binary PDF, Chrome a11y-tré tómt, pdftotext ekki uppsett") | ("Setja upp poppler eða niðurhala handvirkt") |

Ef engar beiðnir, sleppa undirkafla.

---

## Reglur sem aldrei má brjóta

1. **Vísanir verða að vera í texta einhverrar heimildar.** Aldrei uppspinnaðar. Sýndu hvaða heimild í gap-töflu.
2. **Engar nýjar flokka-leitir.** Ef þér dettur í hug sjónarhorn sem engin heimild nefnir, þá tilheyrir það `/rannsaka`, ekki hér.
3. **Idempotent.** Aldrei yfirskrifa, aldrei eyða.
4. **Skref 0 lágmark.** Ef <3 heimildir, stöðvaðu og bentu á `/rannsaka`.
5. **Derivation chain er skylda.** Hver ný heimild skal tengjast aftur í Tengingar-kafla við a.m.k. eina heimild sem nefndi vísunina.
6. **Ekki skrifa README, ai-greining, eða ritstjorn.md.**
7. **Engin emoji.**
8. **Stöðunarregla úr `/rannsaka` gildir áfram:** ef hagsmunatengd heimild lendir á því að vera lykilheimild, stöðvaðu og spurðu ritstjóra.

---

## Bilanaham — algeng mistök

- **"Innfella nýja flokka"** — að bæta við "ég held við þurfum líka að leita að X" þar sem X er ekki nefnt í neinni heimild. Það er `/rannsaka`-svæðið. Hættu.
- **"Sleppa derivation chain"** — vista nýja heimild án að nefna úr hvaða heimild snjóboltinn rúllaði.
- **"Of almennar leitir"** — leita "borgarlína gagnrýni" í stað "Ragnar Árnason borgarlína 2018". Snjóbolti krefst tiltekinna leita.
- **"Of fáar leitir"** — gefast upp eftir 2 gap. Hár-gap eiga öll að fá tilraun.
- **"Skrifa-fasinn læðist inn"** — engar README-breytingar, engar greiningar. Heimildir aðeins.
- **"Vísa í heimildir sem ekki nefna vísunina"** — derivation chain skal vera nákvæm. Ekki segja "H012 vísar í Ragnar Árnason" nema H012 vísi raunverulega í Ragnar Árnason.
- **"Sleppa Skref 3.1 grep-staðfestingu"** — að vinna með gap-tafluna eins og hún sé endanleg þegar agent/AI bjó hana til. Hver lína skal staðfest með grep gegn safninu áður en leitar-tími er eytt í hana.
- **"Gefast upp á rödda-leitum"** — að sleppa nafngreindri rödd af því að almennar leitir með nafni einu skila aðeins endurspegli-greinum. Reyndu nafn + sérstakt orð sem rödd notar ("Hildur Björnsdóttir Miklubrautargöng einkaframkvæmd"), eða nafn + viðtals-vefur ("Vilhjálmur Árnason ruv viðtal samgöngusáttmáli"), eða blaðamannafundur-archive.
- **"Telja binary PDF sem 'óaðgengilegt'"** — WebFetch nær oft PDF-skrá en getur ekki extraktað innihaldið. Það þýðir EKKI að heimildin sé glötuð — Chrome a11y-tré eða `pdftotext` ná oftast efninu. Sjá 5.3.

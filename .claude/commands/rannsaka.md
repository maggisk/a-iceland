---
description: Safna heimildum fyrir málefni — leitar, sækir og vistar heimildaskrár. Idempotent (má keyra aftur til að finna fleiri).
argument-hint: <slug>
---

Notandi vill safna heimildum fyrir mál `$1`.

> **Hugarfar:** Þú ert að byggja upp **traustverðan grunn** af heimildum. Þetta er ekki skrifa-fasi — það er `/greina`. Þú ert **eingöngu** að finna, sækja og vista heimildaskrár. Engin samantekt, engin greining utan við hlutlæga lýsingu á efni hverrar heimildar.

> **Idempotent:** Þessi skipun má (og á) að keyra aftur og aftur. Hver keyrsla **bætir við** nýjum heimildum — yfirskrifar aldrei né eyðir. Ef ritstjóri vill meira efni eða sjónarhorn, þá bara endurkeyrir.

---

## Skref 0 — fyrirskoðun (pre-flight)

1. **Staðfestu slug:** Athugaðu að `malefni/$1/` sé til. Ef ekki, stöðvaðu og spurðu ritstjóra hvort búa eigi til nýtt mál eða leiðrétta slug.
2. **Athugaðu nauðsynlegar skrár:** `malefni/$1/ritstjorn.md` og `snidmat/heimild.md` og `leidbeiningar/fyrir-ai.md` verða allar að vera til. Ef einhver vantar, stöðvaðu.
3. **Skráðu keyrslu:** Birtu efst í svari þínu: model-nafn, dagsetning (`2026-05-21`), slug `$1`, fjölda **núverandi** heimilda í `heimildir/`, og næstu H### númer sem þú munt nota.

Ef einhver athugun bregst — **STÖÐVAÐU**.

---

## Skref 1 — lestur (engin stytting)

Lestu í þessari röð, til enda:

1. `leidbeiningar/fyrir-ai.md` — almennar reglur.
2. `malefni/$1/ritstjorn.md` — mannlegar leiðbeiningar. **Æðsta forgang.** Sérstaklega: áhersla, afmörkun, hvaða heimildir/sjónarmið ritstjóri biður um, "Athugasemdir við AI-úttak" (ef einhverjar — gætu vísað á gap í núverandi safni).
3. `snidmat/heimild.md` — sniðmát fyrir heimildaskrár.
4. **Allar** núverandi skrár í `malefni/$1/heimildir/`. Þú þarft að vita hvað er þegar þar — bæði til að forðast tvíverknað og til að greina hvaða sjónarmið/efni eru þegar dekkar.

**Eftir lestur, birtu stutta greiningu (3–6 línur):**
- Hve margar heimildir eru þegar til, og frá hvaða sjónarhornum (A / B / hlutlaust / hagsmunatengd).
- Hvaða svæði ritstjórn biður um sem **ekki** eru ennþá dekkar (gap).
- Hvaða aðila/sjónarhorn vantar (t.d. „engin frumheimild frá X", „engin gagnrýni á aðferðafræði", „engin alþjóðleg dæmisaga").

Þetta er kortlagning leitar — ekki kurteisi.

---

## Skref 2 — heimildaleit

### 2.1 Flokka-yfirgreining (NAUÐSYNLEG — fyrsta skref leitar)

**Áður en þú gerir eina einustu leit**, birtu lista af **6–10 efnisflokkum** sem eiga við málið. Flokkarnir eru sjónarhornin og víddirnar sem þurfa að vera dekkar — ekki listi af leitarorðum. Dæmi um flokka eftir málaflokki:

- **Samgöngumál:** almenningssamgöngur · hjólainnviðir · gangandi · stofnvegir · veggjöld/fjármögnun · alþjóðlegur samanburður · samgönguhagfræði · söguleg vídd · gagnrýni · hagsmunatengingar
- **Húsnæðismál:** opinber stefna · lóðaframboð · byggingariðnaður · leigumarkaður · þéttingarsvæði · sveitarfélaganir · norrænt módel · söguleg vídd · gagnrýni
- **Menntamál:** opinber stefna · kennarakjör · PISA/alþjóðleg viðmið · skólagerð · einkareknir vs. opinberir · söguleg vídd · gagnrýni
- **Heilbrigðismál:** opinber stefna · einkarekstur vs. opinber · biðlistar · kostnaður · norræn samanburður · söguleg vídd · gagnrýni

Aðlagaðu flokkana að málinu — láttu ritstjorn.md leiða þig. Birtu lista með stutta lýsingu á hverjum flokki (1 lína per flokk).

**Lykilatriði:** Hver leit á að beinast að EINUM flokki frekar en að vera almenn. Ef þú gerir 16 leitir sem allar eru í 2 flokkum, missirðu af 4-8 öðrum flokkum. Þetta er algeng leitarvilla.

### 2.2 Stilltu leit eftir gap-greiningu

Eftir flokka-yfirgreiningu, kortlagðu núverandi heimildir í flokkana. Forgangaðu leit að flokkum sem ekki eru þegar dekkar. Ef safnið er tómt — leitaðu breitt í öllum flokkum. Ef safnið hefur þegar 10+ heimildir — leitaðu þrengra eftir gap.

### 2.3 Leit — lágmarkskröfur

**Lágmark per keyrslu (þú mátt fara langt yfir):**

- **8 íslenskar leitir** með ólíkum orðasamböndum
- **8 enskar leitir** — sérstaklega fyrir fræðiheimildir, alþjóðlegar dæmisögur, og almennt fræðilegt samhengi
- **Að minnsta kosti 1 leit per flokki** úr 2.1 (ef flokkarnir eru 8, þá lágmark 8 leitir sem dekka allan flokkahópinn — meira ef flokkur er sérlega mikilvægur)
- **3 leitir sem beinast að gagnrýni / andstæðum sjónarmiðum** (ekki bara opinberum yfirlýsingum)

**Ekki hætta of fljótt.** Ef málið er staðbundið íslenskt, þá er enski leitarvinkillinn samt mikilvægur:
- Erlend sambærileg mál (t.d. samgöngumál → norrænar borgir; húsnæðismál → norrænt módel; menntamál → PISA samanburður)
- Fræðilegur grunnur og alþjóðleg umræða
- Stofnanir eins og OECD, World Bank, ESB, Norden samstarf

Ef málið er alþjóðlegt, þá er íslenski leitarvinkillinn samt mikilvægur — hvernig er málið rætt á Íslandi, hver eru íslensk dæmi.

### 2.4 Leitaraðferð

- Notaðu `WebSearch` með ólíkum orðasamböndum á báðum tungumálum.
- Tengdu hverja leit við flokk úr 2.1 — skráðu hver leit beinist að hvaða flokki.
- Reyndu fleiri orðasambönd: opinber, fræðileg, fréttamiðla, gagnrýnin/ósammála sjónarhorn.
- Ef málið varðar ákveðna stofnun/manneskju — leitaðu sérstaklega að **gagnrýni** og **andstæðum sjónarmiðum**, ekki bara opinberum yfirlýsingum.
- Notaðu site-restrictions þegar viðeigandi (t.d. `site:ssrn.com`, `site:nber.org`, `site:scholar.google.com`).

### 2.5 Innra val (ekki birta sem samþykkislista — bara skrá í lokaskýrslu)

Fyrir hverja kandídatu, metðu innra með þér:
- **Titill, slóð, tegund, útgefandi, dagsetning**
- **Sjónarhornsgisk** (hvaða hlið / hagsmuni / nálgun)
- **Rökstuðningur** (af hverju þessi á við)
- **Mat á áreiðanleika** (hár / miðlungs / lágur)
- **Hagsmunatenging** (sjá undantekningarreglu að neðan)
- **Takmarkanir** (paywall, vantar dagsetningu, óljósir höfundar)
- **Tvíverknað** — er þessi slóð þegar í `heimildir/`? Athugaðu með `grep -l "^url: <URL>" malefni/$1/heimildir/*.md` áður en þú vistar.

### 2.6 Hagsmunatengdar heimildir — eina stöðunarreglan

Ef heimild sem þú metur sem **hagsmunatengda** (verktaki, hagsmunasamtök, hluthafi með fjárhagslegan ávinning) lendir á því að vera **lykilheimild** — þ.e. ein af fáum sem styður mikilvæga fullyrðingu, eða ein af 3–5 mikilvægustu heimildum málsins — þá **STÖÐVAÐU**, leggðu fram heimildina sérstaklega með rökstuðningi, og spurðu ritstjóra hvort hún eigi heima í málinu. Hagsmunatengd heimild sem er aðeins notuð til að sýna sjónarmið viðkomandi aðila (og er ein af mörgum), krefst ekki stöðvunar — segðu samt frá í lokaskýrslu.

---

## Skref 3 — sækja og vista

### 3.1 Sækja efni

Fyrir hverja kandídatu sem stenst gæðakröfur, sæktu efnið:

**Fyrsta tilraun:** `WebFetch` á slóðina.

**Ef WebFetch bregst** (403 Forbidden, paywall, leiðbeinandi gögn án innihalds, ECONNREFUSED, eða svar sem inniheldur ekki greinina sjálfa):

1. **Athugaðu hvort Chrome DevTools MCP sé tiltækt** (`chrome-devtools` MCP tools). Það notar ekta Chromium og fær oft að sjá síður sem hafna WebFetch (RÚV, Heimildin, Mbl, mörg paywall-laus síður sem blokkera ‚bots‘).
2. **Ef Chrome DevTools MCP er til**, notaðu það til að sækja síðuna (navigate + extract text/markdown).
3. **Ef Chrome MCP er ekki uppsett**, skráðu höfnun í lokaskýrslu með ástæðu „WebFetch blocked, no Chrome MCP available — install with `claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest` and re-run".

Ekki gefast upp á gæða-heimild bara vegna 403. Reyndu Chrome MCP. Ef það er ekki uppsett, þá láttu ritstjóra vita svo hann setji það upp.

### 3.2 Vista

Fyrir hverja heimild sem þú sækir:

- Búðu til `malefni/$1/heimildir/H###-stutt-slug.md` nákvæmlega skv. `snidmat/heimild.md`.
- Númeraðu hækkandi frá hæsta H### sem þegar er til (skoðaðu fyrst með `ls malefni/$1/heimildir/`).
- Slug skal vera 2–4 orð, kebab-case, ASCII (engir íslenskir stafir).
- Fylltu inn frontmatter, lýsingu, tilvitnanir, greiningu, og fullt efni (archive).
- **Tengingar við aðrar heimildir** í Greining-kafla — ef þú sérð að ný heimild styður/stangast á við/bætir við aðra sem þegar er til, þá vísaðu með smellanlegri `[H###](H###-...md)` tilvísun.

### 3.3 Engin yfirskrift, engin eyðing

- **Aldrei yfirskrifa** núverandi `heimildir/H###-*.md` skrá. Ef slóð er þegar til, slepptu — það er ekki villa, það er normal við endurkeyrslu.
- **Aldrei eyða** núverandi heimild. Ef ritstjóri vill eyða, þá gerir hann það sjálfur handvirkt.

---

## Skref 4 — lokaskýrsla (stutt)

Eftir keyrslu, skilaðu þessari skýrslu:

### 4.1 Nýjar heimildir vistar
Tafla:

| H### | Titill | Útgefandi | Sjónarhorn | Hagsmuna­tenging |
|---|---|---|---|---|

### 4.2 Hafnaðar kandídötur
Tafla. Ástæða skal vera nákvæm — ekki bara „hafnað", heldur „403 Forbidden", „lág gæði: óljós höfundur", „tvíverknaður á H005", „WebFetch blocked, Chrome MCP not installed".

| Slóð | Stutt lýsing | Ástæða |
|---|---|---|

### 4.3 Leitarorð notuð

Sýndu öll leitarorð sem þú prófaðir — bæði íslensk og ensk. Þetta hjálpar ritstjóra að sjá slagsíðu í leitinni.

### 4.4 Sjónarhorn / efni sem þú gast EKKI fundið heimild fyrir
Heiðarlegur listi. Ekki sleppa. Þetta er það sem næsta `/rannsaka`-keyrsla á að beinast að.

### 4.5 Næsta skref
Endaðu skýrsluna með einni af:
- *„Vantar fleiri sjónarmið — biddu mig að keyra `/rannsaka $1` aftur og ég beini leit að [þessi gap]."*
- *„Safnið virðist nógu fjölbreytt. Biddu mig að keyra `/greina $1` til að búa til samantekt og greiningar."*

---

## Reglur sem aldrei má brjóta

1. **Ekki breyta `ritstjorn.md`.** Tillögur fara í skýrslu, ritstjóri ákveður.
2. **Stöðvaðu ef hagsmunatengd heimild er lykilheimild.**
3. **Ekki skrifa README.md né ai-greining/.** Það er hlutverk `/greina`.
4. **Idempotent:** aldrei yfirskrifa, aldrei eyða.
5. **Ekki gefast upp á 403** — reyndu Chrome MCP eða skráðu höfnun með ástæðu.
6. **Ekki útbúa tilvitnanir** — ef tilvitnun er ekki orðrétt í heimild, ekki nota gæsalappir.
7. **Ekki stytta lestur** — lestu allar nýjar heimildir til enda áður en þú skrifar Tengingar-kafla.
8. **Ef þú ert óviss, segðu það.**
9. **Engin emoji.**

---

## Bilanaham — algeng mistök

- **„Of fljótt af stað"** — að hætta leit eftir 3 íslenskar leitir. Lágmark er 8 + 8.
- **„Þröng flokka-fókus"** — að gera 16 leitir sem allar eru í 2-3 flokkum (t.d. samgöngumál: allt um almenningssamgöngur, ekkert um hjólainnviði eða gangandi). Flokka-yfirgreiningin í 2.1 á að koma í veg fyrir þetta — fylgdu henni.
- **„Að gefast upp á 403"** — að skrá höfnun án þess að prófa Chrome MCP.
- **„Tvívistuð heimild"** — að bæta sömu slóð aftur við þegar hún er í `heimildir/`. Athugaðu með `grep` áður en þú vistar.
- **„Skrifa-fasinn læðist inn"** — að byrja að skrifa samantekt eða greiningar. Þetta er `/greina`. Stoppaðu.
- **„Falsk samhverfa"** — að safna jafn mörgum heimildum á hverja hlið. Heimildaval á að endurspegla það sem er til, ekki manngert jafnvægi.

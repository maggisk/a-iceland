# Þverfaglegar nálganir — samgongur (uppfært 2026-05-22)

> Skipun: `/baeta-utfyrir-boxid samgongur`. Tillögur að fræðigreinum utan ríkjandi ramma málsins. Ritstjóri eða AI velur hvaða á að innleiða — annað hvort með `/baeta-heimildir` til að safna heimildum úr þeim fræðigreinum, eða með `/baeta-tilraunir` til að smíða Python-líkön úr þeim, eða með handvirkri uppfærslu á `ritstjorn.md` til að breyta ramma málsins.

## Ríkjandi ramma málsins (eins og hann birtist í núverandi safni)

Núverandi greining hvílir á fimm fræðilegum stoðum, allar innan hefðbundinnar samgönguhagfræði og borgarverkfræði:

- **Samgönguhagfræði (cost-benefit, IRR, þjóðhagsleg ábatagreining):** [H001](../heimildir/H001-samgongusattmali-stjornarradid.md), [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md), [H020](../heimildir/H020-mbl-ragnar-arnason-ekki-hagkvaem.md), [H029](../heimildir/H029-skemman-palmi-thjodhagsleg-hagkvaemni.md), [H031](../heimildir/H031-hess-taylor-yoh-brt-vs-lrt.md)
- **Induced demand / umferðar-eftirspurnar-hagfræði:** [H010](../heimildir/H010-wikipedia-induced-demand.md), [H016](../heimildir/H016-vtpi-generated-traffic-induced-travel.md), [H034](../heimildir/H034-duranton-turner-fundamental-law-road-congestion.md)
- **Borgarskipulagsfræði (modal split, þétting, virkir ferðamátar):** [H011](../heimildir/H011-reykjavik-municipal-plan.md), [H014](../heimildir/H014-reykjavik-modal-split-2024.md), [H025](../heimildir/H025-reykjavik-hjolastigar-2023.md), [H027](../heimildir/H027-reykjavik-gangandi-forgangur.md)
- **BRT/LRT-verkfræðileg samanburðar-greining og erlend dæmi:** [H004](../heimildir/H004-visir-lett-borgarlina.md), [H008](../heimildir/H008-tampere-light-rail.md), [H015](../heimildir/H015-bussveien-stavanger-brt.md), [H019](../heimildir/H019-trondheim-miljopakken.md), [H022](../heimildir/H022-oulu-winter-cycling.md), [H023](../heimildir/H023-aarhus-letbane.md), [H024](../heimildir/H024-copenhagen-cycling.md), [H031](../heimildir/H031-hess-taylor-yoh-brt-vs-lrt.md), [H035](../heimildir/H035-mbl-sfa-lett-borgarlina-2021.md)
- **Pólitísk umræða og kjósenda-skipting:** [H012](../heimildir/H012-mbl-eythor-hundrud-thusunda.md), [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md), [H021](../heimildir/H021-heimildin-klyfur-frambodin.md), [H030](../heimildir/H030-heimildin-sundabraut-bru-betri-en-gong.md), [H032](../heimildir/H032-mbl-dagur-hradbrautarkarakter.md)
- **Loftslags-/umhverfismat (skuldbundin markmið):** [H026](../heimildir/H026-reykjavik-co2-2024.md)

Greinilegt **gap:** Allt sem snertir mannlegt atferli, lífsgæði-mat utan CO2-tölu, lýðheilsu-vídd, áhættustjórn megaverkefna, fasteignahagfræði kringum stöðvar, og menningarlegt merkis-hlutverk bílsins er fjarverandi eða aðeins óbeint nefnt.

## Tillögur utan ríkjandi ramma

### B1 — Megaprojekt-áhættustjórnun (Flyvbjerg-ramma)

**Hvað hún myndi bæta:** Greining á því hvort Borgarlína/Sundabraut hagi sér eins og dæmigert "megaproject" með kerfisbundna optimism bias og strategic misrepresentation — frekar en að taka kostnaðarhækkun úr 100/120/160 mrd í 311 mrd sem séríslenskt vandræði.

**Konkret-konsept sem ætti við:**
- **Bent Flyvbjerg "iron law of megaprojects"** — "over budget, over time, under benefits, over and over again" — gefur empíríska dreifingu kostnaðar-framúrkeyrslu sem hægt er að bera saman Borgarlínu við (er hún typical eða outlier?)
- **Optimism bias og strategic misrepresentation** — hvers vegna upphaflegar áætlanir eru kerfisbundnar of lágar; Flyvbjerg sýnir að rail-verkefni fara að meðaltali 45% yfir áætlun
- **Reference class forecasting** — aðferð til að spá kostnaði stórs verkefnis með samanburði við sögulega flokk svipaðra verkefna, ekki bottom-up útreikning frá núlli
- **Premortem-hugmyndin** og fjórar leiðir til að halda kostnaði niðri (Flyvbjerg & Gardner, "How Big Things Get Done", 2023)

**Heimildir/höfundar sem mætti leita að:**
- Flyvbjerg, B. (2014) — "What You Should Know About Megaprojects and Why" í Project Management Journal
- Flyvbjerg & Gardner (2023) — How Big Things Get Done (bók) — sérstaklega kafli um rail-verkefni
- Cantarelli o.fl. (2010) — "Cost Overruns in Large-Scale Transportation Infrastructure Projects" í EJTIR
- OECD/ITF (2017) — Strategic Infrastructure Planning skýrsla

**Hvernig þetta breytti greiningu (ef rétt reynist):**
- README-fullyrðing "Kostnaður hefur margfaldast frá 2019" yrði sett í alþjóðlegt samhengi — er Borgarlína í 95-percentile á kostnaðar-framúrkeyrslu eða innan venjulegrar dreifingar?
- Bætti við spurningu hvort 311 mrd sé endanleg eða hvort fræðileg reference-class spá segi 400–600 mrd (sem Eyþór Arnalds heldur fram [H012](../heimildir/H012-mbl-eythor-hundrud-thusunda.md) án empíríska grunns) — gæti styrkt eða veikt þá tölu
- Stjórnsýslu-tillaga (e. sjálfstæða úttektarstofnun) yrði þá byggð á sérstökum aðferðum (reference class forecasting, premortem) frekar en almennri "meira gagnsæi" hugmynd

**Tengsl við önnur skref:**
- Mun /baeta-heimildir leita: já — Flyvbjerg 2014 paper, Cantarelli 2010, OECD ITF skýrsla
- Mun /baeta-tilraunir prófa: já — reference-class forecasting á Borgarlínu með opnu gagnasafni Flyvbjerg's Cost Overrun Database (rail-verkefni)

**Stenst ritstjórnar-afmörkun:** Já — beinlínis um samgöngu-stórverkefni á höfuðborgarsvæðinu, alþjóðleg fræði sem ritstjorn biður um.

**Forgangur:** HÁR — kostnaðarspurningin er kjarni málsins (ritstjorn nefnir "Fjármögnun er hluti af spurningunni") og Flyvbjerg er staðlað fræðilegt svar við henni. Augljóst gap.

### B2 — Atferlishagfræði og félagsfræði ferðamáta (mode-choice psychology)

**Hvað hún myndi bæta:** Útskýring á því hvers vegna íslenska 2012-samkomulagið og AR2010-30 strætó-markmiðið mistókust þrátt fyrir fjárfestingu — og hvers vegna hjólreiðar svöruðu en strætó ekki. Núverandi greining notar "modal-shift teygjur" sem efnahagslega frekar en sálfræðilega.

**Konkret-konsept sem ætti við:**
- **Status quo bias og default effects** — bíleigandi sem hefur þegar greitt fastan kostnað (bíll, bílskúr, trygging) sér aðeins jaðarkostnað og kýs því bílinn aftur og aftur, jafnvel þegar strætó er ódýrari heildarséð
- **Habit discontinuity hypothesis (Verplanken & Wood)** — fólk skiptir helst um ferðamáta þegar lífshögun breytist (flutningar, ný vinna, barneignir); innleiðing ný innviði þarf að miðast við þessi gluggar
- **Self-perception og identity-based mode choice (Steg, Bamberg)** — bíll sem hluti af sjálfsmynd ("ég er bílamaður") gerir modal-shift erfiðari en einföld verðteygja gerir ráð fyrir
- **Kahneman/Tversky framing** á veggjöldum: loss aversion gerir veggjöld pólitískt erfiðari en jafn-stór skattahækkun á eldsneyti

**Heimildir/höfundar sem mætti leita að:**
- Verplanken, B. (2018) — "Habit and behaviour change" yfirlits-grein
- Bamberg, S. (2006) — "Is a residential relocation a good opportunity to change people's travel behavior?" Environment and Behavior
- Steg, L. (2005) — "Car use: lust and must" í Transportation Research Part A
- Innes, D. & Mitchell, V. (2019) — yfirlit um nudge-tilraunir í modal shift
- Hver íslensk könnun um viðhorf til Borgarlínu (skv. Maskína/Gallup) — ekki í safni

**Hvernig þetta breytti greiningu (ef rétt reynist):**
- README-fullyrðing "Pattern: hjólreiðar svara fjárfestingu, strætó ekki" myndi fá fræðilega skýringu — hjólreiðar krefjast minni breytinga á identity/status quo (geta verið hluti af heilsu/útiveru-identity sem er nú þegar jákvæð á Íslandi)
- Ráðlegging um veggjöld yrði nuanced — pólitísk fyrirstaða er ekki bara "Hildur hafnar þeim" [H021](../heimildir/H021-heimildin-klyfur-frambodin.md) heldur er hún rótgróin í loss aversion
- Ný undir-spurning: er "habit discontinuity" gluggi opinn á Íslandi (fjarvinna eftir 2020 + hækkun bensínverðs gæti verið slíkur gluggi)?
- Ráðlegging gæti bætt við "soft policies" — nudge-tilraunir samhliða innviðum, ekki bara innviði eitt

**Tengsl við önnur skref:**
- Mun /baeta-heimildir leita: já — Verplanken 2018, Steg 2005, og íslenskar viðhorfskannanir
- Mun /baeta-tilraunir prófa: kannski — hægt að byggja agent-based líkan af modal choice þar sem agentar hafa status quo bias parameter

**Stenst ritstjórnar-afmörkun:** Já — beinlínis um samgöngu-val íbúa á höfuðborgarsvæðinu.

**Forgangur:** HÁR — útskýrir lykil-empirísku staðreyndina sem ríkjandi ramma getur ekki útskýrt almennilega (af hverju gengur ekki strætó-markmiðum). Bætir við bæði greiningu (hvers vegna) og ráðleggingu (hvernig).

### B3 — Lýðheilsa og umferðar-utanaðkomu-kostnaðir (transport health economics)

**Hvað hún myndi bæta:** Núverandi greining notar 42% CO2-tölu [H026](../heimildir/H026-reykjavik-co2-2024.md) sem eina umhverfis/heilsu-rökið. Lýðheilsu-vídd nær miklu lengra: loftgæði (PM2.5, NOx), líkamleg hreyfing, dauðsföll í umferð, hávaði, og heilbrigðiskostnaður. Kaupmannahöfn-talan (DKK 534 m/ár) [H024](../heimildir/H024-copenhagen-cycling.md) er nefnd en ekki sundurliðuð fyrir Reykjavík.

**Konkret-konsept sem ætti við:**
- **Disability-Adjusted Life Years (DALYs) og value of statistical life** — kvantitatíf umbreyting heilsuáhrifa í krónutölur sem geta keppt við Cowi-tölur
- **Health Economic Assessment Tool (HEAT) frá WHO** — staðlað tæki sem reiknar heilsu-ábata af göngu og hjólreiðum (notað í Kaupmannahöfn, Stokkhólmi)
- **Air pollution attributable mortality** — loftmengun nálægt umferðar-æðum (Miklubraut, Sundabraut-leiðin) myndi gefa lífslíkindatap í árum tapaðs lífs
- **"Burden of disease" greining á inactivity** — hreyfingarleysi er einn stærsti áhættuþáttur dauða á Íslandi (skv. Lýðheilsustofnun)
- **Vision Zero** — sænsk umferðaröryggis-stefna sem byrjar frá "engin dauðsföll" frekar en cost-benefit

**Heimildir/höfundar sem mætti leita að:**
- WHO HEAT tool og notkunarleiðbeiningar (whothlondon.com)
- Khreis, H. o.fl. (2017) — "Outdoor air pollution and the burden of childhood asthma" í Environment International
- Mueller, N. o.fl. (2017) — "Health impact assessment of cycling network expansions" í Preventive Medicine
- Embætti landlæknis / Lýðheilsustofnun gögn um umferðarslys og hreyfingu
- Tingvall, C. & Haworth, N. — Vision Zero theory paper

**Hvernig þetta breytti greiningu (ef rétt reynist):**
- README-fullyrðing um Kaupmannahöfn (DKK 534 m heilsuábati) yrði stækkuð í líkans-yfirfærslu á Reykjavík með íslenskum lýðheilsu-gögnum — mögulega ný íslensk tala á borð við "X mrd/ári heilsuábati ef hjóla-modal share verður 15%"
- Sundabraut-mat yrði víkkað út yfir cost-benefit yfir í lýðheilsu — íbúar Gufuness/Geldinganess sem fyrr eru bara nefndir undir "lífsgæðaskerðing" [H032](../heimildir/H032-mbl-dagur-hradbrautarkarakter.md) fengju kvantitatíft mat (PM2.5-stig, dB-hávaði, dauðsföll umfram)
- Ráðleggingin um vetrarviðhald hjólastíga fengi sterkari rökstuðning — það er ekki bara modal-shift heldur lífstíma-vörn

**Tengsl við önnur skref:**
- Mun /baeta-heimildir leita: já — WHO HEAT tool, Mueller 2017, Embætti landlæknis tölfræði
- Mun /baeta-tilraunir prófa: já — HEAT-líkan yfirfært á Reykjavík með íslenskum gildum og sensitivity á modal-shift senario

**Stenst ritstjórnar-afmörkun:** Já — höfuðborgarsvæðis-samgöngur og bein áhrif á íbúa.

**Forgangur:** HÁR — kvantitatíft framlag (DALYs í krónutölur) sem getur staðið við hlið Cowi-tölu og styrkt rökin fyrir hjóla-fjárfestingu. Tæki (HEAT) þegar til.

### B4 — Land-economics og value capture (fasteignahagfræði kringum stoppistöðvar)

**Hvað hún myndi bæta:** Núverandi greining tekur ekki á því hvernig Borgarlína breytir landverði, hverjir hagnast (landeigendur við stoppistöðvar), og hvernig hægt er að fjármagna verkefnið sjálft með þeim hagnaði (value capture). Þetta er beint svar við "hver borgar?" spurningu sáttmálans og ritstjorn-spurningu um fjármögnun.

**Konkret-konsept sem ætti við:**
- **Hedonic pricing models** á áhrif fjarlægðar frá nýjum stoppistöðvum á íbúðaverð — alþjóðleg fræði sýnir 5–15% hækkun innan 500 m af BRT/LRT stöðvum
- **Land Value Capture (LVC)** — verkfæri til að ná hluta þess landverðs-hækkunar í opinberar tekjur (mikil notuð í Tokyo, Hong Kong, sums staðar í Bandaríkjunum)
- **Transit-Oriented Development (TOD) financing** — sameina þéttingu byggðar og stöðvarþróun til að fjármagna kerfið
- **Betterment levy / "betri-skattur"** — skattlagning á lóðir sem hækka í verði vegna almannafjárfestingar — hefur lagalegan grunn á Íslandi (skipulagslög) en hefur ekki verið nýtt í þessu samhengi
- **Keldnaland sem case** — landið sem á að fjármagna sáttmálann að hluta [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md) er nákvæmlega TOD-verkefni; greining frá land-economics myndi sýna hvort verðmat er raunhæft

**Heimildir/höfundar sem mætti leita að:**
- Suzuki, H., Murakami, J., Hong, Y.H. (2015) — "Financing Transit-Oriented Development with Land Values" Heimsbankinn
- Smith, J. & Gihring, T. (2006) — "Financing Transit Systems Through Value Capture: An Annotated Bibliography"
- Cervero, R. & Murakami, J. (2009) — "Rail and Property Development in Hong Kong" í Urban Studies
- Medda, F. (2012) — "Land value capture finance for transport accessibility" í Transport Policy
- BBR/HMS gögn um íslenskt fasteignaverð fyrir hedonic líkan

**Hvernig þetta breytti greiningu (ef rétt reynist):**
- README-fullyrðing "Keldnaland sem fjármögnun" myndi verða prófuð — er það raunhæft að selja land á þeim verðmat áður en innviðir eru komnir, eða er það "chicken-and-egg" sem klassísk LVC-fræði leysir með bundnum verðmat eftir uppbyggingu?
- Ný stoð í fjármögnunar-tillögu: betterment levy á lóðir innan 500 m af Borgarlínu-stöðvum — gæti gefið verulega tekjur án að íbúar utan kerfisins greiði
- Ráðleggingin um 25% sveitarfélaga-fjármögnun [H023](../heimildir/H023-aarhus-letbane.md) Aarhus-líkanið) myndi fá nákvæmari aðferð — sveitarfélögin myndu fjármagna sinn hlut með LVC á eigin landi
- Gagnrýni á Borgarlínu-aðferðafræði: Cowi 2024 ábatatala 1.140 mrd [H001](../heimildir/H001-samgongusattmali-stjornarradid.md) inniheldur ekki land value uplift sem er staðlað í alþjóðlegri TOD-fræði

**Tengsl við önnur skref:**
- Mun /baeta-heimildir leita: já — Suzuki 2015 Heimsbanka-skýrsla, Cervero 2009, og íslenskt fasteignaverð gagnasafn
- Mun /baeta-tilraunir prófa: já — hedonic líkan á Reykjavík með BBR-gögnum, sensitivity-greining á LVC-tekjur við ólíkar skatt-prósentur

**Stenst ritstjórnar-afmörkun:** Já — beinlínis um fjármögnun samgangna á höfuðborgarsvæðinu, sem ritstjorn segir vera "hluti af spurningunni".

**Forgangur:** HÁR — bein viðbót við lykilspurningu málsins (fjármögnun) og opnar nýja leið sem hvorki Hildur Björnsdóttir, Eyþór Arnalds, né Dagur B. Eggertsson hafa lagt til. Konkret tæki (LVC, betterment levy) sem hægt er að innleiða.

### B5 — Rhetorical/framing-greining á bílamenningu og "frelsi á vegum"

**Hvað hún myndi bæta:** Núverandi greining tekur pólitíska afstöðu sem gefna staðreynd ("Sjálfstæðisflokkur vill X", "Miðflokkur vill Y") en greinir ekki hvers vegna sömu rökin (verðstýring, hjólastígar, Borgarlína) eru pólitískt heitari á Íslandi en t.d. í Noregi þar sem veggjöld eru sjálfgefin. Framing-greining gæti útskýrt hvers vegna bíllinn er sterk merkis-mynd í íslenskri umræðu.

**Konkret-konsept sem ætti við:**
- **Lakoff frames** — "freedom of the road" vs. "shared space" sem competing conceptual metaphors sem stýra pólitískri umræðu
- **Bourdieu habitus á modal choice** — bíll sem class marker í íslensku samfélagi (jepp/dýr-bíll vs. strætó); hvers vegna miðstéttin þarf "ekki" að nota strætó
- **Discourse analysis á íslenskum fjölmiðlum** — orðanotkun: "umferðartappi" (vandinn) vs. "umferðar-flæði" (lausn) vs. "bílaháð" (vandinn) vs. "frelsi á vegum" (lausn)
- **Sigurvegarinn skrifar söguna** — hvers vegna 2012-samkomulagið er sögð sem "mistök" af Sjálfstæðisflokki [H012](../heimildir/H012-mbl-eythor-hundrud-thusunda.md) en gæti verið sögð sem "ófullnægjandi fjárfesting" af Samfylkingu — báðar tillögur eru rökréttar túlkanir á sömu staðreyndum
- **Carbon culture (Urry)** — bíllinn sem grundvallar-stoð íslenskrar nútímans og hvers vegna engin önnur ferðamáti hefur sömu menningarlegu áherslu

**Heimildir/höfundar sem mætti leita að:**
- Urry, J. (2004) — "The 'System' of Automobility" í Theory, Culture & Society
- Lakoff, G. (2004) — "Don't Think of an Elephant" — politískar frames
- Sheller, M. & Urry, J. (2000) — "The City and the Car"
- Norton, P. (2008) — "Fighting Traffic: The Dawn of the Motor Age in the American City" (söguleg analógía við "jaywalking")
- Íslensk félagsfræði-rannsóknir á neyslu og lifestyle (Stefán Hrafn Jónsson, HÍ) ef til

**Hvernig þetta breytti greiningu (ef rétt reynist):**
- "Hver heldur hverju fram"-kafli yrði dýpkaður — bætt við greiningu á hvaða frames hver aðili notar (sumir tala um "frelsi", sumir um "umhverfi", sumir um "kostnað")
- Ráðlegging um congestion pricing yrði bætt við communication-strategy ráðum — hvernig á að framsetja gjöldin í íslensku samhengi (t.d. Stokkhólmur kallaði sín gjöld "miljöskatt", ekki "biltulla")
- Ný undir-spurning fyrir framtíðar-greiningar: hvert er ratíó milli "frelsis"-orðræðu og "umhverfis"-orðræðu í íslenskum fjölmiðlum um samgöngur 2019–2026?
- Ráðlegging um Sundabraut sem "breiðstræti frekar en hraðbraut" [README] fengi rökstuðning úr framing-fræði — orðin sjálf stýra hvernig hluturinn er hannaður (hraðbraut → 80 km/klst hugsun; breiðstræti → 50 km/klst hugsun)

**Tengsl við önnur skref:**
- Mun /baeta-heimildir leita: já — Urry 2004, Lakoff 2004, og íslenskar félagsfræði-greiningar á bíla-menningu
- Mun /baeta-tilraunir prófa: kannski — corpus-greining á íslenskum fjölmiðla-greinum með NLP (orðatíðni, frame detection) er möguleg í Python en líklega utan ramma /baeta-tilraunir

**Stenst ritstjórnar-afmörkun:** Já — fjallar um umræðuna á höfuðborgarsvæðinu, ekki landsbyggðina sérstaklega. Þó: hugsanlega vill ritstjóri ekki tæknilega framing-analyse innan málsins; gæti verið betra sem reference-skjal í ai-greining/.

**Forgangur:** MIÐ — auðgar greiningu og getur breytt orðalagi ráðleggingar (mikilvægt fyrir innleiðingu), en breytir líklega ekki kjarnaráðleggingunni (lite-Borgarlína + congestion pricing). Áhugavert en með óvissari áhrif en B1-B4.

### B6 — Faraldsfræði-líkön af modal-shift diffusion

**Hvað hún myndi bæta:** Núverandi greining lítur á modal-shift sem línulegt — "X mrd fjárfesting → Y prósentustig hækkun á 5 árum". Faraldsfræði-líkön (S-laga aðtöku-kúrfa með peer-effect) gefa raunsærri spá um hvernig nýr ferðamáti dreifist í gegnum samfélag, sem getur útskýrt hvers vegna sumar borgir (Kaupmannahöfn) fóru í gegnum "tipping point" en aðrar staðna í lágu hlutfalli.

**Konkret-konsept sem ætti við:**
- **Bass diffusion model** — staðlað aðtöku-líkan fyrir ný tækni/hegðun með innovator-imitator dynamic; reikna p (innovation rate) og q (imitation rate) fyrir hjólreiðar á Íslandi
- **Network contagion (Christakis & Fowler)** — hegðun dreifist í gegnum félagsnet (vinir, samstarfsfólk); ef einn manneskja byrjar að hjóla, líkur á að næsti í neti geri það líka
- **Tipping point dynamics (Granovetter threshold model)** — samfélög hafa dreifingu þröskulda; modal-shift gerist ekki línulega heldur þegar hlutfall fer yfir critical mass (oft 15–25%)
- **Reykjavík sem dæmi:** 2008 = 11% virkir, 2024 = 22% [H014](../heimildir/H014-reykjavik-modal-split-2024.md) — er Reykjavík nálægt tipping point eða enn í early adopter-fasa?

**Heimildir/höfundar sem mætti leita að:**
- Christakis, N. & Fowler, J. (2009) — "Connected: The Surprising Power of Our Social Networks"
- Centola, D. (2018) — "How Behavior Spreads: The Science of Complex Contagions"
- Bass, F. (1969/2004) — Bass diffusion model (klassísk + endurskoðuð)
- Aldred, R. (2013) — "Incompetent or too competent? Negotiating everyday cycling identities in a motor dominated society" í Mobilities (sálfræðileg vídd)
- Munro, C. (2020) — "Cycling participation as social contagion" ef til

**Hvernig þetta breytti greiningu (ef rétt reynist):**
- README-fullyrðing "Modal-shift er hægur — Kaupmannahöfn 40 ár" yrði sundurliðuð — líklega tók fyrstu 20 árin lítil hreyfing (innovators), seinni 20 árin steep S-kúrfa (mass adoption). Reykjavík gæti verið nálægt steep hluta kúrfunnar.
- Ný undir-spurning: er hægt að spá hvenær Reykjavík nær tipping point? Ef módel segir 2030, þá er fjárfestingu réttlætt; ef það segir 2050, þá þarf annarra leiða
- Tillaga gæti orðið nákvæmari um hvar á að setja hjólainnviði — netkerfis-líkön (network science, sem er undir-skarast en ekki samhljóða) myndu segja hvaða línur eru "kjarna-tengingar"
- Ráðlegging um aðgerðir gegn habit discontinuity (sjá B2) yrði tengd diffusion — að skapa "innovator-cluster" í tilteknum hverfum sem dreifa hegðun

**Tengsl við önnur skref:**
- Mun /baeta-heimildir leita: já — Christakis 2009, Centola 2018, Aldred 2013
- Mun /baeta-tilraunir prófa: já — Bass diffusion líkan á Reykjavík með söguleg gögn (2008–2024), forecast til 2040 með ólíkum p/q gildum

**Stenst ritstjórnar-afmörkun:** Já — beint um samgöngu-val íbúa á höfuðborgarsvæðinu.

**Forgangur:** MIÐ — konkret tæki (Bass líkan) og söguleg gögn til, en líkans-niðurstöður eru aðeins eins góðar og inntakið. Gæti styrkt eða veikt núverandi ráðleggingu (gæti sagt að ráðleggingin sé of varfærin ef tipping point er nálægt, eða of bjartsýn ef hann er fjarlægur).

## Status-tafla

| # | Fræðigrein | Forgangur | Staða |
|---|---|---|---|
| B1 | Megaprojekt-áhættustjórnun (Flyvbjerg) | HÁR | tillaga |
| B2 | Atferlishagfræði / mode-choice psychology | HÁR | tillaga |
| B3 | Lýðheilsa og umferðar-utanaðkomu-kostnaðir | HÁR | tillaga |
| B4 | Land-economics / value capture | HÁR | tillaga |
| B5 | Rhetorical/framing-greining á bílamenningu | MIÐ | tillaga |
| B6 | Faraldsfræði-líkön af modal-shift diffusion | MIÐ | tillaga |

Ritstjóri uppfærir Staða-dálk: "tillaga" | "innleidd í ritstjorn.md" | "í gangi: /baeta-heimildir leit hafin" | "hafnað: <ástæða>"

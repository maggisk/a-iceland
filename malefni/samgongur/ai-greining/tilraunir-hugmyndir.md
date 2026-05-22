# Hugmyndir að Python-tilraunum — samgongur (uppfært 2026-05-22)

> Skipun: `/baeta-tilraunir samgongur`. Þetta eru **tillögur**, ekki keyrslur. Ritstjóri eða AI velur hvaða á að framkvæma. Þegar tilraun er keyrð, skrá hana í `greining/src/samgongur/` skv. `greining/README.md` reglum.
>
> Líkans-niðurstöður eru ekki sama og heimildir. Þegar vísað er í tilraun í README, aðgreina skýrt: "Skv. eigin sensitivity-greiningu (sjá `greining/src/...`)" frekar en "Skv. [H001]".

## Keyrslu-skýrsla

- Model: claude-opus-4-7
- Dagsetning: 2026-05-22
- Slug: samgongur
- Fjöldi heimilda: 36 (H001–H036)
- README til staðar: já (drög, 32+ heimildir samanteknar)
- Eldri tillögu-skjal: nei (fyrsta keyrsla)
- Núverandi tilraunir í `greining/src/samgongur/`: engar

## Yfirlit

4 HÁR-tillögur, 2 MIÐ, 1 LÁGUR. Engar núverandi tilraunir. Síðasta keyrsla: 2026-05-22 (fyrsta).

Sjónarhorn í forgangsröð: (1) cost-benefit sensitivity sem prófar IRR/BCR-tölur Cowi 2024 — kjarna-tala í ráðleggingu; (2) Flyvbjerg reference-class forecasting á Borgarlínu — beint úr B1 utfyrir-boxid; (3) HEAT-líkan á lýðheilsuábata hjólreiða — beint úr B3; (4) Bass-diffusion á modal-shift — beint úr B6. Þeir tveir miðluðu þætti styðja við hverra tillögu fyrir sig (Sundabraut induced demand + samanburður Cowi vs Ragnar Árnason).

## Status-tafla

| # | Tilraun (stutt) | Forgangur | Staða |
|---|---|---|---|
| T1 | Cowi cost-benefit sensitivity (afsláttarvextir, farþegaspá, kostnaðar-framúrkeyrsla) | HÁR | tillaga (ekki keyrt) |
| T2 | Flyvbjerg reference-class forecasting á Borgarlínu (rail-overrun-dreifing) | HÁR | tillaga |
| T3 | HEAT-yfirfærsla á Reykjavík — heilsuábati hjóla-modal-shift | HÁR | tillaga |
| T4 | Bass-diffusion modal-shift Reykjavík 2008–2024 → spá 2040 | HÁR | tillaga |
| T5 | Sundabraut induced demand senario með Duranton-Turner elasticity | MIÐ | tillaga |
| T6 | Innra samræmi — endurreikna Cowi-líkan með Ragnar-leiðréttingu (fargjöld, hrakvirði) | MIÐ | tillaga |
| T7 | LVC/hedonic verðmat Keldnalands — value capture potential | LÁGUR | tillaga |

Ritstjóri uppfærir Staða-dálk handvirkt: "tillaga" | "í vinnslu" | "klárt: <slóð>" | "hafnað: <ástæða>"

---

## T1 — Cowi cost-benefit sensitivity

**Tilgáta:** Cowi 2024 IRR 9,2% og BCR 3,5 eru viðkvæm fyrir afsláttarvöxtum, lengd ábata-tímabils, og farþegaspám. Tilgátan er **falsifiable**: ef IRR helst yfir 4% (ávöxtunarkrafa Vegagerðarinnar [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md)) við allar plausible forsendubreytingar, þá stenst Cowi-talan stress-prófið. Ef IRR fellur niður fyrir 4% í einum eða fleiri plausible scenarios, þá er ráðlegging um "halda Borgarlínu" háðari forsendum en lesandi heldur.

**Aðferð:** Sensitivity-greining (univariate + tornado plot + multivariate Monte Carlo).

**Forsendur (explicit — engin "magic numbers"):**
- Heildarfjárfesting: 311 mrd ISK (heimild: [H001](../heimildir/H001-samgongusattmali-stjornarradid.md))
- Þjóðhagslegur ábati 1.140 mrd ISK á 50 árum (heimild: [H001](../heimildir/H001-samgongusattmali-stjornarradid.md), [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md))
- Núverandi IRR-tala Cowi: 9,2% (heimild: [H001](../heimildir/H001-samgongusattmali-stjornarradid.md))
- Núverandi BCR: 3,5 (heimild: [H001](../heimildir/H001-samgongusattmali-stjornarradid.md))
- Ávöxtunarkrafa Vegagerðarinnar: 4% (heimild: [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md))
- Ábati-tímabil: 50 ár (heimild: [H001](../heimildir/H001-samgongusattmali-stjornarradid.md))
- Fjárfestingar-uppbygging: ~14 mrd/ári 2024–2029, ~19 mrd/ári 2030–2040 (heimild: [H001](../heimildir/H001-samgongusattmali-stjornarradid.md))
- Cowi-líkan-spá um modal-shift: ferðir með almenningssamgöngum og hjólandi þrefaldast 2019–2040 (heimild: [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md))
- AI-val sem ritstjóri má hafna: dreifing ábata yfir 50 árin er **antaka línuleg ramp-up úr 0 (2024) yfir í full ábatatöku (2040)** — Cowi-aðferðafræði ekki birt opinberlega, þetta er sanngjarn proxy

**Grunngögn:**
- [H001](../heimildir/H001-samgongusattmali-stjornarradid.md): heildartölur og fjárfestingar-prófíll
- [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md): Cowi-líkan modal-shift spá, ávöxtunarkrafa
- [H020](../heimildir/H020-mbl-ragnar-arnason-ekki-hagkvaem.md): aðferðafræði-gagnrýni (notuð sem motivation)
- [H029](../heimildir/H029-skemman-palmi-thjodhagsleg-hagkvaemni.md): fjögur spátilfelli umferðarþróunar (gott samhengi)

**Væntanlegt output:**
- Tornado plot — sýnir hvaða forsendur hafa mest áhrif á IRR (líklega afsláttarvextir + farþegaspá)
- 2D-heatmap: IRR-tala við [afsláttarvextir × farþegaspár-multiplier]
- Tafla með breakpoints: hvenær IRR fer niður fyrir 4% (ávöxtunarkrafa), 0% (þjóðhagslega óhagkvæmt)
- Monte Carlo histogram (10.000 keyrslur) með empíríska dreifingu IRR
- Sensitivity-skylda: prófa afsláttarvextir [2%, 3%, 4%, 5%, 6%, 7%], ábati-tímabil [30, 40, 50, 60 ár], kostnaðar-framúrkeyrsla [0%, +25%, +50%, +100%] (sbr. Flyvbjerg ~45% mediía), farþegaspár [-50%, -25%, baseline, +25%]

**Þar sem hún yrði keyrð:** `greining/src/samgongur/cowi_sensitivity.py`

**Tengsl við README:** Prófar fullyrðingu í **TL;DR** og kafla **Núverandi staða** ("þjóðhagslegan ábata 1.140 milljarða á 50 árum, hlutfall ábata/kostnaðar 3,5 og innri arðsemi 9,2%"). Ef Cowi-talan er fragile, þá veikist forsenda í ráðleggingar-kafla (a) ("Halda Borgarlínu sem stefnu") og styrkist veikleika #1 og #2 í "Veikleikar í þessari ráðleggingu" (Ragnar Árnason ein rödd; engin frumheimild fyrir Cowi).

**Rökstuðningur fyrir forgang HÁR:** Sterkasta einstaka tölu-fullyrðing í allri greiningu málsins (9,2% IRR er nefnd í 4+ heimildum og er grunnur að ráðstöfun 311 mrd af opinberu fé). Aðgengileg gögn (allar tölur í vistuðum heimildum). Lágur kostnaður (NPV-formúla + numpy random; sensitivity-greining er stundir-vinna). Möguleg breyting á ráðleggingu: ef IRR < 4% í plausible scenarios, þá þarf README-ráðlegging að bæta við varúðar-kafla um forsendur. Bein bonus: stress-prófar einnig veikleika #2 ("Engin frumheimild fyrir Mannvit/Cowi skýrslum") með opnu, skiljanlegu líkani.

---

## T2 — Flyvbjerg reference-class forecasting á Borgarlínu

**Tilgáta:** Núverandi áætlun 311 mrd (eða 136 mrd fyrir 1. áfanga) er undirmat á endanlegum kostnaði þegar **rail-cost-overrun-dreifing Flyvbjerg er beitt**. Tilgátan er falsifiable: ef Borgarlína fellur innan 50-percentile (median) rail-overrun-dreifingar (~45%), þá er "normal megaproject"-mat réttlætt. Ef hún er nú þegar í 90+ percentile, þá er ráðlegging um "halda Borgarlínu" háð því að ráðstafa séríslenskum aðferðum til að koma henni aftur niður.

**Aðferð:** Reference-class forecasting (RCF) skv. Flyvbjerg-aðferðafræði. Bera Borgarlínu (cost overrun frá 2019-áætlun til 2024-áætlun) saman við empíríska dreifingu rail-cost-overruns úr Flyvbjerg-gagnasafni.

**Forsendur (explicit):**
- Borgarlína 1. áfangi upphafsáætlun: ~36 mrd 2019-verðlagi (þarf staðfestingu úr [H033](../heimildir/H033-stjornarradid-samgongusattmali-2019.md))
- Borgarlína 1. áfangi núverandi áætlun: 136 mrd ISK (janúar 2026) [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md)
- Heildarsáttmáli 2019: 100/120/160 mrd (þrjár ólíkar tölur skv. heimildum — sjá [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md), [H005](../heimildir/H005-fib-kostnadur-upp-ur-ollu-valdi.md), [H017](../heimildir/H017-ruv-uppfaerdur-sattmali-2024.md))
- Heildarsáttmáli 2024: 311 mrd [H001](../heimildir/H001-samgongusattmali-stjornarradid.md), [H017](../heimildir/H017-ruv-uppfaerdur-sattmali-2024.md), [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md)
- Empírísk rail-cost-overrun media: ~45% (Flyvbjerg, [H036](../heimildir/H036-flyvbjerg-megaprojects-overview-2014.md))
- AI-val: nota Flyvbjerg open-data ef hægt að sækja; ef ekki, gera proxy úr abstract-tölum + standard lognormal-fitting með skewed-right dreifingu sem er typical fyrir cost-overruns
- AI-val sem ritstjóri má hafna: nota raunverðs-leiðréttingu á 2019-tölurnar miðað við 2024-verðlag (sem ekki er gerð beint í heimildum — sumar af 100/120/160 mrd-mismun gæti útskýrt þannig)

**Grunngögn:**
- [H036](../heimildir/H036-flyvbjerg-megaprojects-overview-2014.md): empírísk rail-overrun-tölur, reference-class forecasting aðferð
- [H033](../heimildir/H033-stjornarradid-samgongusattmali-2019.md): upphaflega 2019-áætlunin (kjarna-baseline)
- [H001](../heimildir/H001-samgongusattmali-stjornarradid.md), [H017](../heimildir/H017-ruv-uppfaerdur-sattmali-2024.md), [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md): 2024-áætlanir
- [H005](../heimildir/H005-fib-kostnadur-upp-ur-ollu-valdi.md): kostnaðarhækkun-tímalína (frá Eyþóri/Bjarna)
- Flyvbjerg Megaproject Cost Database (utan safns — open data; ef hægt að sækja, ef ekki, þá staðfest proxy)

**Væntanlegt output:**
- Histogram með empíríska dreifingu rail-cost-overruns + Borgarlínu sem vertical line (sýnir percentile)
- Prediction interval fyrir endanlegan Borgarlínu-kostnað: 50%, 80%, 95% CIs
- Samanburðar-tafla: bottom-up (núverandi 136 mrd) vs reference-class spá (líklega 180–250 mrd ef í 50-percentile rail-overruns)
- Sensitivity-skylda: prófa hvaða comparison class (innfellt rail í þéttbýli, BRT-only, rail-and-bus blandað) gefur breytilegustu spár
- Stress-test: spurning Eyþórs Arnalds "300 → 600 mrd" — er sú tala við 95-percentile reference-class spá?

**Þar sem hún yrði keyrð:** `greining/src/samgongur/flyvbjerg_rcf.py`

**Tengsl við README:** Prófar fullyrðinguna í **TL;DR** og **Núverandi staða** ("Kostnaður hefur margfaldast frá 2019") og styðja eða veikja "Veikleiki #2" í ráðleggingu ("Engin frumheimild fyrir Mannvit/Cowi skýrslum"). Veitir empíríska samhengi fyrir gagnrýni Eyþórs [H012](../heimildir/H012-mbl-eythor-hundrud-thusunda.md) sem hingað til er án empírísks grunns. Beint útfærsla á B1-tillögu úr [`ai-greining/utfyrir-boxid.md`](utfyrir-boxid.md). Gæti styrkt ráðleggingu (f) ("sjálfstæð úttektarstofnun") með konkret aðferðum (RCF + premortem).

**Rökstuðningur fyrir forgang HÁR:** Bein útfærsla á B1 utfyrir-boxid-tillögu sem fékk forgang HÁR. Konkret tæki (RCF) með viðurkenndri aðferðafræði. Aðgengileg gögn (kostnaðar-tímalína í safninu, Flyvbjerg-gagnasafn alkunna). Möguleg breyting á ráðleggingu: ef Borgarlína er empírísk líkleg að halda áfram að hækka, þá þarf README-tímalína-kafli (e) að bæta við buffer eða annan strúktúr. Útkomu-spread líklega stór — gæti ýtt undir "fasaðri uppbyggingu" enn frekar.

---

## T3 — HEAT-yfirfærsla á Reykjavík — heilsuábati hjóla-modal-shift

**Tilgáta:** Að tvöfalda hjóla-modal-share í Reykjavík (úr 5% í 10%) gefur kvantitatífan heilsuábata í krónutölum sem nálgast eða er stærri en upphafsfjárfesting í aukinni hjóla-innviðum (80 mrd að miðju ráðleggingar). Tilgátan er falsifiable: ef HEAT-yfirfærsla gefur <30 mrd árlegan ábata (eða <600 mrd á 20 árum), þá er hjóla-ráðlegging réttlætt af modal-shift/CO2-rökum en ekki af lýðheilsu einum saman; ef hún gefur >60 mrd ársábata, þá er hjólaábati stærri en það sem Cowi 2024 reiknar fyrir Borgarlínu sjálfa.

**Aðferð:** Cross-field líkan — HEAT-aðferðafræði WHO yfirfærð á íslensk gildi.

**Forsendur (explicit):**
- Núverandi hjóla-modal-share Reykjavík: 5% [H014](../heimildir/H014-reykjavik-modal-split-2024.md)
- Núverandi rafhjól-modal-share: 2% [H014](../heimildir/H014-reykjavik-modal-split-2024.md) (sumir HEAT-implementations innihalda, sumir ekki)
- Söguleg viðmiðun: 11% (2008) → 22% (2024) fyrir virka ferðamáta samtals [H014](../heimildir/H014-reykjavik-modal-split-2024.md)
- Kaupmannahöfn-benchmark: heilsuábati DKK 534 m/ári, +1,22 DKK/km hjól vs -0,69 DKK/km bíll [H024](../heimildir/H024-copenhagen-cycling.md)
- Kaupmannahöfn-modal-share-grunnur: 21% af öllum ferðum á svæði, 62% commuter-share í kjarna [H024](../heimildir/H024-copenhagen-cycling.md)
- Reykjavík-íbúafjöldi: ~140.000 (Reykjavík eingöngu) eða ~250.000 (höfuðborgarsvæði) — þarf staðfestingu úr opinberum gögnum (heimildirnar nefna 34.000 nýja íbúa 2016–2024, +100k spá til 2034 [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md))
- AI-val: nota WHO HEAT-formúlu með íslenskum value-of-statistical-life (VSL) og þá íslensku dauðsfalla-tíðni vegna lífsstíls (utan safns; verður að sækja sérstaklega)
- AI-val sem ritstjóri má hafna: nota linear scaling úr Kaupmannahöfn frekar en endurreikna með íslenskum gildum — réttlætanleg shortcut sem fyrsta nálgun

**Grunngögn:**
- [H014](../heimildir/H014-reykjavik-modal-split-2024.md): núverandi modal split + söguleg þróun
- [H024](../heimildir/H024-copenhagen-cycling.md): Kaupmannahöfn-benchmark (heilsuábati, hagfræði)
- [H022](../heimildir/H022-oulu-winter-cycling.md): Oulu vetrar-modal-share (kalda-loftslags-leiðrétting)
- [H025](../heimildir/H025-reykjavik-hjolastigar-2023.md): núverandi hjólastíga-staða (innviða-grunnur)
- [H026](../heimildir/H026-reykjavik-co2-2024.md): CO2-bonus af hjólreiðum vs bíll
- WHO HEAT-tól og íslensk Lýðheilsustofnun-tölfræði (utan safns — þarf /baeta-heimildir keyrslu fyrst)

**Væntanlegt output:**
- Tafla: heilsuábati í krónum/ári fyrir [modal-share 5%, 7,5%, 10%, 15%, 20%] miðað við [íbúafjölda 140k, 200k, 250k]
- Samanburðar-tafla: HEAT-tala vs ávöxtunar-tala af hjóla-fjárfestingu (80 mrd skv. ráðleggingu) — payback-tímabil
- Sundurliðun: dauðsfalla-fjöldi vörn, DALY-tap vörn, sjúkrahúskostnaðar-vörn, vinnudaga-vörn
- Sensitivity-skylda: prófa kalda-loftslags-modifier [Oulu-aðlögun 10% vetrarhlutfall], aðlögunar-spá-curve [línuleg / exponential / logistic], life-expectancy parameter Íslands [eðlilegt íslenskt vs WHO-staðlað]

**Þar sem hún yrði keyrð:** `greining/src/samgongur/heat_reykjavik.py`

**Tengsl við README:** Styrkir ráðleggingu (c) ("Hjól og gangandi — tvöfalda hlutfall") sem nú treystir á Kaupmannahöfn-tölu eingöngu. Beint útfærsla á B3-tillögu úr [`ai-greining/utfyrir-boxid.md`](utfyrir-boxid.md). Gæti gefið sjálfstæða íslenska tölu sem rivalar Cowi 2024 (1.140 mrd ábati Borgarlínu) — ef hjóla-HEAT er >100 mrd PV, þá er rökstuðningur fyrir tilfærslu fjárfestinga úr Borgarlínu í hjóla-innviði sterkari.

**Rökstuðningur fyrir forgang HÁR:** Beint útfærsla á B3-tillögu (sem hefur forgang HÁR í utfyrir-boxid). Konkret WHO-tæki, viðurkennd aðferðafræði. **Möguleg breyting á ráðleggingu:** ef HEAT-tala er nálægt Cowi-tölu, þá er ráðlegging um 25% hjól-hlutfall réttlætanlegt á standalone-grunni; ef hún er smærri, þá þarf modal-shift/CO2-rök til viðbótar. Lágur tæknilegur kostnaður (HEAT-formúla er einfaldur). Eitt athugavert: krefst að /baeta-heimildir sækir íslensk Lýðheilsustofnun-tölfræði fyrst — annars er Kaupmannahöfn-scaling lélegri proxy.

---

## T4 — Bass-diffusion modal-shift Reykjavík 2008–2024 → spá 2040

**Tilgáta:** Reykjavík er á steep-S-hluta Bass-diffusion kúrfu fyrir virka ferðamáta og mun ná 30–35% modal-share fyrir 2040 við nuverandi fjárfestingar-prófíl, ÁN viðbótar fjárfestinga. Annað sjónarmið: ef Bass-spá segir Reykjavík sé enn í early-adopter-fasa (sem tók Kaupmannahöfn 20 ár), þá þarf miklu meiri fjárfestingu til að ná Reykjavík-markmiðum á tímalínu sáttmálans. Tilgáta er falsifiable: söguleg gögn 2008 (11%) → 2024 (22%) gefa nóg dynamic til að fitta Bass-líkan með p (innovation) og q (imitation) parametrum. Ef forecast 2040 er innan ±5% af tilteknu sett markmiði, þá staðfestir tilgáta um steep-S; ef það víkur mikið, þá hefur tilgáta hrunið.

**Aðferð:** Bass-diffusion líkan með söguleg gögn. Maximum-likelihood-aðlögun p, q parametra. Spá til 2040 við [counterfactual: enginn sáttmáli, baseline: núverandi sáttmáli, bjartsýni: aukin hjóla-fjárfesting].

**Forsendur (explicit):**
- Söguleg modal-share virkra ferðamáta: 11% (2008), 22% (2024) [H014](../heimildir/H014-reykjavik-modal-split-2024.md)
- Bíla-modal-share söguleg: 73% (2017), 71% (2019), 67% (2022), 70% (2024) [H014](../heimildir/H014-reykjavik-modal-split-2024.md) — bíll ekki að fjara út línulega
- Mörk Bass-líkans (m): saturation level. AI-val: nota Kaupmannahöfn 41-50% sem upper-bound proxy [H024](../heimildir/H024-copenhagen-cycling.md), nema "carbon culture"-rök (B5 utfyrir-boxid) myndu setja það lægra fyrir Ísland (utan safns)
- Strætó-failure-mode: 4% (2008) → 5–8% (2024) ekki Bass-aðlögun heldur stöðun [H011](../heimildir/H011-reykjavik-municipal-plan.md), [H014](../heimildir/H014-reykjavik-modal-split-2024.md). AI-val að líkana strætó sérstaklega með **stalled diffusion** (lágt q) frekar en að nota sömu parametra og hjóla-Bass
- AI-val sem ritstjóri má hafna: aðgreina hjólreiðar (5%) frá gangandi (12,5%) frá rafknúnum (4,5%) — annars eru þrír ólíkir adoption-flokkar limit sem ekki er hægt að líkana saman
- Tímapunktar: 5 söguleg gögn fyrir bíla-modal-share, 2 söguleg gögn fyrir virka ferðamáta — **lágmark** fyrir Bass-fit (tæknilegt veikleiki)

**Grunngögn:**
- [H014](../heimildir/H014-reykjavik-modal-split-2024.md): söguleg gögn 2008–2024 (kjarna-time-series)
- [H011](../heimildir/H011-reykjavik-municipal-plan.md): AR2010-30 markmið (4%→12% strætó, 21%→30% göngu/hjól) — gefur viðmið
- [H024](../heimildir/H024-copenhagen-cycling.md): Kaupmannahöfn söguleg gögn 1970 (10%) → 2010 (50%) — international comparison
- [H022](../heimildir/H022-oulu-winter-cycling.md): Oulu sem dæmi um borg sem náði háu modal-share í köldu loftslagi
- [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md): Vegagerðin-mæling (5% hjól, 18% gangandi, 5% strætó) — viðbótartímapunktur (höfuðborgarsvæði-skala)

**Væntanlegt output:**
- Bass-fitting curves: hjólreiðar + gangandi + (sérstaklega) strætó, með söguleg gögnpunktum + spá til 2040
- Prediction intervals (bootstrap CI): 80%, 95% fyrir 2040-modal-share
- Senario-tafla: [no-policy, baseline sáttmáli, aukin hjóla-fjárfesting] — hver gefur p/q parametra-modifier
- Tipping point analysis: hvenær fer hjóla-share yfir 15% critical-mass (sem fræði segir kveiki sjálfvirkari aðstöku)
- Sensitivity-skylda: m (saturation) [25%, 35%, 50%], q-modifier af viðbótarfjárfestingu [+10%, +25%, +50%], söguleg gögn outliers (sleppa 2022 sem COVID-rugl?)

**Þar sem hún yrði keyrð:** `greining/src/samgongur/bass_modal_shift.py`

**Tengsl við README:** Prófar lykilfullyrðinguna í **Saga** og **Núverandi staða** ("Pattern: hjólreiðar svara fjárfestingu, strætó ekki"). Gefur empíríska grunn að ráðleggingar (a) (Borgarlína lite — réttlætanleg ef Bass-líkan spáir lágu strætó-share) og (c) (hjóla-25% — réttlætanleg ef Bass-líkan spáir hraðri aðtöku). Beint útfærsla á B6-tillögu úr [`ai-greining/utfyrir-boxid.md`](utfyrir-boxid.md).

**Rökstuðningur fyrir forgang HÁR:** Empíríska kjarnastaðreyndin í málinu (hjól vs strætó pattern) hefur ekki fræðilegan grunn í núverandi greiningu. Bass er staðlað tól. Gögnin eru í safninu. Lágur tæknilegur kostnaður (scipy.optimize.curve_fit eða statsmodels). **Möguleg breyting á ráðleggingu:** ef Bass-spá segir Reykjavík sé nálægt tipping-point, þá er ráðlegging (c) jafnvel of varfærin (25% er innan reach); ef hún er enn í early-adopter, þá er ráðlegging (a) (Borgarlína lite) of bjartsýn um modal-shift. Veikleiki: lágmarks-fjöldi söguleg gögn (tveir punktar fyrir virka ferðamáta).

---

## T5 — Sundabraut induced demand senario með Duranton-Turner elasticity

**Tilgáta:** Sundabraut sem 4-akreina brú/breiðstræti mun skapa 80–100% af nýrri umferð innan 6–8 ára af opnun (skv. elasticity ≈ 1.0 fra Duranton-Turner 2011). Tilgáta er falsifiable með senario: ef nýtt VKT 5 árum eftir opnun er reiknað sem <50% af kapacitet, þá hrekur tilgáta um induced demand fyrir Sundabraut sérstaklega; ef >75%, þá staðfestir.

**Aðferð:** Senario-mat með elasticity-líkani — Duranton-Turner empírískum gildum yfirfært á Sundabraut-spá.

**Forsendur (explicit):**
- Sundabraut kostnaður (2021-verðlag): 69–83 mrd; uppfært: ~92–111 mrd [H006](../heimildir/H006-stjornarradid-sundabraut.md), [H032](../heimildir/H032-mbl-dagur-hradbrautarkarakter.md)
- Núverandi traffic Höfðabakki/Vesturlandsvegur: ~50.000 bílar/dag (Hafnarfjörður-vísun frá [H017](../heimildir/H017-ruv-uppfaerdur-sattmali-2024.md))
- VKT-elasticity wrt lane-kilometer: 1.0 fyrir interstate-vegi (Duranton-Turner 2011 [H034](../heimildir/H034-duranton-turner-fundamental-law-road-congestion.md))
- 80% absorption rule: 80% af nýrri afkastagetu frásogast 6–8 árum [H010](../heimildir/H010-wikipedia-induced-demand.md)
- Goodwin meta-analýsa: 10% lane-km hækkun → 4% strax + 10% innan fárra ára [H010](../heimildir/H010-wikipedia-induced-demand.md)
- AI-val: yfirfæra Duranton-Turner sem voru bandarísk gögn á Reykjavík þrátt fyrir varúðir í [H034](../heimildir/H034-duranton-turner-fundamental-law-road-congestion.md) ("ekki sérstaklega við um norrænar borgir, smærri evrópskar borgir")
- AI-val sem ritstjóri má hafna: nota höfuðborgarsvæðis-population-growth-spá +100k til 2034 [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md) sem viðbótar-driver fyrir nýtt VKT

**Grunngögn:**
- [H034](../heimildir/H034-duranton-turner-fundamental-law-road-congestion.md): elasticity ≈ 1.0, IV-aðferð
- [H010](../heimildir/H010-wikipedia-induced-demand.md): 80% absorption rule, 4%/10% short-run/long-run
- [H016](../heimildir/H016-vtpi-generated-traffic-induced-travel.md): VTPI-greining
- [H006](../heimildir/H006-stjornarradid-sundabraut.md): Sundabraut-tækniforsendur (afkastageta, leiðsla)
- [H030](../heimildir/H030-heimildin-sundabraut-bru-betri-en-gong.md): Vegagerðar-spá um traffic-flow eftir opnun
- [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md): +100k íbúa-spá til 2034

**Væntanlegt output:**
- Línurit: VKT vs tíminn (0–20 ár eftir opnun) fyrir [no induced demand, partial 50%, full Duranton 100%] senario
- Tafla: % afkastageta nýtt 1 ár, 5 ár, 10 ár, 20 ár eftir opnun
- Sensitivity: elasticity [0.5, 0.8, 1.0, 1.2], population-growth [40k, 60k, 100k til 2034], modal-shift baseline [-2pp bíll, 0, +2pp bíll]
- Cost-effectiveness: kostnaður á varanlegt traffic-relief-hour (líklega lélegt útkomu fyrir Sundabraut)

**Þar sem hún yrði keyrð:** `greining/src/samgongur/sundabraut_induced_demand.py`

**Tengsl við README:** Styrkir ráðleggingu (b) ("Endurhanna Sundabraut sem fjölhliða breiðstræti") og rökstuðning í **Hugmynd 2** ("Sundabraut brú vs. göng vs. ekki gert"). Ef induced demand líkan sýnir að Sundabraut sem hraðbraut leysi <20% af tafa-vandanum innan 10 ára, þá er ráðlegging mín um breiðstrætis-endurhönnun (eða "ekki gert"-valkostur Miðflokks) sterkari rökstuðdd. **Veikleiki #6** ("Endurhönnun Sundabrautar sem breiðstrætis er ekki tillaga í neinni heimild") gæti minnkað ef tilraun gefur empíríska grunn.

**Rökstuðningur fyrir forgang MIÐ:** Sterk fræðileg rök eru þegar í heimildum (Duranton-Turner mjög skýrt); útkomu-spread er kannski takmarkað (líkan mun næstum örugglega gefa "Sundabraut leysir ekki vandann"-niðurstöðu, sem styrkir lite ekki gold útgáfu af núverandi ráðleggingu en breytir henni ekki dramatískt). Yfirfærsla úr US-gögnum hefur óvissu sem dregur úr trúverðugleika. Aðgengilegir grunngögn en óvissa um framtíðar-VKT-spá.

---

## T6 — Innra samræmi — endurreikna Cowi-líkan með Ragnar-leiðréttingu

**Tilgáta:** Ágreiningur milli Cowi 2024 (1.140 mrd ábati, 9,2% IRR) og Ragnar Árnason ("þjóðhagslegt núvirði verulega neikvætt") má **rekja að mestu** til tveggja aðferðafræði-mismunar: (a) hvort greidd fargjöld eru talin félagslegur ábati eða tilfærsla; (b) hvort "hrakvirði" framkvæmdarinnar er hluti af útreikningi. Tilgátan er falsifiable: ef fjarlæging beggja gefur NPV nálægt 0 (innan ±20% af núlli), þá útskýrir aðferðafræði-munurinn allan ágreining; ef NPV helst verulega jákvætt eftir leiðréttingar, þá er gagnrýni Ragnars veikari en hún virðist; ef NPV verður mjög neikvætt, þá er hún sterkari.

**Aðferð:** Reproduce Cowi-greiningar með opnum forsendum + sensitivity á tveimur Ragnar-gagnrýnis-atriðum.

**Forsendur (explicit):**
- Cowi 2024: 1.140 mrd ábati, 311 mrd kostnaður, 9,2% IRR, 3,5 BCR, 50 ár [H001](../heimildir/H001-samgongusattmali-stjornarradid.md)
- Ragnar-gagnrýni: fargjöld og hrakvirði rangtaldir [H020](../heimildir/H020-mbl-ragnar-arnason-ekki-hagkvaem.md)
- Strætó 12,6 milljónir innstiga 2023 (gefur ferskar viðmiðun fyrir fargjalda-tekjur) [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md)
- AI-val: gera ráð fyrir að fargjalda-hlutur af 1.140 mrd ábatanum sé 15–25% (Cowi-aðferðafræði ekki opinber, þetta er proxy úr typical transit cost-benefit-greiningum)
- AI-val: hrakvirði sé 10–20% af heildarábatatölu (typical proxy fyrir terminal-value í 50 ára CBA)
- AI-val sem ritstjóri má hafna: ef proxy-tölur eru of bjartsýnar, þá er Ragnar-leiðrétting smávægileg; ef of svartsýnar, þá er hún öflug — sensitivity gerir þetta sýnilegt

**Grunngögn:**
- [H020](../heimildir/H020-mbl-ragnar-arnason-ekki-hagkvaem.md): aðferðafræði-gagnrýni Ragnars (núvirði "verulega neikvætt")
- [H029](../heimildir/H029-skemman-palmi-thjodhagsleg-hagkvaemni.md): Pálmi BS-ritgerð (leiðbeinandi Ragnar) — fjögur spátilfelli
- [H001](../heimildir/H001-samgongusattmali-stjornarradid.md), [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md): Cowi-tölur
- [H007](../heimildir/H007-borgarlinan-afhverju.md), [H013](../heimildir/H013-borgarlinan-skyrslur-utgefid-efni.md): Mannvit 2020-líkans (eldri grunnur)

**Væntanlegt output:**
- Vatnsfalls-skema (waterfall chart): hvernig 1.140 mrd brotnar niður þegar (a) fargjöld eru tekin út, (b) hrakvirði tekið út, (c) bæði tekin út
- Tafla: NPV og IRR fyrir 4 senario [Cowi-baseline, no-fargjöld, no-hrakvirði, no-bæði]
- Sensitivity-skylda: fargjalda-hlutur [10%, 15%, 20%, 25%] × hrakvirðis-hlutur [5%, 10%, 15%, 20%]
- Niðurstaða: hvort Ragnar-gagnrýni gæti útskýrt 100% af ágreiningnum

**Þar sem hún yrði keyrð:** `greining/src/samgongur/cowi_vs_ragnar.py`

**Tengsl við README:** Beint próf á **Hugmynd 1** kafla ("Cowi 9,2% vs Ragnar 'verulega neikvætt'"). Gæti aðlagað **Veikleiki #1** ("Of mikið treyst á eina rödd") — ef Ragnar-rök eru reproducible með opnum forsendum, þá er sjálfstæð rödd ekki nauðsynlegur. Tengist beint kafla **Lykilheimildir** (H001, H018, H020).

**Rökstuðningur fyrir forgang MIÐ:** Sterk fullyrðing í README (innra samræmi) og lágur tæknilegur kostnaður (sömu NPV-formúla og T1 + tvö breytingar). En **eitt mikilvægt vandamál:** án Cowi-frumskýrslu er fjárhæð fargjalda og hrakvirðis í líkani ekki vituð. Sensitivity getur upplýst hve viðkvæmt ágreiningur er, en endanlegt svar krefst Cowi-PDFs (sem heimildirnar segja vera utan safns — sjá Hvað vantar í safnið kafla README). Niðurstaða gæti orðið ófullnægjandi: "Ragnar-rök eru plausible við sumar plausible proxy-tölur en hrekjast við aðrar." Réttilegt sem MIÐ heldur en HÁR.

---

## T7 — LVC/hedonic verðmat Keldnalands — value capture potential

**Tilgáta:** Land-value-uplift kringum Borgarlínu-stoppistöðvar í Keldnalandi er nógu stór til að réttlæta betterment-levy sem fjármögnunar-tæki. Tilgátan er falsifiable: ef hedonic líkan á íslensk fasteignagögn sýnir <5% hækkun innan 500 m af stoppistöð, þá veikist B4-tillaga utfyrir-boxid; ef >10%, þá styrkist hún og opnar nýja fjármögnunar-leið sem ekki er í núverandi ráðleggingu.

**Aðferð:** Cross-field líkan — hedonic pricing model á íslensk fasteignagögn (HMS/BBR) með distance-to-station sem lykilbreytu.

**Forsendur (explicit):**
- Keldnaland sem fjármögnunar-component sáttmálans [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md)
- Borgarlína fyrsti áfangi: Ártúnshöfði–Hamraborg [H009](../heimildir/H009-wikipedia-borgarlina.md)
- Alþjóðleg fræði: 5–15% hækkun innan 500 m af BRT/LRT stöð (utfyrir-boxid B4 — utan safns; þarf /baeta-heimildir keyrslu)
- Aarhus-fjármögnunarmódel: 47/47/6 ríki/sveitarfélag/private [H023](../heimildir/H023-aarhus-letbane.md)
- AI-val: nota gerviborgar-data fyrir distance til Borgarlína-stoppistöðva (verkefnið skipulagt en ekki opnað enn) — proxy úr almenningssamgöngu-stoppistöðvum í dag
- AI-val sem ritstjóri má hafna: nota strætó-stoppistöð sem proxy fyrir BRT-stoppistöð (strætó-stoppistöð er ekki sambærileg — venjuleg strætó-stoppistöð gefur ekki sama uplift sem BRT/LRT)

**Grunngögn:**
- HMS/BBR fasteignagögn (utan safns — opin gögn en þarf sækja)
- [H018](../heimildir/H018-heimildin-hvad-kosta-lofordin.md): Keldnaland-samhengi
- [H009](../heimildir/H009-wikipedia-borgarlina.md): Borgarlína-leið og stoppistöðvar
- [H023](../heimildir/H023-aarhus-letbane.md): Aarhus value-capture-líkan
- [H011](../heimildir/H011-reykjavik-municipal-plan.md): Aðalskipulag 2010–30 (þétting kringum stoppistöðvar)

**Væntanlegt output:**
- Hedonic regression coefficient: % verðhækkun per 100 m nær stoppistöð
- Heatmap: spá um verðmat Keldnalands við ólíkar Borgarlína-útfærslur
- Tekjustofn-spá: hve mikið betterment-levy myndi gefa á 20 árum
- Sensitivity: distance threshold [300 m, 500 m, 800 m], uplift-magnitude [low 5%, med 10%, high 15%], levy-percentage [10%, 25%, 50%]

**Þar sem hún yrði keyrð:** `greining/src/samgongur/lvc_keldnaland.py`

**Tengsl við README:** Bætir nýju undir-tilboði í ráðleggingu (d) ("Fjármögnun") sem í dag nefnir aðeins veggjöld og congestion pricing. Beint útfærsla á B4-tillögu úr [`ai-greining/utfyrir-boxid.md`](utfyrir-boxid.md). Tengist **Hvað vantar í safnið** — "Engin nákvæm greining á áhrifum Borgarlínu á einkabílinn" og "Keldnaland sem fjármögnun [án verðmats-prófs]".

**Rökstuðningur fyrir forgang LÁGUR:** Hár forgangur sem B4-tillaga (forgangur HÁR í utfyrir-boxid) en lágur sem **tilraun** vegna þess að: (1) Krefst utan-safns gagna (HMS/BBR fasteignagögn) — /baeta-heimildir verður að keyra fyrst, (2) Hedonic-líkan á íslensk gögn er fjölvírkari en sensitivity-greining — krefst geographic data + price-data merger sem er **dagar af vinnu**, ekki klukkutímar, (3) Útkoma-spread á hedonic-regression er stór (íslensk markaður er smár, noise-hlutfall hátt) og gæti gefið ekkert clear-cut answer. **Þessi tilraun er framsetting sem ætti að keyra þegar tvær (T1, T2) hafa skilað skýrum niðurstöðum og frekari heimildaöflun hefur skilað HMS-gögnum.** Setja á LÁGUR af practical-reason.

---

## Skref 5 — lokaskýrsla

### 5.1 Nýjar tillögur

| Tnr | Nafn | Forgangur | Tengsl við README |
|---|---|---|---|
| T1 | Cowi cost-benefit sensitivity | HÁR | TL;DR + Núverandi staða (IRR 9,2%, BCR 3,5); Veikleiki #1 og #2 |
| T2 | Flyvbjerg reference-class forecasting | HÁR | TL;DR (kostnaðar-hækkun) + Veikleiki #2; B1 utfyrir-boxid |
| T3 | HEAT-yfirfærsla á Reykjavík | HÁR | Ráðlegging (c) hjólainnviðir 25%; Hugmynd 4; B3 utfyrir-boxid |
| T4 | Bass-diffusion modal-shift | HÁR | Saga + Núverandi staða ("hjól vs strætó pattern"); Ráðlegging (a)+(c); B6 utfyrir-boxid |
| T5 | Sundabraut induced demand senario | MIÐ | Hugmynd 2 + Ráðlegging (b) Sundabraut-endurhönnun |
| T6 | Cowi vs Ragnar innra-samræmi | MIÐ | Hugmynd 1 (Cowi vs Ragnar); Lykilheimildir |
| T7 | LVC/hedonic Keldnaland | LÁGUR | Ráðlegging (d) Fjármögnun; B4 utfyrir-boxid |

### 5.2 Eldri tillögur sem haldnar eru ófrágengnar

(engar — fyrsta keyrsla)

### 5.3 Fullyrðingar í README sem ég gat EKKI lagt til tilraun fyrir

- **"Spáin um farþegafjölda (~1.000/klst) fellur undir BRT-svæði"** ([H009](../heimildir/H009-wikipedia-borgarlina.md), Hugmynd 1) — spáin er ein punkt-tala án dreifingar/aðferðafræði; sensitivity-greining krefst að farþegaspár-líkan sé reproduced fyrst (klárið verk, krefst nýrra heimilda eða Mannvit-PDF).
- **"Sundabraut umhverfismat lá fyrir í október 2025"** (Núverandi staða) — eingöngu staðreynd, ekki kvantitatív fullyrðing.
- **"2012-samkomulagið um að stöðva stofnvegaframkvæmdir mistókst"** (Saga) — fræðileg túlkun, ekki kvantitatív; gæti orðið Bass-líkan (T4) ef horft er á 4%→5–8% strætó-fórnun en það er nú þegar inni.
- **"Hildur hafnar veggjöldum á eldri vegi (Ártúnsbrekka)"** — pólitísk afstaða, ekki testanleg með Python.
- **"Hagsmunatengingar heimilda (FÍB, Borgarlínan ohf.)"** (Mat á heimildum) — eigindlegt mat ritstjóra, ekki testanlegt.
- **"Skemman BS-ritgerðin var ekki sótt sem PDF; fjögur spátilfelli ekki sundurliðuð"** (Veikleiki #8) — ekki tilraun heldur heimildaöflun (/baeta-heimildir krefst).
- **"Engin gögn um íslensk viðhorf almennings"** (Veikleiki #7) — krefst nýrra heimilda (kannanir) áður en tilraun er möguleg.
- **"PM2.5 og dB-hávaði nálægt Sundabraut"** (úr B3 utfyrir-boxid) — krefst air-quality gagna sem ekki eru í safninu; tilraun framkvæmanleg en aðeins eftir /baeta-heimildir.
- **"Bergen Bybanen samanburður"** — krefst /baeta-heimildir til að sækja ScienceDirect-grein.

### 5.4 Næsta skref

4 nýjar HÁR-tillögur (T1–T4), 2 MIÐ (T5, T6), 1 LÁGUR (T7). T1–T4 nota allar grunngögn sem þegar eru í safninu og þurfa engar nýjar heimildir. T3 og T7 myndu græða af /baeta-heimildir-keyrslu sem sækir íslensk Lýðheilsustofnun-tölfræði (T3) og HMS/BBR fasteignagögn (T7). Biddu mig að keyra `/baeta-tilraunir samgongur` aftur eftir að þú hefur farið yfir og merkt klárðar/hafnaðar tillögur — eða `/baeta-heimildir samgongur` ef þú vilt fá utan-safns gögn sem T3 og T7 krefjast.

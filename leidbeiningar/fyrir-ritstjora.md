# Leiðbeiningar fyrir ritstjóra

Þú berð ábyrgð á því sem birtist í þessu repo. AI-ið er rithöfundurinn; þú ert ritstjórinn. Skipting verka:

| Hver gerir hvað | |
|---|---|
| **Manneskja** | Velur mál. Skrifar `ritstjorn.md` (áherslu, afmörkun, leiðbeiningar, **markmið fyrir ráðleggingu**). Yfirfer útkomu eftir á — fjarlægir lélegar heimildir, uppfærir `ritstjorn.md` með athugasemdum, og keyrir AI aftur ef þörf er á. **Vegur ráðleggingu AI á móti eigin reynslu**. |
| **AI í `/rannsaka`** | Leitar að heimildum, velur sjálf þær sem standast gæðakröfur, sækir, vistar og lýsir í `heimildir/H###-*.md`. Idempotent — má keyra aftur til að bæta við. Stöðvar aðeins ef hagsmunatengd heimild lendir á því að vera lykilheimild. |
| **AI í `/greina`** | Les allar heimildir og skrifar/uppfærir aðalskjalið `README.md` málsins með "Niðurstöður og tillögur gervigreindar"-kafla, og valkvæð reference-skjöl í `ai-greining/`. Bætir aldrei við heimildum. |

`ritstjorn.md` er skjalið þar sem þín rödd setur rammann. AI gerir rannsóknina, greininguna og **leggur fram tillögu að lausn** — undir leiðsögn þinni. Mikilvægt: AI tekur afstöðu í ráðleggingar-skjalinu. Þú vegur hana, gagnrýnir, og uppfærir leiðbeiningar þegar þörf er á.

## Vinnuflæði fyrir nýtt mál

1. **Stofna mál** með `/nyttmal <slug> "<heiti>"`. Skipun afritar sniðmát úr `snidmat/`.

2. **Skrifa `ritstjorn.md`.** Þetta er **mikilvægasta skrefið** og kemur á undan heimildaöflun. Hér setur þú:
   - **Áherslu og afmörkun** — hvað á málið að fjalla um, hvað ekki
   - **Verkefnalista fyrir AI** — hvaða skjöl á að búa til, hvaða spurningum á að svara, hvaða köflum á að skipta greiningu í
   - **Leiðbeiningar fyrir heimildaöflun** — t.d. "leitaðu á íslenskum fréttasíðum", "passaðu að ná báðum sjónarmiðum", "ekki nota greinar eldri en 2020"
   - Allt sem þú vilt að AI taki tillit til

3. **Safna heimildum með `/rannsaka <slug>`.** AI leitar (mikið — íslenskt + ensku), velur og vistar heimildir sjálf í `heimildir/`. Skipunin er **idempotent**: keyrðu hana aftur og aftur til að dýpka safnið eða finna ný sjónarhorn. Hver keyrsla bætir við — yfirskrifar aldrei. Þú færð lokaskýrslu með leitarorðum, höfnuðum kandídötum, og sjónarmiðum sem AI fann ekki heimild fyrir. AI stöðvar eingöngu ef hagsmunatengd heimild er metin sem lykilheimild.

4. **Bæta tilteknum heimildum við ef þú vilt** með `/heimild <slug> <URL>` — t.d. ef þú átt PDF eða slóð sem AI fann ekki.

5. **Yfirfara heimildasafnið.** Lestu lokaskýrsluna úr `/rannsaka`. Eyddu lélegum heimildum handvirkt. Ef heimild þarf sérstaka meðhöndlun (hagsmunatengd, skoðanagrein), bættu henni við „Mat á heimildum" í `ritstjorn.md`.

6. **Skrifa samantekt og greiningar með `/greina <slug>`.** Þegar safnið er nógu fjölbreytt. AI les allar heimildir og skrifar `README.md` + skrár í `ai-greining/`. Bætir aldrei við heimildum — ef vantar, þá keyrir þú `/rannsaka` aftur.

7. **Sannprófa.** Keyrðu `/sannprofa <slug>` til að athuga tilvitnanir. Opnaðu líka nokkrar heimildir handvirkt og athugaðu að AI hafi ekki misskilið.

8. **Skrá athugasemdir í `ritstjorn.md`** og endurkeyra. Iterativt: ef niðurstaða er ekki nógu góð — eða heimildaval er einsleitt — þá bætirðu við leiðbeiningu ("rannsakaðu líka X", "ekki nota heimildir frá Y"), krossar gamla úr, og keyrir AI aftur (`/rannsaka` fyrir heimildir, `/greina` fyrir skrif). Ekki breyta AI-útgáfunni handvirkt nema í smáleiðréttingum (innsláttarvillur).

9. **Commit-a.** Eitt mál = ein eða fleiri commits með skýrum titli. Hver AI-keyrsla má vera sér commit.

## Yfirferðargátlisti

Áður en mál fer í stöðuna "yfirfarið":

- [ ] `ritstjorn.md` skráir skýra áherslu og afmörkun.
- [ ] Verkefnalisti í `ritstjorn.md` er allur krossaður eða með skýringu á því sem stendur eftir.
- [ ] Allar `[H###]` tilvitnanir í `README.md` málsins og `ai-greining/` vísa í heimildaskrá sem er raunverulega til í `heimildir/`.
- [ ] `/sannprofa <slug>` skilar STENST — engar AI-hallucinations.
- [ ] Hver heimild í `heimildir/` hefur fullt textaefni vistað (ekki bara slóð).
- [ ] Heimildir koma frá fleiri en einu sjónarhorni (þar sem það á við), og hagsmunatengingar eru skráðar í `ritstjorn.md`.
- [ ] Þú hefur sannprófað **hverja einustu tilvitnun** með því að opna heimildina.
- [ ] Model og dagsetning eru skráð í AI-skjölum.
- [ ] Dagsetningar í frontmatter heimildaskráa (sott, birt) eru réttar.

## Þegar mál þróast

Mál breytast. Lög taka gildi, nýjar skýrslur birtast, fólk skiptir um skoðun. Þegar það gerist:

- Bættu við nýrri heimild með nýju auðkenni — ekki yfirskrifa gamla.
- Bættu við leiðbeiningu í `ritstjorn.md` ("Endurskrifaðu samantekt í ljósi H012") og keyrðu AI aftur.
- Geymdu fyrri AI-keyrslur í git-sögu fremur en í aukaskrám — git man þetta.
- Færðu inn í `Saga`-kafla `ritstjorn.md` hvað breyttist og hvers vegna.

## Hvenær á að ekki birta

- Ef þú getur ekki sannprófað grundvallarheimild.
- Ef AI-úttak heldur áfram að bregðast leiðbeiningum þrátt fyrir endurteknar tilraunir — taktu málið út, lagfærðu prompt eða sniðmát, og reyndu aftur. Það á ekki að "redda" með handvirkri endurskrift.
- Ef málið er persónulegt og varðar nafngreinda einstaklinga sem eru ekki opinberir aðilar.

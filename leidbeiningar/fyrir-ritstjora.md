# Leiðbeiningar fyrir ritstjóra

Þú berð ábyrgð á því sem birtist í þessu repo. AI-ið er rithöfundurinn; þú ert ritstjórinn. Skipting verka:

| Hver gerir hvað | |
|---|---|
| **Manneskja** | Velur mál. Skrifar `ritstjorn.md` (áherslu, afmörkun, leiðbeiningar). Samþykkir heimildir sem AI leggur til. Yfirfer útkomu. |
| **AI** | Leitar að heimildum og leggur til. Sækir, vistar og lýsir samþykktum heimildum í `heimildir/H###-*.md`. Skrifar `README.md` málsins (samantekt). Skrifar greiningar í `ai-greining/`. |

`ritstjorn.md` er eina skjalið þar sem þín rödd birtist beint í málinu. Allt annað skrifar AI undir leiðsögn þeirrar raddar.

## Vinnuflæði fyrir nýtt mál

1. **Stofna mál** með `/nyttmal <slug> "<heiti>"`. Skipun afritar sniðmát úr `snidmat/`.

2. **Skrifa `ritstjorn.md`.** Þetta er **mikilvægasta skrefið** og kemur á undan heimildaöflun. Hér setur þú:
   - **Áherslu og afmörkun** — hvað á málið að fjalla um, hvað ekki
   - **Verkefnalista fyrir AI** — hvaða skjöl á að búa til, hvaða spurningum á að svara, hvaða köflum á að skipta greiningu í
   - **Leiðbeiningar fyrir heimildaöflun** — t.d. "leitaðu á íslenskum fréttasíðum", "passaðu að ná báðum sjónarmiðum", "ekki nota greinar eldri en 2020"
   - Allt sem þú vilt að AI taki tillit til

3. **Láta AI leita að heimildum.** Keyrðu `/rannsaka <slug>`. Þar sem `heimildir/` er tóm leggur AI fyrst til lista af kandídat-heimildum (með titli, slóð, tegund, sjónarhornsgiski og rökstuðningi), og bíður eftir samþykki þínu. Það segir líka frá leitarorðum sem það notaði — svo þú sjáir slagsíðu. Þú samþykkir, hafnar, eða bætir við.

4. **Bæta tilteknum heimildum við ef þörf er** með `/heimild <slug> <URL>` — t.d. ef þú átt PDF eða slóð sem AI fann ekki.

5. **Keyra AI aftur** með `/rannsaka <slug>` til að skrifa samantekt og greiningar út frá samþykktum heimildum.

6. **Sannprófa.** Keyrðu `/sannprofa <slug>` til að athuga tilvitnanir. Opnaðu líka nokkrar heimildir handvirkt og athugaðu að AI hafi ekki misskilið.

7. **Skrá athugasemdir í `ritstjorn.md`** og endurkeyra. Iterativt: ef niðurstaða er ekki nógu góð — eða heimildaval er einsleitt — þá bætirðu við leiðbeiningu ("rannsakaðu líka X"), krossar gamla úr, og keyrir AI aftur. Ekki breyta AI-útgáfunni handvirkt nema í smáleiðréttingum (innsláttarvillur).

8. **Commit-a.** Eitt mál = ein eða fleiri commits með skýrum titli. Hver AI-keyrsla má vera sér commit.

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

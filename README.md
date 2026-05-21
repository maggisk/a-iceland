# a-iceland

AI-stutt rannsóknar- og lausnamiðuð vinna um íslensk samfélagsmál sem eru í umræðunni.

## Hvað er þetta?

Opið safn af AI-greiningum og **AI-ráðleggingum** á samfélagsmálum á Íslandi. Markmiðið er ekki bara samantekt heldur að finna lausnir — AI fer yfir eins mikið af efni og mögulegt er, gagnar úr því sem mikilvægt er, og skilar **rökstuddri tillögu** að lausn. Skipting verka:

- **Manneskja** velur mál, skrifar `ritstjorn.md` (áherslu, afmörkun, leiðbeiningar, mat á heimildum), og yfirfer útkomu — sérstaklega ráðleggingar AI sem þarf að dæma um.
- **AI** leitar að heimildum, sækir og vistar þær (með archive ef linkur deyr), skrifar samantektir, greiningar, **og rökstudda ráðleggingu um besta lausn málsins** — allt undir leiðsögn `ritstjorn.md` og með vistuðu heimildirnar sem eina leyfilega gagnaheimild.

Þetta er meðvituð undantekning frá venjulegri AI-fræðasiðferði "ekki taka afstöðu". Ástæðan: nákvæmt þekkingar-yfirlit getur framkallað gagnlegri tillögur en almenn opinber umræða — en aðeins ef AI er agað um heimildir og er heiðarlegt um veikleika eigin tillögu.

`ritstjorn.md` er hluti hvers máls þar sem mannleg rödd setur ramma. Allt AI-úttak hefur strangar reglur um tilvitnanir og veikleika-yfirferð.

## Af hverju þessi skipting?

Trúverðugleiki AI-rannsókna og -ráðleggingar stendur og fellur með fjórum reglum:

1. **Heimildir geta verið uppspunnar.** Tungumálamódel búa stundum til tilvitnanir sem eru ekki til. Í þessu repo má AI **aðeins** vísa í heimildir sem eru raunverulega til í `malefni/<mál>/heimildir/` möppunni. Hver tilvitnun hefur auðkenni á borð við `[H001]` sem vísar í tilsvarandi skrá `heimildir/H001-...md`. Heimildaskrár innihalda fullt textaefni heimildarinnar (archive ef upprunaslóð deyr), tilvitnanir til notkunar, og AI-skrifaða hlutlæga greiningu á efninu. Engar utanaðkomandi tilvitnanir, engin "almenn þekking" — sérstaklega ekki í ráðleggingum.

2. **Heimildaval er ritstjórnarval — en yfirferðin er eftir á.** Verkflæðið er tveggja-skipana: `/rannsaka` safnar heimildum (idempotent, má keyra aftur til að bæta við), og `/greina` skrifar samantekt, greiningar **og ráðleggingu** út frá þeim. AI velur heimildir sjálf og vistar þær sem standast gæðakröfur. Ritstjórinn yfirfer eftir á: fjarlægir lélegar heimildir, skráir hagsmunatengingar í `ritstjorn.md`, og keyrir aftur ef þörf er á. Eina undantekningin: ef hagsmunatengd heimild lendir á því að vera lykilheimild, þá stöðvar AI og spyr áður en hún er vistuð.

3. **AI á að taka rökstudda afstöðu, ekki forðast hana.** Þetta er munur frá venjulegri AI-fræðisiðferði. AI á að synthese, dæma vægi heimilda, og leggja fram **tillögu að lausn** byggða á heimildum. Reglur fyrir ráðleggingu: (a) hver fullyrðing studd af heimild, (b) skýr forsendur um markmið (kostnaður, umhverfi, lífsgæði o.s.frv.), (c) **veikleika-listi þar sem AI gagnrýnir eigin tillögu**. Ráðleggingin er ekki dómur — hún er inntak sem manneskja vegur. En án afstöðu er repo-ið aðeins yfirlit; með afstöðu verður það lausnamiðað.

4. **AI fær skýrar leiðbeiningar, ekki opinn forsendulausan prompt.** `ritstjorn.md` segir AI hvað á að skrifa, hvaða spurningum á að svara, hvaða markmið á að nota fyrir ráðleggingu, og hvernig á að meðhöndla hverja heimild. Iterativt: ritstjóri uppfærir leiðbeiningar þegar úttak er ekki nógu gott, og keyrir AI aftur.

## Strúktúr

```
malefni/
  <mál>/
    README.md          # Samantekt málsins — AI-skrifuð, fyrsta skjalið sem lesandi sér
    ritstjorn.md       # Mannleg leiðsögn til AI — eina mannlega skjalið
    heimildir/         # Ein skrá per heimild: frontmatter + lýsing + tilvitnanir + greining + fullt efni
      H001-stutt-slug.md
      H002-stutt-slug.md
      ...
    ai-greining/       # AI-skrifaðar greiningar (ein skrá per sjónarhorn eða spurning)
snidmat/               # Sniðmát fyrir ný mál
leidbeiningar/         # Reglur fyrir AI og ritstjóra
.claude/commands/      # Slash commands fyrir Claude Code workflow
```

## Hvernig á að lesa þetta repo

Byrjaðu á `malefni/<mál>/README.md` — það er aðalskjalið. Uppbygging:
1. **TL;DR** efst (5–8 línur) — ef þú vilt stoppa hér, gerðu það.
2. **Núverandi staða** og **Saga** — samhengi.
3. **Hver heldur hverju fram** — landslag stjórnmála og hagsmunaaðila.
4. **Rök með og móti einstökum hugmyndum** — skipulagt eftir hugmyndum, ekki hliðum.
5. **Niðurstöður og tillögur gervigreindar** — rödd AI með rökstuddri afstöðu, sex svið, veikleika-listi. **Þetta er kjarnaframleiðsla repo-isins.**
6. **Lykilheimildir** og **hvað vantar**.

Ef þú vilt dýpri viðmiðun á tilteknu efni: skoðaðu `ai-greining/` (fræðilegan ramma, alþjóðlegan samanburð, lærdóma erlendis). Til að dæma um trúverðugleika: berðu saman við `heimildir/`. Til að skilja hvernig málið var afmarkað: lestu `ritstjorn.md`.

## Takmarkanir

- AI-greiningar **og ráðleggingar** geta haft slagsíðu sem er ekki augljós, jafnvel þegar heimildirnar eru réttar. Veikleika-listi í ráðleggingu er fyrsti staður til að skoða.
- Heimildaval er ekki tæmandi — það er háð því hver ritstjórinn er og hvað hann fann.
- AI-ráðlegging er ekki dómur — hún er rökstudd tillaga sem manneskja vegur á móti eigin reynslu og forsendum sem AI hefur ekki aðgang að.
- Þetta er ekki blaðamennska — engin frumheimildaöflun, engin viðtöl.
- Dagsetningar skipta máli: mál þróast, heimildir verða úreltar, ráðleggingar úreltast hraðar en heimildir.

## Að leggja til

Sjá [leidbeiningar/ad-leggja-til.md](leidbeiningar/ad-leggja-til.md).

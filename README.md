# a-iceland

AI-stutt rannsóknarvinna um íslensk samfélagsmál sem eru í umræðunni.

## Hvað er þetta?

Opið safn af greiningum á samfélagsmálum á Íslandi. Skipting verka er afdráttarlaus:

- **Manneskja** velur mál og skrifar `ritstjorn.md` (áherslu, afmörkun, leiðbeiningar, mat á heimildum). Ef AI yfirsést mikilvæg heimild, bætir manneskja við leiðbeiningu í `ritstjorn.md` — t.d. "rannsakaðu líka X" eða "bættu við heimild frá Y" — og keyrir aftur.
- **AI** leitar að heimildum, sækir og vistar þær (með archive ef linkur deyr), skrifar samantektir og greiningar — allt undir leiðsögn `ritstjorn.md` og með vistuðu heimildirnar sem eina leyfilega gagnaheimild.

`ritstjorn.md` er eini hluti hvers máls þar sem mannleg rödd birtist beint. Allt annað er AI-úttak með ströngum reglum um tilvitnanir.

## Af hverju þessi skipting?

Trúverðugleiki AI-rannsókna stendur og fellur með þrennu:

1. **Heimildir geta verið uppspunnar.** Tungumálamódel búa stundum til tilvitnanir sem eru ekki til. Í þessu repo má AI **aðeins** vísa í heimildir sem eru raunverulega til í `mal/<mál>/heimildir/` möppunni. Hver tilvitnun hefur auðkenni á borð við `[H001]` sem vísar í tilsvarandi skrá `heimildir/H001-...md`. Heimildaskrár innihalda fullt textaefni heimildarinnar (archive ef upprunaslóð deyr), tilvitnanir til notkunar, og AI-skrifaða hlutlæga greiningu á efninu. Engar utanaðkomandi tilvitnanir, engin "almenn þekking".
2. **Heimildaval er ritstjórnarval.** AI leitar að heimildum, en manneskja samþykkir hverja viðbót áður en hún er vistuð. Mat á því hverjar séu traustar eða hagsmunatengdar er skráð í `ritstjorn.md`. AI verður líka að segja frá leitarorðum sem það notaði og heimildum sem það sleppti — svo ritstjórinn sjái hvar slagsíða AI gæti hafa skert valið.
3. **AI fær skýrar leiðbeiningar, ekki opinn forsendulausan prompt.** `ritstjorn.md` segir AI hvað á að skrifa, hvaða spurningum á að svara, og hvernig á að meðhöndla hverja heimild. Iterativt: ritstjóri uppfærir leiðbeiningar þegar úttak er ekki nógu gott, og keyrir AI aftur.

## Strúktúr

```
mal/
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

Byrjaðu á `mal/<mál>/README.md` — það er AI-skrifuð samantekt með tilvitnunum. Ef þú vilt dýpra: lestu `ai-greining/` og berðu saman við `heimildir/`. Ef þú vilt sjá hvernig málið var afmarkað og hvaða leiðbeiningar AI fékk: lestu `ritstjorn.md` — þar talar manneskjan beint.

## Takmarkanir

- AI-greiningar geta haft slagsíðu sem er ekki augljós, jafnvel þegar heimildirnar eru réttar.
- Heimildaval er ekki tæmandi — það er háð því hver ritstjórinn er og hvað hann fann.
- Þetta er ekki blaðamennska — engin frumheimildaöflun, engin viðtöl.
- Dagsetningar skipta máli: mál þróast, heimildir verða úreltar.

## Að leggja til

Sjá [leidbeiningar/ad-leggja-til.md](leidbeiningar/ad-leggja-til.md).

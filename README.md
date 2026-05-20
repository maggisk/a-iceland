# aisland

AI-stutt rannsóknarvinna um íslensk samfélagsmál sem eru í umræðunni.

## Hvað er þetta?

Opið safn af greiningum á samfélagsmálum á Íslandi. Hvert mál inniheldur:

- **Heimildir** — hráar, sannprófaðar heimildir (greinar, skýrslur, tölfræði, lög)
- **AI-greining** — texti skrifaður af tungumálamódeli út frá þeim heimildum
- **Ritstjórn** — nótur, leiðréttingar og athugasemdir mannlegs ritstjóra

## Hvers vegna þessi aðgreining?

Trúverðugleiki AI-rannsókna stendur og fellur með þrennu:

1. **Heimildir geta verið uppspunnar.** Tungumálamódel búa stundum til tilvitnanir sem eru ekki til. Í þessu repo má AI **aðeins** vísa í heimildir sem eru raunverulega til í `mal/<mál>/heimildir/` möppunni. Engar utanaðkomandi tilvitnanir.
2. **AI tekur ritstjórnarval.** Hvað er dregið fram, hvað er sleppt, hvernig orðað — allt er val. Þess vegna er prompt-ið sem var notað geymt með hverri greiningu, og mannlegur ritstjóri merkir hvar hann er sammála eða ósammála.
3. **Heimildaval er líka ritstjórnarval.** Ef aðeins heimildir frá einni hlið eru notaðar, þá er niðurstaðan fyrirfram ákveðin. Hvert mál skal hafa heimildir frá fleiri en einu sjónarhorni þegar það á við.

## Strúktúr

```
mal/
  <mál>/
    heimildir/         # Hráar heimildir (PDF, skjáskot, slóðir, útdrættir)
    heimildir.md       # Skráning yfir heimildir með lýsingu og dagsetningu
    ai-greining/       # AI-skrifuð greining (með model, dagsetningu, prompti)
    ritstjorn.md       # Mannlegar nótur, leiðréttingar, ósammæli
    samantekt.md       # Stutt samantekt fyrir lesanda (skrifuð af manni)
snidmat/               # Sniðmát fyrir ný mál
leidbeiningar/         # Vinnureglur fyrir AI og ritstjóra
```

## Hvernig á að lesa þetta repo

Byrjaðu á `samantekt.md` í hverju máli. Það er stutt yfirlit skrifað af manneskju. Ef þú vilt dýpra: lestu `ai-greining/` og berðu saman við `heimildir/`. `ritstjorn.md` segir hvar mannlegur ritstjóri er ekki sammála AI-greiningunni.

## Takmarkanir

- AI-greiningar geta haft slagsíðu sem er ekki augljós.
- Heimildaval er ekki tæmandi.
- Þetta er ekki blaðamennska — engin frumheimildaöflun, engin viðtöl.
- Dagsetningar skipta máli: mál þróast, heimildir verða úreltar.

## Að leggja til

Sjá [leidbeiningar/ad-leggja-til.md](leidbeiningar/ad-leggja-til.md).

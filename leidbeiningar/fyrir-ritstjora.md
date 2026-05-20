# Leiðbeiningar fyrir ritstjóra

Þú berð ábyrgð á því sem birtist í þessu repo. AI-ið er verkfæri, ekki höfundur.

## Vinnuflæði fyrir nýtt mál

1. **Stofna möppu** í `mal/<stutt-kebab-heiti>/` (t.d. `mal/utlendingafrumvarp-2025/`).
2. **Afrita sniðmát** úr `snidmat/` inn í nýju möppuna.
3. **Safna heimildum.** Hlaða niður PDF, taka skjáskot af greinum, vista útdrætti. Skrá hverja heimild í `heimildir.md` með auðkenni.
4. **Skrifa `samantekt.md` sjálfur.** Þetta er andlit málsins fyrir lesanda — það á að vera þitt.
5. **Keyra AI-greiningu** með heimildirnar sem inntak. Geyma prompt-ið og útgáfu módelsins.
6. **Sannprófa hverja tilvitnun.** Opna heimildina, finna staðinn, staðfesta að módelið hafi ekki misskilið.
7. **Skrá ósammæli í `ritstjorn.md`.** Ef þú ert sammála öllu, skrifaðu samt eitthvað — "ég er sammála en hefði sjálfur lagt áherslu á X" er gagnlegt.
8. **Commit-a.** Eitt mál = ein grein af commits. Aldrei breyta AI-greiningu án þess að uppfæra `ritstjorn.md`.

## Yfirferðargátlisti

Áður en mál fer í stöðuna "lokið yfirferð":

- [ ] Allar tilvitnanir í AI-greiningu vísa í heimild sem er til.
- [ ] Hver heimild í `heimildir.md` er raunverulega til í `heimildir/` möppunni eða með virkri slóð.
- [ ] Heimildir koma frá fleiri en einu sjónarhorni (þar sem það á við).
- [ ] `samantekt.md` er skrifuð af manneskju, ekki límd úr AI-úttaki.
- [ ] `ritstjorn.md` skráir a.m.k. eina athugasemd, eða segir skýrt að ekkert hafi þurft að breyta.
- [ ] Prompt-ið er geymt í AI-greiningunni.
- [ ] Dagsetningar eru réttar (sótt, birt, yfirfarið).

## Þegar mál þróast

Mál breytast. Lög taka gildi, nýjar skýrslur birtast, fólk skiptir um skoðun. Þegar það gerist:

- Bættu við nýrri heimild með nýju auðkenni — ekki yfirskrifa gamla.
- Keyrðu nýja AI-greiningu í nýrri skrá (t.d. `ai-greining/uppfaersla-2026-06.md`), ekki yfirskrifa gömlu.
- Uppfærðu `samantekt.md` og skráðu breytinguna neðst.

Saga málsins er hluti af gildi þessa repo.

## Hvenær á að ekki birta

- Ef þú getur ekki sannprófað grundvallarheimild.
- Ef AI-greiningin er svo lituð að hún þarfnast endurskrifunar — þá er það ekki AI-greining lengur, og hún á ekki heima í `ai-greining/`.
- Ef málið er persónulegt og varðar nafngreinda einstaklinga sem eru ekki opinberir aðilar.

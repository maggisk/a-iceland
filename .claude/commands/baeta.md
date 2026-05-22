---
description: Wrapper-skipun sem keyrir /baeta-heimildir + /baeta-tilraunir + /baeta-utfyrir-boxid í röð. Notaðu þegar þú vilt alhliða "uppfærsla" á máli í einni keyrslu.
argument-hint: <slug>
---

Notandi vill keyra alla `/baeta`-fjölskylduna á mál `$1`.

> **Hugarfar:** Þetta er **wrapper**. Þú keyrir þrjár aðskildar skipanir í röð. Hver hefur sín eigin reglur og output-skrá. Ekki blanda þeim saman — virða strangari afmörkun hverrar.

> **Röð sem skiptir máli:**
> 1. `/baeta-utfyrir-boxid` fyrst — gæti opinberað fræðigreinar sem benda á nýjar leitarvinkilar
> 2. `/baeta-heimildir` næst — getur notað nýju vinklana sem viðbót við snjóbolta-leit
> 3. `/baeta-tilraunir` síðast — vinnur með fyllsta heimildasetti og uppfærðri þekkingu á ramma

> **Stöðunarregla:** Ef einhver sub-skipun mistekst í Skref 0 (lágmarks-massa, vantar README, o.s.frv.), stöðva alla wrapper-keyrsluna og tilkynna ritstjóra hvaða undirskipun mistókst og af hverju. Ekki halda áfram með næstu sub-skipun ef sú á undan mistókst.

---

## Verklag

### Fasi 1 — Pre-flight (öll wrapper-keyrslan)

1. **Staðfestu slug:** `malefni/$1/` skal vera til.
2. **Athugaðu nauðsynlegar skrár:**
   - `malefni/$1/ritstjorn.md`
   - `malefni/$1/README.md` (krafa fyrir /baeta-tilraunir og /baeta-utfyrir-boxid)
   - `heimildir/` með a.m.k. **5 heimildum** (krafa fyrir /baeta-utfyrir-boxid og /baeta-tilraunir; /baeta-heimildir krefst 3)
   - `snidmat/heimild.md`, `leidbeiningar/fyrir-ai.md`, `greining/README.md`
3. **Skráðu wrapper-keyrslu:** birtu efst: model, dagsetning, slug `$1`, fjölda núverandi heimilda, og hvort hver output-skrá þeirra þriggja sé þegar til (sýnir hvort er endurkeyrsla eða fyrsta).

Ef einhver krafa bregst — **STÖÐVAÐU** og bentu ritstjóra á hvað þarf að koma fyrst (`/rannsaka` eða `/greina`).

### Fasi 2 — Keyra /baeta-utfyrir-boxid

Lestu `.claude/commands/baeta-utfyrir-boxid.md` og framkvæmdu Skref 0–5 fyrir slug `$1`. Skilaðu **stuttri lokaskýrslu** úr 5.1, 5.4 (ekki allan 5-kaflann — wrapperinn skal halda samanlagðri skýrslu þéttri).

### Fasi 3 — Keyra /baeta-heimildir

Lestu `.claude/commands/baeta-heimildir.md` og framkvæmdu Skref 0–6 fyrir slug `$1`. **Mikilvægt:** ef Fasi 2 skilaði HÁR-tillögum sem nefna konkret-fræðigreinar eða höfunda, þá má /baeta-heimildir í Skref 2 (útdráttur) telja þá sem viðbótar-leitarvinkilar. Skilaðu **stuttri lokaskýrslu** úr 6.1, 6.5 og 6.6.

### Fasi 4 — Keyra /baeta-tilraunir

Lestu `.claude/commands/baeta-tilraunir.md` og framkvæmdu Skref 0–5 fyrir slug `$1`. **Mikilvægt:** nýju heimildirnar úr Fasa 3 skulu telja með í heimildalestri. Skilaðu **stuttri lokaskýrslu** úr 5.1, 5.4.

### Fasi 5 — Samanlögð wrapper-skýrsla

Þrjár-kafla samantekt:

```markdown
# /baeta $1 — alhliða uppfærsla (YYYY-MM-DD)

## Yfirlit

- /baeta-utfyrir-boxid: X nýjar tillögur (sjá ai-greining/utfyrir-boxid.md)
- /baeta-heimildir: X nýjar heimildir, Y gap eftir (sjá heimildir/)
- /baeta-tilraunir: X nýjar tillögur (sjá ai-greining/tilraunir-hugmyndir.md)

## /baeta-utfyrir-boxid samandregið
[Lykilatriði úr 5.1 og 5.4]

## /baeta-heimildir samandregið
[Lykilatriði úr 6.1, 6.5, 6.6]

## /baeta-tilraunir samandregið
[Lykilatriði úr 5.1, 5.4]

## Heildar-næsta-skref ráðlegging

[Lesa þrjár skýrslur saman. Hver er forgangs-action? Yfirleitt:
- Ef HÁR-tillögur úr utfyrir-boxid: ritstjóri uppfærir ritstjorn.md eða keyrir /baeta-heimildir aftur fyrir nýjar leiðar
- Ef HÁR-gap eftir í heimildum: keyra /baeta-heimildir aftur eða /rannsaka
- Ef HÁR-tilraunir tilbúnar: smíða Python-tilraun í greining/src/$1/]
```

---

## Reglur sem aldrei má brjóta

1. **Röðin skiptir máli** — utfyrir-boxid → heimildir → tilraunir. Snúa ekki við.
2. **Stöðva ef fasi mistekst** — ekki halda áfram með næstu sub-skipun.
3. **Lesa hverja sub-skipunar-skrá orðrétt áður en þú framkvæmir hana** — ekki giska á hvað hún segir. Sub-skipanir hafa eigin uppfærslu-sögu og þú þarft að fylgja núverandi útgáfu.
4. **Virða allar reglur úr sub-skipunum** — wrapperinn afnemir engar þeirra. Sérstaklega: stöðunarregla úr /baeta-heimildir um hagsmunatengda lykilheimild gildir á sama hátt í wrapper.
5. **Skipta ekki út útgáfu sub-skipunar með eigin túlkun** — ef /baeta-tilraunir-skráin segir eitthvað sérstakt, fylgdu því.
6. **Engin emoji í final report.**

---

## Bilanaham

- **"Sleppa lestri sub-skráar"** — að keyra sub-skipun úr minni án að opna núverandi útgáfu skráarinnar. Sub-skipunar-uppfærslur eru tíðar; alltaf lesa fyrst.
- **"Blanda saman output-skrám"** — heimildir, tilraunir-hugmyndir, og utfyrir-boxid eru þrjár sjálfstæðar útkomu-skrár sem ekki má blanda.
- **"Sleppa Fasi 1 pre-flight"** — wrapperinn skal stöðva snemma ef forsendur eru ekki uppfylltar, áður en sub-skipun er hafin.
- **"Halda áfram eftir misheppnaðan fasa"** — ef Fasi 2 stöðvast, ekki keyra Fasi 3 og 4.

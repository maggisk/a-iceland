# greining/ — kvantitatív tilraunir

Þessi mappa hýsir Python-greiningar sem AI keyrir ofan á heimildir í málefnum. Tilgangurinn er að færa repo-ið úr "texta-samansetningu" yfir í "raunverulegar tilraunir með gögn".

## Hvenær á að nota þetta

Þegar fullyrðing í heimild krefst kvantitatífrar prófunar — t.d.:

- **Sensitivity analysis** á cost-benefit greiningu (hvað gerist ef forsendur breytast?)
- **Senario-greining** ("ef 5% bílferða færast yfir á hjól, hvað gerist með CO2?")
- **Cross-field líkön** beitt á íslensk gögn (diffusion-líkan fyrir modal-shift, network-flæði, o.s.frv.)
- **Verifýun** á tölum heimilda (samanburður við opin gögn Hagstofu)

Ef málefnið er **eingöngu eigindlegt** (qualitative) — engin þörf á tilraun. Sumir málaflokkar henta þessu betur en aðrir.

## Uppbygging

```
greining/
  pyproject.toml      # uv-managed dependencies, læst í uv.lock
  src/
    <slug>/           # málefnis-háðar tilraunir
      <tilraun>.py
  notebooks/          # exploratory analysis (ekki commitað í generellt)
  data/
    raw/              # niðurhalið efni
    processed/        # hreinsað
  outputs/
    <slug>/
      *.png, *.csv    # myndir og töflur, tengt frá README málefnisins
```

## Setja upp

```bash
uv sync --directory greining
```

Þetta býr til `.venv` innan `greining/` og setur upp læstar dependencies.

## Keyra tilraun

```bash
cd greining
uv run python src/<slug>/<tilraun>.py
```

eða

```bash
uv run --directory greining python src/<slug>/<tilraun>.py
```

## Reglur fyrir tilraunir

Þetta er **agandi viðbót við repo-prinsipp**, ekki léttvæg tilraun-skrifa-eftir-vilja.

1. **Hver tilraun skal hafa skýra tilgátu efst.** Hvað ertu að prófa? Hvaða forsenda fer í kallið?
2. **Forsendur skulu vera explicit.** Ekki "magic numbers" — heldur skýr breyta með athugasemd.
3. **Heimildir fyrir gögnum.** Ef tilraun notar tölu úr H001 (samgöngusáttmáli), þá skal það koma fram í athugasemd.
4. **Sensitivity analysis er skylda.** Ekki bara "niðurstaða er X" heldur "niðurstaða er X við forsendur Y; breytist í X' ef forsenda Y' o.s.frv."
5. **Output skal vera reproducible.** Tilraun má aldrei nota randomness án seed. Niðurstöður (PNG/CSV) skulu vera birtar í `outputs/<slug>/` og hægt að endurframleiða með einni skipun.
6. **Tengja við README málefnisins.** Tilraun sem ekki er nefnd í README er gleymd. Tengja gegnum smellanlegan tengil.

## Áhætta sem þarf að halda í huga

- **AI-kóði hefur villur.** Verifýa með að keyra og athuga niðurstöðu á móti heilbrigðu skyni.
- **Garbage in, garbage out.** Bad data → bad niðurstaða, sama hve flott líkanið er.
- **Ekki láta líkans-niðurstöður yfirskyggja heimildir.** "Líkanið mitt segir X" er ekki sama og "heimildir segja X". Aðgreina skýrt.

## Dependencies

Núverandi (sjá `pyproject.toml`):
- `pandas`, `numpy` — gögn
- `matplotlib` — myndir
- `scipy` — tölfræði
- `requests` — niðurhal

Bæti við eftir þörfum. `uv add <pakki>` og `uv sync`.

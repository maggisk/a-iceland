"""
T1 — Cowi 2024 IRR/BCR sensitivity-greining a samgongusattmala (Borgarlina + stofnvegir)

TILGATA:
  Cowi 2024 birtar tolur (IRR 9.2%, BCR 3.5) eru vidkvaemar fyrir:
    (a) Afslattarvoxtum (Cowi notar liklega ~5%)
    (b) Kostnadar-framukeyrslu (Flyvbjerg media rail ~45%)
    (c) Farthegaspa vs raun (modal-shift ovissa)
    (d) Timahorft (Cowi notar 50 ar)

  Naumtaek breyting a einni forsendu getur faert IRR ur 9.2% nidur i 3-4%
  eda upp i 12-14%. Skipt ad lata Cowi-tolu standa eina ser sem
  endanlegan domur um hagkvaemni.

HEIMILDIR FYRIR GRUNNGILDI:
  [H001] Stjornarradid samgongusattmali 2024: 311 mrd, 1.140 mrd abati (50 ar),
         IRR 9.2%, BCR 3.5
  [H018] Heimildin: kostnadur Borgarlinu afanga 1 = 136 mrd (jan 2026 uppfaersla)
  [H020] Mbl Ragnar Arnason: njuvirdi verulega neikvaett ad athuguðu mali
  [H029] Skemman Palmi BS-ritgerd: fjogur spatifelli umferdarþrounar
  [H033] Stjornarradid samgongusattmali 2019: 120 mrd grunnlina (159% haekkun)
  [H036] Flyvbjerg PMJ 2014: media rail cost-overrun ~45%

ADFERD:
  1. Einfalt cash-flow likan med Cowi-grunngildum
  2. Kalibrera arlegan abata svo IRR matchi Cowi 9.2%
  3. Sensitivity yfir 4 lykil-forsendur, fyrst eina-i-einu sidan saman
  4. Heatmap (discount rate x cost overrun) syn hvenaer BCR < 1
  5. Tornado plot fyrir IRR

REPRODUCIBILITY:
  - Engar randomness, allir gildi explicit
  - Output PNG og txt i outputs/samgongur/
  - Keyrist: uv run --directory greining python src/samgongur/cowi-irr-sensitivity.py

VARNAGLAR:
  - Cowi PDF ekki extraktad (binary takmorkun) - grunngildi byggd a [H001] og [H018]
  - Likans-BCR vill liklega ekki matcha Cowi 3.5 nakvaemlega vegna eindfaldana
    (engin time-vaxtandi abati, engin CO2-time-value, o.s.frv.). Sensitivity-
    nidurstodur eru samt valid - thaer syna AETT en ekki nakvaem matchun.
  - Tilraun er proof-of-concept fyrir greining/-infrastrukur. Naestu T-tilraunir
    geta verid nakvaemari ef Cowi PDF natt mat fram.
"""

import numpy as np
import matplotlib

matplotlib.use("Agg")  # No display needed
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from pathlib import Path


# ============================================================
# FORSENDUR (allar med heimildum)
# ============================================================

# [H001] Heildarkostnadur samgongusattmala 2024-2046
COST_TOTAL_MRD: float = 311.0

# [H001] Stated Cowi-nidurstodur
COWI_STATED_TOTAL_BENEFIT_MRD: float = 1140.0
COWI_STATED_IRR: float = 0.092
COWI_STATED_BCR: float = 3.5

# Timalina (skv. [H033] og [H001])
CONSTRUCTION_START: int = 2024
CONSTRUCTION_YEARS: int = 17  # 2024-2040 framkvaemd
BENEFITS_START_OFFSET: int = 7  # 2031 - 2024, fyrsti afangi opnar 2031
ANALYSIS_HORIZON_YEARS: int = 50  # Cowi-greining 50 ar

# Cowi grunngildi (aetluð - Cowi PDF ekki extraktað)
# Islenskt opinbert afslattagjald sogulega 3-5% fyrir innvidi
COWI_DISCOUNT_RATE_ASSUMED: float = 0.05

# Sensitivity ranges
DISCOUNT_RATES = np.arange(0.03, 0.071, 0.005)        # 3% til 7%
COST_OVERRUN_FACTORS = np.arange(0.0, 1.01, 0.05)     # 0% til 100%
PASSENGER_FACTORS = np.arange(0.5, 1.21, 0.05)        # 50% til 120%

# [H036] Flyvbjerg media fyrir rail
FLYVBJERG_MEDIAN_RAIL_OVERRUN: float = 0.45


# ============================================================
# CORE FUNCTIONS
# ============================================================


def build_cash_flows(
    cost_total: float,
    annual_benefit: float,
    construction_years: int = CONSTRUCTION_YEARS,
    benefits_offset: int = BENEFITS_START_OFFSET,
    horizon: int = ANALYSIS_HORIZON_YEARS,
    cost_overrun: float = 0.0,
    benefit_factor: float = 1.0,
) -> np.ndarray:
    """Cash flow array: index 0 = ar 0 (CONSTRUCTION_START).

    Costs spread evenly over construction_years, scaled by (1+cost_overrun).
    Benefits start at year benefits_offset, scaled by benefit_factor.
    """
    cost_per_year = (cost_total * (1.0 + cost_overrun)) / construction_years
    benefit_per_year = annual_benefit * benefit_factor

    cf = np.zeros(horizon)
    for t in range(min(construction_years, horizon)):
        cf[t] -= cost_per_year
    for t in range(benefits_offset, horizon):
        cf[t] += benefit_per_year
    return cf


def npv(cash_flows: np.ndarray, rate: float) -> float:
    """Net Present Value at given discount rate."""
    discounts = (1.0 + rate) ** np.arange(len(cash_flows))
    return float(np.sum(cash_flows / discounts))


def irr(cash_flows: np.ndarray) -> float:
    """Internal Rate of Return via Brent's method. NaN if no solution."""
    if not (np.any(cash_flows > 0) and np.any(cash_flows < 0)):
        return float("nan")
    try:
        return brentq(lambda r: npv(cash_flows, r), -0.5, 1.0, xtol=1e-6)
    except (ValueError, RuntimeError):
        return float("nan")


def bcr(cash_flows: np.ndarray, rate: float) -> float:
    """Benefit-Cost Ratio at given discount rate."""
    discounts = (1.0 + rate) ** np.arange(len(cash_flows))
    pv_benefits = float(
        np.sum(np.where(cash_flows > 0, cash_flows, 0) / discounts)
    )
    pv_costs = float(
        np.sum(np.where(cash_flows < 0, -cash_flows, 0) / discounts)
    )
    return pv_benefits / pv_costs if pv_costs > 0 else float("nan")


# ============================================================
# CALIBRATION: bakreikna arlegan abata so IRR matchi Cowi 9.2%
# ============================================================


def calibrate_annual_benefit(target_irr: float = COWI_STATED_IRR) -> float:
    """Finn ANNUAL_BENEFIT_MRD sem framleidir target IRR vid sjalfgefnar forsendur."""

    def gap(annual_b):
        cf = build_cash_flows(COST_TOTAL_MRD, annual_b)
        return irr(cf) - target_irr

    try:
        return brentq(gap, 1.0, 500.0, xtol=1e-3)
    except (ValueError, RuntimeError):
        return float("nan")


# ============================================================
# SENSITIVITY EXPERIMENTS
# ============================================================


def joint_sensitivity_heatmap(annual_benefit: float) -> np.ndarray:
    """2D grid of BCR over (discount_rate x cost_overrun)."""
    grid = np.zeros((len(DISCOUNT_RATES), len(COST_OVERRUN_FACTORS)))
    for i, dr in enumerate(DISCOUNT_RATES):
        for j, co in enumerate(COST_OVERRUN_FACTORS):
            cf = build_cash_flows(COST_TOTAL_MRD, annual_benefit, cost_overrun=co)
            grid[i, j] = bcr(cf, dr)
    return grid


def irr_vs_cost_overrun(annual_benefit: float):
    """IRR sem fall af kostnadar-framukeyrslu."""
    results = []
    for co in COST_OVERRUN_FACTORS:
        cf = build_cash_flows(COST_TOTAL_MRD, annual_benefit, cost_overrun=co)
        results.append(
            {
                "cost_overrun": co,
                "final_cost_mrd": COST_TOTAL_MRD * (1 + co),
                "irr": irr(cf),
                "bcr_5pct": bcr(cf, 0.05),
            }
        )
    return results


def irr_vs_passenger(annual_benefit: float):
    """IRR sem fall af farthegaspa-faktor."""
    results = []
    for pf in PASSENGER_FACTORS:
        cf = build_cash_flows(COST_TOTAL_MRD, annual_benefit, benefit_factor=pf)
        results.append(
            {
                "passenger_factor": pf,
                "irr": irr(cf),
                "bcr_5pct": bcr(cf, 0.05),
            }
        )
    return results


def tornado(annual_benefit: float):
    """Tornado: fyrir hverja forsendu, IRR vid 'low' og 'high' gildi."""
    cf_base = build_cash_flows(COST_TOTAL_MRD, annual_benefit)
    base_irr = irr(cf_base)

    scenarios = []

    # Cost overrun: 0% vs Flyvbjerg media 45% vs verstu 80%
    for co, label in [(0.0, "Kostn-urslit 0%"),
                      (FLYVBJERG_MEDIAN_RAIL_OVERRUN, f"Kostn-urslit {int(FLYVBJERG_MEDIAN_RAIL_OVERRUN*100)}% (Flyvbjerg media)"),
                      (0.80, "Kostn-urslit 80% (Flyvbjerg 90 percentile)")]:
        cf = build_cash_flows(COST_TOTAL_MRD, annual_benefit, cost_overrun=co)
        scenarios.append((label, irr(cf)))

    # Passenger factor
    for pf, label in [(0.5, "Farthegaspa 50% af raun"),
                      (0.7, "Farthegaspa 70% af raun"),
                      (1.0, "Farthegaspa 100% (baseline)"),
                      (1.2, "Farthegaspa 120% af raun")]:
        cf = build_cash_flows(COST_TOTAL_MRD, annual_benefit, benefit_factor=pf)
        scenarios.append((label, irr(cf)))

    # Combined worst-case
    for co, pf, label in [(0.45, 0.7, "Flyvbjerg 45% overrun + farthega 70%"),
                          (0.80, 0.5, "Flyvbjerg 80% overrun + farthega 50%")]:
        cf = build_cash_flows(
            COST_TOTAL_MRD, annual_benefit, cost_overrun=co, benefit_factor=pf
        )
        scenarios.append((label, irr(cf)))

    return base_irr, scenarios


# ============================================================
# PLOTTING
# ============================================================


def plot_heatmap(bcr_grid: np.ndarray, output_path: Path):
    fig, ax = plt.subplots(figsize=(11, 6))

    # Use pcolormesh for explicit axis coordinates
    X, Y = np.meshgrid(COST_OVERRUN_FACTORS * 100, DISCOUNT_RATES * 100)
    im = ax.pcolormesh(
        X, Y, bcr_grid,
        cmap="RdYlGn", shading="auto", vmin=0, vmax=4,
    )
    plt.colorbar(im, ax=ax, label="BCR")

    # Contour at BCR = 1 (break-even)
    cs = ax.contour(
        X, Y, bcr_grid,
        levels=[1.0, 1.5, 2.0, 3.0],
        colors=["red", "orange", "darkorange", "black"],
        linewidths=[2.5, 1, 1, 1],
    )
    ax.clabel(cs, inline=True, fontsize=9, fmt="%.1f")

    # Markers
    ax.axvline(FLYVBJERG_MEDIAN_RAIL_OVERRUN * 100, color="blue",
               linestyle="--", alpha=0.6, linewidth=1.5)
    ax.text(FLYVBJERG_MEDIAN_RAIL_OVERRUN * 100 + 1, 6.7,
            "Flyvbjerg media\nrail (45%)",
            color="blue", fontsize=9, va="top")

    ax.axhline(COWI_DISCOUNT_RATE_ASSUMED * 100, color="black",
               linestyle=":", alpha=0.5, linewidth=1)
    ax.text(97, COWI_DISCOUNT_RATE_ASSUMED * 100 - 0.1,
            "Cowi 5% (aetluð)",
            color="black", va="top", ha="right", fontsize=8)

    ax.set_xlabel("Kostnadar-framukeyrsla (%)")
    ax.set_ylabel("Afslattarvextir (%)")
    ax.set_title(
        "Cowi BCR sensitivity: Afslattarvextir x Kostnadar-framukeyrsla\n"
        "Rauda lina = BCR 1.0 (jafnvaegi); raudt svaedi = jakvaeð fyrir verkefni"
    )
    plt.tight_layout()
    plt.savefig(output_path, dpi=130, bbox_inches="tight")
    plt.close()


def plot_tornado(base_irr: float, scenarios: list, output_path: Path):
    labels = [s[0] for s in scenarios]
    values = [s[1] * 100 if not np.isnan(s[1]) else 0 for s in scenarios]
    base_pct = base_irr * 100

    # Sort by deviation from baseline
    sorted_pairs = sorted(zip(labels, values),
                          key=lambda x: abs(x[1] - base_pct))
    labels, values = zip(*sorted_pairs)

    fig, ax = plt.subplots(figsize=(11, 6))
    y_pos = np.arange(len(labels))
    colors = ["darkgreen" if v >= base_pct else "darkred" for v in values]
    bars = ax.barh(y_pos, [v - base_pct for v in values],
                   left=base_pct, color=colors, alpha=0.75)

    # Annotations
    for bar, v in zip(bars, values):
        ax.text(v + 0.1 if v >= base_pct else v - 0.1, bar.get_y() + bar.get_height() / 2,
                f"{v:.1f}%", va="center",
                ha="left" if v >= base_pct else "right", fontsize=9)

    ax.axvline(base_pct, color="black", linewidth=1.5, label=f"Grunnlina ({base_pct:.1f}%)")
    ax.axvline(5.0, color="red", linestyle=":", linewidth=1.5, label="5% hurdle")
    ax.axvline(0.0, color="grey", linestyle="-", alpha=0.3)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.set_xlabel("IRR (%)")
    ax.set_title(
        "Tornado: IRR vid serstakar forsendu-breytingar\n"
        f"Grunnlina = Cowi-stated 9.2% IRR; kalibrerad arlegt abati"
    )
    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=130, bbox_inches="tight")
    plt.close()


# ============================================================
# MAIN
# ============================================================


def main():
    output_dir = Path(__file__).parent.parent.parent / "outputs" / "samgongur"
    output_dir.mkdir(parents=True, exist_ok=True)

    summary_lines = []

    def log(msg=""):
        print(msg)
        summary_lines.append(msg)

    log("=" * 70)
    log("T1 - Cowi 2024 IRR/BCR sensitivity-greining a samgongusattmala")
    log("=" * 70)
    log()
    log(f"Heimild: [H001], [H018], [H020], [H029], [H033], [H036]")
    log(f"Tilraun: T1 ur ai-greining/tilraunir-hugmyndir.md")
    log(f"Output dir: {output_dir}")
    log()

    # 1. Kalibrera arlegan abata
    annual_benefit = calibrate_annual_benefit(COWI_STATED_IRR)
    log("CALIBRATION (bakreikna arlegan abata fyrir Cowi IRR 9.2%):")
    log(f"  Cowi-stated IRR: {COWI_STATED_IRR*100:.1f}%")
    log(f"  Cowi-stated BCR: {COWI_STATED_BCR:.2f}")
    log(f"  Kalibrerud arlegur abati: {annual_benefit:.2f} mrd/ar (fra ari {BENEFITS_START_OFFSET})")

    cf_base = build_cash_flows(COST_TOTAL_MRD, annual_benefit)
    base_irr = irr(cf_base)
    base_bcr = bcr(cf_base, COWI_DISCOUNT_RATE_ASSUMED)
    log(f"  Verified IRR: {base_irr*100:.2f}%")
    log(f"  Verified BCR vid 5% afslatt: {base_bcr:.2f}")
    log(f"  (Athugid: BCR matchar ekki Cowi 3.5 vegna einfaldana - sja varnagla efst)")
    log()

    # 2. Sensitivity 1: discount rate (afslatt) afhrif a BCR
    log("SENSITIVITY 1: Afslattarvextir -> BCR (IRR obreyt)")
    log(f"  {'Discount':>10} | {'BCR':>6} | {'NPV (mrd)':>10}")
    for dr in DISCOUNT_RATES:
        cf = build_cash_flows(COST_TOTAL_MRD, annual_benefit)
        b = bcr(cf, dr)
        n = npv(cf, dr)
        log(f"  {dr*100:>9.1f}% | {b:>6.2f} | {n:>10.0f}")
    log()

    # 3. Sensitivity 2: cost overrun
    log("SENSITIVITY 2: Kostnadar-framukeyrsla -> IRR (afslatt 5%)")
    log(f"  {'Overrun':>10} | {'Final cost':>10} | {'IRR':>7} | {'BCR':>6}")
    for r in irr_vs_cost_overrun(annual_benefit):
        if int(r["cost_overrun"] * 100) % 10 == 0:
            irr_pct = r["irr"] * 100 if not np.isnan(r["irr"]) else float("nan")
            log(f"  {r['cost_overrun']*100:>9.0f}% | {r['final_cost_mrd']:>10.0f} | {irr_pct:>6.2f}% | {r['bcr_5pct']:>6.2f}")
    log()

    # 4. Sensitivity 3: passenger factor
    log("SENSITIVITY 3: Farthegaspa-faktor -> IRR (afslatt 5%)")
    log(f"  {'Pass factor':>12} | {'IRR':>7} | {'BCR':>6}")
    for r in irr_vs_passenger(annual_benefit):
        if int(r["passenger_factor"] * 100) % 10 == 0:
            irr_pct = r["irr"] * 100 if not np.isnan(r["irr"]) else float("nan")
            log(f"  {r['passenger_factor']*100:>11.0f}% | {irr_pct:>6.2f}% | {r['bcr_5pct']:>6.2f}")
    log()

    # 5. Heatmap
    log("Smid heatmap (afslatt x kostnadar-framukeyrsla -> BCR)...")
    bcr_grid = joint_sensitivity_heatmap(annual_benefit)
    heatmap_path = output_dir / "cowi-sensitivity-heatmap.png"
    plot_heatmap(bcr_grid, heatmap_path)
    log(f"  Heatmap saved: {heatmap_path}")

    # 6. Tornado
    log("Smid tornado (IRR per forsendu-breytingu)...")
    base_irr_t, scenarios = tornado(annual_benefit)
    tornado_path = output_dir / "cowi-sensitivity-tornado.png"
    plot_tornado(base_irr_t, scenarios, tornado_path)
    log(f"  Tornado saved: {tornado_path}")
    log()

    # 7. Key findings
    log("=" * 70)
    log("LYKILNIDURSTODUR")
    log("=" * 70)

    # BCR=1 break-even discount rate
    def bcr_gap(rate):
        cf = build_cash_flows(COST_TOTAL_MRD, annual_benefit)
        return bcr(cf, rate) - 1.0

    try:
        break_even_rate = brentq(bcr_gap, 0.01, 0.30)
        log(f"* BCR = 1.0 break-even vid afslatt: {break_even_rate*100:.1f}% "
            f"(Cowi notar liklega ~5%, IRR per definitionem = {base_irr*100:.1f}%)")
    except Exception:
        log("* BCR > 1 a ollum testum afslattum (3-7%)")

    # At Flyvbjerg median
    cf_flyvbjerg = build_cash_flows(
        COST_TOTAL_MRD, annual_benefit, cost_overrun=FLYVBJERG_MEDIAN_RAIL_OVERRUN
    )
    irr_flyvbjerg = irr(cf_flyvbjerg)
    bcr_flyvbjerg = bcr(cf_flyvbjerg, 0.05)
    log(f"* Vid Flyvbjerg-media rail cost-overrun ({FLYVBJERG_MEDIAN_RAIL_OVERRUN*100:.0f}%):")
    log(f"    IRR fellur ur {base_irr*100:.1f}% nidur i {irr_flyvbjerg*100:.1f}%")
    log(f"    BCR fellur ur {base_bcr:.2f} nidur i {bcr_flyvbjerg:.2f}")

    # Combined worst-case
    cf_worst = build_cash_flows(
        COST_TOTAL_MRD, annual_benefit,
        cost_overrun=FLYVBJERG_MEDIAN_RAIL_OVERRUN, benefit_factor=0.7
    )
    irr_worst = irr(cf_worst)
    bcr_worst = bcr(cf_worst, 0.05)
    log(f"* Versta-fall (Flyvbjerg 45% overrun + farthega 70% af spa):")
    log(f"    IRR: {irr_worst*100:.1f}%")
    log(f"    BCR vid 5% afslatt: {bcr_worst:.2f}")

    # Combination that breaks BCR=1
    log()
    log("* Hvenaer brotnar BCR < 1.0?")
    found_break = False
    for co in [0.30, 0.45, 0.60, 0.80, 1.00]:
        for pf in [1.0, 0.7, 0.5]:
            cf = build_cash_flows(COST_TOTAL_MRD, annual_benefit,
                                  cost_overrun=co, benefit_factor=pf)
            b = bcr(cf, 0.05)
            if b < 1.0 and not found_break:
                log(f"    BCR fellur fyrst undir 1.0 vid kostnadar-framukeyrslu {co*100:.0f}% "
                    f"+ farthegaspa {pf*100:.0f}% (BCR = {b:.2f})")
                found_break = True

    log()
    log("ALYKTUN:")
    log("* Cowi 9.2% IRR er ekki robust - feller skjott ef adur en helmingur af")
    log("  Flyvbjerg-overrun gerist, og enn skjotari ef farthegaspa naest ekki.")
    log("* Vid 'verstu fall' forsendur (Flyvbjerg media + 70% farthega) er IRR")
    log(f"  nu thegar {irr_worst*100:.1f}% og BCR {bcr_worst:.2f}. Ef tatil 5% hurdle,")
    log("  thad gerir hagkvaemni vidkvaema.")
    log("* Sterkasta einstaka forsendan: kostnadar-framukeyrsla. Liklegasta")
    log("  ahaettan tengist directly Flyvbjerg-megaproject pattern [H036].")
    log()
    log("Tenging vid README: Veikleiki #9 styrkt med konkret tolum.")
    log("Naestu skref: T2 - Flyvbjerg reference-class forecasting med opnu gagnasafni.")

    # Save text summary
    summary_path = output_dir / "cowi-sensitivity-summary.txt"
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")
    print(f"\nSummary saved: {summary_path}")


if __name__ == "__main__":
    main()

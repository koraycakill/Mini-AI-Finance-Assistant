import numpy as np


def calculate_risk_score(
    annual_volatility,
    max_drawdown,
    weights
):
    """
    Returns:
    {
        "score": float,
        "label": str
    }
    """

    # Volatilite skoru (0-10)
    vol_score = min(
        annual_volatility / 0.50 * 10,
        10
    )

    # Drawdown skoru (0-10)
    dd_score = min(
        abs(max_drawdown) / 0.60 * 10,
        10
    )

    # Konsantrasyon riski
    concentration = max(weights.values())

    conc_score = min(
        concentration * 10,
        10
    )

    score = (
        vol_score * 0.4
        + dd_score * 0.4
        + conc_score * 0.2
    )

    score = round(score, 1)

    if score < 4:
        label = "LOW"

    elif score < 7:
        label = "MEDIUM"

    else:
        label = "HIGH"

    return {
        "score": score,
        "label": label
    }
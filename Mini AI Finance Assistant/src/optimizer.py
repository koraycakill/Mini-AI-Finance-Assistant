import numpy as np
import pandas as pd
import yfinance as yf


def get_returns(tickers):

    data = yf.download(
        tickers,
        period="1y",
        auto_adjust=True,
        progress=False
    )["Close"]

    returns = data.pct_change()

    return returns.dropna()


def optimize_portfolio(tickers):

    returns = get_returns(tickers)

    mean_returns = returns.mean() * 252

    cov_matrix = returns.cov() * 252

    num_assets = len(tickers)

    best_sharpe = -999

    best_weights = None

    best_return = None

    best_volatility = None

    for _ in range(5000):

        weights = np.random.random(
            num_assets
        )

        weights /= np.sum(weights)

        portfolio_return = np.sum(
            mean_returns * weights
        )

        portfolio_volatility = np.sqrt(
            np.dot(
                weights.T,
                np.dot(
                    cov_matrix,
                    weights
                )
            )
        )

        sharpe = (
            portfolio_return
            / portfolio_volatility
        )

        if sharpe > best_sharpe:

            best_sharpe = sharpe

            best_weights = weights

            best_return = portfolio_return

            best_volatility = portfolio_volatility

    return {

        "weights": dict(
            zip(
                tickers,
                np.round(
                    best_weights,
                    4
                )
            )
        ),

        "expected_return": round(
            best_return,
            4
        ),

        "volatility": round(
            best_volatility,
            4
        ),

        "sharpe": round(
            best_sharpe,
            4
        )
    }
import pandas as pd
import numpy as np
import yfinance as yf


def get_portfolio_data(weights, period="1y"):

    returns = pd.DataFrame()

    for ticker in weights.keys():

        data = yf.download(
            ticker,
            period=period,
            auto_adjust=True,
            progress=False
        )

        returns[ticker] = data["Close"].pct_change()

    returns = returns.dropna()

    return returns


def portfolio_metrics(weights):

    returns = get_portfolio_data(weights)

    weight_vector = np.array(
        list(weights.values())
    )

    portfolio_returns = (
        returns @ weight_vector
    )

    annual_return = (
        portfolio_returns.mean()
        * 252
    )

    annual_volatility = (
        portfolio_returns.std()
        * np.sqrt(252)
    )

    sharpe_ratio = (
        annual_return
        / annual_volatility
    )

    cumulative = (
        1 + portfolio_returns
    ).cumprod()

    running_max = cumulative.cummax()

    drawdown = (
        cumulative
        - running_max
    ) / running_max

    max_drawdown = drawdown.min()

    return {
        "annual_return": annual_return,
        "annual_volatility": annual_volatility,
        "sharpe_ratio": sharpe_ratio,
        "max_drawdown": max_drawdown,
        "cumulative": cumulative
    }
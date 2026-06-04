from ta.momentum import RSIIndicator

def add_indicators(df):

    df["SMA20"] = (
        df["Close"]
        .rolling(window=20)
        .mean()
    )

    df["SMA50"] = (
        df["Close"]
        .rolling(window=50)
        .mean()
    )

    df["SMA200"] = (
        df["Close"]
        .rolling(window=200)
        .mean()
    )

    df["RSI"] = RSIIndicator(
        close=df["Close"]
    ).rsi()

    return df
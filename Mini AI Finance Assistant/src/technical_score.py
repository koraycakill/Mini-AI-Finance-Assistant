def calculate_technical_score(df):

    latest = df.iloc[-1]

    score = 0

    close = latest["Close"]
    sma20 = latest["SMA20"]
    sma50 = latest["SMA50"]
    sma200 = latest["SMA200"]
    rsi = latest["RSI"]

    if close > sma20:
        score += 2

    if close > sma50:
        score += 2

    if close > sma200:
        score += 3

    if 40 <= rsi <= 70:
        score += 3

    if score <= 3:
        label = "BEARISH"

    elif score <= 6:
        label = "NEUTRAL"

    else:
        label = "BULLISH"

    return {
        "score": score,
        "label": label
    }
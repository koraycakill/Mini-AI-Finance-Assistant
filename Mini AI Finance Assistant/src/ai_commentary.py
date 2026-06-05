def generate_comment(df):

    latest = df.iloc[-1]

    close = latest["Close"]
    sma20 = latest["SMA20"]
    sma50 = latest["SMA50"]
    sma200 = latest["SMA200"]
    rsi = latest["RSI"]

    comments = []

    # Trend
    if close > sma200:
        comments.append(
            "The stock remains above its 200-day moving average, indicating a positive long-term trend."
        )
    else:
        comments.append(
            "The stock trades below its 200-day moving average, suggesting a weaker long-term trend."
        )

    # SMA Structure
    if sma20 > sma50 > sma200:
        comments.append(
            "Moving averages show a strong bullish structure."
        )

    elif sma20 < sma50 < sma200:
        comments.append(
            "Moving averages show a strong bearish structure."
        )

    # RSI
    if rsi > 70:
        comments.append(
            "RSI indicates overbought conditions and increased correction risk."
        )

    elif rsi < 30:
        comments.append(
            "RSI indicates oversold conditions and potential recovery opportunities."
        )

    else:
        comments.append(
            "RSI remains in a balanced range without extreme momentum signals."
        )

    return "\n\n".join(comments)
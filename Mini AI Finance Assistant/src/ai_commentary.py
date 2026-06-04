def generate_comment(df):

    rsi = df["RSI"].iloc[-1]

    if rsi > 70:
        return (
            "RSI is in the overbought region. "
            "There may be a risk of a correction in the short term."
        )

    elif rsi < 30:
        return (
            "RSI is in the oversold region. "
            "There may be a buying opportunity."
        )

    else:
        return (
            "RSI is in a neutral region. "
            "No clear overbought or oversold signal."
        )
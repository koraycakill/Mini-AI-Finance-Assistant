import yfinance as yf

POSITIVE_WORDS = [
    "growth",
    "profit",
    "upgrade",
    "strong",
    "beat",
    "record",
    "surge",
    "increase"
]

NEGATIVE_WORDS = [
    "loss",
    "downgrade",
    "decline",
    "weak",
    "miss",
    "drop",
    "fall",
    "decrease"
]


def get_news_sentiment(ticker):

    stock = yf.Ticker(ticker)
    news = stock.news

    if not news:
        return {
            "score": 0,
            "label": "NEUTRAL",
            "headlines": []
        }

    score = 0
    headlines = []

    for article in news[:10]:

        title = article.get("title", "")

        headlines.append(title)

        title_lower = title.lower()

        for word in POSITIVE_WORDS:
            if word in title_lower:
                score += 1

        for word in NEGATIVE_WORDS:
            if word in title_lower:
                score -= 1

    if score > 2:
        label = "POSITIVE"
    elif score < -2:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    return {
        "score": score,
        "label": label,
        "headlines": headlines
    }
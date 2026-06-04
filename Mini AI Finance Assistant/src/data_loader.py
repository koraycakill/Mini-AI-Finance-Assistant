import yfinance as yf

def get_stock_data(ticker, period="1y"):
    stock = yf.Ticker(ticker)

    df = stock.history(period=period)

    if df.empty:
        raise ValueError("Data not found")

    return df
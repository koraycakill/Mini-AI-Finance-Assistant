# Mini AI Finance Assistant
![Dashboard Screenshot](Mini%20AI%20Finance%20Assistant/images/dashboard.png)

A lightweight AI-powered financial analysis dashboard built with Python and Streamlit.

## Overview

Mini AI Finance Assistant is a web application that allows users to analyze stocks, visualize price movements, calculate technical indicators, and receive automated market commentary.

The project was developed to combine financial analysis, data science, and Python development skills in a practical portfolio project.

## Features

✅ Historical stock price analysis

✅ Interactive price charts

✅ Technical indicators

- SMA 20
- SMA 50
- SMA 200
- RSI (Relative Strength Index)

✅ Automated AI-style market commentary

✅ Support for global stocks through Yahoo Finance

✅ Interactive dashboard built with Streamlit

✅ Portfolio analytics

- Annual Return
- Volatility
- Sharpe Ratio
- Max Drawdown

✅ Portfolio Risk Score

---

## Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- yfinance
- ta (Technical Analysis Library)

---

## Project Structure

mini-ai-finance-assistant/

├── app.py
├── requirements.txt
├── README.md

├── src/
│   ├── data_loader.py
│   ├── indicators.py
│   └── ai_commentary.py

└── .gitignore

---

## Installation

Clone the repository:

bash git clone https://github.com/koraycakill/mini-ai-finance-assistant.git cd mini-ai-finance-assistant 

Install dependencies:

bash pip install -r requirements.txt 

Run the application:

bash streamlit run app.py 

---

## Example Usage

Enter a stock ticker such as:

text AAPL MSFT TSLA GARAN.IS AKBNK.IS TCELL.IS 

The application will:

1. Download historical market data
2. Calculate technical indicators
3. Display interactive charts
4. Generate automated analysis commentary

---

## Future Improvements

- MACD indicator
- Bollinger Bands
- Portfolio analysis
- Risk scoring
- Sharpe Ratio calculation
- Max Drawdown analysis
- News sentiment analysis
- OpenAI-powered financial commentary
- BIST-focused stock analysis

---

## Disclaimer

This project is for educational and research purposes only.

The information provided does not constitute investment advice. Always conduct your own research before making investment decisions.

---

## Author

Koray Yusuf Çakıl

Finance | Data Analysis | Python | Machine Learning

GitHub: https://github.com/koraycakill

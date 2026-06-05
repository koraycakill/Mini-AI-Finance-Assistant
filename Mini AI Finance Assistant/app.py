import streamlit as st
import plotly.graph_objects as go

from src.data_loader import get_stock_data
from src.indicators import add_indicators
from src.ai_commentary import generate_comment
from src.technical_score import calculate_technical_score
from src.portfolio import portfolio_metrics
from src.risk import calculate_risk_score
from src.news_sentiment import get_news_sentiment
from src.optimizer import optimize_portfolio

st.set_page_config(
    page_title="Mini AI Finance Assistant",
    layout="wide"
)

st.title("📈 Mini AI Finance Assistant")

st.write(
    "This application analyzes stock prices and provides AI-powered insights. "
    "Get started by entering the stock code."
)

tab1, tab2 = st.tabs(
    [
        "Stock Analysis",
        "Portfolio Analysis"
    ]
)

with tab1:
    ticker = st.text_input(
        "Stock Code",
        value="GARAN.IS"
    )

    if ticker:

        try:

            df = get_stock_data(ticker)

            df = add_indicators(df)

            technical_score = calculate_technical_score(df)

            sentiment = get_news_sentiment(ticker)
    
            latest_price = df["Close"].iloc[-1]
            latest_rsi = df["RSI"].iloc[-1]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Latest Price",
                    f"{latest_price:.2f}"
                )

            with col2:
                st.metric(
                    "RSI",
                    f"{latest_rsi:.2f}"
                )

                st.metric(
                    "Technical Score",
                    f"{technical_score['score']}/10"
                )

            with col3:
                st.metric(
                    "News Sentiment",
                    sentiment["label"]
                )

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df["Close"],
                    name="Close"
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df["SMA20"],
                    name="SMA20"
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=df.index,
                    y=df["SMA50"],
                    name="SMA50"
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.subheader("Latest Headlines")

            for headline in sentiment["headlines"]:

                st.write(f"• {headline}")
                

            st.subheader("AI commentary")

            if technical_score["label"] == "BULLISH":
                st.success(
                    f"🟢 Technical Outlook: {technical_score['label']}"
                )

            elif technical_score["label"] == "NEUTRAL":
                st.warning(
                    f"🟡 Technical Outlook: {technical_score['label']}"
                )

            else:
                st.error(
                    f"🔴 Technical Outlook: {technical_score['label']}"
                )

            st.subheader("Market Sentiment")

            if sentiment["label"] == "POSITIVE":

                st.success(
                    f"🟢 News Sentiment: {sentiment['label']}"
                )

            elif sentiment["label"] == "NEUTRAL":

                st.warning(
                    f"🟡 News Sentiment: {sentiment['label']}"
                )

            else:

                st.error(
                    f"🔴 News Sentiment: {sentiment['label']}"
                )

            st.info(
                generate_comment(df)
            )

        except Exception as e:

            st.error(str(e))

with tab2:

    st.header("Portfolio Analytics")

    garan = st.slider(
        "GARAN",
        0,
        100,
        30
    )

    akbnk = st.slider(
        "AKBNK",
        0,
        100,
        30
    )

    tcell = st.slider(
        "TCELL",
        0,
        100,
        40
    )

    total = garan + akbnk + tcell

    if total == 100:

        weights = {
            "GARAN.IS": garan / 100,
            "AKBNK.IS": akbnk / 100,
            "TCELL.IS": tcell / 100
        }

        metrics = portfolio_metrics(weights)

        risk = calculate_risk_score(
        metrics["annual_volatility"],
        metrics["max_drawdown"],
        weights
)

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Annual Return",
                f"{metrics['annual_return']:.2%}"
            )

            st.metric(
                "Volatility",
                f"{metrics['annual_volatility']:.2%}"
            )

        with col2:
            st.metric(
                "Sharpe Ratio",
                f"{metrics['sharpe_ratio']:.2f}"
            )

            st.metric(
                "Max Drawdown",
                f"{metrics['max_drawdown']:.2%}"
            )

            st.metric(
                "Risk Score",
                f"{risk['score']}/10"
            )

        if risk["label"] == "LOW":
            st.success(
                f"🟢 Risk Level: {risk['label']}"
        )

        elif risk["label"] == "MEDIUM":
            st.warning(
                f"🟡 Risk Level: {risk['label']}"
            )
        

        else:
            st.error(
                f"🔴 Risk Level: {risk['label']}"
        )
            
        st.line_chart(
            metrics['cumulative']
        )

        st.divider()

        st.subheader(
            "Portfolio Optimization"
        )

        if st.button(
            "Optimize Portfolio"
        ):

            result = optimize_portfolio(
                [
                    "GARAN.IS",
                    "AKBNK.IS",
                    "TCELL.IS"
                ]
            )

            st.success(
                "Optimal portfolio generated"
            )

            st.write(
                "Optimal Weights"
            )

            st.json(
                result["weights"]
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Expected Return",
                    f"{result['expected_return']:.2%}"
                )

            with col2:

                st.metric(
                    "Volatility",
                    f"{result['volatility']:.2%}"
                )

            with col3:

                st.metric(
                    "Sharpe Ratio",
                    f"{result['sharpe']:.2f}"
                )

    else:

        st.warning(
            "Weights must sum to 100%"
        )

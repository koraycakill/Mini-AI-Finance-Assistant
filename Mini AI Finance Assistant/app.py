import streamlit as st
import plotly.graph_objects as go

from src.data_loader import get_stock_data
from src.indicators import add_indicators
from src.ai_commentary import generate_comment

st.set_page_config(
    page_title="Mini AI Finance Assistant",
    layout="wide"
)

st.title("📈 Mini AI Finance Assistant")
st.altair_chart(
    go.Figure(
        go.Scatter(
            x=[1, 2, 3],
            y=[1, 4, 9],
            mode="markers"
        )
    ),
    use_container_width=True
)   
st.write("This application analyzes stock prices and provides AI-powered insights. Get started by entering the stock code.")

ticker = st.text_input(
    "Stock Code",
    value="GARAN.IS"
)

if ticker:

    try:

        df = get_stock_data(ticker)

        df = add_indicators(df)

        latest_price = df["Close"].iloc[-1]
        latest_rsi = df["RSI"].iloc[-1]

        col1, col2 = st.columns(2)

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

        st.subheader("AI commentary")

        st.info(
            generate_comment(df)
        )

    except Exception as e:

        st.error(str(e))
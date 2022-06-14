import yfinance as yf
import pandas as pd
impor streamlit as streamlit

st.write("""
# Aplikasi Yahoo Finance
## Data saham Google

Berikut ini adalah Closing price dan volume dari Google.
""")

ticker = 'GOOGL'
tickerData = yf.Ticker(ticker)
tickerDF = tickerData.history(period='Id', start='2022-01-01', end='2022-05-30')

st,line_chart(tickerDF,Close)
st,line_chart(tickerDF,Volume)
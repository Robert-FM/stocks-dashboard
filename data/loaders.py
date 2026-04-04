import pandas as pd
import streamlit as st
import yfinance as yf


@st.cache_data
def carregar_tickers_acoes(caminho_csv="IBOV.csv"):
    base_tickers = pd.read_csv(caminho_csv, sep=';')
    tickers = list(base_tickers["Código"])
    tickers = [ticker + ".SA" for ticker in tickers]
    return tickers


@st.cache_data
def carregar_dados(empresas, start="2020-01-01", end="2025-12-31"):
    texto_tickers = " ".join(empresas)
    dados_acao = yf.Tickers(texto_tickers)
    cotacao_acao = dados_acao.history(start=start, end=end)

    if "Close" not in cotacao_acao:
        return pd.DataFrame()

    cotacao_acao = cotacao_acao["Close"]
    return cotacao_acao
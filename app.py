import streamlit as st
from data.loaders import carregar_tickers_acoes, carregar_dados
from ui.filters import aplicar_filtros
from utils.performance import calcular_performance


def main():
    st.markdown("""
    # App de Preço de Ações
    #### O gráfico abaixo representa a evolução do preço das ações ao longo dos anos.
    """)

    acoes = carregar_tickers_acoes()
    dados = carregar_dados(acoes)

    if dados.empty:
        st.error("Não foi possível carregar os dados das ações.")
        return

    dados_filtrados, lista_acoes = aplicar_filtros(dados)

    st.line_chart(dados_filtrados)

    texto_performance_ativos, texto_performance_carteira = calcular_performance(
        dados_filtrados,
        lista_acoes
    )

    st.write(texto_performance_ativos)
    st.write(texto_performance_carteira)


if __name__ == "__main__":
    main()
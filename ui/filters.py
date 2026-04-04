import streamlit as st


def aplicar_filtros(dados):
    st.sidebar.header("Filtros")

    lista_acoes = st.sidebar.multiselect(
        "Escolha as ações para visualizar:",
        dados.columns
    )

    dados_filtrados = dados.copy()

    if lista_acoes:
        dados_filtrados = dados_filtrados[lista_acoes]

    data_inicial = dados_filtrados.index.min().to_pydatetime()
    data_final = dados_filtrados.index.max().to_pydatetime()

    intervalo_de_data = st.sidebar.slider(
        "Selecione o período:",
        min_value=data_inicial,
        max_value=data_final,
        value=(data_inicial, data_final)
    )

    dados_filtrados = dados_filtrados.loc[intervalo_de_data[0]:intervalo_de_data[1]]

    return dados_filtrados, lista_acoes
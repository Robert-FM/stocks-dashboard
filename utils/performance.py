def calcular_performance(dados, lista_acoes):
    texto_performance_ativos = ""

    if len(lista_acoes) == 0:
        lista_acoes = list(dados.columns)

    carteira = [1000 for _ in lista_acoes]
    total_inicial_carteira = sum(carteira)

    for i, acao in enumerate(lista_acoes):
        performance_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1
        performance_ativo = float(performance_ativo)

        carteira[i] = carteira[i] * (1 + performance_ativo)

        if performance_ativo > 0:
            texto_performance_ativos += f"  \n{acao}: :green[{performance_ativo:.1%}]"
        elif performance_ativo < 0:
            texto_performance_ativos += f"  \n{acao}: :red[{performance_ativo:.1%}]"
        else:
            texto_performance_ativos += f"  \n{acao}: {performance_ativo:.1%}"

    total_final_carteira = sum(carteira)
    performance_carteira = total_final_carteira / total_inicial_carteira - 1

    if performance_carteira > 0:
        texto_performance_carteira = f"Performance da carteira: :green[{performance_carteira:.1%}]"
    elif performance_carteira < 0:
        texto_performance_carteira = f"Performance da carteira: :red[{performance_carteira:.1%}]"
    else:
        texto_performance_carteira = f"Performance da carteira: {performance_carteira:.1%}"

    return texto_performance_ativos, texto_performance_carteira
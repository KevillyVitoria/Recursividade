def simular_investimento():
    acao1 = {"codigo": "ITUB4", "nome": "Itaú Unibanco", "precos": [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41], "dividendos": [0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.30, 0.31]}
    acao2 = {"codigo": "PETR4", "nome": "Petrobras", "precos": [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], "dividendos": [0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26]}
    acao3 = {"codigo": "VALE3", "nome": "Vale", "precos": [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], "dividendos": [0.30, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.40, 0.41]}

    investimento_mensal = 80
    montante_100k = 100000
    montante_1m = 1000000
    valor_acumulado = 0
    dividendos_acumulados = 0
    meses = 0
    marco_100k = False
    marco_1m = False

    # cotas de cada ação
    cotas_acao1 = 0
    cotas_acao2 = 0
    cotas_acao3 = 0

    while not (marco_100k and marco_1m):
        meses += 1
        mes_atual = (meses - 1) % 12 

        valor_por_acao = investimento_mensal / 3
        cotas_acao1 += valor_por_acao / acao1["precos"][mes_atual]
        cotas_acao2 += valor_por_acao / acao2["precos"][mes_atual]
        cotas_acao3 += valor_por_acao / acao3["precos"][mes_atual]

        valor_acumulado = (
            cotas_acao1 * acao1["precos"][mes_atual] +
            cotas_acao2 * acao2["precos"][mes_atual] +
            cotas_acao3 * acao3["precos"][mes_atual]
        )

        # Recebe dividendos
        dividendos_mes = (
            cotas_acao1 * acao1["dividendos"][mes_atual] +
            cotas_acao2 * acao2["dividendos"][mes_atual] +
            cotas_acao3 * acao3["dividendos"][mes_atual]
        )
        dividendos_acumulados += dividendos_mes

        # Verifica se o marco de R$ 100.000,00 foi atingido
        if not marco_100k and valor_acumulado >= montante_100k:
            marco_100k = True
            tempo_100k = meses
            valor_investido_100k = investimento_mensal * meses
            juros_compostos_100k = valor_acumulado - valor_investido_100k

        # Verifica se o marco de R$ 1.000.000,00 foi atingido
        if not marco_1m and valor_acumulado >= montante_1m:
            marco_1m = True
            tempo_1m = meses
            valor_investido_1m = investimento_mensal * meses
            juros_compostos_1m = valor_acumulado - valor_investido_1m

    # Converter meses em anos e meses
    anos_100k, meses_100k = divmod(tempo_100k, 12)
    anos_1m, meses_1m = divmod(tempo_1m, 12)

    print(f"Ação 1 - {acao1['codigo']} ({acao1['nome']}):")
    print(f"  Quantidade de cotas: {cotas_acao1:.2f}")
    print(f"  Valor total: R$ {cotas_acao1 * acao1['precos'][mes_atual]:.2f}")
    print(f"  Dividendos recebidos: R$ {cotas_acao1 * sum(acao1['dividendos']):.2f}")
    print()

    print(f"Ação 2 - {acao2['codigo']} ({acao2['nome']}):")
    print(f"  Quantidade de cotas: {cotas_acao2:.2f}")
    print(f"  Valor total: R$ {cotas_acao2 * acao2['precos'][mes_atual]:.2f}")
    print(f"  Dividendos recebidos: R$ {cotas_acao2 * sum(acao2['dividendos']):.2f}")
    print()

    print(f"Ação 3 - {acao3['codigo']} ({acao3['nome']}):")
    print(f"  Quantidade de cotas: {cotas_acao3:.2f}")
    print(f"  Valor total: R$ {cotas_acao3 * acao3['precos'][mes_atual]:.2f}")
    print(f"  Dividendos recebidos: R$ {cotas_acao3 * sum(acao3['dividendos']):.2f}")
    print()

    print(f"Tempo gasto para atingir o marco inicial de R$ 100.000,00: {anos_100k} anos e {meses_100k} meses")
    print(f"  Valor investido: R$ {valor_investido_100k:.2f}")
    print(f"  Dividendos recebidos: R$ {dividendos_acumulados:.2f}")
    print(f"  Juros compostos: R$ {juros_compostos_100k:.2f}")
    print()

    print(f"Tempo gasto para atingir o objetivo final de R$ 1.000.000,00: {anos_1m} anos e {meses_1m} meses")
    print(f"  Valor investido: R$ {valor_investido_1m:.2f}")
    print(f"  Dividendos recebidos: R$ {dividendos_acumulados:.2f}")
    print(f"  Juros compostos: R$ {juros_compostos_1m:.2f}")

simular_investimento()
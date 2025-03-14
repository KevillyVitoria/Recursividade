def calcular_investimento_bitcoin():
    # considerando o ano de 2024
    precos_bitcoin = {
            1:200000, 2:210000, 3:220000, 4:230000, 5:240000, 6:250000,
            7:260000, 8:270000, 9:280000, 10:290000, 11:300000, 12:310000
    }
    valor_investido = 0
    montante_reais = 0
    montante_bitcoin = 0
    meses = 0
    marco_100k = False
    marco_1m = False
    marco_1btc = False

    while not (marco_100k and marco_1m and marco_1btc):
        meses += 1
        mes_atual = (meses - 1) % 12 + 1  # Calcula o mês 
        preco_bitcoin = precos_bitcoin[mes_atual]  # Preço do Bitcoin no mês atual

        valor_investido += 250
        montante_reais += 250

        # Compra de Bitcoin com o investimento mensal
        montante_bitcoin += 250 / preco_bitcoin

        # Verifica se o montante em reais atingiu R$ 100.000,00
        if not marco_100k and montante_reais >= 100000:
            marco_100k = True
            tempo_100k_anos = meses // 12
            tempo_100k_meses = meses % 12
            print(f"Marco de R$ 100.000,00 atingido em {tempo_100k_anos} anos e {tempo_100k_meses} meses.")
            print(f"Valor investido até R$ 100.000,00: R$ {valor_investido:.2f}")
            print(f"Montante em Bitcoin até R$ 100.000,00: {montante_bitcoin:.8f} BTC")

        # Verifica se o montante em reais atingiu R$ 1.000.000,00
        if not marco_1m and montante_reais >= 1000000:
            marco_1m = True
            tempo_1m_anos = meses // 12
            tempo_1m_meses = meses % 12
            print(f"Marco de R$ 1.000.000,00 atingido em {tempo_1m_anos} anos e {tempo_1m_meses} meses.")
            print(f"Valor investido até R$ 1.000.000,00: R$ {valor_investido:.2f}")
            print(f"Montante em Bitcoin até R$ 1.000.000,00: {montante_bitcoin:.8f} BTC")

        # Verifica se o montante em Bitcoin atingiu 1 BTC
        if not marco_1btc and montante_bitcoin >= 1:
            marco_1btc = True
            tempo_1btc_anos = meses // 12
            tempo_1btc_meses = meses % 12
            print(f"Marco de 1 Bitcoin atingido em {tempo_1btc_anos} anos e {tempo_1btc_meses} meses.")
            print(f"Valor investido até 1 Bitcoin: R$ {valor_investido:.2f}")
            print(f"Montante em Reais até 1 Bitcoin: R$ {montante_reais:.2f}")

calcular_investimento_bitcoin()
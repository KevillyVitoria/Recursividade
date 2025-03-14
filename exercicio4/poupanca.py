def calcular_investimento():
    valor_investido = 0
    montante = 0
    meses = 0
    juros_compostos = 0
    marco_100k = False
    marco_1m= False

    while not marco_1m:
        meses += 1
        valor_investido += 500  
        montante += 500  

        # Aplica o rendimento de 0,05% sobre o montante que está na conta há mais de 30 dias
        if meses > 1:
            rendimento = montante * 0.0005
            montante += rendimento
            juros_compostos += rendimento

        # Verifica se atingiu R$ 100.000,00
        if not marco_100k and montante >= 100000:
            marco_100k = True
            tempo_100k_anos = meses // 12
            tempo_100k_meses = meses % 12
            print(f"Marco de R$ 100.000,00 atingido em {tempo_100k_anos} anos e {tempo_100k_meses} meses.")
            print(f"Valor investido até R$ 100.000,00: R$ {valor_investido:.2f}")
            print(f"Juros compostos obtidos até R$ 100.000,00: R$ {juros_compostos:.2f}")

        # Verifica se atingiu R$ 1.000.000,00
        if montante >= 1000000:
            marco_1m = True
            tempo_1m_anos = meses // 12
            tempo_1m_meses = meses % 12
            print(f"Marco de R$ 1.000.000,00 atingido em {tempo_1m_anos} anos e {tempo_1m_meses} meses.")
            print(f"Valor investido total: R$ {valor_investido:.2f}")
            print(f"Juros compostos obtidos: R$ {juros_compostos:.2f}")
            print(f"Montante final: R$ {montante:.2f}")

calcular_investimento()
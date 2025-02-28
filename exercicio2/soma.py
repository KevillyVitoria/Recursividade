def soma (numero : int) -> int:
    if numero > 1:
        return numero + soma(numero - 1)
    return numero

print (soma(5))
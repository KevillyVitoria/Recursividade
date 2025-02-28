def inverter(nome : str) -> str:
    emon = ""
    if len (nome) > 0:
        emon += nome[-1] + inverter(nome[:-1])
        
    return emon

print(inverter('casa'))
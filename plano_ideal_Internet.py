def recomendar_plano(consumo_mensal):
    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo_mensal > 10 and consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
       return "Plano Premium Fibra - 300Mbps"

consumo = float(input())

print(recomendar_plano(consumo))
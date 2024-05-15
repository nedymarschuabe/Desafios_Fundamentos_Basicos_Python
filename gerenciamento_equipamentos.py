itens = []

for _ in range(3):
    equipamento = input()
    itens.append(equipamento)

print("Lista de Equipamentos:")
for item in itens:
    print(f"- {item}")
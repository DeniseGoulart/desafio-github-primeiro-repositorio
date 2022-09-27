valores = input().split()

total_cachorros_quentes = int(valores[0])
total_de_participantes = int(valores[1])

while (total_cachorros_quentes < 1) or (total_de_participantes > 1000) or (total_de_participantes <= 0):
    valores = input().split()

    total_cachorros_quentes = int(valores[0])
    total_de_participantes = int(valores[1])

print()

media = float(total_cachorros_quentes / total_de_participantes)
print(f"{media:.2f}")
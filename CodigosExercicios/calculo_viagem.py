valores = input().split()

tempo_gasto = int(valores[0])
velocidade_media = int(valores[1])

while (tempo_gasto <= 0) or (velocidade_media <= 0):
    valores = input().split()

    tempo_gasto = int(valores[0])
    velocidade_media = int(valores[1])

print()

distancia = float(velocidade_media * tempo_gasto)
quantidade_litros = float(distancia / 12)

print(f"{quantidade_litros:.3f}")
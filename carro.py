valores = input().split()

horas_viagem = int(valores[0])
velocidade_media = int(valores[1])

media = horas_viagem * velocidade_media
litros = media / 12

print(f"{litros:.3f}")

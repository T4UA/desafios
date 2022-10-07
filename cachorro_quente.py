valores = input().split() 

cachorro_quente_total = int(valores[0])
numero_participantes = int(valores[1])

media = cachorro_quente_total / numero_participantes

print(f"{media:.2f}")

entrada = input().split()
while True:
	contador = 0
	for valores in entrada:
		contador += 1
	if contador == 3:
		break
	else:
		print("Insira 3 valores inteiros")
		entrada = input().split()

while True:
	distancia = int(entrada[0])
	if distancia < 0 or distancia > 10000:
		print("Insira um valor valido entre 0 e 10000")
		break

	diametro_sauron = int(entrada[1])
	if diametro_sauron < 0 or diametro_sauron > 100:
		print("Insira um valor valido entre 0 e 100")
		break

	diametro_saruman = int(entrada[2])
	if diametro_saruman < 0 or diametro_saruman > 100:
		print("Insira um valor valido entre 0 e 100")
		break

	resultado = distancia / (diametro_sauron + diametro_saruman)

	print(f"{resultado:.2f}")
	break

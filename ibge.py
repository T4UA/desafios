i = 0
maior = 0
soma = 0
soma_vitimas = 0
cont = 0
while True:
    cod_cidade = int(input("Digite o codigo da cidade: "))
    num_veiculos_passeio = int(input("Digite a quantidade de veiculos de passeio: "))
    num_acidentes_vitimas= int(input("Digite a quantidade de acidentes com vitimas: "))
    soma += num_veiculos_passeio

    if maior == 0:
        maior = num_veiculos_passeio
        menor = num_veiculos_passeio
        cid_max_indice = cod_cidade
        cid_min_indice = cod_cidade
    elif num_veiculos_passeio > maior:
        maior = num_veiculos_passeio
        cid_max_indice = cod_cidade
    elif num_veiculos_passeio < menor:
        menor = num_veiculos_passeio
        cid_min_indice = cod_cidade

    if num_veiculos_passeio < 2000:
        soma_vitimas += num_acidentes_vitimas
        cont +=1
    i+=1
    continuar = input("Deseja continuar o cadastro? s ou n: ").strip().lower()
    if continuar == 'n':
        break

media_acidentes = soma_vitimas / cont
media = soma / i

print(f"indice_max {maior} - cidade {cid_max_indice} | indice_min {menor} - cidade {cid_min_indice}")
print(f"A media de veiculos nas cidades é {media:.2f}")
print(f"A media de acidentes de transito nas cidades com menos de 2000 veiculos é {media_acidentes:.2f}")

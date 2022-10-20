extrato = [0]
movimentacao = {}
from datetime import datetime
def menu():
	print(30*"*")
	print("*Seja Bem-Vindo ao Banco X")
	print("*Qual operação você deseja executar?")
	print("*Extrato[1]\n*Deposito[2]\n*Saque[3]\n*Pix[4]\n*Encerrar[5]")
	print(30*"*")

def hora_registro():
	data_atual = datetime.now()
	movimentacao[data_atual.strftime('%d/%m/%Y %H:%M:%S')] = cenario
	print("Operação realizada com sucesso!")

while True:
	menu()
	opcao = int(input("O que deseja realizar? "))
	if opcao == 1:
		print(30*"_")
		print("Seu extrato")
		for chave, valor in movimentacao.items():
			print(f"{chave} - {valor}")
		print(f"Total R${extrato[-1]:.2f}")
	elif opcao == 2:
		while True:
			valor_depositado = float(input("Valor a ser depositado R$: "))
			ultima_operacao = extrato[-1]
			if valor_depositado > 0:
				ultima_operacao += valor_depositado
				extrato.append(ultima_operacao)
				cenario = f"Deposito no valor de R${valor_depositado:.2f} realizado"
				hora_registro()
				break
			elif valor_depositado == 0:
				break
			else:
				print("Insira um valor válido ou [0] para retornar ao menu")
	elif opcao == 3:
		valor_saque = float(input("Valor do saque R$: "))
		ultima_operacao = extrato[-1]
		if valor_saque > ultima_operacao:
			print("Valor indisponivel para saque")
		else:
			ultima_operacao -= valor_saque
			extrato.append(ultima_operacao)
			cenario = f"Saque no valor de R${valor_saque:.2f} realizado"
			hora_registro()
	elif opcao == 4:
		valor_pix = float(input("Digite o valor a ser transferido R$: "))
		ultima_operacao = extrato[-1]
		if valor_pix > ultima_operacao:
			print("Transferencia cancelada, valor em conta insuficiente, favor verificar extrato")
		else:
			ultima_operacao -= valor_pix
			extrato.append(ultima_operacao)
			cenario = f"Pix no valor de R${valor_pix:.2f} realizado"
			hora_registro()
	else:
		break

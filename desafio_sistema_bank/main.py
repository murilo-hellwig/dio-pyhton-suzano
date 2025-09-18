menu = """
 
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
	opcao = input(menu)
	if opcao == "d":
		print("Depósito")
		valor_deposito = float(input('Digite o valor que deseja depositar: '))

		if valor_deposito > 0:
			saldo += valor_deposito
			extrato += f"---> Depósito no valor de \tR${valor_deposito:.2f}\n"

		else: print("Operação de depósito falhor! Por favor digite um valor váido")
			
	elif opcao == "s":
		print("Saque")
		valor_saque = float(input('Digite o valor que deseja sacar: '))

		excedeu_saldo = valor_saque > saldo
		excedeu_limite = valor_saque > limite
		excedeu_saques = numero_saques >= LIMITE_SAQUES

		if excedeu_limite and excedeu_saldo: 
			print(f"Operação falhou! O valor limite de cada saque é de R$500,00, e o seu saldo atual é R${saldo:.2f}.")
		elif excedeu_saldo:
			print(f"Operação falhou! Você não tem saldo suficiente. Seu saldo atual é R${saldo:.2f}")
		elif excedeu_limite and not excedeu_saldo: 
			print("Operação falhou! O valor limite de cada saque é de R$500,00.")
		elif excedeu_saques:
			print("Operação falhou! Número máximo de saques diários é de três.")
		elif valor_saque > 0:
			saldo -= valor_saque
			print(f"Saque realizado com sucesso! Seu saldo atual é R${saldo:.2f}.")
			extrato += f"---> Saque no valor de \t\tR${valor_saque:.2f}.\n"
			numero_saques += 1

		else:
			print("Operação falhou! Por favor digite um valor válido para o saque.")
		
	elif opcao == "e":
		print("Extrato")
		print("\n========== EXTRATO ==========\n")
		print("\nNão foram realizadas movimentações." if not extrato else extrato)
		print(f"\nSeu saldo atual é: \t\tR${saldo:.2f}")
		print("\n=============================\n")
		
	elif opcao == "q":
		print("Caixa fechado!")
		break
		
	else:
		print("Operação inválida, por favor selecione novamente a operação desejada.")
	
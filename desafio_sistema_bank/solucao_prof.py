 #solução do professor, com as instruções dentro do arquivo main:
 
 
menu = """
 Operações disponíveis:

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
		valor = float(input("Informe o valor do depósito: "))
		
		if valor > 0:
			saldo += valor
			extrato += f"--> Depósito: R$ {valor:.2f}\n" #corrigir string para usar data
			
		else: print("Operação falhou! O valor informado é inválido.")
		
	elif opcao == "s":
		print("Saque")
		valor = float(input("Informe o valor do saque: "))
		
		excedeu_saldo = valor > saldo
		excedeu_limite = valor > limite
		excedeu_saques = numero_saques >= LIMITE_SAQUES
		
		if excedeu_saldo:
			print("Operação falhou! Você não tem saldo suficiente.")
			
		elif excedeu_limite and excedeu_saldo: 
			print(f"Operação falhou! O valor limite de cada saque é de R$500,00, e o seu saldo atual é {saldo}")
		elif excedeu_limite and not excedeu_saldo: 
			print("Operação falhou! O valor limite de cada saque é de R$500,00")
			
		elif excedeu_saques:
			print("Operação falhou! Número máximo de saques excedido.")
		
		elif valor > 0:
			saldo -= valor
			print(f"Saque realizado com sucesso! Seu saldo atual é: R$ {saldo:.2f}")
			extrato += f"--> Saque: R$ {valor:.2f}\n" #corrigir string para usar data
			numero_saques += 1
			
		else:
			print("Operação falhou! O valor informado é inválido!")
			
	elif opcao == "e":
		print("Opção escolhida: Extrato")
		print("\n========== EXTRATO ==========") #usar a sintaxe de .center das strings
		print("Não foram realizadas movimentações." if not extrato else extrato) #caso a string extrato ainda esteja vazia
		print(f"\nSeu saldo atual é: R$ {saldo:.2f}")
		print("==============================")
		
	elif opcao == "q":
		print("Caixa fechado!")
		break
		
	else:
		print("Operação inválida, por favor selecione novamente a operação desejada.")
	
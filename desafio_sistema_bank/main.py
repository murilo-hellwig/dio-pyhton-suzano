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
	if opcao === "d":
		print("Depósito")
		deposito() #codificar a função deposito
		
	elif opcao == "s":
		print("Saque")
		saque() #codificar a função saque
		
	elif opcao == "e":
		print("Extrato")
		extrato() #codificar a função extrato
		
	elif opcao == "q":
		print("Caixa fechado!")
		break
		
	else:
		print("Operação inválida, por favor selecione novamente a operação desejada.")
	
#para IF ternario
saldo = 5100
saque = 3500
#fica tudo em uma linha
status = 'Sucesso' if saldo > saque else 'Falha'

print(f'{status} ao realizar o saque')
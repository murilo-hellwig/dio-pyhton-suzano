#exemplos while
opcao = -1

while opcao != 0:
    opcao = int(input('Digite a opção desejada: \n [1] Sacar \n [2] Depositar \n [0] Sair \n'))
    if opcao == 1:
        print('sacando...')
    elif opcao == 2:
        print('depositando...') 
else:
    print('Obrigado por usar nosso sistema!')
    print('saindo do programa...')


while True:
    numero = int(input('Digite um número: '))

    if numero == 10:
        print(f'Você digitou o número {numero} e acertou a aposta!')
        break


#alem do break, podemos usar continue para pular uma iteração, evitando uma situação específica

for numero in range(100):

    if numero == 12:
        continue

    print(numero, end=' ')

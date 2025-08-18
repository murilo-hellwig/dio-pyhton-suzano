nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
jogo_favorito = input("Qual é o seu jogo favorito? ")

if int(idade) < 18:
    print(f"Olá {nome}, você tem {idade} anos então pode jogar {jogo_favorito}.\n\n\n\n\n")
else:
    print(f"Olá {nome}, você tem {idade} anos então {jogo_favorito} está liberado.\n\n\n\n\n")


print("Você sabe que horas são?")

hora = input("Digite a hora:")
if int(hora) < 12:
    print(f"Bom dia, {nome}!")
elif 12 <= int(hora) < 18:
    print(f"Boa tarde, {nome}!")   
elif int(hora) > 18:
    print(f"já está tarde mesmo, você precisa dormir, {nome}. Boa noite!")

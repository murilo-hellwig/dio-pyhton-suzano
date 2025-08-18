#Exemplos de estruturas de repetição em Python como FOR e WHILE
texto = input('Digite um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(f'{letra} é uma vogal')
    else:
        print(f'{letra} não é uma vogal')  


#RANGE
# range tem a estrutura de range(inicio, fim, passo), sendo início e passo opcionais
lista_1 = list(range(1, 100, 5))
lista_2 = list(range(4)) #aqui o '4' é o fim (início é 0 e passo é 1 e estão omissos)
print(lista_1)
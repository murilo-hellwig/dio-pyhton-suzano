#modos de passar os argumentos
#posicionais
def carros(modelo, ano, placa, marca, cor, motor):
    print(f'Modelo: {modelo}, Ano: {ano}, Placa: {placa}, Marca: {marca}, Cor: {cor}, Motor: {motor}')

carros('Fusca', 1970, 'ABC-1234', 'Volkswagen', 'azul', '1.3')

#nomeados
def carros_2(modelo, ano, placa, marca, cor, motor):
    print(f'Modelo: {modelo}, Ano: {ano}, Placa: {placa}, Marca: {marca}, Cor: {cor}, Motor: {motor}')

carros_2(modelo='Fusca', ano=1970, placa='ABC-1234', marca='Volkswagen', cor='azul', motor='1.3')

#hibridos
def carros_3(modelo, ano, placa, /, *, marca, cor, motor):
    print(f'Modelo: {modelo}, Ano: {ano}, Placa: {placa}, Marca: {marca}, Cor: {cor}, Motor: {motor}')

carros_3('Fusca', 1970, 'ABC-1234', marca='Volkswagen', cor='azul', motor='1.3')


#usando função como variavel para outra função
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
def calcular(funcao, x, y):
    resultado = funcao(x, y)
    print(f"O resultado da operação {x} + {y} é: {resultado}")

#abaixo estamos usando a função somar como argumento para a função calcular
calcular(somar, 5, 3)
#abaixo estamos usando a função subtrair como argumento para a função calcular
calcular(subtrair, 500, 3)

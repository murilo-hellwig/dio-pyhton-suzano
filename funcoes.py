#funções em Python são definidas com a palavra-chave def e servem para agrupar um conjunto de instruções que realizam uma tarefa específica.
#reaproveitamento de código é uma das principais vantagens de se usar funções.
#exemplos

def saudacao():
    print("Olá, intruso!")
    print("Você não deveria estar aqui!")

def saudacao_2(nome):
    print(f"Olá, {nome}!")
    print("Seja bem-vindo(a)!")

def saudacao_3(nome="Anônimo"):
    print(f"Olá, {nome}!")
    print("Seja bem-vindo(a)!")

saudacao()
print("-----")
saudacao_2("João")
print("-----")
saudacao_3()
print("-----")
saudacao_3("Maria")


##função retornando valores
def soma(a, b):
    return a + b 

soma(5, 3)

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro salvo: {marca} {modelo}, Ano: {ano}, Placa: {placa}")
    return f"Carro: {marca} {modelo}, Ano: {ano}"

salvar_carro("Toyota", "Corolla", 2020, "ABC-1234") #usando argumentos posicionais
salvar_carro(marca="Honda", modelo="Civic", ano=2021, placa="XYZ-5678") #usando argumentos nomeados

#os argumentos podem ser definidos como  *args ou **kwargs. Onde são salvos como tuplas (*args) ou dicionarios (**kwargs).
def exibir_informacoes(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)

exibir_informacoes("Python", "Funções", 42, linguagem="Python", ano=2023)


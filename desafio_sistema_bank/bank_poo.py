from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Historico:
    def adicionar_transacao(transacao: Transacao):
        pass

class Conta:
    saldo = float
    numero = int
    agencia = ''
    cliente = Cliente
    historico = historico

    def saldo():
        return float
    
    def nova_conta(cliente:Cliente, numero:int):
        return Conta
    
    def sacar(valor:float):
        return bool
    
    def depositar(valor:float):
        return bool
    
class ContaCorrente(Conta):
    limite = float
    limite_saques = int

class Cliente:
    endereco = ''
    contas = []

    def realizar_transacao(conta : Conta, transacao : Transacao):
        pass

    def adicionar_conta(conta : Conta):
        pass

class PessoaFisica(Cliente):
    cpf = ''
    nome = ''
    data_nascimento = date

class Transacao(ABC):
    pass

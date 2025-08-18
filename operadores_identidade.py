# IS é o operador de identidade
#exemplos abaixo
curso = 'Python DIO'
nome_curso = curso
print(curso is nome_curso)  # True, porque ambos apontam para o mesmo objeto

saldo, limite = 100, 200
print(saldo is limite)  # False, porque são objetos diferentes

saldo, limite = 200, 200
print(saldo is limite)  # True, porque ambos apontam para o mesmo valor
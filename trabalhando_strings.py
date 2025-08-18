#maiusculas, minusculas e titulos
curso = 'pYtHon é muito bom, atualmente estou estudando este asSunTo'

print(curso.upper())  # Converte para maiúsculas
print(curso.lower())  # Converte para minúsculas   
print(curso.title())  # Converte para título (primeira letra de cada palavra em maiúscula)
print(curso.capitalize())  # Converte para capitalização (primeira letra em maiúscula, o resto em minúsculas)

#removendo espaços
curso_2 = '                 python, que tal!          '

print(curso_2)  # Exibe a string original com espaços
print(curso_2.strip())  # Remove espaços no início e no final
print(curso_2.lstrip())  # Remove espaços apenas no início
print(curso_2.rstrip())  # Remove espaços apenas no final

#junções e centralizações

curso_3 = 'Python'
curso_4 = 'pYtHon é a linguagem mais usada atualmente'
curso_5 = 'JAVA'
print(curso_3.center(30, '*'))  # Centraliza a string em um campo de 20 caracteres, preenchendo com '*'
print(curso_3.center(30))
print(curso_5.center(30))
print(".".join(curso_3))
print("_".join(curso_4.split()))  # Junta as palavras com '.'
print(".".join(curso_4))

#formatação de strings
#f-string é uma maneira moderna e eficiente de formatar strings em Python
nome = 'Murilo'
idade = 36
profissao = 'Analista de Sistemas'

print(f'Olá, meu nome é {nome}, tenho {idade} anos e trabalho como {profissao}.')  # Usando f-string

#exemplo do PI, definindo espaços antes da variavel (idef) e casas decimais
PI = 3.141592653589793
print(f'O valor de PI é {PI:.2f}')  # Formata PI com 2 casas decimais
print(f'O valor de PI é {PI:10.2f}')  # Formata PI com 2 casas decimais e alinha à direita em um campo de 10 caracteres



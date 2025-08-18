#para acessar cada valor de uma string, usamos o fatiamento
#é definido como string[inicio:fim:passo] ou string[start:stop:step]
#exemplo
nome = "Murilo Wiegand Hellwig"

nome_fatiado = nome[0:6]  # fatiamento do índice 0 ao 5
print(nome_fatiado)  # Saída: Murilo
nome_fatiado = nome[:6]
print(nome_fatiado)  # Saída: Murilo
nome_fatiado = nome[10:16]
print(nome_fatiado) 
nome_fatiado = nome[14:20:2]
print(nome_fatiado)  # Saída: Hlg
nome_espelhado = nome[::-1]  # Inverte a string
print(nome_espelhado)  # Saída: giwlleH dgniew  
nome_fatiado = nome[:6:-1]
print(nome_fatiado)  # Saída: giwlleH dgniew
nome_fatiado = nome[:-1]
print(nome_fatiado)  # Saída: Murilo Wiegand Hellwi
nome_fatiado = nome[-7:] #as 7 ultimas letras, porque coloquei o -7 no start
print(nome_fatiado)  # Saída: Hellwig
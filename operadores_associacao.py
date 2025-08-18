# Operadores de associação verificam se um objeto está contido em outro, como listas, tuplas ou strings.
curso = 'Curso Python DIO'

'Python' in curso  # Verifica se 'Python' está contido em 'Curso Python DIO'
print('Python' in curso)  # True, porque 'Python' está contido na string

frutas = ['Laranja', 'Maçã', 'Banana']
print('Maçã' in frutas)  # True, porque 'Maçã' está na lista de frutas  

saques = [100, 200, 300]
200 in saques  # Verifica se 200 está na lista de saques
print(200 in saques)  # True, porque 200 está na lista de saques 
print(400 in saques)  # False, porque 400 não está na lista de saques



# Quando for fazer uma comparação de associação, lembre-se de garantir o case, upper ou lower, para evitar erros de comparação.


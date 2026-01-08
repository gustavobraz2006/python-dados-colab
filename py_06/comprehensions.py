# Compreensões de listas em Python
# Exemplo: Criar uma lista de quadrados de números pares de 0 a 9
quadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(quadrados_pares)
# Output: [0, 4, 16, 36, 64]
# Exemplo: Criar uma lista de tuplas (número, quadrado) para números de 0 a 4
tuplas_quadrados = [(x, x**2) for x in range(5)]
print(tuplas_quadrados) 
# Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
# Exemplo: Criar um dicionário de números e seus quadrados para números de 0 a 4
dicionario_quadrados = {x: x**2 for x in range(5)}
print(dicionario_quadrados)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# Exemplo: Criar um conjunto de quadrados únicos de números de 0 a 9
conjunto_quadrados = {x**2 for x in range(10)}
print(conjunto_quadrados)
# Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
# Exemplo: Filtrar e criar uma lista de nomes em maiúsculas
nomes = ['ana', 'bruno', 'carla', 'daniel']
nomes_maiusculas = [nome.upper() for nome in nomes if len(nome) > 3]
print(nomes_maiusculas)
# Output: ['BRUNO', 'CARLA', 'DANIEL']
# Exemplo: Criar uma lista de números pares a partir de uma lista existente
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_pares)

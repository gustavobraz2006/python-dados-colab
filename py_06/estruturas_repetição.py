# Estruturas de repetição em Python
# 1. Loop "for"
# Exemplo: Iterar sobre uma lista de números
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(num)
# Output: 1, 2, 3, 4, 5

# 2. Loop "while"
# Exemplo: Contar até 5
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# Output: 0, 1, 2, 3, 4
# 3. Loop com "break"
# Exemplo: Parar o loop quando o número 3 for encontrado
for num in numeros:
    if num == 3:
        break
    print(num)
# Output: 1, 2
# 4. Loop com "continue"
# Exemplo: Pular o número 3
for num in numeros:
    if num == 3:
        continue
    print(num)
# Output: 1, 2, 4, 5
# 5. Loop aninhado
# Exemplo: Imprimir uma tabela de multiplicação
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-----")
# Output: Tabela de multiplicação de 1 a 5
# 6. Usando "else" com loops
# Exemplo: Verificar se um número é primo
num = 7
for i in range(2, num):
    if num % i == 0:
        print(f"{num} não é primo")
        break
else:
    print(f"{num} é primo")
# Output: 7 é primo
# 7. Loop com "range()"
# Exemplo: Imprimir números de 0 a 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
# 8. Loop com "enumerate()"
# Exemplo: Iterar sobre uma lista com índices
frutas = ['maçã', 'banana', 'cereja']
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
# Output: 0: maçã, 1: banana, 2: cereja
# 9. Loop com "zip()"
# Exemplo: Iterar sobre duas listas simultaneamente
nomes = ['Ana', 'Bruno', 'Carlos']
idades = [25, 30, 35]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")
# Output: Ana tem 25 anos, Bruno tem 30 anos, Carlos tem 35 anos
# 10. Loop com compreensão de listas
# Exemplo: Criar uma lista de quadrados de números
quadrados = [x**2 for x in range(6)]
print(quadrados)
# Output: [0, 1, 4, 9, 16, 25]
# 11. Loop com dicionários
# Exemplo: Iterar sobre chaves e valores de um dicionário
pessoa = {'nome': 'João', 'idade': 28, 'cidade': 'São Paulo'}
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
# Output: nome: João, idade: 28, cidade: São Paulo
# 12. Loop com conjuntos (sets)
# Exemplo: Iterar sobre um conjunto de números únicos
conjunto_numeros = {1, 2, 3, 4, 5}
for num in conjunto_numeros:
    print(num)
# Output: 1, 2, 3, 4, 5 (ordem pode variar)
# 13. Loop infinito (com cuidado!)
# Exemplo: Loop que roda até ser interrompido manualmente
# contador = 0
# while True:
#     print(contador)
#     contador += 1
# Output: Contador incrementando indefinidamente (use Ctrl+C para parar)
# 14. Loop com função "map()"
# Exemplo: Aplicar uma função a todos os itens de uma lista
def dobrar(x):
    return x * 2
numeros_dobrados = list(map(dobrar, numeros))
print(numeros_dobrados)
# Output: [2, 4, 6, 8, 10]
# 15. Loop com função "filter()"
# Exemplo: Filtrar números pares de uma lista
def eh_par(x):
    return x % 2 == 0
numeros_pares = list(filter(eh_par, numeros))
print(numeros_pares)
# Output: [2, 4]

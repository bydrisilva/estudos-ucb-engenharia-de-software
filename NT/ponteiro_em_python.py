# Em C, um ponteiro armazena o endereço de memória de uma variável.
# No Python, tudo é um objeto, e o que chamamos de "variável" é, na verdade, apenas um nome (uma etiqueta) que aponta para um objeto na memória.
# Exemplo do comportamento de "ponteiro":
lista_a = [1, 2, 3]
lista_b = lista_a  # lista_b agora aponta para o mesmo lugar que lista_a

lista_b.append(4)

print(lista_a)  # resultado: [1, 2, 3, 4]
print(lista_b)  # resultado: [1, 2, 3, 4]

# Quando você faz a = b, você não está copiando os dados. Você está dizendo que o nome a agora aponta para o mesmo objeto que b.

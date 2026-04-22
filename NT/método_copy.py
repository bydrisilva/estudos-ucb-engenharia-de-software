# Ele serve para quebrar o vínculo de referência.
# Quando você usa o .copy(), o Python cria um novo objeto na memória com os mesmos valores, mas em um endereço diferente.
# usando o .copy() para separar as coisas
lista_original = [10, 20, 30]
lista_copia = lista_original.copy()

lista_copia.append(40)

print(lista_original) # resultado: [10, 20, 30]
print(lista_copia)   # resultado: [10, 20, 30, 40]

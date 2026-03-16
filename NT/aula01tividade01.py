# ATIVIDADE 04/03 - Calculadora de IMC.
#Escreva um programa que:
#Solicite ao usuário seu nome, peso (kg) e altura (m)1.
#Calcule o IMC: peso / altura²2.
#Exiba o nome do usuário e a classificação correspondente.



# RECEBENDO OS DADOS. 
nome = input("Digite o seu nome:")
 # Delcaramos a variável, imprimimos na tela e pedimos para o usuário digitar com o input.
peso = float(input("Digite o seu peso em kg (ex: 65.5): "))
 # Declaramos outra variável, como topo retorno do usuário é uma STRING, declaramos o float antes para transformar esse dado.
 # Optamos pelo FLOAT ao invés do INT pois o tipo de dado geralmente tem decimais.
altura = float(input("Digite a sua altura em metros (ex: 1.65): "))
 # Declaramos a variável, o tipo dela, um input e a frase que será exibida. 
 
 
 
# 2. CALCULANDO O IMC.
imc = peso / (altura ** 2)
# Os parênteses servem para "Resolver o que está dentro PRIMEIRO!
# Variável ALTURA vezes 2. Depois divide esse valor pela variável PESO.
# O operador ** faz a elevação ao quadrado (altura * altura).
# Declaramos a variável e atribuimos mais duas variáveis a ela e usamos os operadores lógicos.
# ** é para ao quadrado. 



# 3. VERIFICANDO A CLASSIFICAÇÃO.
 # Aqui iniciamos um efeito cascata que lê de cima para baixo. 
if imc < 18.5:
    classificacao = "Abaixo do peso"
 # Se o IMC for menor que 18.5, ele vai retornar a variável CLASSIFICAÇÃO com a frase que está atribuida. 
elif imc < 25:
    classificacao = "Peso normal"
 # Elif (se senão) só será lido se o de cima for falso.
elif imc < 30:
    classificacao = "Sobrepeso"
 # Novamente, o elif (se não) só será lido se o de cima for falso.
else:
    classificacao = "Obesidade"
 #O else (Senão) nunca recebe uma condição matemática do lado dele, ele é o ultimo plano se tudo falhar.



# 4. EXIBINDO O RESULTADO.
print(f"\nResultado de {nome}:")
#Aqui estamos imprimindo na tela, o f deixa chamar uma variável dentro do texto usando {}.
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}.")
# Novamente imprimindo na tela e as variáveis IMC e CLASSIFICACAO está dentro do texto. 
# DICA: O ':.2f' dentro das chaves arredonda o número para apenas 2 casas decimais! o f siginifica FLOAT. Isso evita que tenhamos um numero como 24.958324232...
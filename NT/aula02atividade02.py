# DESAFIO 2: ANALISADOR DE TEXTO:
# Objetivo: Processamento de strings, contagem com dicionários e estatística básica.
# Escreva um programa que receba uma frase do usuário e produza um relatório estatístico sobre ela.
# Contagem de Palavras
# Separe a frase em palavras (.split()) e use um dicionário para contar quantas vezes cada palavra aparece.
# Palavras Únicas:
# Identificar o número de palavras únicas na frase e exibir quais se repetem mais de uma vez.
# Relatório Final:
# Exiba: total de palavras, total de palavras únicas, e a palavra mais frequente.



# 1. ENTRADA DE DADOS
# .lower() padroniza o texto para evitar que "Python" e "python" sejam lidas como diferentes.
frase = input("Digite uma frase para análise: ").lower()

# 2. PROCESSAMENTO INICIAL
# .split() quebra a string em uma lista de palavras usando os espaços como separador.
palavras = frase.split()

# 3. CONTAGEM DE FREQUÊNCIA
# Criamos um dicionário vazio para armazenar {palavra: quantidade}.
contagem = {}

for p in palavras:
    # .get(p, 0) tenta pegar o valor da palavra. Se não existir, retorna 0.
    # Somamos +1 a cada ocorrência encontrada.
    contagem[p] = contagem.get(p, 0) + 1

# 4. IDENTIFICAÇÃO DE PALAVRAS ÚNICAS E REPETIDAS
# Palavras únicas são todas as chaves do dicionário.
total_unicas = len(contagem)

# List Comprehension para filtrar apenas palavras que aparecem mais de uma vez.
repetidas = [palavra for palavra, qtd in contagem.items() if qtd > 1]

# 5. DESCOBRIR A PALAVRA MAIS FREQUENTE
# max() percorre o dicionário e retorna a chave com o maior valor (v).
palavra_mais_frequente = max(contagem, key=contagem.get)

# 6. RELATÓRIO FINAL
print("\n" + "="*30)
print("RELATÓRIO ESTATÍSTICO")
print("="*30)
print(f"Total de palavras: {len(palavras)}")
print(f"Total de palavras únicas: {total_unicas}")
print(f"Palavras que se repetem: {', '.join(repetidas) if repetidas else 'Nenhuma'}")
print(f"Palavra mais frequente: '{palavra_mais_frequente}' ({contagem[palavra_mais_frequente]}x)")
print("="*30)
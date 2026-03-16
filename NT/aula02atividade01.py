# DESAFIO 1: INVENTÁRIO DE LOJA
# Objetivo: Gestão de estoque, cálculos acumulados e filtragem rápida.
# Crie um programa que simule o estoque de uma loja de eletrônicos.
# Estrutura:
# Represente o estoque como uma lista de dicionários, onde cada item possui nome, preco e quantidade.
# Operações:
# Com um laço for, calcule o valor total em estoque (preço × quantidade) e imprima os itens com valor acima de R$ 500.
# Bônus:
# Use uma list comprehension para gerar uma lista só com os nomes dos produtos em falta (quantidade == 0). 



# 1. ESTRUTURA DE DADOS
# Lista [] armazena a ordem; Dicionários {} armazenam os atributos do objeto.
estoque = [
    {"nome": "Fone Bluetooth", "preco": 150.0, "quantidade": 10},
    {"nome": "Teclado Mecânico", "preco": 350.0, "quantidade": 5},
    {"nome": "Monitor 24'", "preco": 850.0, "quantidade": 3},
    {"nome": "Mouse Gamer", "preco": 120.0, "quantidade": 0},
    {"nome": "Cabo HDMI", "preco": 30.0, "quantidade": 0}
]

# 2. VARIÁVEL ACUMULADORA
# Inicializada em 0 para somar os valores durante o loop.
valor_total_estoque = 0

print("--- ITENS COM ALTO VALOR EM ESTOQUE (> R$ 500) ---")

# 3. LAÇO DE REPETIÇÃO (PROCESSAMENTO)
# 'item' referencia cada dicionário da lista por vez.
for item in estoque:
    # Cálculo: Acessamos os valores pelas chaves ["nome_da_chave"].
    valor_individual = item["preco"] * item["quantidade"]
    
    # Soma o valor deste item ao montante total da loja.
    valor_total_estoque += valor_individual
    
    # Condicional: Filtra apenas itens com impacto financeiro alto.
    if valor_individual > 500:
        # :.2f formata para 2 casas decimais.
        print(f"Produto: {item['nome']} | Total: R$ {valor_individual:.2f}")

# 4. SAÍDA DO TOTAL GERAL
print(f"\nValor total geral em estoque: R$ {valor_total_estoque:.2f}")

# 5. BÔNUS: LIST COMPREHENSION (FILTRAGEM PERFORMANCE)
# [resultado | laço | condição] -> Cria lista rápida de produtos esgotados.

produtos_em_falta = [p["nome"] for p in estoque if p["quantidade"] == 0]

print(f"Produtos em falta (estoque 0): {produtos_em_falta}")
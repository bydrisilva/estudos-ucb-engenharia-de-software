# DESAFIO 3: VALIDADOR E ANALISADOR DE SENHAS.
# Objetivo: Validação em loop, verificação de caracteres e classificação de força.
# Crie um programa que solicite uma senha ao usuário em loop até que ela seja válida. Uma senha é válida se:
# Tiver pelo menos 8 caracteres.
# Contiver pelo menos um número (use any() + isdigit()).
# Contiver pelo menos uma letra maiúscula (isupper()).
# Após aceitar a senha, exiba um relatório de segurança:
# Tamanho da senha.
# Quantidade de letras, números e caracteres especiais.
# Nível: Fraca (8–9 chars), Média (10–12), Forte (13+).



print("--- SISTEMA DE CADASTRO DE SENHA ---")
# 1. LOOP DE VALIDAÇÃO
while True:
    senha = input("\nCrie uma senha segura: ")
    
    # Critérios de Validação
    comp_minimo = len(senha) >= 8
    tem_numero = any(caractere.isdigit() for caractere in senha)
    tem_maiuscula = any(caractere.isupper() for caractere in senha)
    
    # Verificação de segurança
    if comp_minimo and tem_numero and tem_maiuscula:
        print("Senha válida e aceita!")
        break
    else:
        print("Senha inválida. Certifique-se de ter:")
        print("- No mínimo 8 caracteres")
        print("- Pelo menos um número")
        print("- Pelo menos uma letra maiúscula")

# 2. ANÁLISE ESTATÍSTICA (Relatório)
qtd_letras = 0
qtd_numeros = 0
qtd_especiais = 0

for c in senha:
    if c.isalpha():
        qtd_letras += 1
    elif c.isdigit():
        qtd_numeros += 1
    else:
        qtd_especiais += 1

# 3. CLASSIFICAÇÃO DE NÍVEL
tamanho = len(senha)
if 8 <= tamanho <= 9:
    nivel = "Fraca"
elif 10 <= tamanho <= 12:
    nivel = "Média"
else:
    nivel = "Forte"

# 4. EXIBIÇÃO DO RELATÓRIO FINAL
print("\n" + "="*30)
print("RELATÓRIO DE SEGURANÇA")
print("="*30)
print(f"Tamanho total: {tamanho} caracteres")
print(f"Letras: {qtd_letras}")
print(f"Números: {qtd_numeros}")
print(f"Especiais: {qtd_especiais}")
print(f"Nível de Segurança: {nivel}")
print("="*30)
# DESAFIO 2: ADIVINHE O NÚMERO.
# Escreva um programa que:
# 1. Defina uma constante NUMERO_SECRETO = 42.
# 2. Defina uma constante MAX_TENTATIVAS = 5.
# 3. Use um while para permitir até 5 tentativas.
# 4. Cada jogada deve ser armazenada numa variável.
# 5. A cada tentativa, diga se o chute foi maior, menor ou correto.
# 6. Ao final, informe se o usuário ganhou ou perdeu.




# 1. DEFINIÇÃO DE CONSTANTES.
# Usamos MAIÚSCULAS para valores fixos. 
# O '=' atribui o valor à direita para o nome à esquerda.
NUMERO_SECRETO = 42 
MAX_TENTATIVAS = 5 

# 2. VARIÁVEIS DE CONTROLE.
tentativa_atual = 1 
# Variável do tipo INT (inteiro) que conta as rodadas.
acertou = False     
# Variável do tipo BOOL (booleano). Começa como Falso.
chute_da_vez = 0   
# Variável que guardará o valor de cada jogada individualmente.

print("JOGO DE ADIVINHAÇÃO")

# 3. ESTRUTURA DE REPETIÇÃO (WHILE).
# O ':' indica que o bloco de código abaixo (indentado) será repetido.
while tentativa_atual <= MAX_TENTATIVAS:
# O while funciona como um if que se repete.
# O IF morre ao final, mas o While continua a rodar novamente depois que finaliza.
# <= (Menor ou Igual): Ele compara os dois valores das variáveis. 
#O Só irá rodar se o resultado for True (verdadeiro).

    # 4. CAPTURA DA JOGADA NA VARIÁVEL.
    # f"..." permite usar a variável {tentativa_atual} dentro da frase.
    # int() converte o texto do input em número para podermos calcular.
    # A variável 'chute_da_vez' é atualizada a cada nova jogada.
    chute_da_vez = int(input(f"Tentativa {tentativa_atual}/{MAX_TENTATIVAS}: "))
    
    # 5. VERIFICAÇÃO COM IF / ELIF / ELSE.
    # 'if' inicia o teste. '==' compara se os dois lados são iguais.
    if chute_da_vez == NUMERO_SECRETO:
        print("Correto!")
        acertou = True 
        # Atribuímos True para indicar vitória.
        break 
        # O 'break' interrompe o loop 'while' imediatamente.
        
    # 'elif' (senão se) testa uma nova condição se o 'if' for falso.
    elif chute_da_vez < NUMERO_SECRETO:
        # '<' é o operador de 'menor que'.
        print("Muito baixo! Tente maior.")
        
    # 'else' (senão) captura qualquer outro caso (neste caso, se for maior).
    else:
        print("Muito alto! Tente menor.")
    
    # 6. ATUALIZAÇÃO DO CONTADOR.
    # Somamos 1 à variável para que o loop avance e não seja infinito.
    tentativa_atual = tentativa_atual + 1

# 7. EXIBIÇÃO DO RESULTADO FINAL.
# Este bloco está fora da indentação (sem o espaço na margem), logo só roda no fim.
if acertou:
    # O '\n' pula uma linha para o texto ficar mais bonito no console.
    print(f"\nParabéns! O seu último chute {chute_da_vez} foi certeiro.")
else:
    # f-string usando a constante NUMERO_SECRETO e a variável final.
    print(f"\nTentativas esgotadas. O número era {NUMERO_SECRETO}. Você perdeu!")
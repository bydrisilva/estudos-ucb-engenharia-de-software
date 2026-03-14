// 1. O computador escolhe um número secreto.
// Math.random gera um decimal (ex: 0.5), multiplicamos por 20 e o floor arredonda para baixo. Somamos 1 para garantir que seja de 1 a 20.
const numSecreto = Math.floor(Math.random() * 20) + 1;

// 2. Criamos uma "gaveta" vazia para guardar o palpite que o usuário vai digitar depois.
let palpite;

// 3. Inicia um laço de repetição.
// Tradução: "Enquanto o palpite for diferente do número secreto, continue perguntando".
while (palpite !== numSecreto) {
    
    // 4. Abre uma caixinha na tela perguntando o número.
    // O comando 'Number' transforma o texto digitado em um número matemático real.
    palpite = Number(prompt("Tente adivinhar o número secreto (entre 1 e 20):"));

    // 5. Se o palpite for MAIOR que o segredo...
    if (palpite > numSecreto) {
        // ...ele avisa no console do VS Code que o número é mais baixo.
        console.log("Dica: O número secreto é menor que " + palpite + ".");
        
    // 6. Se não for maior, mas for MENOR que o segredo...
    } else if (palpite < numSecreto) {
        // ...ele avisa que o número secreto é mais alto.
        console.log("Dica: O número secreto é maior que " + palpite + ".");
        
    // 7. Se não for nem maior nem menor, significa que o usuário ACERTOU!
    } else if (palpite === numSecreto) {
        // Exibe a mensagem de vitória usando Template Literal (o tal do $ que vimos).
        console.log(`Parabéns, Adrielle! Você acertou. O número era ${numSecreto}.`);
        
    // 8. Caso o usuário digite algo que não seja um número (como uma letra).
    } else {
        console.log("Ops! Isso não parece um número válido.");
    }
}
// 9. O jogo termina aqui porque o laço 'while' percebeu que palpite agora é IGUAL ao numSecreto.
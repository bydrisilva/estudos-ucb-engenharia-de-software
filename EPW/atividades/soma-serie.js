// 1. Entrada: Quantos termos a série terá.
let n = Number(prompt("Digite a quantidade de termos:"));

let termoAtual = 0; // Guarda o número atual da série (ex: 111).
let somaTotal = 0;  // Acumula a soma de todos os termos.
let serieTexto = ""; // Guarda o texto da sequência para exibir no final.

// 2. Laço 'for' para gerar cada termo.
for (let i = 1; i <= n; i++) {
    
    // Lógica Matemática: Multiplica por 10 e soma 1.
    // Ex: (1 * 10) + 1 = 11 | (11 * 10) + 1 = 111.
    termoAtual = (termoAtual * 10) + 1;
    
    // Soma o novo número ao total.
    somaTotal += termoAtual;

    // Monta o texto da série (adiciona o '+' entre os números).
    serieTexto += (i === n) ? `${termoAtual}` : `${termoAtual} + `;
}

// 3. Saída: Exibe a sequência e o resultado final.
console.log(serieTexto);
console.log(`A soma é: ${somaTotal.toLocaleString('pt-BR')}`);
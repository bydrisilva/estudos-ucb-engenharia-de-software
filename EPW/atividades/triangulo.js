// 1. Entrada: Pergunta quantas linhas o triângulo terá.
let linhas = Number(prompt("Digite o número de linhas para o triângulo:"));

// 2. Laço externo: Controla cada linha do triângulo.
for (let i = 1; i <= linhas; i++) {
    
    let asteriscos = ""; // Gaveta vazia para montar a linha atual.

    // 3. Laço interno: Adiciona a quantidade certa de estrelas (*) na linha.
    for (let j = 1; j <= i; j++) {
        asteriscos += "*"; // Soma um asterisco à linha.
    }

    // 4. Saída: Imprime a linha montada no console.
    console.log(asteriscos);
}
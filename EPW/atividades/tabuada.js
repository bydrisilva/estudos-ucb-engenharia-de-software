// 1. Entrada: Pede o número e converte para tipo numérico.
let numero = Number(prompt("Digite um número para ver a tabuada:"));

console.log(`Tabuada do ${numero}:`); 

// 2. Laço de repetição 'for'.
// (Começa em 1; vai até 10; aumenta de 1 em 1).
for (let i = 1; i <= 10; i++) { 
    
    // 3. Processamento e Saída formatada.
    // Usamos Template Literal para montar a "tabela".
    let resultado = numero * i;
    console.log(`${numero} x ${i} = ${resultado}`); 
}
// 1. Entrada do usuário via prompt.
// .toLowerCase() converte para minúsculo para facilitar a comparação.
let escolhaUsuario = prompt("Escolha: Pedra, Papel ou Tesoura?").toLowerCase();

// 2. O Computador escolhe aleatoriamente.
// Math.random gera um número, multiplicamos por 3 e arredondamos para baixo (0, 1 ou 2).
let opcoes = ["pedra", "papel", "tesoura"]; 
let escolhaComputador = opcoes[Math.floor(Math.random() * 3)]; 

console.log(`Você escolheu: ${escolhaUsuario}`); 
console.log(`Computador escolheu: ${escolhaComputador}`);

// 3. Lógica para determinar o vencedor.
if (escolhaUsuario === escolhaComputador) {
    console.log("Resultado: Empate!");
} else if (
    (escolhaUsuario === "pedra" && escolhaComputador === "tesoura") ||
    (escolhaUsuario === "papel" && escolhaComputador === "pedra") ||
    (escolhaUsuario === "tesoura" && escolhaComputador === "papel")
) {
    console.log("Resultado: Você venceu!"); 
} else {
    console.log("Resultado: O computador venceu!"); 
}
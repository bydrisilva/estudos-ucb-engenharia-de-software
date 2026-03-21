//alert("Olá mundo!");

//variáveis
// var (escopo global e local - função) - reatribuição
var animal = "gato";
console.log(animal);
animal = 'peixe'
console.log(animal)

// let (escopo local) - reatribuição
let nomeCompleto = "Fulano da Silva";
console.log(nomeCompleto);
nomeCompleto = "Beltrano";

// const (escopo global e local) - não permite reatribuição
const valor0 = 10;
//valor0= 20; não é permitido para o tipo const
var valor1;

//verificar o tipo de dados (typeof)
console.log(typeof valor0);
console.log(typeof nomeCompleto);

//algoritmo: entrada + processamento + saída
//var nome = window.prompt("Digite o nome: ");

//console.log("Nome digitado: " + nome + " Aproveite.");

//template literal: html + string + variáveis
//console.log(`Nome: ${nome}. Aproveite`);

// operadores aritméticos: + - * / ** %
// (2 + 2) * 5

//operadores de comparação: < > >= <= == !=
// === !==
console.log(5 == '5'); // olha apenas os valores
console.log(5 === '5'); // olha tipo e valor
// E LÓGICO 
// OU LÓGICO


//DESAFIO:
//Criar um sistema que realize a soma de dois números
//O usuário vai informar esses números
//Apresente o resultado no console.log
var n1 = parseFloat(window.prompt("N1: "));
console.log(typeof n1);
var n2 = parseFloat(window.prompt("N2: "));
var resultado = n1 + n2;
console.log("Resultado: " + resultado);
document.writeln(`<b>Resultado: ${resultado}<b>`);

//estruturas de controle: if-else / switch-case
var hora = 10;
if(hora < 12) {
    console.log("bom dia");
} else if (hora < 18) { 
    console.log("boa tarde");
} else {
    console.log("boa noite");
}

var diaSemana = 2;
switch (diaSemana) {
    case 1:
        console.log("domingo");
        break;
    case 2:
        console.log("segunda-feira");
        break;
    default:
        console.log("escolha uma opção");
}

//estruturas de repetição: for e while
for (let i=0;i<10;i++){
    console.log("Valor: " + i); //break e continue
}

var n = 5;
while (n < 5){
    console.log(n);
    n++;
}

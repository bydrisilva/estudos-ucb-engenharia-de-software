// Sintaxe do manipulador.

// 1. Evento de clique no botão 1.
botao1.onclick = function() {
    alert("Clique!"); // Exibe alerta ao clicar.
};

// 2. Busca o elemento pelo ID 'botao2'.
let botao2 = document.getElementById("botao2");

// 3. Muda cor para vermelho quando o mouse passa em cima.
botao2.onmouseover = function() {
    botao2.style.backgroundColor = "red";
};

// 4. Volta a cor original (vazia) quando o mouse sai de cima.
botao2.onmouseout = function() {
    botao2.style.backgroundColor = "";
};
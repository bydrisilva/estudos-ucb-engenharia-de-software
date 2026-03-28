// --- Lógica do contador ---
let total = 0;
const display = document.getElementById("numContador");

document.getElementById("btnMais").onclick = () => {
    total++;
    display.textContent = total;
};

document.getElementById("btnMenos").onclick = () => {
    if (total > 0) total--; 
    display.textContent = total;
};

// --- Bloco de notas (Retorno em tempo real) ---
const notaInput = document.getElementById("inputNota");
const feedbackSaida = document.getElementById("msgFeedback");

notaInput.addEventListener("input", () => {
    // Retorna exatamente o que você digitar no parágrafo abaixo
    feedbackSaida.textContent = `Você registrou: ${notaInput.value}`; 
});

// --- Gerador de lista aleatória com dados do usuário ---
const btnGerar = document.getElementById("btnGerar");
const painel = document.getElementById("painelLista");

btnGerar.onclick = () => {
    const textoUsuario = document.getElementById("itensLista").value;
    const tag = document.getElementById("estiloLista").value;
    
    // Transforma o texto digitado em um Array (separando por vírgula)
    let itensArray = textoUsuario.split(",").map(item => item.trim());

    // Se a caixa estiver vazia, não faz nada
    if (textoUsuario === "") return alert("Por favor, digite algo para a lista!");

    const listaFinal = document.createElement(tag);

    // Lógica Aleatória: embaralha se for 'ul'
    if (tag === "ul") {
        itensArray.sort(() => Math.random() - 0.5); 
    }

    // Cria os elementos LI dinamicamente
    itensArray.forEach(itemTexto => {
        let li = document.createElement("li");
        li.textContent = itemTexto;
        listaFinal.appendChild(li);
    });

    painel.innerHTML = ""; // Limpa a lista anterior
    painel.appendChild(listaFinal);
};
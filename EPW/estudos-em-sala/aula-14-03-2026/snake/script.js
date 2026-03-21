const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const tamanho = 20;

let snake = [
    {x:200, y:200}
];

let direcao = "right";

let comida = {
    x:100,
    y:100
};

function desenharComida(){

    ctx.fillStyle = "red";
    ctx.fillRect(comida.x, comida.y, tamanho, tamanho);

}

function desenharSnake(){

    ctx.fillStyle = "lime";

    for(let i = 0; i < snake.length; i++){

        ctx.fillRect(snake[i].x, snake[i].y, tamanho, tamanho);

    }

}

function moverSnake(){

    let head = {x:snake[0].x, y:snake[0].y};

    if(direcao === "right") head.x += tamanho;
    if(direcao === "left") head.x -= tamanho;
    if(direcao === "up") head.y -= tamanho;
    if(direcao === "down") head.y += tamanho;

    snake.unshift(head);

    if(head.x === comida.x && head.y === comida.y){

        comida.x = Math.floor(Math.random() * 20) * tamanho;
        comida.y = Math.floor(Math.random() * 20) * tamanho;

    }else{

        snake.pop();

    }

}

function colisao(){

    let head = snake[0];

    if(
        head.x < 0 ||
        head.y < 0 ||
        head.x >= canvas.width ||
        head.y >= canvas.height
    ){

        alert("Game Over");

        snake = [{x:200,y:200}];
        direcao = "right";

    }

    for(let i = 1; i < snake.length; i++){

        if(head.x === snake[i].x && head.y === snake[i].y){

            alert("Game Over");

            snake = [{x:200,y:200}];
            direcao = "right";

        }

    }

}

function atualizar(){

    ctx.clearRect(0,0,canvas.width,canvas.height);

    desenharComida();

    moverSnake();

    colisao();

    desenharSnake();

}

document.addEventListener("keydown", function(event){

    if(event.key === "ArrowRight" && direcao !== "left") direcao = "right";
    if(event.key === "ArrowLeft" && direcao !== "right") direcao = "left";
    if(event.key === "ArrowUp" && direcao !== "down") direcao = "up";
    if(event.key === "ArrowDown" && direcao !== "up") direcao = "down";

});

setInterval(atualizar, 100);

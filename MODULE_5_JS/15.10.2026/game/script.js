const gameContainer = document.getElementById('gameContainer');
const player = document.getElementById('player');
const startScreen = document.getElementById('startScreen');
const startBtn = document.getElementById('startBtn');


let isPlaying = false; 

let playerX = 325; //начальная координата X;
const playerSpeed = 12;
const playerWidth = 60;

let gameInterval;



let keys = {}//отслеживание нажатых клавиш
let bullets = []//для хранения активных снарядов
let enemies = [];
let enemyBullets = [];


// отслеживаем нажатие клавиш
window.addEventListener('keydown', (e)=>{
    keys[e.code] = true;
    if (e.code === 'Space' && isPlaying){
        shootBullet();
    }    
});

window.addEventListener('keyup', (e)=>{
    keys[e.code] = false;
});

startBtn.addEventListener('click', startGame);

function startGame(){
    startScreen.classList.add('hidden');

    playerX = (gameContainer.clientWidth/2) - (playerWidth/2);
    player.style.left = playerX + 'px';
    isPlaying = true;

    clearInterval(gameInterval);
    gameInterval = setInterval(updateGame, 1000/60);
}

function shootBullet(){
    const bullet = document.createElement('div');
    bullet.classList.add('bullet');
    bullet.style.left = (playerX + playerWidth / 2 - 2.5)+'px';
    bullet.style.top = (gameContainer.clientHeight - 80) + 'px';
    gameContainer.appendChild(bullet);
    bullets.push(bullet);
}


function spawnEnemy(){
    if (Math.random() <= 0.03){
        const enemy = document.createElement('div');
        enemy.classList.add('enemy');
        const maxSpawnX = gameContainer.clientWidth - 50;
        const enemyX = Math.random() * maxSpawnX;
        enemy.style.left = enemyX + 'px';
        enemy.style.top = '-50px';
        gameContainer.appendChild(enemy);
        enemies.push({element: enemy, x: enemyX, y: -50, lastShot: 0});
    }
}

function updateGame(){
    const gameWidth = gameContainer.clientWidth;
    const gameHeight = gameContainer.clientHeight;

    if (keys['ArrowLeft'] && playerX > 0) {
        playerX -= playerSpeed;
    }

    if (keys['ArrowRight'] && playerX < gameWidth - playerWidth){
        playerX += playerSpeed;
    }
    player.style.left = playerX + 'px';

        //генерация врагов
    spawnEnemy();

    // движение снарядов
    for (let i = bullets.length - 1; i >= 0; i--){
        let b = bullets[i];
        // получаем вертикальную позицию пули
        let currentTop = parseInt(b.style.top);
        currentTop -= 10; 
        if (currentTop < 0){
            b.remove()
            bullets.splice(i, 1);
        }else{
            b.style.top = currentTop + 'px';
        }
    }

    // движение врагов и их стрельба
    for (let i = enemies.length - 1; i >=0 ; i--){
        let e = enemies[i];
        e.y += 1;
        e.element.style.top = e.y + 'px';

        let now = Date.now();
        if (now - e.lastShot > 2000 && Math.random() < 0.25 ){
            e.lastShot = now;
            const eb = document.createElement('div');
            eb.classList.add('enemy-bullet');
            eb.style.top = (e.x + 25 - 2.5) + 'px';
            eb.style.left = (e.y + 50) + 'px';
            gameContainer.appendChild(eb);
            enemyBullets.push(eb);
        }
    }

    for (let i = enemyBullets.length - 1; i >= 0; i--){
        let eb = enemyBullets[i];
        let currentTop = parseInt(eb.style.top);
        currentTop += 2;
        if (currentTop > gameHeight){
            eb.remove();
            enemyBullets.splice(i, 1);
        }else{
            eb.style.top = currentTop + 'px';
        }
    }


}

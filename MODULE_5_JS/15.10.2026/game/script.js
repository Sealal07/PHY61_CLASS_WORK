const gameContainer = document.getElementById('gameContainer');
const player = document.getElementById('player');
const startScreen = document.getElementById('startScreen');

const gameOverScreen = document.getElementById('gameOver');

const startBtn = document.getElementById('startBtn');
const scoreEl = document.getElementById('score');
const timerEl = document.getElementById('timer');
const livesEl = document.getElementById('lives');
const restartBtn = document.getElementById('restartBtn');
const saveBtn = document.getElementById('saveBtn');
const finalScore = document.getElementById('finalScore');
const leaderList = document.getElementById('leaderList');
const playerName = document.getElementById('playerName');

let isPlaying = false; 

let playerX = 325; //начальная координата X;
const playerSpeed = 12;
const playerWidth = 60;
const playerHeight = 60;

let score = 0;
let lives = 0;
let gameTime = 60; // время игры в секундах
let gameInterval;
let timerInterval;




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
restartBtn.addEventListener('click', startGame);
saveBtn.addEventListener('click', saveResult);

updateLeaderBoard(); // подгрузка результатов

function startGame(){
    clearObjects(); //очистка состояния

    startScreen.classList.add('hidden');

    gameOverScreen.classList.add('hidden'); //скрываем экран
    
    restartBtn.classList.add('hidden');
    saveBtn.classList.add('hidden');
    playerName.classList.add('hidden');
    playerName.value = '';

    score = 0;
    lives = 3;
    gameTime = 60;

    scoreEl.textContent = score;
    livesEl.textContent = lives;
    timerEl.textContent = gameTime;


    playerX = (gameContainer.clientWidth/2) - (playerWidth/2);
    player.style.left = playerX + 'px';
    player.style.display = 'block';

    isPlaying = true;

    clearInterval(gameInterval);
    clearInterval(timerInterval);

    gameInterval = setInterval(updateGame, 1000/60);

    timerInterval = setInterval(()=> {
        if (isPlaying) {
            gameTime--;
            timerEl.textContent = gameTime;
            if (gameTime <= 0){
                endGame('время вышло!'); // функция сделать
            }
        }
    }, 1000);
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
    if (Math.random() <= 0.02){
        const enemy = document.createElement('div');
        enemy.classList.add('enemy');
        const maxSpawnX = gameContainer.clientWidth - 50;
        const enemyX = Math.random() * maxSpawnX;
        enemy.style.left = enemyX + 'px';
        enemy.style.top = '-50px';
        gameContainer.appendChild(enemy);
        enemies.push({element: enemy, 
                       x: enemyX, 
                       y: -50, 
                       width: 50,
                       height: 50,
                       lastShot: Date.now()});
    }
}

function updateGame(){
    if (!isPlaying) return;

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
            // попадание пули во врагов
            const bRect = {x: parseInt(b.style.left), 
                           y: currentTop, 
                           width: 5,
                           height: 15};


            for (let j = enemies.length - 1; j >= 0; j--){
                let e = enemies[j];
                if (isCollided(bRect, e)){
                    e.element.remove();
                    enemies.splice(j, 1);
                    b.remove();
                    bullets.splice(i, 1);
                    score += 100;
                    scoreEl.textContent = score;
                    break;
                }
            }
        }  
    }

    // движение врагов и их стрельба
    const playerY = gameContainer.clientHeight - playerHeight - 20;
    const playerRect = { x: playerX, 
                        y: playerY,
                        width: playerWidth, 
                        height: playerHeight};

    for (let i = enemies.length - 1; i >=0 ; i--){
        let e = enemies[i];
        e.y += 1;
        e.element.style.top = e.y + 'px';

        let now = Date.now();
        if (now - e.lastShot > 3500 && Math.random() < 0.25 ){
            e.lastShot = now;
            const eb = document.createElement('div');
            eb.classList.add('enemy-bullet');
            eb.style.left = (e.x + 25 - 2.5) + 'px';
            eb.style.top = (e.y + 50) + 'px';
            gameContainer.appendChild(eb);
            enemyBullets.push({element: eb, 
                                x: e.x + e.width / 2 - 2.5,
                                y: e.y + e.height,
                                width: 5, height: 15
                            });
        }
        if (isCollided(e, playerRect)){
            e.element.remove();
            enemies.splice(i, 1);
            takeDamage(); // функция написать
        }else if (e.y > gameHeight){
            e.element.remove();
            enemies.splice(i, 1);
        }

    }

    for (let i = enemyBullets.length - 1; i >= 0; i--){
        let eb = enemyBullets[i];
        eb.y += 2;
        eb.element.style.top = eb.y + 'px';

        if (isCollided(eb, playerRect)){
            eb.element.remove();
            enemyBullets.splice(i, 1);
            takeDamage();
        }else if (eb.y > gameHeight){
            eb.element.remove();
            enemyBullets.splice(i, 1);
        }
    }
}


function takeDamage(){
    lives--;
    livesEl.textContent = lives;
    player.style.opacity = '0.3';
    setTimeout(()=>{player.style.opacity = '1';}, 200);
    if (lives <= 0){
        endGame('Вы проиграли');
    }
}

function isCollided(rect1, rect2){
    return (
        rect1.x < rect2.x + rect2.width && 
        rect1.x + rect1.width > rect2.x &&
        rect1.y < rect2.y + rect2.height &&
        rect1.y + rect1.height > rect2.y
    );
}

function endGame(message){
    isPlaying = false;
    clearInterval(gameInterval);
    clearInterval(timerInterval);

    finalScore.textContent = `Ваш результат: ${score}`;
    gameOverScreen.classList.remove('hidden');
}

function saveResult(){
    const name = playerName.value;
    let leaderboard = JSON.parse(localStorage.getItem('space')) || [];
    leaderboard.push({name: name, score: score});
    localStorage.setItem('space', JSON.stringify(leaderboard));

    updateLeaderBoard();
    restartBtn.classList.remove('hidden');
}
function clearObjects(){
    bullets.forEach(b => b.remove());
    enemies.forEach(e => e.element.remove());
    enemyBullets.forEach(eb => eb.element.remove());

    bullets = [];
    enemies = [];
    enemyBullets = [];
}

function updateLeaderBoard(){}
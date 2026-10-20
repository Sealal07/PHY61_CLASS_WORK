const gameContainer = document.getElementById('gameContainer');
const player = document.getElementById('player');
const startScreen = document.getElementById('startScreen');
const gameOverScreen = document.getElementById('gameOver');
const startBtn = document.getElementById('startBtn');
const restartBtn = document.getElementById('restartBtn');
const scoreEl = document.getElementById('score');
const timerEl = document.getElementById('timer');
const livesEl = document.getElementById('lives');

let isPlaying = false; 

let playerX = 325; // начальная координата X
const playerSpeed = 12;
const playerWidth = 60;
const playerHeight = 60;

let score = 0;
let lives = 3;
let gameTime = 60; // время игры в секундах
let gameInterval;
let timerInterval;

let keys = {}; // отслеживание нажатых клавиш
let bullets = []; // для хранения активных снарядов игрока
let enemies = []; // массив врагов
let enemyBullets = []; // массив вражеских снарядов

// Отслеживаем нажатие клавиш
window.addEventListener('keydown', (e) => {
    keys[e.code] = true;
    if (e.code === 'Space' && isPlaying){
        shootBullet();
    }    
});

window.addEventListener('keyup', (e) => {
    keys[e.code] = false;
});

startBtn.addEventListener('click', startGame);
restartBtn.addEventListener('click', startGame);

function startGame(){
    startScreen.classList.add('hidden');
    gameOverScreen.classList.add('hidden');

    // Очищаем старые объекты на поле, если они остались
    clearGameObjects();

    score = 0;
    lives = 3;
    gameTime = 60;

    scoreEl.textContent = score;
    livesEl.textContent = lives;
    timerEl.textContent = gameTime;

    playerX = (gameContainer.clientWidth / 2) - (playerWidth / 2);
    player.style.left = playerX + 'px';
    player.style.display = 'block';

    isPlaying = true;

    clearInterval(gameInterval);
    clearInterval(timerInterval);

    gameInterval = setInterval(updateGame, 1000 / 60);

    timerInterval = setInterval(() => {
        if (isPlaying) {
            gameTime--;
            timerEl.textContent = gameTime;
            if (gameTime <= 0){
                endGame('Время вышло!');
            }
        }
    }, 1000);
}

function shootBullet(){
    const bullet = document.createElement('div');
    bullet.classList.add('bullet');
    bullet.style.left = (playerX + playerWidth / 2 - 2.5) + 'px';
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
        
        // Обязательно передаем width и height для корректных коллизий
        enemies.push({
            element: enemy, 
            x: enemyX, 
            y: -50, 
            width: 50, 
            height: 50, 
            lastShot: Date.now()
        });
    }
}

function updateGame(){
    if (!isPlaying) return;

    const gameWidth = gameContainer.clientWidth;
    const gameHeight = gameContainer.clientHeight;

    // Управление игроком
    if (keys['ArrowLeft'] && playerX > 0) {
        playerX -= playerSpeed;
    }
    if (keys['ArrowRight'] && playerX < gameWidth - playerWidth){
        playerX += playerSpeed;
    }
    player.style.left = playerX + 'px';

    // Генерация врагов
    spawnEnemy();

    // 1. Движение снарядов ИГРОКА и проверка попаданий во врагов
    for (let i = bullets.length - 1; i >= 0; i--){
        let b = bullets[i];
        let currentTop = parseInt(b.style.top);
        currentTop -= 10; 
        
        if (currentTop < 0){
            b.remove();
            bullets.splice(i, 1);
        } else {
            b.style.top = currentTop + 'px';
            
            const bRect = { 
                x: parseInt(b.style.left), 
                y: currentTop, 
                width: 5, 
                height: 15 
            };

            // ИСПРАВЛЕНО: используем индекс j для врагов
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

    // Правильные координаты игрока для проверки столкновений
    const playerY = gameHeight - playerHeight - 20; // 20px - отступ снизу у игрока в CSS
    const playerRect = { 
        x: playerX, 
        y: playerY, 
        width: playerWidth, 
        height: playerHeight 
    };

    // 2. Движение ВРАГОВ, их стрельба и столкновение с игроком
    for (let i = enemies.length - 1; i >= 0; i--){
        let e = enemies[i];
        e.y += 1;
        e.element.style.top = e.y + 'px';

        // Стрельба врага (реже, раз в 3.5 секунды, из центра)
        let now = Date.now();
        if (now - e.lastShot > 3500 && Math.random() < 0.25){
            e.lastShot = now;
            const eb = document.createElement('div');
            eb.classList.add('enemy-bullet');
            
            // Вычисляем центр врага по X
            const ebX = e.x + e.width / 2 - 2.5;
            const ebY = e.y + e.height;

            eb.style.left = ebX + 'px';
            eb.style.top = ebY + 'px';
            gameContainer.appendChild(eb);

            enemyBullets.push({
                element: eb, 
                x: ebX,
                y: ebY,
                width: 5,
                height: 15
            });
        }

        // Столкновение врага с игроком
        if (isCollided(e, playerRect)){
            e.element.remove();
            enemies.splice(i, 1);
            takeDamage();
        } else if (e.y > gameHeight){
            e.element.remove();
            enemies.splice(i, 1);
        }
    }

    // 3. Движение СНАРЯДОВ ВРАГА и проверка попадания в игрока
    for (let i = enemyBullets.length - 1; i >= 0; i--){
        let eb = enemyBullets[i];
        eb.y += 3; // скорость вражеской пули
        eb.element.style.top = eb.y + 'px';

        // Проверяем столкновение вражеской пули с игроком
        if (isCollided(eb, playerRect)){
            eb.element.remove();
            enemyBullets.splice(i, 1);
            takeDamage();
        } else if (eb.y > gameHeight){
            eb.element.remove();
            enemyBullets.splice(i, 1);
        }
    }
}

// Функция получения урона
function takeDamage(){
    lives--;
    livesEl.textContent = lives;
    player.style.opacity = '0.3';
    setTimeout(() => { player.style.opacity = '1'; }, 200);
    
    if (lives <= 0){
        endGame('Вы проиграли!');
    }
}

// ИСПРАВЛЕНО: Правильная формула проверки пересечения прямоугольников (AABB)
function isCollided(rect1, rect2){
    return (
        rect1.x < rect2.x + rect2.width && 
        rect1.x + rect1.width > rect2.x &&
        rect1.y < rect2.y + rect2.height &&
        rect1.y + rect1.height > rect2.y
    );
}

// ДОБАВЛЕНО: Функция окончания игры
function endGame(message){
    isPlaying = false;
    clearInterval(gameInterval);
    clearInterval(timerInterval);

    // Меняем текст на экране окончания (можно добавить элемент для текста, если нужно)
    const gameOverTitle = gameOverScreen.querySelector('h1');
    if (gameOverTitle) gameOverTitle.textContent = message;

    gameOverScreen.classList.remove('hidden');
}

// Очистка массивов и DOM-элементов при перезапуске
function clearGameObjects(){
    bullets.forEach(b => b.remove());
    enemies.forEach(e => e.element.remove());
    enemyBullets.forEach(eb => eb.element.remove());

    bullets = [];
    enemies = [];
    enemyBullets = [];
}
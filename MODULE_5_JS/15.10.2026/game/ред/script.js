// const gameContainer = document.getElementById('gameContainer');
// const player = document.getElementById('player');
// const startScreen = document.getElementById('startScreen');
//  #const gameOverScreen = document.getElementById('gameOver');
// const startBtn = document.getElementById('startBtn');
 // #const restartBtn = document.getElementById('restartBtn');
 // #const saveBtn = document.getElementById('saveBtn');
 // #const playerNameInput = document.getElementById('playerName');
 // #const finalScoreText = document.getElementById('finalScoreText');

 // // #const scoreEl = document.getElementById('score');
 // // #const timerEl = document.getElementById('timer');
 // // #const livesEl = document.getElementById('lives');
 // #const leaderboardList = document.getElementById('leaderboardList');

// Параметры игрока
// let isPlaying = false; 
// let playerX = 325; 
// const playerSpeed = 12;
// const playerWidth = 60;
 // #const playerHeight = 60;

// Игровое состояние
 // #let score = 0;
 // #let lives = 3;
 // #let gameTime = 60; // Время игры в секундах
// let gameInterval;
 // #let timerInterval;

// let keys = {};
// let bullets = [];
// let enemies = [];
// let enemyBullets = [];

// Отслеживаем клавиши
// window.addEventListener('keydown', (e) => {
//     keys[e.code] = true;
//     if (e.code === 'Space' && isPlaying) {
//         shootBullet();
//     }    
// });

// window.addEventListener('keyup', (e) => {
//     keys[e.code] = false;
// });

// startBtn.addEventListener('click', startGame);
 // #restartBtn.addEventListener('click', startGame);
 // #saveBtn.addEventListener('click', saveResult);

// Первоначальная загрузка таблицы рекордов
//  #updateLeaderboardUI();

// function startGame() {
//     // Очистка предыдущего состояния
//     clearGameObjects();

    // startScreen.classList.add('hidden');
     // #gameOverScreen.classList.add('hidden');
     // #restartBtn.classList.add('hidden');
     // #saveBtn.classList.remove('hidden');
     // #playerNameInput.classList.remove('hidden');
     // #playerNameInput.value = '';

     // #score = 0;
     // #lives = 3;
     // #gameTime = 60;

     // #scoreEl.textContent = score;
     // #livesEl.textContent = lives;
     // #timerEl.textContent = gameTime;

    // playerX = (gameContainer.clientWidth / 2) - (playerWidth / 2);
    // player.style.left = playerX + 'px';
     // #player.style.display = 'block';

    // isPlaying = true;

    // clearInterval(gameInterval);
    // clearInterval(timerInterval);

    // Запуск игрового цикла и таймера
//     gameInterval = setInterval(updateGame, 1000 / 60);
//     timerInterval = setInterval(() => {
//         if (isPlaying) {
//             gameTime--;
//             timerEl.textContent = gameTime;
//             if (gameTime <= 0) {
//                 endGame('Время вышло!');
//             }
//         }
//     }, 1000);
// }

// function shootBullet() {
//     const bullet = document.createElement('div');
//     bullet.classList.add('bullet');
//     // Позиционируем пулю точно по центру игрока
//     bullet.style.left = (playerX + playerWidth / 2 - 2.5) + 'px';
//     bullet.style.top = (gameContainer.clientHeight - 80) + 'px';
//     gameContainer.appendChild(bullet);
//     bullets.push(bullet);
// }

// function spawnEnemy() {
//     if (Math.random() <= 0.02) { // Немного снизили частоту спавна
//         const enemy = document.createElement('div');
//         enemy.classList.add('enemy');
//         const maxSpawnX = gameContainer.clientWidth - 50;
//         const enemyX = Math.random() * maxSpawnX;
//         enemy.style.left = enemyX + 'px';
//         enemy.style.top = '-50px';
//         gameContainer.appendChild(enemy);
//         enemies.push({ element: enemy, x: enemyX, y: -50, width: 50, height: 50, lastShot: Date.now() });
//     }
// }

// function updateGame() {
    // #if (!isPlaying) return;

    // const gameWidth = gameContainer.clientWidth;
    // const gameHeight = gameContainer.clientHeight;

    // Движение игрока
    // if (keys['ArrowLeft'] && playerX > 0) {
    //     playerX -= playerSpeed;
    // }
    // if (keys['ArrowRight'] && playerX < gameWidth - playerWidth) {
    //     playerX += playerSpeed;
    // }
    // player.style.left = playerX + 'px';

    // Генерация врагов
    // spawnEnemy();

    // Движение снарядов игрока
    // for (let i = bullets.length - 1; i >= 0; i--) {
    //     let b = bullets[i];
    //     let currentTop = parseInt(b.style.top);
    //     currentTop -= 10; 

    //     if (currentTop < 0) {
    //         b.remove();
    //         bullets.splice(i, 1);
    //     } else {
    //         b.style.top = currentTop + 'px';

    //         // Проверка попадания пули игрока во врагов
    //         const bRect = { x: parseInt(b.style.left), y: currentTop, width: 5, height: 15 };
    //         for (let j = enemies.length - 1; j >= 0; j--) {
    //             let e = enemies[j];
    //             if (isColliding(bRect, e)) {
    //                 // Враг уничтожен
    //                 e.element.remove();
    //                 enemies.splice(j, 1);

    //                 // Пуля уничтожена
    //                 b.remove();
    //                 bullets.splice(i, 1);

    //                 score += 100;
    //                 scoreEl.textContent = score;
    //                 break;
    //             }
    //         }
    //     }
    // }

    // Движение врагов и их стрельба
//     const playerY = gameHeight - 80;
//     const playerRect = { x: playerX, y: playerY, width: playerWidth, height: playerHeight };

//     for (let i = enemies.length - 1; i >= 0; i--) {
//         let e = enemies[i];
//         e.y += 2;
//         e.element.style.top = e.y + 'px';

//         // ИСПРАВЛЕНО: Стрельба врага РЕЖЕ (раз в 3.5 секунды) и ИЗ ЦЕНТРА
//         let now = Date.now();
//         if (now - e.lastShot > 3500 && Math.random() < 0.3) {
//             e.lastShot = now;
//             const eb = document.createElement('div');
//             eb.classList.add('enemy-bullet');
//             // Центр врага по X: e.x + (50/2) - (5/2) = e.x + 22.5
//             eb.style.left = (e.x + e.width / 2 - 2.5) + 'px'; 
//             eb.style.top = (e.y + e.height) + 'px';
//             gameContainer.appendChild(eb);
//             enemyBullets.push({ element: eb, x: e.x + e.width / 2 - 2.5, y: e.y + e.height });
//         }

//         // Столкновение врага с игроком
//         if (isColliding(e, playerRect)) {
//             e.element.remove();
//             enemies.splice(i, 1);
//             takeDamage();
//         } else if (e.y > gameHeight) {
//             e.element.remove();
//             enemies.splice(i, 1);
//         }
//     }

//     // Движение снарядов врага
//     for (let i = enemyBullets.length - 1; i >= 0; i--) {
//         let eb = enemyBullets[i];
//         eb.y += 5;
//         eb.element.style.top = eb.y + 'px';

//         const ebRect = { x: eb.x, y: eb.y, width: 5, height: 15 };

//         // Столкновение вражеской пули с игроком
//         if (isColliding(ebRect, playerRect)) {
//             eb.element.remove();
//             enemyBullets.splice(i, 1);
//             takeDamage();
//         } else if (eb.y > gameHeight) {
//             eb.element.remove();
//             enemyBullets.splice(i, 1);
//         }
//     }
// }

// // Получение урона
// function takeDamage() {
//     lives--;
//     livesEl.textContent = lives;
    
//     // Мигание игрока при уроне
//     player.style.opacity = '0.3';
//     setTimeout(() => { player.style.opacity = '1'; }, 200);

//     if (lives <= 0) {
//         endGame('Вы проиграли!');
//     }
// }

// // Функция проверки столкновений (AABB)
// function isColliding(rect1, rect2) {
//     return (
//         rect1.x < rect2.x + rect2.width &&
//         rect1.x + (rect1.width || 5) > rect2.x &&
//         rect1.y < rect2.y + rect2.height &&
//         rect1.y + (rect1.height || 15) > rect2.y
//     );
// }

// // Завершение игры
// function endGame(reasonText) {
//     isPlaying = false;
//     clearInterval(gameInterval);
//     clearInterval(timerInterval);

//     document.getElementById('gameOverTitle').textContent = reasonText;
//     finalScoreText.textContent = `Ваш результат: ${score}`;
//     gameOverScreen.classList.remove('hidden');
// }

// Очистка игрового поля
// function clearGameObjects() {
//     bullets.forEach(b => b.remove());
//     enemies.forEach(e => e.element.remove());
//     enemyBullets.forEach(eb => eb.element.remove());

//     bullets = [];
//     enemies = [];
//     enemyBullets = [];
// }

// // Сохранение результатов в localStorage
// function saveResult() {
//     const name = playerNameInput.value.trim() || 'Пилот';
    
//     let leaderboard = JSON.parse(localStorage.getItem('space_leaderboard')) || [];
//     leaderboard.push({ name: name, score: score });
    
//     // Сортировка по убыванию очков
//     leaderboard.sort((a, b) => b.score - a.score);
//     // Оставляем ТОП-5
//     leaderboard = leaderboard.slice(0, 5);

//     localStorage.setItem('space_leaderboard', JSON.stringify(leaderboard));

//     updateLeaderboardUI();

//     // Скрываем форму ввода и показываем кнопку "Играть снова"
//     playerNameInput.classList.add('hidden');
//     saveBtn.classList.add('hidden');
//     restartBtn.classList.remove('hidden');
// }

// Отрисовка турнирной таблицы
function updateLeaderboardUI() {
    leaderboardList.innerHTML = '';
    const leaderboard = JSON.parse(localStorage.getItem('space_leaderboard')) || [];

    if (leaderboard.length === 0) {
        leaderboardList.innerHTML = '<li>Пока нет рекордов</li>';
        return;
    }

    leaderboard.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name}: ${item.score}`;
        leaderboardList.appendChild(li);
    });
}
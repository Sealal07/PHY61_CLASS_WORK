// СПОСОБ 2

const btn = document.getElementById('second');
// через свойство элемента
btn.onclick = function(){
    console.log('Обработчик сработал');
}

// СПОСОБ 3
// obj.addEventListener('event', handler)
// handler - функция-обработчик события

const btn3 = document.getElementById('third');

function handlerClick(event){
    btn3.style.backgroundColor = 'pink';
    // console.log(event);
    console.log(event.target); // исходный элемент
    console.log(event.type); // click, keydown, mouseover
    console.log(event.timeStamp);// время возникновения
}

btn3.addEventListener('drag', handlerClick);

// Объект event
// click, keydown, keyup, mousemove, scroll,
// mouseover, drag(перетаскивание), 
// change(измение значения эл формы), input(при вводе)

// ПРИМЕРЫ
// 1. Отслеживание координат мыши
const box = document.getElementById('box');
const coords = document.getElementById('coords');

box.addEventListener('mousemove', function(event){
    // clientX clientY - координаты курсора
    const x = event.clientX;
    const y = event.clientY;
    coords.textContent = `X: ${x}, Y: ${y}`;
});
// f'TExt: {num}'


// 2. Обработка клавиш клавиатуры (keydown)
// event.key (символ)  event.code(физическая клавиша)

const input = document.getElementById('keyInput');
const log = document.getElementById('keyLog');

box.style.position = "relative";
let pos = 0;
box.style.left = `${pos}px`;

input.addEventListener('keydown', function(event){
    log.textContent += ` ${event.key} (${event.code})`;
    if(event.key === 'Enter'){
        alert('Нажат Enter!');
    }
    if (event.code === 'ArrowRight'){
        pos = pos + 20;
        box.style.left = `${pos}px`;
    }
    if (event.code === 'ArrowLeft'){
        pos = pos - 20;
        box.style.left = `${pos}px`;
    }
});

// 3. Остановка стандартного поведения

const link = document.getElementById('link');
const message = document.getElementById('message');

link.addEventListener('click', function(e){
    e.preventDefault(); // запрет перехода по ссылке
    message.textContent = 'Попытка перехода по ссылке';
});
// // window
// // BOM DOM
// // window.location - управление URL
// console.log(location.href) // URL
// console.log(location.protocol) // http / https
// console.log(location.host) //  домен с портом
// console.log(location.hostname)
// console.log(location.port)

// // 1. изменение адресса с записью в историю
// // location.assign('https://ru.wikipedia.org/')
// //2. перенаправление без возможности вернуться назад
// // location.replace('https://ru.wikipedia.org/')
// // 3. Перезагрузка 
// // location.reload()

// // window.navigator 
// console.log(navigator.userAgent) // браузер и ос
// console.log(navigator.language) // язык интерфейса
// console.log(navigator.onLine) // есть ли подключение к сети
// console.log(navigator.cookieEnabled) //включены ли куки
// console.log(navigator.hardwareConcurrency) //кол-во логических ядер в процессоре

// // window.history
// // history.back()  
// // history.forward()
// // history.go(-2)
// // history.go(1)
// // console.log(history.length)
// //МОНИТОР
// // console.log(screen.width)
// // console.log(screen.height)
// // console.log(screen.availWidth)
// // console.log(screen.availHeight)

// // ТАЙМЕРЫ
// //задержка (однократная) setTimeout(function, time, [data])
// // const timeId = setTimeout((data)=>{
// //     console.log('Запуск таймера', data);
// // }, 2000, 'DemoData');

// //интервал setInterval
// // let count = 0;
// // const intervalId = setInterval(() => {
// //     count++;
// //     console.log('Прошло секунд', count);
// //     if (count >= 10){
// //         clearInterval(intervalId);
// //         console.log('Таймер окончен');
// //     }
// // }, 1000);

// // DOM document object model

// //     HTMLDocument (document)
// //             |
// //             |
// //     ElementNode (<html>)
// //             |                     
// //     ElementNode (<head>)      
// //     |                    |
// // ElementNode (<meta>)     ElementNode (<title>)
// // |                               |
// // AttributeNode (charset)      TextNode (BOM DOM)

const body_p = document.body;
console.log(body_p.firstChild)//первый дочерний
console.log(body_p.childNodes)//NodeList со всеми узлами

console.log(body_p.firstElementChild)//html тег
console.log(body_p.lastElementChild)
console.log(body_p.children)

// ПОИСК ЭЛЕМЕНТОВ В DOM
const parent = document.querySelector('p#child');
// console.log(parent);
const span = document.getElementsByClassName('selector');
console.log(span);
const p = document.getElementById('parent');
console.log(p);
const spans = document.getElementsByTagName('span');
console.log(spans);
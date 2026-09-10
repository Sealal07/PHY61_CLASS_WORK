// // Функции
// // Декларативный
// function greet(){
//     console.log('Hello');
// }
// // greet();

// function greetName(name){
//     console.log(`Hello, ${name}`);
// }
// // greetName('Sasha');

// function sum(a, b){
//     return a + b;
// }
// let result = sum(4, 9);
// // console.log(sum(6, 9), result);

// // Стрелочные функции
// // когда есть возвращаемое значение и
// // вмещается в одну строку
// const multiply = (x, y) => x * y;
// // console.log(multiply(4, 6));

// // nameFunction = (p1, p2) => действие;


// // Функция-калькулятор
// // Принимает три параметра (n1, n2, operator)
// // Возвращает значение (switch, case)

// function calculate(n1, n2, operator){
//     switch (operator){
//         case '+':
//             return n1 + n2;
//         case '-':
//             return n1 - n2;
//         case '*':
//             return n1 * n2;
//         case '/':
//             if(n2 == 0){return 'На ноль делить нельзя';}
//             return n1 / n2;
//         case '%':
//             return n1 % n2;
//         default:
//             return 'Оператор неизвестен';
//      }
// }
// // console.log(calculate(6, 8, '-'));
// // console.log(calculate(6, 4, '%'));
// // console.log(calculate(9, 0, '/'));
// // console.log(calculate(1, 2, '#'));

// // alert('Message');
// // let str = prompt('Введите сообщение');
// // // Если ОК-строка сохраняется, если ОТМЕНА-вернется null
// // alert(`Пользователь ввел: ${str}`);
// // let question = confirm('Ответьте на вопрос?')
// // // OK - true, ОТМЕНА - false
// // alert(question);

// function dialog(){
//     alert('Добро пожаловать в систему');
//     let userAge = prompt('Сколько вам лет?');
//     if (userAge === null){
//         alert('Ввод отменен! В доступе отказано!');
//         return;
//     }else{
//         let age = Number(userAge);
//         if (isNaN(age)){
//             alert('Вы ввели не число!');
//         }else{
//             if (age >= 18){
//                 let isBoss = confirm('Вы админ?');
//                 if (isBoss){
//                     alert('Доступ разрешен');
//                 }else{
//                     alert('Доступ ограничен!');
//                 }
//             }else{
//                 alert('В доступе отказано!');
//             }
//         }
//     }
// }
// // dialog();

// // МАССИВЫ (Array) arr = Array(); arr = [];
// let arr1 = [4, 7, 9, 4];
// let arr2 = ['apple', 'banana', true, 0];
// // console.log(arr1[2], arr2[3]);
// // console.log(arr2.length);
// // console.log(arr1[arr1.length-1]);

// let arr = [];
// arr.push(4);
// arr.push(8);
// arr.push(10);
// // console.log(arr);

// // Перебор массива
// // 1
// for (let i = 0; i < arr.length; i++){
//     console.log(arr[i]);
// }

// // 2
// for (let item of arr){
//     console.log(item);
// }

// ЗАДАЧА 1
let ages = [16, 21, 15, 18, 30];

function checkGuest(agesArray){
    // 1
    let newAge;
    while (true){
        let userInput = prompt('Введите возраст');
        newAge = Number(userInput);
        if (isNaN(newAge)){
            alert('Вы ввели не число!');
        }else{
            break;
        }
    }
    // 2
    agesArray[agesArray.length] = newAge;
    // 3
    let adults = 0;
    let minors = 0;
    for (let item of agesArray){
        if (item >= 18){
            adults++;
        }else{
            minors++;
        }
    }
    //4
    alert(
        `Всего гостей: ${agesArray.length}`+
        `\nСовершеннолетние: ${adults}`+
        `\nНесовершеннолетние: ${minors}`
    );
    //5
    let addMore = confirm('Хотите добавить еще одного?');
    if (addMore){
        checkGuest(agesArray);
    }else{
        alert('Регистрация завершена');
    }
}

// checkGuest(ages);

// ЗАДАЧА 2
let prices = [150, 320, 80, 500];

function calculateTotal(priceList){
    // 1
    let total = 0;
    for (let item of priceList){
        total += item;
    }
    let hasCard =  confirm('Есть ли у вас скидочная карта?');
    if (hasCard){
        let code = prompt('Введите промокод');
        if (code === 'SALE10'){
            total = total * 0.9;
            alert('Скидка применилась!');
        }else{
            alert('Неверный промокод');
        }
    }
    return total;
}

// let result = calculateTotal(prices);
// alert(`Итого к оплате ${result}`);

// ЗАДАЧА 3

let scores = [120, 450, 310, 890, 600];
function analyzeScores(scoresArray){
    // 1
    let maxScore = scoresArray[0];
    let sum = 0;

    for (let i = 0; i < scoresArray.length; i++){
        if (scoresArray[i] > maxScore){
            maxScore = scoresArray[i];
        }
        sum += scoresArray[i];
    } 
    let avgScore = sum / scoresArray.length;

    let userInput = +prompt('Введите ваш результат');
    if (userInput > maxScore){
        alert('Поздравляем!');
    }else{
        alert(`До рекорда не хватило ${maxScore-userInput}`+
            `\nСредний результат ${avgScore}`
        );
    }
}
analyzeScores(scores);
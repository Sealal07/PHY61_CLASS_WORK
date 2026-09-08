// // // // // let age = 16; //локальная/блочная
// // // // // age = 14; // let можно переопределить

// // // // // const pi = 3.14;

// // // // // var i = 1; //глобальная/функциональная область видимости

// // // // // console.log(age, pi, i);

// // // // // let x;
// // // // // console.log(x);
// // // // // x = 10;

// // // // // console.log(y);
// // // // // let y = 6;

// // // // // console.log(z);
// // // // // var z = 5;

// // // // // ТИПЫ ДАННЫХ
// // // // // let userName = 'Kate'; // String
// // // // // let userAge = 45; // Number
// // // // // let isStudent = true; // Boolean
// // // // // let emptyValue = null; // Null
// // // // // let undefinedVar; // undefined 

// // // // // let strNum1 = '4.2px';
// // // // // let strNum2 = '5.7';
// // // // // // parseInt()  parseFloat()
// // // // // console.log(parseInt(strNum1)); // 4
// // // // // console.log(parseFloat(strNum1)); // 4.2
// // // // // console.log(Number(strNum2));

// // // // // //  Проверка на NaN (not a number)
// // // // // let invalidStr = '12345';
// // // // // let badNum = +invalidStr;
// // // // // console.log(badNum);

// // // // // ОПЕРАТОРЫ И ЛОГИКА
// // // // let a = 10, b = 3;
// // // // console.log(a + b);
// // // // console.log(a - b);
// // // // console.log(a * b);
// // // // console.log(a / b);
// // // // console.log(a % b);

// // // // // Инкремент(+) / декремент(-)
// // // // let i = 5;
// // // // console.log(++i); //префиксный  
// // // // console.log(i++); //постфиксный
// // // // console.log(i);

// // // // // Сравнение
// // // // console.log(6 == '6'); // true -нестрогое
// // // // console.log(6 === '6');// false -строгое(+проверка типов)

// // // // // Логические
// // // // let x1 = true, x2 = false;
// // // // console.log(x1 && x2); // [И] false and
// // // // console.log(x1 || x2); // [ИЛИ] true or
// // // // console.log(!x1); // [НЕ] false  not

// // // // if -- else if -- else
// // // let score = 60;
// // // if (score >= 80){
// // //     console.log('Отлично');
// // // } else if (score >= 35){
// // //     console.log('Хорошо');
// // // }else{
// // //     console.log('Плохо');
// // // }

// // // let day = 9;
// // // switch (day){
// // //     case 1:
// // //     case 7:
// // //         console.log('Выходной');
// // //         break;
// // //     case 2:
// // //     case 3:
// // //         console.log('Нужный результат');
// // //         break;
// // //     case 4:
// // //     case 5:
// // //     case 6:
// // //         console.log('Рабочий день');
// // //         break; 
// // //     default:
// // //         console.log('Неизвестный день');   
// // // }

// // // // Тернарный оператор
// // // let accessAge = 12;
// // // let message = accessAge >= 18 ? "Разрешен" : "Запрещен";
// // // // condition ? если true : если false
// // // console.log(message);

// // // for 
// // // for i in range(0, 5, 1): 
// // for (let i = 0; i < 5; i++){
// //     console.log(i);
// // }
// // // while - выполняется пока выполнимо условие
// // let count = 0;
// // while (count > 5){
// //     console.log(count);
// //     count++;
// // }
// // // do ... while выполнится минимум один раз
// // let k = 0;
// // do {
// //     console.log(k);
// //     k++;
// // }while (k > 5);

// for (let n = 0; n < 5; n++){
//     if (n === 2) continue; //прерывает иттерацию
//     if (n === 4) break; // прерывает цикл
//     console.log(n);
// }// 0 1 3


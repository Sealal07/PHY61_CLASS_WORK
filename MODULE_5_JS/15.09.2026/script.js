//  Напишите скрипт, который через 10 секунд после загрузки страницы
// проверяет, находится ли пользователь онлайн (navigator.onLine). Если сеть есть —
// запустите таймер обратного отсчета с помощью setInterval, который каждую секунду
// выводит в консоль остаток времени до блокировки (начиная с 5 секунд). Когда отсчет дойдет
// до 0, выведите сообщение "Сессия завершена из-за неактивности" и
// остановите интервал.

function task_1(){
    if(navigator.onLine){
        setTimeout(()=>{
            let secondLeft = 5;
            const timeId = setInterval(()=>{
                console.log('До выхода из системы осталось ', secondLeft);
                
                if (secondLeft === 0){
                    clearInterval(timeId);
                    alert('Сессия завершена из-за неактивности');
                }
                secondLeft--;
            }, 1000);
        }, 10000);
    }
}
// task_1();

function task_2(){
    const feed = document.querySelector('#feed');
    const articles = feed.children;
    let firstDraft = null;
    // [a1, a2, a3]  0 1 2
    for (let i=0; i < articles.length; i++){
        if (articles[i].tagName === 'ARTICLE' && articles[i].className === 'draft'){
            firstDraft = articles[i];
            break;
        }
    }
    alert(firstDraft);
    console.log(firstDraft);
}
// task_2();

function task_3(){
    const isMobileScreen = screen.availWidth < 768;
    const isOnline = navigator.onLine;
    if (isMobileScreen && isOnline){
        console.log('перенаправление на мобилку');
        // location.assign('url');
    }else if (!isOnline){
        console.log('не в сети');
    }
    else{
        console.log('десктопная версия');
    }
}
task_3();
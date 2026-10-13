// form - submit

const form = document.getElementById('loginForm');

form.addEventListener('submit', function(e){
    e.preventDefault();// отменяем отправку и перезагрузку страницы

    const data = new FormData(form);
    alert('Email: ' + data.get('email')); // по атрибуту name
    alert('Password: ' + data.get('pass'));
})

// у элементов ввода - input (при каждом изменении значения)

const search = document.getElementById('search');
const len = document.getElementById('len');

search.addEventListener('input', (e)=>{
    len.textContent = e.target.value.length;
})

// у элементов формы - change (когда поле теряет focus)

document.getElementById('city').addEventListener('change', (e)=>{
    console.log('Выбран город ', e.target.value);
});

document.getElementById('agree').addEventListener('change', (e)=>{
    console.log('Чекбокс ', e.target.value);
});

//у элементов ввода focus-готов к вводу, blur - когда теряет focus

const phone = document.getElementById('phone');
const phoneError = document.getElementById('phoneError');

phone.addEventListener('blur', (e)=>{
    const digits = phone.value.split('').filter(char => char >= '0' && char <= '9');
    console.log(digits);

    if (digits.length < 10){
        phone.classList.add('invalid');
        phone.classList.remove('valid');
        phoneError.textContent = 'Введите минимум 10 цифр';
    }else{
        phone.classList.add('valid');
        phone.classList.remove('invalid');
        phoneError.textContent = '';
    }
});

// form - reset (очистка формы)
document.getElementById('myForm').addEventListener('reset', (e)=>{
    const name = e.target.elements.name.value;
    if (name && !confirm('Точно стереть все введенное?')){
        e.preventDefault();
    }
})


// ЖИВАЯ СТОИМОСТЬ ЗАКАЗА

const PRICE = 1000;
const qty = document.getElementById('qty');
const delivery = document.getElementById('delivery');
const vip = document.getElementById('vip');
const total = document.getElementById('total');

function recalc(){
    let sum = PRICE * (+qty.value);
    sum += +delivery.value;
    if (vip.checked) sum += 500;
    total.textContent = sum + 'р.'; 
}

[qty, delivery, vip].forEach(el => {
    el.addEventListener('input', recalc);
    el.addEventListener('change', recalc);
})
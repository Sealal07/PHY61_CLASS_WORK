// TASK 1

const passInput = document.getElementById('passInput');
const toggleBtn = document.getElementById('toggleBtn');

toggleBtn.addEventListener('click', function(e){
    if (passInput.type === 'password'){
        passInput.type = 'text';
        toggleBtn.textContent = 'Скрыть';
    }else{
        passInput.type = 'password';
        toggleBtn.textContent = 'Показать';
    }
});

// TASK 2
const area = document.getElementById('area');
const dot = document.getElementById('cursor');

area.addEventListener('mousemove', function(e){
    // offsetX offsetY возвращают координаты относительно элемента
    dot.style.left = e.offsetX - 10 + 'px';
    dot.style.top = e.offsetY - 10 + 'px';
});
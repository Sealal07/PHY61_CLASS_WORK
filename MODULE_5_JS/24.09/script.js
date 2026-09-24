// TASK 1

const alertToggle = document.getElementById('alertToggle');
const statusLabel = document.getElementById('statusLabel');

alertToggle.addEventListener('change', function(event){
    if (event.target.checked){
        document.body.classList.add('alert-mode');
        statusLabel.textContent = 'Режим тревоги';
    }else {
        document.body.classList.remove('alert-mode');
        statusLabel.textContent = 'Штатный режим';
    }
})

// TASK 2
const sliderTrack = document.querySelector('.slider-track');
const sliderTumb = document.getElementById('sliderTumb');
const sliderFill = document.getElementById('sliderFill');
const reactorValue = document.getElementById('reactorValue');

let isDragging = false;

function updateSlider(percent){
    percent = Math.max(0, Math.min(100, percent));
    sliderFill.style.width = percent + '%';
    sliderTumb.style.left = percent + '%';
    reactorValue.value = Math.round(percent);
}

sliderTumb.addEventListener('mousedown', function(e){
    isDragging = true;
    e.preventDefault();
})

document.addEventListener('mousemove', function(e){
    if (!isDragging) return;

    // вычисляем позицию относительно трека
    const trackRect = sliderTrack.getBoundingClientRect();
    const percent = ((e.clientX - trackRect.left)/trackRect.width)*100;
    updateSlider(percent);
})

document.addEventListener('mouseup', function(){
    isDragging = false;
})

reactorValue.addEventListener('input', function(e){
    const value = parseInt(e.target.value);
    updateSlider(value);
})
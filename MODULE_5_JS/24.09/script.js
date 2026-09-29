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

// TASK 3
const contextMenu = document.getElementById('contextMenu');
const widgets = document.querySelectorAll('.widget');

widgets.forEach(widget => {
    widget.addEventListener('contextmenu', function(e){
        e.preventDefault();
        const x = e.pageX;
        const y = e.pageY;

        const menuWidth = 200;
        const menuHeight = 150;

        const finalX = (x + menuWidth > window.innerWidth) ? x - menuWidth : x;
        const finalY = (y + menuHeight > window.innerHeight) ? y - menuHeight : y;

        contextMenu.style.left = finalX + 'px';
        contextMenu.style.top = finalY + 'px'; 

        contextMenu.classList.add('show');
// ссылки на виджеты для действий
        contextMenu.dataset.targetWidget = widget.dataset.widget;
    });
});

document.addEventListener('click', function(e){
    if (!contextMenu.contains(e.target)){
        contextMenu.classList.remove('show');
    }
});

// TASK 4
function showNotification(text, type='success'){
    const container = document.getElementById('notCont');
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = text;
    container.appendChild(notification);

    setTimeout(()=>{
        notification.classList.add('fade-out');
        setTimeout(()=>{
            notification.remove();
        }, 300);
    }, 3000);
}


// TASK 9

const viewportContainer = document.getElementById('viewportContainer');
const stars = document.getElementById('starsLayer');
const planet = document.getElementById('planetLayer');
const frame = document.getElementById('frameLayer');

document.addEventListener('mousemove', function(e){
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    const offsetX = (e.clientX - centerX) / centerX;
    const offsetY = (e.clientY - centerY) / centerY;

    stars.style.transform = `translate(${offsetX*5}px, ${offsetY*5}px)`;
    planet.style.transform = `translate(${offsetX*20}px, ${offsetY*20}px) translate(-50%, -50%)`;
    frame.style.transform = `translate(${offsetX*2}px, ${offsetY*2}px)`;

})

// TASK 7
const dragWidgets = document.getElementById('draggable');
const widgets7 = document.querySelectorAll('.wid');

let draggedElement = null;

widgets7.forEach(wid => {
    wid.addEventListener('dragstart', function(e){
        draggedElement = e.target;
        draggedElement.classList.add('dragging');
        e.dataTransfer.effectAllowed = 'move';
    });
    wid.addEventListener('dragend', function(e){
        draggedElement.classList.remove('dragging');
        draggedElement = null;
    });
});

dragWidgets.addEventListener('dragover', function(e){
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
})

dragWidgets.addEventListener('drop', function(e){
    e.preventDefault();
    if(!draggedElement) return;
    const target = e.target.closest('.wid');
    if (target && target !== draggedElement){
        const allWidgets = Array.from(dragWidgets.children);
        const draggedIndex = allWidgets.indexOf(draggedElement);
        const targetIndex = allWidgets.indexOf(target);

        if (draggedIndex < targetIndex){
            target.parentNode.insertBefore(draggedElement, target.nextSibling);
        }
        else{
            target.parentNode.insertBefore(draggedElement, target);
        }
    }
})
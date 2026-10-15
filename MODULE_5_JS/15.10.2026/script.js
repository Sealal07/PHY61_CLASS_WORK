// localStorage - локальное хранилище
// {key: value}
// localStorage.getItem()-прочитать по ключу
// localStorage.removeItem()-удалить по ключу
// localStorage.clear()-полная очистка
// localStorage.setItem()-сохранить данные по ключу

const noteInput = document.getElementById('noteInput');
const saveBtn = document.getElementById('saveBtn');
const clearBtn = document.getElementById('clearBtn');
const statusTxt = document.getElementById('status');

// при загрузке страницы проверяем есть ли сохраненная заметка
document.addEventListener('DOMContentLoaded', function(){
    const savedNote = localStorage.getItem('user_note');
    if (savedNote !== null){
        noteInput.value = savedNote;
        statusTxt.textContent = 'заметка загружена из браузера';
    }
});

saveBtn.addEventListener('click', function(){
    const textInput = noteInput.value;
    localStorage.setItem('user_note', textInput);
    statusTxt.textContent = 'успешно сохранено';
    setTimeout(()=>{statusTxt.textContent = ''}, 2000);
});

clearBtn.addEventListener('click', function(){
    localStorage.removeItem('user_note');
    noteInput.value = '';
    statusTxt.textContent = 'Память очищена';
});


const todoList = ['Поспать', 'Поработать', 'Погулять'];
// JSON.stringify(object) - превращает объект/массив в строку JSON
// JSON.parse(string) - превращает строку JSON в объект

localStorage.setItem('my_todo', JSON.stringify(todoList));

const loadedData = localStorage.getItem('my_todo');
const parsedData = JSON.parse(loadedData);
console.log(parsedData);
console.log(parsedData[0]);












const baseUrl = 'http://www.omdbapi.com/';
const apiKey = '2fc47281';

const searchForm = document.getElementById('searchForm');
const movieTitle = document.getElementById('movieTitle');
const typeSelect = document.getElementById('typeSelect');
const result = document.getElementById('result');
const pagination = document.getElementById('pagination');

// хранение текщего номера страницы
let currentPage = 1;

searchForm.addEventListener('submit', function(e){
    e.preventDefault();
    currentPage = 1;
    searchMovies();
});



// http://www.omdbapi.com/?apikey=2fc47281&s=harry&type=movie&page=1

async function searchMovies(){

    result.innerHTML = '';
    pagination.innerHTML = '';

    const title = movieTitle.value;
    const type = typeSelect.value;

    // URLSearchParams() - объект параметров для запроса
    const params = new URLSearchParams({
        apikey: apiKey,
        s: title,
        type: type,
        page: currentPage
    })

    const url = `${baseUrl}?${params.toString()}`;

    try{//fetch-отправляет запрос
        const response = await fetch(url);
         //преобразование ответа
        const data = await response.json();

        if (data.Response === 'False'){
            result.textContent = 'Movie not found!';
        }else{
            // пользовательская функция для отображения
            displayMovie(data.Search);
            createPagination(data.totalResults);
            console.log(data.Search);
        }
    } catch (error){
        result.textContent = 'Произошла ошибка при запросе';
        console.log(error);
    }
}

function displayMovie(movies){
    movies.forEach(movie => {
        const card = document.createElement('div');
        card.classList.add('movie-card');
        card.innerHTML = `
            <img src="${movie.Poster}">
            <h3>${movie.Title}</h3>
            <p>${movie.Year}</p>
            <button class="details-btn">Details</button>
        `;
        result.appendChild(card);
    });
}

function createPagination(totalResults){
    pagination.innerHTML = '';
    const totalPages = Math.ceil(totalResults / 10);

    if(totalPages <= 1) return;
    
    let startPage = Math.max(1, currentPage - 5);
    let endPage = Math.min(totalPages, startPage + 9);

    if (endPage - startPage < 9){
        startPage = Math.max(1, endPage - 9);
    }

    // Кнопка назад
    if (startPage > 1){
        const prevBtn = document.createElement('button');
        prevBtn.textContent = '<';
        prevBtn.classList.add('page-btn');
        prevBtn.addEventListener('click', function(){
            currentPage = currentPage - 1;
            searchMovies();
        });
        pagination.appendChild(prevBtn);
    }

        for (let i = startPage; i <= endPage; i++){
            const pageBtn = document.createElement('button');
            pageBtn.textContent = i;
            pageBtn.classList.add('page-btn');
            if (i === currentPage){
                pageBtn.classList.add('active');
            }
            pageBtn.addEventListener('click', function(){
                currentPage = i;
                searchMovies();
            });
            pagination.appendChild(pageBtn);
        }
        // кнопка вперед
        if (endPage < totalPages){
            const nextBtn = document.createElement('button');
            nextBtn.textContent = '>';
            nextBtn.classList.add('page-btn');
            nextBtn.addEventListener('click', function(){
                currentPage = currentPage + 1;
                searchMovies();
            });
            pagination.appendChild(nextBtn);
        }



    }



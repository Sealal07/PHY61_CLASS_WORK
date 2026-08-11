-- Задание 1 18 результов
SELECT Title, Budget
FROM IMDB
WHERE Budget BETWEEN 50000000 AND 100000000;

-- Задание 2 24 результата
SELECT Title
FROM IMDB
WHERE Title LIKE 'The%';




-- Задание 3 82 результата
SELECT Movie_id, genre
FROM genre
WHERE genre IN ('Sci-Fi', 'Action', 'Comedy');
-- Задание 4 0 результатов
SELECT Title
FROM IMDB
WHERE MetaCritic IS NULL;
-- 7 результатов
SELECT Title
FROM IMDB
WHERE MetaCritic='';



-- Задание 5 22 результата
SELECT Title, Budget
FROM IMDB
WHERE ((Rating > 8.0 AND TotalVotes > 500000) 
OR Budget > 200000000) AND Budget <> '';  

-- Задание 6

SELECT i.Title, i.Rating, e.Worldwide
FROM IMDB i
INNER JOIN earning e
ON i.Movie_id = e.Movie_id;











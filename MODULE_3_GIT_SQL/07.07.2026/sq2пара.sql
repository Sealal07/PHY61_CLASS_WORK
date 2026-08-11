-- ЗАДАЧА 1
SELECT Title, Rating
FROM IMDB 
WHERE Title LIKE '%Star%'
AND Rating BETWEEN 7.0 AND 8.5;

-- ЗАДАЧА 2
SELECT COUNT(*) AS TotalMovies,
COUNT(MetaCritic) AS MoviesWithMetric
FROM IMDB;

--  ЗАДАЧА 3
SELECT Title, Runtime, Budget
FROM IMDB 
WHERE Budget IN (10000000, 20000000, 50000000)
AND VotesM IS NULL;

-- ЗАДАЧА 4
SELECT MAX(Rating) AS HighesRating,
MIN(MetaCritic) AS LowesMetacritic,
AVG(Budget) AS AverageBudget 
FROM IMDB  
WHERE TotalVotes > 100000;

--  ЗАДАЧА 5
SELECT Title, TotalVotes
FROM IMDB
ORDER BY TotalVotes DESC 
LIMIT 5 OFFSET 10;

-- ЗАДАЧА 6
SELECT i.Title, e.Domestic, e.Worldwide
FROM IMDB i 
INNER JOIN earning e
ON i.Movie_id = e.Movie_id
ORDER BY e.Worldwide DESC;

-- ЗАДАЧА 8
SELECT g.genre, AVG(i.Rating) AS AverageRating
FROM genre g 
INNER JOIN IMDB i 
ON g.Movie_id = i.Movie_id
WHERE g.genre IS NOT NULL
GROUP BY g.genre 
HAVING AverageRating > 7.5;

-- ЗАДАЧА 11
SELECT SUM(e.Worldwide) AS TotalWorldwide,
g.genre, i.Budget, 
AVG(i.Rating) AS AvgRating 
FROM  genre g
INNER JOIN IMDB i ON g.Movie_id = i.Movie_id
INNER JOIN earning e ON i.Movie_id = e.Movie_id
WHERE i.Budget > 50000000 AND g.genre = 'Action';

-- ЗАДАЧА 12
SELECT g.genre, SUM(i.TotalVotes) AS SumVotes
FROM genre g
INNER JOIN IMDB i ON g.Movie_id = i.Movie_id 
WHERE g.genre IS NOT NULL 
GROUP BY g.genre
HAVING SumVotes > 1000000;





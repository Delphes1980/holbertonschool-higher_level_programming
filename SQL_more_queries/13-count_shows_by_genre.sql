-- A script that lists all genres from the 'hbtn_0d_tvshows' database
-- and displays the number of TV shows linked to each genre
SELECT tv_genres.name AS genre,  -- Selects the NAME of the genre
COUNT(tv_show_genres.show_id) AS number_of_shows  -- Counts the number of 'show_id' entries linked to each genre
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre  -- Groups the results by the genre's NAME
ORDER BY number_of_shows DESC;

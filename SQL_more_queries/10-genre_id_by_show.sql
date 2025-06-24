-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Each record displays the show's title & the ID of its associated genre
SELECT tv_shows.title,  -- Selects the title of the TV show
tv_show_genres.genre_id  -- Selects the ID of the genre linked to the show
FROM tv_shows  -- Starts the query from the 'tv_shows' table, which contains show titles
INNER JOIN tv_show_genres  -- Joins 'tv_shows' with 'tv_show_genres', the linking table between shows and genres
ON tv_shows.id = tv_show_genres.show_id  -- The join condition: links a show's ID from 'tv_shows'
										-- to the 'show_id' (foreign key) in 'tv_show_genres'
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

-- A script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title,  -- Selects the title of the TV show
tv_show_genres.genre_id  -- Selects the ID of the genre linked to the show
FROM tv_shows  -- Starts the query from the 'tv_shows' table, which contains show titles
LEFT JOIN tv_show_genres  -- Performs a LEFT JOIN: Includes all shows from 'tv_shows' (left table)
                        -- and matching genres from 'tv_show_genres' (right table)
                    	-- Shows without a linked genre will still appear, with NULL in genre_id
ON tv_shows.id = tv_show_genres.show_id  -- The join condition: links a show's ID from 'tv_shows'
										-- to the 'show_id' (foreign key) in 'tv_show_genres'
WHERE tv_show_genres.genre_id IS NULL  -- Filters the results: This condition selects only those shows
                                	-- where the LEFT JOIN found NO corresponding genre, meaning 'genre_id' is NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

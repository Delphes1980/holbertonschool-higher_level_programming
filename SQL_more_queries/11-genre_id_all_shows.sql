-- A script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title,  -- Selects the title of the TV show
tv_show_genres.genre_id  -- Selects the ID of the genre linked to the show
FROM tv_shows  -- Starts the query from the 'tv_shows' table, which contains show titles
LEFT JOIN tv_show_genres  -- Performs a LEFT JOIN: Includes all shows from 'tv_shows' (left table)
                        -- and matching genres from 'tv_show_genres' (right table)
                    	-- Shows without a linked genre will still appear, with NULL in genre_id
ON tv_shows.id = tv_show_genres.show_id  -- The join condition: links a show's ID from 'tv_shows'
										-- to the 'show_id' (foreign key) in 'tv_show_genres'
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

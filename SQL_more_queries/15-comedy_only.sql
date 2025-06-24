-- A script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title AS title
FROM tv_shows -- Database containing the names of all genres
INNER JOIN tv_show_genres  -- First join: Links 'tv_shows' with 'tv_show_genres'
                           -- This is the linking table that connects shows to their genres
ON tv_shows.id = tv_show_genres.show_id  -- Join condition: Matches the show's primary 'id' from 'tv_shows'
                        				 -- with the 'show_id' (foreign key) in the 'tv_show_genres' table
INNER JOIN tv_genres  -- Second join: Links 'tv_show_genres' with 'tv_genres'
                      -- This table contains the actual genre names
ON tv_show_genres.genre_id = tv_genres.id  -- Join condition: Matches the 'genre_id' (foreign key) from 'tv_show_genres'
                        				   -- with the primary 'id' of the genre in the 'tv_genres' table
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;

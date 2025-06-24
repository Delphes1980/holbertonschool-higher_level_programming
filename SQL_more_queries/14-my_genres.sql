-- A script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name AS name
FROM tv_genres -- Database containing the names of all genres
INNER JOIN tv_show_genres  -- First join: Links 'tv_genres' with 'tv_show_genres'
                        -- which is the many-to-many linking table between shows and genres
ON tv_genres.id = tv_show_genres.genre_id  -- Join condition: Matches the genre's ID from 'tv_genres'
                            -- with the genre ID in the linking table
INNER JOIN tv_shows  -- Second join: Links 'tv_show_genres' with 'tv_shows'
                     -- which contains the show titles. Necessary to filter by show title
ON tv_show_genres.show_id = tv_shows.id  -- Join condition: Matches the show ID from the linking table
                           				 -- with the show's primary ID in the 'tv_shows' table
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;

-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT tv_shows.title AS title, tv_genres.name AS name
FROM tv_shows -- Database containing the names of all genres
LEFT JOIN tv_show_genres  -- First LEFT JOIN: Includes ALL shows from 'tv_shows' (the left table)
                          -- and any matching genre links from 'tv_show_genres'
ON tv_shows.id = tv_show_genres.show_id  -- Join condition: Links a show's primary ID from 'tv_shows'
                                        -- to its corresponding 'show_id' in 'tv_show_genres'
LEFT JOIN tv_genres  -- Second LEFT JOIN: Continues from the previous join's result,
                     -- including all linked 'tv_show_genres' entries, and matching genre names from 'tv_genres'
ON tv_show_genres.genre_id = tv_genres.id  -- Join condition: Links the 'genre_id' from 'tv_show_genres'
                                            -- to the primary 'id' of the genre in 'tv_genres'
ORDER BY title ASC;

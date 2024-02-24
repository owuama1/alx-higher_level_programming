-- List all shows without the Comedy genre from the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id <> (
    SELECT id
    FROM tv_genres
    WHERE name = 'Comedy'
) OR tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;

-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- each record should display: tv_genres.name
SELECT tv_genres.name AS name FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;

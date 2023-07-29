-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- first column must be called genre
-- second column must be called number_of_shows
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

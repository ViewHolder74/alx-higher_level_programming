-- THis script lists all shows contatined in hbtn_0d_tvshows that have at least
-- one genre linked
-- Each record display tv_shows.title - tv_show_genres.genre_id
-- Results is sorted by ascending order by
-- tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genress.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

-- A script that lists all shows without the genre 
-- Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT `title`
  FROM `tv_shows` AS tv
  LEFT JOIN `tv_show_genres` AS shw
    ON shw.`show_id` = tv.`id`
  LEFT JOIN `tv_genres` AS tvg
    ON tvg.`id` = shw.`genre_id`
 WHERE tv.`title` NOT IN (
       SELECT `title`
         FROM `tv_shows` AS tv
	INNER JOIN `tv_show_genres` AS shw
           ON shw.`show_id` = tv.`id`
        INNER JOIN `tv_genres` AS tvg
           ON tvg.`id` = shw.`genre_id`
        WHERE tvg.`name` = "Comedy")
 ORDER BY `title`;

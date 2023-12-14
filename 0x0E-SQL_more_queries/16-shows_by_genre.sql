-- A script that lists all shows, 
-- and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv.`title`, tvg.`name`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS shw
         ON tv.`id` = shw.`show_id`
       LEFT JOIN `tv_genres` AS tvg
         ON shw.`genre_id` = tvg.`id`
 ORDER BY tv.`title`, tvg.`name`;

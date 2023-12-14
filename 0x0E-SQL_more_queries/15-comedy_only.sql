-- A script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv.`title`
  FROM `tv_shows` AS tv
       INNER JOIN `tv_show_genres` AS shw
          ON tv.`id` = shw.`show_id`
       INNER JOIN `tv_genres` AS tvg
          ON tvg.`id` = shw.`genre_id`
       WHERE tvg.`name` = "Comedy"
 ORDER BY tv.`title`;

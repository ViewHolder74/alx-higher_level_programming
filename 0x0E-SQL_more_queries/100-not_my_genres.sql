-- A script that uses the hbtn_0d_tvshows database 
-- to list all genres not linked to the show Dexter
SELECT DISTINCT `name`
  FROM `tv_genres` AS tvg
       INNER JOIN `tv_show_genres` AS shw
          ON tvg.`id` = shw.`genre_id`
       INNER JOIN `tv_shows` AS tv
          ON shw.`show_id` = tv.`id`
       WHERE tvg.`name` NOT IN (
      SELECT `name`
        FROM `tv_genres` AS tvg
       INNER JOIN `tv_show_genres` AS shw
	  ON tvg.`id` = shw.`genre_id`
  INNER JOIN `tv_shows` AS tv
	  ON shw.`show_id` = tv.`id`
       WHERE tv.`title` = "Dexter")
 ORDER BY tvg.`name`;

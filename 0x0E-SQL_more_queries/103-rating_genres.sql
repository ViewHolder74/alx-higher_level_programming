-- A script that lists all genres in the database 
-- hbtn_0d_tvshows_rate by their rating.
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS tvg
 INNER JOIN `tv_show_genres` AS shw
    ON shw.`genre_id` = tvg.`id`
 INNER JOIN `tv_show_ratings` AS rat
    ON rat.`show_id` = shw.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;

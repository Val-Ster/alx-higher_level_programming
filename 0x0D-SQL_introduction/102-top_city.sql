-- Import in hbtn_0c_0 database this table dump: (a link to a file to be downloaded was provided (same as Temperatures #0))
-- a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Display top 3 cities during July and August

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` IN (7, 8)
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;

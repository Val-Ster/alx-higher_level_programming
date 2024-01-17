-- Import in hbtn_0c_0 database this table dump:(a link to a file was provided (same as Temperatures #0))
-- a script that displays the max temperature of each state (ordered by State name).
-- Max temperature of each state

SELECT `state`, MAX(value) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;

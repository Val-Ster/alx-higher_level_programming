a script that lists all records of a table except name is not null
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL AND `name` != ''
ORDER BY `score` DESC;

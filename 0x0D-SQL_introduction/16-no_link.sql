-- quaries two columens and order them by the numeric value in desending order
SELECT `score`, `name` 
FROM `second_table` 
WHERE `name` IS NOT 
NULL ORDER BY `score` DESC;

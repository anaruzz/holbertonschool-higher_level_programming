-- lists all records of the `second_table`, except the ones that don't have a
-- `name` value
SELECT score, name FROM second_table WHERE `name` IS NOT NULL ORDER BY score DESC;

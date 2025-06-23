-- A script that computes the score average of all records in the table
-- second_table of the database hbtn_0c_0 in my MySQL server
SELECT SUM(score) / COUNT(score) AS average
FROM second_table;

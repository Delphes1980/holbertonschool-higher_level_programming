/* A script that lists all records of the table second_table of the database
hbtn_0c_0 in my MySQL server.Don’t list rows where the name column does not
contain a value. Results should display the score and the name (in this order)
Records should be listed by descending score */
SELECT score, name FROM second_table
WHERE NOT name = ''
ORDER BY score DESC;

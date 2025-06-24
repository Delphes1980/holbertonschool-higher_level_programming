--  A script that lists all the cities of California that can be found in the
-- database hbtn_0d_usa
SELECT DISTINCT id, name  -- the columns we want
FROM cities  -- in this database
WHERE cities.state_id = ( -- Filters records from the 'cities' table where 'state_id' matches the result of the subquery
	SELECT id  -- Subquery: Selects the 'id' of the state
	FROM states -- Subquery: From the 'states' table
	WHERE name = 'California'  -- Subquery: Finds the state whose 'name' is 'California'
	)
ORDER BY cities.id ASC;

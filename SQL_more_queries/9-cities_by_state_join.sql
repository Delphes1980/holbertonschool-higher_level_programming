--  A script that lists all cities contained in the database hbtn_0d_usa
-- The cities are listed with the corresponding state name
SELECT cities.id,  -- Selects the unique identifier for each city from the 'cities' table
cities.name,  -- Selects the name of the city from the 'cities' table
states.name  -- Selects the name of the corresponding state from the 'states' table
FROM cities  -- Specifies the primary table from which to retrieve city data
INNER JOIN states ON cities.state_id = states.id  -- Joins 'cities' with 'states' based on the foreign key relationship
												-- 'cities.state_id' must match 'states.id' to link a city to its state
ORDER BY cities.id ASC;

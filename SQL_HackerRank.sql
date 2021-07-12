/* Basic SELECT */
-- Problem:
-- Query all columns for all American cities in the CITY table
-- with POPULATION larger than 100000. The CountryCode for America is USA.
SELECT * FROM CITY WHERE COUNTRYCODE='USA' AND POPULATION > 100000;

-- Problem:
-- Query the NAME field for all American cities in the CITY table
-- with POPULATION larger than 120000. The CountryCode for America is USA.
SELECT NAME FROM CITY WHERE COUNTRYCODE='USA' AND POPULATION > 120000;

-- Problem: Query all columns (attributes) for every row in the CITY table.
SELECT * FROM CITY;

-- Problem: Query all columns for a city in CITY with the ID 1661.
SELECT * FROM CITY WHERE ID=1661;

-- Problem: Query all attributes of every Japanese city in the CITY table. 
-- The COUNTRYCODE for Japan is JPN.
SELECT * FROM CITY WHERE COUNTRYCODE='JPN';

-- Problem: Query the names of all the Japanese cities in the CITY table.
-- The COUNTRYCODE for Japan is JPN.
SELECT NAME FROM CITY WHERE COUNTRYCODE='JPN';

-- Query a list of CITY and STATE from the STATION table.
SELECT CITY, STATE FROM STATION;

SELECT
  COUNTY.state_fips_code,
  COUNTY.county_fips_code,
  COUNTY.geo_id,
  COUNTY.county_name,
  FIPS_STATE.state_name,
  COUNTY_2017.total_pop,
  COUNTY_2017.income_per_capita,
  "2017" as year
FROM
  `bigquery-public-data.census_bureau_acs.county_2017_5yr` AS COUNTY_2017
  INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
  ON COUNTY_2017.geo_id = COUNTY.geo_id
  INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
  ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
UNION ALL
SELECT
  COUNTY.state_fips_code,
  COUNTY.county_fips_code,
  COUNTY.geo_id,
  COUNTY.county_name,
  FIPS_STATE.state_name,
  COUNTY_2016.total_pop,
  COUNTY_2016.income_per_capita,
  "2016" as year
FROM
  `bigquery-public-data.census_bureau_acs.county_2016_5yr` AS COUNTY_2016
  INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
  ON COUNTY_2016.geo_id = COUNTY.geo_id
  INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
  ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code
UNION ALL
SELECT
  COUNTY.state_fips_code,
  COUNTY.county_fips_code,
  COUNTY.geo_id,
  COUNTY.county_name,
  FIPS_STATE.state_name,
  COUNTY_2015.total_pop,
  COUNTY_2015.income_per_capita,
  "2015" as year
FROM
  `bigquery-public-data.census_bureau_acs.county_2015_5yr` AS COUNTY_2015
  INNER JOIN `bigquery-public-data.utility_us.us_county_area` AS COUNTY 
  ON COUNTY_2015.geo_id = COUNTY.geo_id
  INNER JOIN `bigquery-public-data.census_utility.fips_codes_states` AS FIPS_STATE
  ON COUNTY.state_fips_code = FIPS_STATE.state_fips_code

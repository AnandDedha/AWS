CREATE TABLE weather_data (
    dt varchar(256) ,
    weather varchar(max) ,
    temp DECIMAL(5, 2),
    feels_like DECIMAL(5, 2),
    min_temp DECIMAL(5, 2),
    max_temp DECIMAL(5, 2),
    pressure bigint,
    sea_level bigint,
    ground_level bigint,
    humidity bigint,
    wind varchar(256) 
);

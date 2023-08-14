CREATE TABLE weather_data (
    dt string,
    weather string,
    temp DECIMAL(5, 2),
    feels_like DECIMAL(5, 2),
    min_temp DECIMAL(5, 2),
    max_temp DECIMAL(5, 2),
    pressure bigint,
    sea_level bigint,
    ground_level bigint,
    humidity bigint,
    wind string
);

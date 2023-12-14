CREATE TABLE seasons (
    id INT PRIMARY KEY,
    poster_url VARCHAR(255),
    name VARCHAR(255) UNIQUE,
    overview TEXT,
    number INT,
    air_date DATE,
    episode_count INT
);

CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    title_id INTEGER REFERENCES titles(id),
    poster_url VARCHAR(255),
    name VARCHAR(255),
    overview TEXT,
    number INTEGER,
    air_date DATE,
    episode_count INTEGER
);
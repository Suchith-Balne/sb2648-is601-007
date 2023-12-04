CREATE TABLE episodes (
    id SERIAL PRIMARY KEY,
    season_id INTEGER REFERENCES seasons(id),
    name VARCHAR(255),
    episode_number INTEGER,
    season_number INTEGER,
    tmdb_id INTEGER,
    imdb_id VARCHAR(20),
    thumbnail_url VARCHAR(255),
    release_date DATE,
    runtime_minutes INTEGER,
    overview TEXT
);
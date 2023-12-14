CREATE TABLE episodes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    season_id INT,
    name VARCHAR(255) UNIQUE,
    episode_number INT,
    season_number INT,
    tmdb_id INT,
    imdb_id VARCHAR(255),
    thumbnail_url VARCHAR(255),
    release_date DATE,
    runtime_minutes INT,
    overview TEXT,
    FOREIGN KEY (season_id) REFERENCES seasons(id) ON DELETE CASCADE
);
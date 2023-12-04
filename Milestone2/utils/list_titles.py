from datetime import datetime
from flask import flash, render_template, request, Blueprint,jsonify
from utils.api import API
from sql.db import DB

title = Blueprint('title', __name__, url_prefix='/title')

@title.route("/update_data", methods=["GET"])
def update_data():
    # Update episodes data
    update_episodes_data()

    # Update seasons data
    update_seasons_data()

    # Update details data
    #update_details_data()

    return jsonify(message="Data updated successfully")

def update_episodes_data():

    url = "/title/3173903/episodes"

    # Make a GET request using the API class
    response_episodes = API.get(url)

    # Print the JSON response length for debugging purposes
    print(f"Length of the episodes resonse:{len(response_episodes)}")

    if isinstance(response_episodes, list):
        
        if response_episodes:
            try:
                insert_query = """
                                INSERT INTO episodes (
                                    season_id, name, episode_number, season_number, tmdb_id, imdb_id,
                                    thumbnail_url, release_date, runtime_minutes, overview
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                    season_id = VALUES(season_id),
                                    name = VALUES(name),
                                    episode_number = VALUES(episode_number),
                                    season_number = VALUES(season_number),
                                    tmdb_id = VALUES(tmdb_id),
                                    imdb_id = VALUES(imdb_id),
                                    thumbnail_url = VALUES(thumbnail_url),
                                    release_date = VALUES(release_date),
                                    runtime_minutes = VALUES(runtime_minutes),
                                    overview = VALUES(overview)
                                """

                # Prepare data for insertion
                episode_data = []
                for episode in response_episodes:
                    episode_values = (
                        episode.get('season_id'),
                        episode.get('name'),
                        episode.get('episode_number'),
                        episode.get('season_number'),
                        episode.get('tmdb_id'),
                        episode.get('imdb_id'),
                        episode.get('thumbnail_url'),
                        episode.get('release_date'),
                        episode.get('runtime_minutes'),
                        episode.get('overview')
                    )
                    episode_data.append(episode_values)

                # Use the insertMany method to insert data into the database
                DB.insertMany(insert_query, episode_data)
                print(f"Inserted {len(response_episodes)} records to the episodes table")
            except Exception as e:
                print(f"insert error in episodes data {e}")
                flash("An error occurred while inserting data to episodes table. Please try again later.", "danger")
        return jsonify(data=response_episodes)
    else:
        return jsonify(error="Unexpected response format"), 500
    
def update_seasons_data():
    url_seasons = "/title/3173903/seasons"
    response_seasons = API.get(url_seasons)
    
    print(f"Length of the seasons resonse:{len(response_seasons)}")
    
    if not isinstance(response_seasons, list):
        return jsonify(error="Unexpected response format"), 500
    
    print(f"Length of the seasons resonse:{len(response_seasons)}")
    
    try:
        insert_query = """
                INSERT INTO seasons (id, poster_url, name, overview, number, air_date, episode_count)
                VALUES (%(id)s, %(poster_url)s, %(name)s, %(overview)s, %(number)s, %(air_date)s, %(episode_count)s)
                ON DUPLICATE KEY UPDATE
                    poster_url = VALUES(poster_url),
                    name = VALUES(name),
                    overview = VALUES(overview),
                    number = VALUES(number),
                    air_date = VALUES(air_date),
                    episode_count = VALUES(episode_count)
            """

        seasons_data = []
        for season_data in response_seasons:
            # Transform API data to match the expected structure for the query
            season_entry = {
                "id": season_data.get("id"),
                "poster_url": season_data.get("poster_url"),
                "name": season_data.get("name"),
                "overview": season_data.get("overview"),
                "number": season_data.get("number"),
                "air_date": datetime.strptime(season_data.get("air_date"), "%Y-%m-%d").date() if season_data.get("air_date") else None,
                "episode_count": season_data.get("episode_count"),
            }
            seasons_data.append(season_entry)
            
        DB.insertMany(insert_query, seasons_data)
        print(f"Inserted {len(response_seasons)} records to the seasons table")
        
    except Exception as e:
        print(f"insert error in seasons data {e}")
        flash("An error occurred while inserting data to seasons table. Please try again later.", "danger")
    
    

    # Similar logic for updating seasons data

# def update_details_data():
#     url_details = "/title/3173903/details"
#     response_details = API.get(url_details)


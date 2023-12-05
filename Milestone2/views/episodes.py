from sql.db import DB
from flask import Blueprint, redirect, render_template, request, flash, url_for

episodes = Blueprint('episodes', __name__, url_prefix='/episodes')

@episodes.route('/list', methods=["GET"])
def get_episodes():
    try:
        # Replace "SELECT * FROM episodes" with your actual query
        result = DB.selectAll("SELECT * FROM episodes")
        if result.status:
            rows = result.rows
            print(f"Episode rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch episodes data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
    return render_template("list_episodes.html", rows=rows)

@episodes.route('/<int:season_id>', methods=["GET"])
def get_episodes_by_season(season_id):
    try:
        print(f"Season ID: {season_id}")
        # Replace "SELECT * FROM episodes" with your actual query
        query = """
            SELECT episodes.*, seasons.name AS season_name, seasons.overview AS season_overview
            FROM episodes
            JOIN seasons ON episodes.season_id = seasons.id
            WHERE episodes.season_id = %s;
        """
        result = DB.selectAll(query, season_id)
        if result.status:
            rows = result.rows
            if rows:
                season_name = rows[0]['season_name']
                season_overview = rows[0]['season_overview']
            else:
                season_name = None
                season_overview = None
            print(f"Episode rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch episodes data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
    return render_template("episodes_for_season.html", rows=rows, season_id=season_id,season_name=season_name, season_overview=season_overview)

@episodes.route('/add', methods=["GET","POST"])
def add_episode():
    if request.method == "POST":
        season_id = request.form.get("season_id")
        name = request.form.get("name")
        episode_number = request.form.get("episode_number")
        season_number = request.form.get("season_number")
        tmdb_id = request.form.get("tmdb_id")
        imdb_id = request.form.get("imdb_id")
        thumbnail_url = request.form.get("thumbnail_url")
        release_date = request.form.get("release_date")
        runtime_minutes = request.form.get("runtime_minutes")
        overview = request.form.get("overview")
        
        has_error = False
        if not season_id:
            flash("Missing season ID. Unable to add.", "danger")
            has_error = True
        if not name:
            flash("Missing name. Unable to add.", "danger")
            has_error = True
        if not overview:
            flash("Missing overview. Unable to add.", "danger")
            has_error = True
        if not episode_number:
            flash("Missing number. Unable to add.", "danger")
            has_error = True
        if not season_number:
            flash("Missing season number. Unable to add.", "danger")
            has_error = True
        if not tmdb_id:
            flash("Missing tmdb id. Unable to add.", "danger")
            has_error = True
        if not imdb_id:
            flash("Missing imdb id. Unable to add.", "danger")
            has_error = True
        if not thumbnail_url:
            flash("Missing thumbnail url. Unable to add.", "danger")
            has_error = True
        if not release_date:
            flash("Missing release date. Unable to add.", "danger")
            has_error = True
        if not runtime_minutes:
            flash("Missing runtime minutes. Unable to add.", "danger")
            has_error = True
            
        if not has_error:
            try:
                result = DB.insertOne("""INSERT INTO episodes (season_id, name, episode_number, season_number, tmdb_id,imdb_id, thumbnail_url, release_date, runtime_minutes ,overview)
                                    VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)""", *(season_id, name, episode_number, season_number, tmdb_id,imdb_id, thumbnail_url, release_date, runtime_minutes ,overview))
                if result.status:
                    print("Episode record added")
                    flash("Added Episode Record", "success")
                    return redirect(url_for("episodes.get_episodes"))
                else:
                    flash("An error occurred while adding the episode record. Please try again later.", "danger")
                    return redirect(url_for("episodes.get_episodes"))
            except Exception as e:
                flash("Error occured" + str(e), "error")
                
    return render_template("manage_episodes.html",episode=request.form)



@episodes.route('/edit', methods=["POST"])
def edit_episode():
    if request.method == "POST":
        episode_id = request.form.get("episode_id")
        season_id = request.form.get("season_id")
        name = request.form.get("name")
        overview = request.form.get("overview")
        number = request.form.get("number")
        air_date = request.form.get("air_date")
        has_error = False
        if not episode_id:
            flash("Missing episode ID. Unable to edit.", "danger")
            has_error = True
        if not season_id:
            flash("Missing season ID. Unable to edit.", "danger")
            has_error = True
        if not name:
            flash("Missing name. Unable to edit.", "danger")
            has_error = True
        if not overview:
            flash("Missing overview. Unable to edit.", "danger")
            has_error = True
        if not number:
            flash("Missing number. Unable to edit.", "danger")
            has_error = True
        if not air_date:
            flash("Missing air date. Unable to edit.", "danger")
            has_error = True
            
        if not has_error:
            try:
                result = DB.update("""
                    UPDATE episodes
                    SET season_id = %s, name = %s, overview = %s, number = %s, air_date = %s
                    WHERE id = %s
                """, (season_id, name, overview, number, air_date, episode_id))
                if result.status:
                    print("Episode record updated")
                    flash("Updated Episode Record", "success")
                else:
                    flash("An error occurred while updating the episode record. Please try again later.", "danger")
            except Exception as e:
                flash("Error occured" + str(e), "error")
                
    return render_template("manage_episodes.html",episode=request.form)

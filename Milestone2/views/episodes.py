from flask import Blueprint, render_template, jsonify
from sql.db import DB
from flask import flash
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
        result = DB.selectAll(f"SELECT * FROM episodes WHERE season_id = {season_id}")
        if result.status:
            rows = result.rows
            print(f"Episode rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch episodes data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
    return render_template("episodes_for_season.html", rows=rows, season_id=season_id)
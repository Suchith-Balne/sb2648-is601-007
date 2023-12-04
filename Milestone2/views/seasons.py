from flask import Blueprint, render_template, jsonify
from sql.db import DB
from flask import flash
seasons = Blueprint('seasons', __name__, url_prefix='/seasons')

@seasons.route('/list', methods=["GET"])
def get_episodes():
    try:
        # Replace "SELECT * FROM episodes" with your actual query
        result = DB.selectAll("SELECT * FROM seasons")
        if result.status:
            rows = result.rows
            print(f"Seasons rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch seasons data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
    return render_template("list_seasons.html", rows=rows)
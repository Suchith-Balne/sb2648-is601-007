from flask import Blueprint, render_template, jsonify
from sql.db import DB
from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from roles.permissions import admin_permission

seasons = Blueprint('seasons', __name__, url_prefix='/seasons')

# sb2648, 12/03/23
# Logic to get all the seasons from the database and display them on the list page
@seasons.route('/list', methods=["GET"])
@login_required
def get_seasons():
    try:
        result = DB.selectAll("SELECT * FROM seasons")
        if result.status:
            rows = result.rows
            print(f"Seasons rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch seasons data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
    return render_template("list_seasons.html", rows=rows)

# sb2648, 12/03/23
# Logic to add season to the database 
@seasons.route('/add', methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
@login_required
def add_season():
    if request.method == "POST":
        season_id = request.form.get("season_id")
        poster_url = request.form.get("poster_url")
        name = request.form.get("name")
        overview = request.form.get("overview")
        number = request.form.get("number")
        air_date = request.form.get("air_date")
        episode_count = request.form.get("episode_count")
        has_error = False
        
        if not season_id:
            flash("season id is required.", "danger")
            has_error = True
        
        if not poster_url:
            flash("poster_url is required.", "danger")
            has_error = True
            
        if not name:
            flash("name is required.", "danger")
            has_error = True
        
        if not overview:
            flash("overview is required.", "danger")
            has_error = True
        
        if not number:
            flash("number is required.", "danger")
            has_error = True
        
        if not air_date:
            flash("air date is required.", "danger")
            has_error = True

        if not episode_count:
            flash("Episode count is required.", "danger")
            has_error = True
        
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO seasons (id, poster_url, name, overview, number, air_date, episode_count)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,  *(season_id, poster_url, name, overview, number, air_date, episode_count)
                )
                if result.status:
                    print("Season record created")
                    flash("Created Season Record", "success")
            except Exception as e:
                print(f"insert error {e}")
                flash("An error occurred while creating the season record. Please try again later.", "danger")
    return render_template("manage_seasons.html",season=request.form)

# sb2648, 12/03/23
# Logic to edit seasons from the list page  and perform update to the database
@seasons.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
@login_required
def edit_season():
    
    row = {}
    
    season_id = request.args.get('id')
    if not season_id:
        flash("Missing season ID. Unable to edit.", "danger")
    else:
        if request.method == "POST":
            season_id = request.form.get("season_id")
            poster_url = request.form.get("poster_url")
            name = request.form.get("name")
            overview = request.form.get("overview")
            number = request.form.get("number")
            air_date = request.form.get("air_date")
            episode_count = request.form.get("episode_count")
            has_error = False
            
            if not season_id:
                flash("season id is required.", "danger")
                has_error = True
            
            if not poster_url:
                flash("poster_url is required.", "danger")
                has_error = True
                
            if not name:
                flash("name is required.", "danger")
                has_error = True
            
            if not overview:
                flash("overview is required.", "danger")
                has_error = True
            
            if not number:
                flash("number is required.", "danger")
                has_error = True
            
            if not air_date:
                flash("air date is required.", "danger")
                has_error = True

            if not episode_count:
                flash("Episode count is required.", "danger")
                has_error = True
            
            if not has_error:
                try:
                    result = DB.update("""
                                        UPDATE seasons
                                        SET poster_url = %s, name = %s, overview = %s, number = %s, air_date = %s, episode_count = %s
                                        WHERE id = %s
                                        """, (poster_url, name, overview, number, air_date, episode_count, season_id))
                    if result.status:
                        print("Season record updated")
                        flash("Updated Season Record", "success")
                        return redirect(url_for("seasons.get_seasons"))
                    else:
                        flash("An error occurred while updating the season record. Please try again later.", "danger")
                        return redirect(url_for("seasons.get_seasons"))
                except Exception as e:
                    print(f"Update error {e}")
                    flash("An error occurred while updating the season record. Please try again later.", "danger")
                    return redirect(url_for("seasons.get_seasons"))
        try:
            result = DB.selectOne("""SELECT * FROM seasons
            WHERE id = %s""", season_id)
            
            if result.status:
                row = result.row
        except Exception as e:
            flash("Error occured" + str(e), "error")
    return render_template("manage_seasons.html",season=row)

# sb2648, 12/05/23
# Logic to delete episode from database
@seasons.route("/delete", methods=["GET"])
@login_required
@admin_permission.require(http_exception=403)
def delete_season():
    season_id = request.args.get('id')
    if not season_id:
        flash("Missing season ID. Unable to delete.", "danger")
    else:
        try:
            result = DB.delete("""
            DELETE FROM seasons
            WHERE id = %s
            """, season_id)
            if result.status:
                print("Season record deleted")
                flash("Deleted Season Record", "success")
            else:
                flash("An error occurred while deleting the season record. Please try again later.", "danger")
        except Exception as e:
            flash("Error occured" + str(e), "error")
    return redirect(url_for("seasons.get_seasons"))
                
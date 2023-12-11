from sql.db import DB
from flask import Blueprint, redirect, render_template, request, flash, url_for, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from roles.permissions import admin_permission

episodes = Blueprint('episodes', __name__, url_prefix='/episodes')


def get_totals(partial_query, args={}):
    try:
        result = DB.selectOne("""SELECT count(1) as total FROM """ +  partial_query, args)
        if result.status and result.row:
            total = int(result.row["total"])
    except Exception as e:
        print(f"Error in totals:{e}")
        total = 0
    return total
    

@episodes.route('/list', methods=["GET"])
@login_required
# sb2648, 12/03/23
# Logic to get all the episodes list and filter the list from the form
def get_episodes():
    rows = []
    args = {"user_id": current_user.id}
    episode_name = request.args.get("episode_name")
    limit = request.args.get("limit", 10)
    season_number = request.args.get("season_number")
    
    query = """SELECT episodes.*,
    IFNULL((SELECT COUNT(1) FROM episodes_watchlist WHERE user_id = %(user_id)s AND episode_id = episodes.id),0) as `is_assoc` FROM  episodes
    WHERE 1=1"""
    
    if episode_name:
        query += " AND name LIKE %(episode_name)s"
        args["episode_name"] = f"%{episode_name}%"
    if season_number:
        query += " AND season_number = %(season_number)s"
        args["season_number"] = f"{season_number}"
    try:
        if 1 <= int(limit) <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = int(limit)
        else:
            raise ValueError("Limit must be a number between 1 and 100")
    except ValueError as e:
        flash(str(e), "danger")
    
    try:
        print(f"Query: {query}")
        print(f"Args: {args}")
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            print(f"Episode rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch episodes data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
        
    total_records = get_totals("episodes")
    return render_template("list_episodes.html", rows=rows, total_records=total_records)

# sb2648, 12/03/23
# Logic to get episodes for particluar season
@episodes.route('/<int:season_id>', methods=["GET"])
@login_required
def get_episodes_by_season(season_id):
    rows = []
    args = {"user_id": current_user.id}
    episode_name = request.args.get("episode_name")
    limit = request.args.get("limit", 10)
    season_number = request.args.get("season_number")
    try:
        query = """
            SELECT episodes.*, seasons.name AS season_name, seasons.overview AS season_overview
            FROM episodes
            JOIN seasons ON episodes.season_id = seasons.id
            WHERE episodes.season_id = %s
        """
        result = DB.selectAll(query, season_id)
        if result.status:
            rows = result.rows
            print(f"Episode rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch episodes data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
    total_records = get_totals("episodes")
    return render_template("list_episodes.html", rows=rows, season_id=season_id,total_records=total_records )

# sb2648, 12/03/23
# Logic to add episode to the database
@episodes.route('/add', methods=["GET","POST"])
@admin_permission.require(http_exception=403)
@login_required
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

# sb2648, 12/03/23
# Logic to edit episode and perform update to the database
@episodes.route('/edit', methods=["GET","POST"])
@admin_permission.require(http_exception=403)
@login_required
def edit_episode():
    episode_id = request.args.get('id')
    if not episode_id:
        flash("Missing episode ID. Unable to edit.", "danger")
    else:
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
            
            if not episode_id:
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
                    result = DB.update("""UPDATE episodes SET name=%s, season_id=%s, season_number=%s, tmdb_id=%s,imdb_id=%s, thumbnail_url=%s, release_date=%s, runtime_minutes=%s, overview=%s
                                    WHERE id=%s""", *(name, season_id, season_number, tmdb_id,imdb_id, thumbnail_url, release_date, runtime_minutes, overview, episode_id))
                    if result.status:
                        print("Episode record updated")
                        flash("Updated Episode Record", "success")
                        return redirect(url_for("episodes.get_episodes"))
                    else:
                        flash("An error occurred while updating the episode record. Please try again later.", "danger")
                        return redirect(url_for("episodes.get_episodes"))
                except Exception as e:
                    flash("Error occured" + str(e), "error")
                    
        try:
            result = DB.selectOne("""SELECT * FROM episodes
            WHERE id = %s""", request.args.get("id"))
            
            if result.status:
                row = result.row
                return render_template("manage_episodes.html",episode=row) 
            else:
                flash("An error occurred while fetching the episode record. Please try again later.", "danger")
                return redirect(url_for("episodes.get_episodes"))
        except Exception as e:
            flash("Error occured" + str(e), "error")
            
    return redirect(url_for("episodes.get_episodes"))

# sb2648, 12/03/23
# Logic to delete episode from database
@episodes.route('/delete', methods=["GET"])
@admin_permission.require(http_exception=403)
@login_required
def delete_episode():
    episode_id = request.args.get('id')

    if not episode_id:
        flash("Missing episode ID. Unable to delete.", "danger")
    else:
        try:
            result = DB.delete("""DELETE FROM episodes
            WHERE id = %s""", episode_id)
            
            if result.status:
                print("Episode record deleted")
                flash("Deleted Episode Record", "success")
            else:
                flash("An error occurred while deleting the episode record. Please try again later.", "danger")
        except Exception as e:
            flash("Error occured" + str(e), "error")
    return redirect(url_for("episodes.get_episodes"))

@episodes.route('/track', methods=["GET"])
@login_required
def track():
    episode_id = request.args.get('id')
    print(episode_id)
    args = {**request.args}
    del args["id"]
    if not episode_id:
        flash("Missing id. Unable to add to watchlist.", "danger")
    else:
        args = {"user_id": current_user.id, "episode_id": episode_id}
        try:
            try:
                result = DB.insertOne("INSERT INTO episodes_watchlist (user_id, episode_id) VALUES (%(user_id)s, %(episode_id)s)", args)
                print(result.status)
                if result.status:
                    flash("Added to watchlist", "success")
                else:
                    print(result.status)
                    flash(f"Not added {result.status}")
            except Exception as e:
                print(e)
                print(f"Duplicate ececption can be ignored {e}")
                result = DB.delete("DELETE FROM episodes_watchlist WHERE user_id = %(user_id)s AND episode_id = %(episode_id)s", args)
                if result.status:
                    flash("Removed from watchlist", "success")
        except Exception as e:
            print(f"Error occured while track/untrack {e}")
            flash("An unhandled error occured.Please try again" + str(e), "error")
    return redirect(url_for("episodes.get_episodes", **args))

@episodes.route('/watchlist', methods=["GET"])
@login_required
def watchlist():
    watchlist_id = request.args.get('id', current_user.id)
    rows = []
    args = {"user_id": watchlist_id}
    episode_name = request.args.get("episode_name")
    limit = request.args.get("limit", 10)
    season_number = request.args.get("season_number")
    
    query = """SELECT e.*,1 as 'is_assoc'
    FROM episodes e 
    JOIN
    episodes_watchlist w ON e.id = w.episode_id
    WHERE w.user_id = %(user_id)s"""
    
    where = ""
    
    if episode_name:
        args["episode_name"] = f"%{episode_name}%"
        where += " AND name LIKE %(episode_name)s"
    if season_number:
        args["season_number"] = f"{season_number}"
        where += " AND season_number = season_number"
    try:
        if 1 <= int(limit) <= 100:
            args["limit"] = int(limit)
            where += " LIMIT %(limit)s"
        else:
            raise ValueError("Limit must be a number between 1 and 100")
    except ValueError as e:
        flash(str(e), "danger")
    
    try:
        print(f"Query: {query+where}")
        print(f"Args: {args}")
        result = DB.selectAll(query+where, args)
        if result.status:
            rows = result.rows
            print(f"Episode rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch episodes data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
        
    total_records = get_totals("episodes e JOIN episodes_watchlist w ON e.id = w.episode_id WHERE w.user_id = %(user_id)s ", {"user_id": watchlist_id})
    return render_template("list_episodes.html", rows=rows, title = "Watchlist", total_records = total_records)

@episodes.route('/clear', methods=["GET"])
@login_required
def clear():
    userid = request.args.get("id")
    args = {**request.args}
    if "id" in args:
        del args["id"]
    
    if not userid:
        flash("Missing id. Unable to add to watchlist.", "danger")
    else:
        if userid == current_user.id or current_user.has_role("Admin"):
            result = DB.delete("DELETE FROM episodes_watchlist WHERE user_id = %(user_id)s", {"user_id":userid})
            try:
                if result.status:
                    flash("Watchlist cleared", "success")
                else:
                    flash("Unable to clear watchlist", "danger")
            except Exception as e:
                flash("Error occured while clearing watchlist" + str(e), "error")
    return redirect(url_for("episodes.watchlist", **args))


@episodes.route("/associations", methods=["GET"])
@admin_permission.require(http_exception=403)
@login_required
def associations():
    rows = []
    args = {}
    
    episode_name = request.args.get("episode_name")
    limit = request.args.get("limit", 10)
    username = request.args.get("username")
    season_number = request.args.get("season_number")
    
    query = """SELECT u.id as user_id, username, e.*,1 as 'is_assoc' FROM episodes e JOIN episodes_watchlist w ON e.id = w.episode_id LEFT JOIN IS601_Users u on u.id = w.user_id 
    WHERE 1=1"""
    where = ""
    
    if username:
        args["username"] = f"%{username}%"
        where += " AND username LIKE %(username)s"
    if episode_name:
        args["episode_name"] = f"%{episode_name}%"
        where += " AND name LIKE %(episode_name)s"
    if season_number:
        args["season_number"] = f"{season_number}"
        where += " AND season_number = season_number"
    try:
        if 1 <= int(limit) <= 100:
            args["limit"] = int(limit)
            where += " LIMIT %(limit)s"
        else:
            raise ValueError("Limit must be a number between 1 and 100")
    except ValueError as e:
        flash(str(e), "danger")
    
    try:
        print(f"Query: {query}")
        print(f"Args: {args}")
        result = DB.selectAll(query+where, args)
        if result.status:
            rows = result.rows
            print(f"Episode rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch episodes data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
        
    total_records = get_totals("episodes e JOIN episodes_watchlist w ON e.id = w.episode_id")
    print(total_records)
    return render_template("admin_watchlist.html", rows=rows, total_records = total_records, username=username, title = "Users Episodes Watchlist")

@episodes.route("/unwatched", methods=["GET"])
# @admin_permission.require(http_exception=403)
@login_required
def unwatched():
    rows = []
    args = {"user_id": current_user.id}    
    episode_name = request.args.get("episode_name")
    limit = request.args.get("limit", 10)
    season_number = request.args.get("season_number")
    
    query = """SELECT e.*,
    IFNULL((SELECT COUNT(1) FROM episodes_watchlist w WHERE user_id = %(user_id)s AND episode_id = e.id),0) as 'is_assoc'
    FROM  episodes e
    WHERE e.id not in (SELECT DISTINCT episode_id FROM episodes_watchlist WHERE episode_id = e.id)
    """
    where =""
    # if username:
    #     args["username"] = f"%{username}%"
    #     where += " AND username LIKE %(username)s"
    if episode_name:
        args["episode_name"] = f"%{episode_name}%"
        where += " AND name LIKE %(episode_name)s"
    if season_number:
        args["season_number"] = f"{season_number}"
        where += " AND season_number = season_number"
    try:
        if 1 <= int(limit) <= 100:
            args["limit"] = int(limit)
            where += " LIMIT %(limit)s"
        else:
            raise ValueError("Limit must be a number between 1 and 100")
    except ValueError as e:
        flash(str(e), "danger")
    
    try:
        print(f"Query: {query}")
        print(f"Args: {args}")
        result = DB.selectAll(query+where, args)
        if result.status:
            rows = result.rows
            print(f"Episode rows: {rows}")
        else:
            return jsonify({"status": "error", "message": "Failed to fetch episodes data"})
    except Exception as e:
        flash("Error occured" + str(e), "error")
        
    total_records = get_totals("episodes e WHERE e.id not in (SELECT DISTINCT episode_id FROM episodes_watchlist) ")
    print(total_records)
    return render_template("unwatchedlist.html", rows=rows, total_records = total_records, title = "Unwatched Episodes")

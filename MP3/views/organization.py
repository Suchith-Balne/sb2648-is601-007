from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB

import pycountry
organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    # sb2648
    # DO NOT DELETE PROVIDED COMMENTS
    # search-1 retrieve id, name, address, city, country, state, zip, website, donation count as donations for the organization
    # don't do SELECT * and replace the below "..." portion
    allowed_columns = ["name", "address", "description","website","city", "country", "state", "zip"]
    query = """SELECT DISTINCT O.id, O.name, O.description, O.address, O.city, O.country, O.state, O.zip, O.website FROM
    IS601_MP3_Organizations AS O LEFT JOIN IS601_MP3_Donations AS D ON O.id = D.organization_id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders

    # sb2648
    # search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    
    #sb2648
    # search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{name}%"
    # sb2648
    # search-4 append an equality filter for country if provided
    if country:
        query += " AND country LIKE %(country)s"
        args["country"] = f"%{country}%"
    # search-5 append an equality filter for state if provided
    if state:
        query += " AND state LIKE %(state)s"
        args["state"] = f"%{state}%"
    # search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    if column and order and column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"
    # sb2648
    # search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    # sb2648
    # search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    try:
        if 1 <= int(limit) <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
        else:
            raise ValueError("Limit must be a number between 1 and 100")
    except ValueError as e:
        flash(str(e), "danger")
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        print(f"result {result.rows}")
        if result.status:
            rows = result.rows
    except Exception as e:
        # sb2648
        # search-9 make message user friendly
        #flash(str(e), "danger")
        flash("DB error occured try modifying the search", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    allowed_columns = [(column, column.replace("_", " ").title()) for column in allowed_columns]
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)

@organization.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        has_error = False # use this to control whether or not an insert occurs
        
        # sb2648
        # add-1 retrieve form data for name, address, city, state, country, zip, website, description
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zipcode = request.form.get("zip")
        website = request.form.get("website")
        description = request.form.get("description")
        # sb2648
        #  add-2 name is required (flash proper error message)
        if not name:
            flash("Organization name is required.", "danger")
            has_error = True
        
        # sb2648
        #  add-3 address is required (flash proper error message)
        if not address:
            flash("Address is required.", "danger")
            has_error = True
            
        # sb2648
        #  add-4 city is required (flash proper error message)
        if not city:
            flash("City is required.", "danger")
            has_error = True
            
        # sb2648
        #  add-5 state is required (flash proper error message)
        if not state:
            flash("State is required.", "danger")
        
        # sb2648
        # add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint: see geography.py and pycountry documentation to solve this
        valid_states = [subdivision.code.split('-')[1] for subdivision in pycountry.subdivisions.get(country_code=country)]
        if state and state not in valid_states:
            flash("Invalid state selected.", "danger")

        # sb2648
        # add-6 country is required (flash proper error message)
        if not country:
            flash("Country is required.", "danger")
        
        # add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation to solve this
        valid_countries = [country.alpha_2 for country in pycountry.countries]
        if country and country not in valid_countries:
            flash("Invalid country selected.", "danger")

        # sb2648
        # add-7 website is not required
        if not website:
            flash("Website is required.", "danger")
            has_error = False
        
        # sb2648
        # add-8 zip is required (flash proper error message)
        if not zipcode:
            flash("Zipcode is required.", "danger")
            has_error = True
        
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        
        # sb2648
        # add-9 description is not required
        if not description:
            flash("Description is required.", "danger")
            has_error = False

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Organizations (name, address, city, state, country, zip, website, description, created, modified)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """, *(name, address, city, state, country, zipcode, website, description)) 
                # sb2648
                # add-10 add query and add arguments
                if result.status:
                    flash("Added Organization", "success")
            except Exception as e:
                # add-11 make message user friendly
                flash("Error Occured:" + str(e), "error")
        
    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    # sb2648
    # edit-1 request args id is required (flash proper error message)
    org_id = request.args.get("id")
    if not org_id:
        flash("Organization ID is required.", "error")
        return redirect(url_for("organization.search"))
    else:
        if request.method == "POST":
            #data = {"id": org_id} # use this as needed, can convert to tuple if necessary
            # sb2648
            # edit-2 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zip_code = request.form.get("zip")
            website = request.form.get("website")
            # sb2648
            has_error = False
            # edit-3 name is required (flash proper error message)
            if not name:
                has_error = True
                flash("Name is required.", "danger")
            # sb2648
            #  edit-4 address is required (flash proper error message)
            if not address:
                has_error = True
                flash("Address is required.", "danger")
            # sb2648
            #  edit-5 city is required (flash proper error message)
            if not city:
                has_error = True
                flash("City is required.", "danger")
            # sb2648
            #  edit-6 state is required (flash proper error message)
            if not state:
                has_error = True
                flash("State is required.", "danger")
            # sb2648
            #  edit-6a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            valid_states = [subdivision.code.split('-')[1] for subdivision in pycountry.subdivisions.get(country_code=country)]
            if state and state not in valid_states:
                flash("Invalid state selected.", "danger")
            # sb2648
            #  edit-7 country is required (flash proper error message)
            if not country:
                has_error = True
                flash("Country is required.", "danger")
            # sb2648
            #  edit-7a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            valid_countries = [country.alpha_2 for country in pycountry.countries]
            if country and country not in valid_countries:
                has_error = True
                flash("Invalid country selected.", "danger")
            # sb2648
            #  edit-8 website is not required
            if not website:
                has_error = False
            # sb2648
            #  edit-9 zipcode is required (flash proper error message)
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            if not zip_code:
                has_error = True
                flash("Zipcode is required.", "danger")
            # populate data dict with mappings
            #has_error = False # use this to control whether or not an insert occurs

            if not has_error:
                try:
                    # sb2648
                    #  edit-10 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE IS601_MP3_Organizations
                    SET
                        name = %s,
                        address = %s,
                        city = %s,
                        state = %s,
                        country = %s,
                        zip = %s,
                        website = %s
                    WHERE id = %s;
                    """, *(name,address,city,state,country,zip_code,website,org_id))
                    
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # sb2648
                    # edit-11 make this user-friendly
                    print(f"{e}")
                    flash("Error updating record. Please try again.", "danger")

        row = {}
        try:
            # sb2648
            #  edit-12 fetch the updated data
            result = DB.selectOne("SELECT name,description, address, website,city, state, country, zip  FROM IS601_MP3_Organizations WHERE id = %s", org_id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # sb2648
            #  edit-13 make this user-friendly
            flash("Error fetching data. Please try again.", "danger")
    
    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    # sb2648
    # delete-1 if id is missing, flash necessary message and redirect to search
    org_id = request.args.get("id")
    if not org_id:
        flash("Organization ID is missing. Unable to delete.", "error")
        return redirect(url_for("organization.search"))
    # sb2648
    # delete-2 delete organization by id (note: you'll likely need to trigger a delete of all donations related to this organization first due to foreign key constraints)
    try:
        query_delete_donations = "DELETE FROM IS601_MP3_Donations WHERE organization_id = %s;"
        result = DB.delete(query_delete_donations, org_id)
        
        query_delete_organizations = "DELETE FROM IS601_MP3_Organizations WHERE id = %s;"
        result = DB.delete(query_delete_organizations, org_id)
        
        if result.status:
            # sb2648
            # delete-3 ensure a flash message shows for successful delete
            flash("Donation successfully deleted.", "success")
        else:
            flash("Error deleting donation. Please try again.", "error")
    except Exception as e:
        flash(str(e), "danger")
    # sb2648
    # delete-4 pass all argument except id to this route
    args = request.args.copy()
    args.pop('id', None)
    
    # sb2648
    # delete-5 redirect to organization search
    return redirect(url_for("organization.search", **args))
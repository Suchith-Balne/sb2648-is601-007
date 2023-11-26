from datetime import datetime, timedelta
import re
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
donations = Blueprint('donations', __name__, url_prefix='/donations')

@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    # DO NOT DELETE PROVIDED COMMENTS
    
    # UCID: sb2648 
    # search-1 retrieve donation id as id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments, organization_name using a LEFT JOIN
    query = """select d.donor_firstname, d.donor_lastname, d.donor_email, O.name as organization_name ,d.item_name,d.item_description, d.item_quantity, d.created, d.modified , d.id, d.organization_id, d.donation_date, d.comments from IS601_MP3_Donations as d LEFT JOIN IS601_MP3_Organizations as O on d.organization_id=O.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "organization_name" ,"item_name", "item_quantity", "created", "modified"]
    
    # UCID: sb2648 
    # search-2 get fn, ln, email, organization_id, column, order, limit from request args
    fn = request.args.get("first_name")
    ln = request.args.get("last_name")
    email = request.args.get("email")
    organization_id = request.args.get("organization_id")
    item_name = request.args.get("item_name")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    
    # UCID: sb2648 
    # search-3 append like filter for donor_firstname if provided
    if fn:
        query += " AND donor_firstname LIKE %(donor_firstname)s"
        args["donor_firstname"] = f"%{fn}%"
        
    # UCID: sb2648 
    # search-4 append like filter for donor_lastname if provided
    if ln:
        query += " AND donor_lastname LIKE %(donor_lastname)s"
        args["donor_lastname"] = f"%{ln}%"
        
    # UCID: sb2648 
    # search-5 append like filter for donor_email if provided
    if email:
        query += " AND donor_email LIKE %(donor_email)s"
        args["donor_email"] = f"%{email}%"
        
    # UCID: sb2648 
    # search-6 append like filter for item_name if provided
    if item_name:
        query += " AND item_name LIKE %(item_name)s"
        args["item_name"] = f"%{item_name}%"
    
    # UCID: sb2648  
    # search-7 append equality filter for organization_id if provided
    if organization_id:
        query += " AND organization_id = %(organization_id)s"
        args["organization_id"] = organization_id
        
    # UCID: sb2648 
    # search-8 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order and column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"
        
    # UCID: sb2648 
    # search-9 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # UCID: sb2648 
    # search-10 provide a proper error message if limit isn't a number or if it's out of bounds
    try:
        if 1 <= int(limit) <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
        else:
            raise ValueError("Limit must be a number between 1 and 100")
    except ValueError as e:
        flash(str(e), "danger")
    
    #print("query",query)
    #print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            print(f"rows: {rows}")
    except Exception as e:
        # search-11 make message user friendly
        flash("DB error occured try modifying the search", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = [(column, column.replace("_", " ").title()) for column in allowed_columns]
    
    # search-12 if request args has organization identifier set organization_name variable to the correct name
    organization_id = request.args.get("organization_id")
    if organization_id:
        organization_name_result = DB.selectOne("SELECT name FROM IS601_MP3_Organizations WHERE id = %(organization_id)s", {"organization_id": organization_id})
        if organization_name_result.status:
            organization_name = organization_name_result.row["name"]
    
    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns)


@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # UCID: sb2648
        # add-1 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments")
        has_error = False
        
        # UCID: sb2648
        # add-2 donor_firstname is required (flash proper error message)
        if not donor_firstname:
            flash("Donor First Name is required.", "danger")
            has_error = True
            
        # UCID: sb2648
        # add-3 donor_lastname is required (flash proper error message)
        if not donor_lastname:
            flash("Donor Last Name is required.", "danger")
            has_error = True
        
        # UCID: sb2648
        # add-4 donor_email is required (flash proper error message)
        if not donor_email:
            flash("Donor Email is required.", "danger")
            has_error = True
        
        # UCID: sb2648
        #  add-4a email must be in proper format (flash proper message)
        if donor_email and not is_valid_email(donor_email):
            flash("Invalid email format.", "danger")
            has_error = True
        
        # UCID: sb2648
        # add-5 organization_id is required (flash proper error message)
        if not organization_id:
            flash("Organization ID is required.", "danger")
            has_error = True
            
        # UCID: sb2648
        #  add-6 item_name is required (flash proper error message)
        if not item_name:
            flash("Item Name is required.", "danger")
            has_error = True
        
        # UCID: sb2648
        # add-7 item_description is optional
        if not item_description:
            has_error = False
        
        # UCID: sb2648
        #  add-8 item_quantity is required and must be more than 0 (flash proper error message)
        if not item_quantity or int(item_quantity) <= 0:
            flash("Item Quantity must be greater than 0.", "danger")
            has_error = True
        
        # UCID: sb2648
        # add-9 donation_date is required and must be within the past 30 days
        if not donation_date or not is_valid_date(donation_date):
            flash("Invalid or missing Donation Date.", "danger")
            has_error = True
        
        # UCID: sb2648
        # add-10 comments are optional
        if not comments:
            has_error = False # use this to control whether or not an insert occurs
        
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Donations (donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,  *(donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments)
                )     # UCID: sb2648      # add-11 add query and add arguments
                if result.status:
                    print("donation record created")
                    flash("Created Donation Record", "success")
            except Exception as e:
                # UCID: sb2648
                # add-7 make message user friendly
                print(f"insert error {e}")
                flash("An error occurred while creating the donation record. Please try again later.", "danger")

    return render_template("manage_donation.html",donation=request.form)

def is_valid_email(email):
    # Basic email format validation using regular expression
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(re.match(email_pattern, email))

def is_valid_date(date_str):
    try:
        # Basic date format validation using datetime
        date_format = "%Y-%m-%d"
        date_obj = datetime.strptime(date_str, date_format)
        
        # Check if the date is within the past 30 days
        thirty_days_ago = datetime.now() - timedelta(days=30)
        return date_obj >= thirty_days_ago
    except ValueError:
        return False

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}
    
    # TODO edit-1 request args id is required (flash proper error message)
    id = False
    if not id: # TODO update this for TODO edit-1
        pass
    else:
        if request.method == "POST":
            
            # TODO add-2 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            # TODO add-3 donor_firstname is required (flash proper error message)
            # TODO add-4 donor_lastname is required (flash proper error message)
            # TODO add-5 donor_email is required (flash proper error message)
            # TODO add-5a email must be in proper format (flash proper message)
            # TODO add-6 organization_id is required (flash proper error message)
            # TODO add-7 item_name is required (flash proper error message)
            # TODO add-8 item_description is optional
            # TODO add-9 item_quantity is required and must be more than 0 (flash proper error message)
            # TODO add-10 donation_date is required and must be within the past 30 days
            # TODO add-11 comments are optional
            has_error = False # use this to control whether or not an insert occurs
                
            if not has_error:
                try:
                    # TODO edit-12 fill in proper update query
                    result = DB.update("""
                    UPDATE ... SET
                    ...
                    """, ...)
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-13 make this user-friendly
                    print(f"update error {e}")
                    flash(e, "danger")
        
        try:
            # TODO edit-14 fetch the updated data 
            result = DB.selectOne("""SELECT 
            ...
            FROM ... LEFT JOIN ... 
              
             WHERE ..."""
            , id)
            
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-15 make this user-friendly
            flash(str(e), "danger")
    
    return render_template("manage_donation.html", donation=row)

@donations.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # TODO delete-2 delete donation by id (fetch the id from the request)
    # TODO delete-3 ensure a flash message shows for successful delete
    # TODO delete-4 pass all argument except id to this route
    # TODO delete-5 redirect to donation search
    pass

    # return redirect(url_for("donations.search", **args))
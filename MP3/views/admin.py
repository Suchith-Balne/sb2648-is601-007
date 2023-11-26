import csv
import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        
        # UCID: sb2648, Date: 11/25/2023
        # importcsv-1 check that it's a .csv file, return a proper flash message if it's not and don't attempt to process the file
        if file and secure_filename(file.filename):
            imported_file = secure_filename(file.filename)
            if imported_file.endswith('.csv'):
                organizations = []
                donations = []
                # DON'T EDIT
                organization_query = """
                INSERT INTO IS601_MP3_Organizations (name, address, city, country, state, zip, website, description)
                            VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s, %(description)s)
                            ON DUPLICATE KEY UPDATE 
                            address=values(address),
                            city=values(city),
                            country=values(country),
                            state=values(state),
                            zip=values(zip),
                            website=values(website),
                            description=values(description)
                """
                # DON'T EDIT
                donation_query = """
                INSERT INTO IS601_MP3_Donations (donor_firstname, donor_lastname, donor_email, item_name, item_description, item_quantity, organization_id, donation_date, comments)
                        VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(item_name)s, %(item_description)s, %(quantity)s, 
                                (SELECT id FROM IS601_MP3_Organizations WHERE name = %(organization_name)s LIMIT 1), 
                                %(donation_date)s, %(comments)s)
                        ON DUPLICATE KEY UPDATE 
                                                donor_firstname=%(donor_firstname)s,
                                                donor_lastname=%(donor_lastname)s,
                                                donor_email=%(donor_email)s,
                                                item_name=%(item_name)s, 
                                                item_quantity = %(quantity)s,
                                                item_description= %(item_description)s,
                                                comments=%(comments)s, 
                                                organization_id = (SELECT id FROM IS601_MP3_Organizations WHERE name=%(organization_name)s LIMIT 1),
                                                donation_date = %(donation_date)s,
                                                comments=%(comments)s
                """
                # Note: this reads the file as a stream instead of requiring us to save it, don't modify/remove it
                stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
                
                # importcsv-2 read the csv file stream as a dict
                # UCID: sb2648, Date: 11/25/2023
                for row in csv.DictReader(stream): 
                    
                    # UCID: sb2648, Date: 11/25/2023
                    # importcsv-3: extract organization data and append to organization list
                    # as a dict only with organization data if all organization fields are present (refer to above SQL)
                    if all(key in row for key in ['organization_name', 'organization_address', 'organization_city', 'organization_country', 'organization_state', 'organization_zip', 'organization_website', 'organization_description']):
                        organizations.append({
                            "name": row["organization_name"],
                            "address": row["organization_address"],
                            "city": row["organization_city"],
                            "country": row["organization_country"],
                            "state": row["organization_state"],
                            "zip": row["organization_zip"],
                            "website": row["organization_website"],
                            "description": row["organization_description"]
                        })
                        
                    # UCID: sb2648, Date: 11/25/2023
                    # importcsv-4: extract donation data and append to donation list
                    # as a dict only with donation data if all donation fields are present (refer to above SQL)
                    if all(key in row for key in ['donor_name', 'donor_email', 'item_name', 'item_description', 'item_quantity', 'donation_date', 'comments', 'organization_name']):
                        donations.append({
                            "donor_firstname": row["donor_name"].split()[0] if row["donor_name"] else '',
                            "donor_lastname": row["donor_name"].split()[1] if len(row["donor_name"].split()) > 1 else '',
                            "donor_email": row["donor_email"],
                            "item_name": row["item_name"],
                            "quantity": row["item_quantity"],
                            "item_description": row["item_description"],
                            "organization_name": row["organization_name"],
                            "donation_date": row["donation_date"],
                            "comments": row["comments"]
                        })
                    
                if len(organizations) > 0:
                    print(f"Inserting or updating {len(organizations)} organizations")
                    try:
                        result = DB.insertMany(organization_query, organizations)
                        # importcsv-5 display flash message about number of organizations inserted
                        # UCID: sb2648, Date: 11/25/2023
                        flash(f"Inserted or updated {len(organizations)} organizations", "success")
                    except Exception as e:
                        traceback.print_exc()
                        flash("There was an error loading in the csv data", "danger")
                else:
                    # importcsv-6 display flash message (info) that no organizations were loaded
                    # UCID: sb2648, Date: 11/25/2023
                    flash("No organizations were loaded from the CSV file", "info")
                if len(donations) > 0:
                    print(f"Inserting or updating {len(donations)} donations")
                    try:
                        result = DB.insertMany(donation_query, donations)
                        # importcsv-7 display flash message about number of donations loaded
                        # UCID: sb2648, Date: 11/25/2023
                        flash(f"Inserted or updated {len(donations)} donations", "success")
                    except Exception as e:
                        traceback.print_exc()
                        flash("There was an error loading in the csv data", "danger")
                else:
                    # importcsv-8 display flash message (info) that no donations were loaded
                    # UCID: sb2648, Date: 11/25/2023
                    flash("No donations were loaded from the CSV file", "info")
                try:
                    result = DB.selectOne("SHOW SESSION STATUS LIKE 'questions'")
                    print(f"Result {result}")
                except Exception as e:
                        traceback.print_exc()
                        flash("There was an error counting session queries", "danger")
            else:
                flash("Only csv files are allowed", "danger")
    return render_template("upload.html")
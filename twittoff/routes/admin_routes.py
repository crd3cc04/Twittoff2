# twittoff/routes/admin_routes.py
  # Resets the whole database without deleting the tables.....

from flask import Blueprint, jsonify, request, flash, redirect # render_template

from twittoff.model import db

admin_routes = Blueprint("admin_routes", __name__)

API_KEY = "him1203"

#GET /admin/db/reset?api_key=him1203
@admin_routes.route("/admin/db/reset")
def reset_db():
#    print(type(db))
#    db.drop_all()
#    db.create_all()
#    return jsonify({"message": "DB RESET OK"})

    print("URL PARMS", dict(request.args))

    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()
        return jsonify({"message": "DB RESET OK"})
    else:
        print("PERMISSION DENIED")
        flash("OOPS Permission Denied", "danger")
        return redirect("/")

  
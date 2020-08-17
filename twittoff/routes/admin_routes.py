# twittoff/routes/admin_routes.py
  # Resets the whole database without deleting the tables.....
  
from flask import Blueprint, jsonify, request, flash, redirect # render_template

from twittoff.model import db

admin_routes = Blueprint("admin_routes", __name__)

@admin_routes.route("/admin/db/reset")
def reset_db():
    print(type(db))
    db.drop_all()
    db.create_all()
    return jsonify({"message": "DB RESET OK"})

  
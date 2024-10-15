from flask import Flask, request, redirect, jsonify
from pymongo import MongoClient  # or use SQLAlchemy for PostgreSQL

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client.tiny_urlz_db
urls = db.urls

@app.route('/shorten', methods=['POST'])
def shorten_url():
    # Extract the URL from the request
    data = request.json
    original_url = data.get('url')
    # Generate a short URL and save to DB...
    return jsonify({"short_url": "generated_short_url"})

@app.route('/<short_id>')
def redirect_to_url(short_id):
    # Lookup the short_id in the database...
    return redirect("original_url")

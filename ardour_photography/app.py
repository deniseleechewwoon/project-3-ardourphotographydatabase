from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

app = Flask(__name__)

CLOUD_NAME = os.environ.get("CLOUD_NAME")

MONGO_URI = os.environ.get('MONGO_URL')
DB_NAME = "ardour_photography"

client = pymongo.MongoClient(MONGO_URI)


@app.route('/photo/create')
def create_photo():
    return render_template('create_photo.template.html')

@app.route('/photo/create', methods=["POST"])
def process_create_photo():
    image_name = request.form.get('image_name')
    photographer_name = request.form.get('photographer_name')
    image_location = request.form.get('image_location')
    image_year = request.form.get('image_year')

    client[DB_NAME].photo.insert_one({
        "title": image_name,
        "photographer": photographer_name,
        "location": image_location,
        "year": image_year
    })

    return "New Photograph Saved"

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

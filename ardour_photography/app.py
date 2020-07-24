from flask import Flask, render_template, request, redirect, url_for
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo

load_dotenv()

app = Flask(__name__)

CLOUD_NAME = os.environ.get("CLOUD_NAME")

MONGO_URI = os.environ.get('MONGO_URL')
DB_NAME = "ardour_photography"

client = pymongo.MongoClient(MONGO_URI)


@app.route('/photos')
def show_all_photos():
    search_terms = request.args.get('search-terms')

    criteria = {}
    
    if search_terms != "" and search_terms is not None:
        criteria['title'] = {
            "$regex": search_terms,
            "$options":"i"
        }

    all_photos = client[DB_NAME].photo.find(criteria)
    return render_template('show_photos.template.html', all_photos=all_photos)


@app.route('/photo/create')
def create_photo():
    all_photography_types = client[DB_NAME].photography_types.find()
    return render_template('create_photo.template.html', all_photography_types=all_photography_types)


@app.route('/photo/create', methods=["POST"])
def process_create_photo():
    image_name = request.form.get('image_name')
    photographer_name = request.form.get('photographer_name')
    image_location = request.form.get('image_location')
    image_year = request.form.get('image_year')
    photography_type = request.form.get('photography_type')
    photograph_description = request.form.get('photograph_description')
    camera_make = request.form.get('camera_make')
    camera_model = request.form.get('camera_model')
    focal_length = request.form.get('focal_length')
    aperture = request.form.get('aperture')
    shutter_speed = request.form.get('shutter_speed')
    iso = request.form.get('iso')

    photography_type_object = client[DB_NAME].photography_types.find_one({
        "_id": ObjectId(photography_type)
    })

    client[DB_NAME].photo.insert_one({
        "title": image_name,
        "photographer": photographer_name,
        "location": image_location,
        "year": image_year,
        "type": {
            "_id": photography_type_object["_id"],
            "name": photography_type_object["type_name"]
        },
        "description": photograph_description,
        "cameraMake": camera_make,
        "cameraModel": camera_model,
        "focalLength": focal_length,
        "aperture": aperture,
        "shutterSpeed": shutter_speed,
        "iso": iso
    })

    return redirect(url_for('show_all_photos'))


@app.route('/photo/update/<id>')
def update_photo(id):
    photo = client[DB_NAME].photo.find_one({
        "_id": ObjectId(id)
    })

    all_photography_types = client[DB_NAME].photography_types.find()

    return render_template("update_photo_template.html", photo=photo, all_photography_types=all_photography_types)


@app.route('/photo/update/<id>', methods=["POST"])
def process_update_photo(id):
    image_name = request.form.get('image_name')
    photographer_name = request.form.get('photographer_name')
    image_location = request.form.get('image_location')
    image_year = request.form.get('image_year')
    photography_type = request.form.get('photography_type')
    photograph_description = request.form.get('photograph_description')
    camera_make = request.form.get('camera_make')
    camera_model = request.form.get('camera_model')
    focal_length = request.form.get('focal_length')
    aperture = request.form.get('aperture')
    shutter_speed = request.form.get('shutter_speed')
    iso = request.form.get('iso')

    photography_type_object = client[DB_NAME].photography_types.find_one({
        "_id": ObjectId(photography_type)
    })

    client[DB_NAME].photo.update_one({
        "_id": ObjectId(id)
    }, {
        "$set": {
            "title": image_name,
            "photographer": photographer_name,
            "location": image_location,
            "year": image_year,
            "type": {
                "_id": photography_type_object["_id"],
                "name": photography_type_object["type_name"]
            },
            "description": photograph_description,
            "cameraMake": camera_make,
            "cameraModel": camera_model,
            "focalLength": focal_length,
            "aperture": aperture,
            "shutterSpeed": shutter_speed,
            "iso": iso
        }
    })

    return redirect(url_for('show_all_photos'))


@app.route('/photo/delete/<id>')
def delete_photo(id):
    photo = client[DB_NAME].photo.find_one({
        "_id": ObjectId(id)
    })

    return render_template('confirm_delete_photo.template.html', photo=photo)


@app.route('/photo/delete/<id>', methods=["POST"])
def process_delete_photo(id):
    client[DB_NAME].photo.remove({
        "_id": ObjectId(id)
    })

    return redirect(url_for('show_all_photos'))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

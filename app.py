from flask import Flask, render_template, request, redirect, url_for
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo

load_dotenv()

app = Flask(__name__)

CLOUD_NAME = os.environ.get("CLOUD_NAME")
MONGO_URI = os.environ.get('MONGO_URI')
UPLOAD_PRESET= os.environ.get("UPLOAD_PRESET")

DB_NAME = "ardour_photography"

client = pymongo.MongoClient(MONGO_URI)

@app.route('/')
def index():
    return render_template('index.template.html')

@app.route('/photos')
def show_all_photos():
    search_terms = request.args.get('search-terms')

    criteria = {}

    if search_terms != "" and search_terms is not None:
        criteria['title'] = {
            "$regex": search_terms,
            "$options":"i"
        }

    search_type = request.args.get('type_wedding')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Wedding Photography"

    search_type = request.args.get('type_event')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Event Photography"

    search_type = request.args.get('type_portrait')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Portrait Photography"

    search_type = request.args.get('type_product')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Product Photography"

    search_type = request.args.get('type_fineart')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Fine Art Photography"

    search_type = request.args.get('type_fashion')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Fashion Photography"

    search_type = request.args.get('type_artitectural')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Artitectural Photography"

    search_type = request.args.get('type_travel')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Travel Photography"

    search_type = request.args.get('type_photojournalism')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Photojournalism"

    search_type = request.args.get('type_lifestyle')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Lifestyle Photography"
    
    search_type = request.args.get('type_pet')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Pet Photography"

    search_type = request.args.get('type_sports')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Sports Photography"

    search_type = request.args.get('type_aerial')
    if search_type is not None and search_type is not False:
        criteria['type.name'] = "Aerial Photography"

    all_photos = client[DB_NAME].photo.find(criteria)
    return render_template('show_photos.template.html', all_photos=all_photos)


@app.route('/photo/create')
def create_photo():
    all_photography_types = client[DB_NAME].photography_types.find()
    return render_template('create_photo.template.html', 
                            all_photography_types=all_photography_types, 
                            cloud_name=CLOUD_NAME, 
                            upload_preset=UPLOAD_PRESET)


@app.route('/photo/create', methods=["POST"])
def process_create_photo():
    image_name = request.form.get('image_name')
    photographer_name = request.form.get('photographer_name')
    photographer_email = request.form.get('photographer_email')
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
    uploaded_file_url = request.form.get('uploaded_file_url')

    photography_type_object = client[DB_NAME].photography_types.find_one({
        "_id": ObjectId(photography_type)
    })

    client[DB_NAME].photo.insert_one({
        "title": image_name,
        "photographer": photographer_name,
        "email": photographer_email,
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
        "iso": iso,
        "uploaded_file_url": uploaded_file_url
    })

    return redirect(url_for('show_all_photos'))


@app.route('/photo/update/<id>')
def update_photo(id):
    photo = client[DB_NAME].photo.find_one({
        "_id": ObjectId(id)
    })

    all_photography_types = client[DB_NAME].photography_types.find()

    return render_template("update_photo_template.html", photo=photo, all_photography_types=all_photography_types, cloud_name=CLOUD_NAME, upload_preset=UPLOAD_PRESET)


@app.route('/photo/update/<id>', methods=["POST"])
def process_update_photo(id):
    image_name = request.form.get('image_name')
    photographer_name = request.form.get('photographer_name')
    photographer_email = request.form.get('photographer_email')
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
    uploaded_file_url = request.form.get('uploaded_file_url')

    photography_type_object = client[DB_NAME].photography_types.find_one({
        "_id": ObjectId(photography_type)
    })

    client[DB_NAME].photo.update_one({
        "_id": ObjectId(id)
    }, {
        "$set": {
            "title": image_name,
            "photographer": photographer_name,
            "email": photographer_email,
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
            "iso": iso,
            "uploaded_file_url": uploaded_file_url
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

@app.route('/photos/genre')
def genre():
    return render_template('photos_genre.template.html')


@app.route('/photo/details/<id>')
def details_photo(id):
    photo = client[DB_NAME].photo.find_one({
        "_id": ObjectId(id)
    })

    return render_template('details_photo.template.html', photo=photo)


@app.route('/photo/details/<id>/review/')
def create_review(id):
    photo = client[DB_NAME].photo.find_one({
        "_id": ObjectId(id)
    })
    return render_template('create_review.template.html', photo=photo)

@app.route('/photo/details/<id>/review/', methods=["POST"])
def process_create_review(id):
    reviewer_name = request.form.get('reviewer_name')
    review_date = request.form.get('review_date')
    reviewer_comment = request.form.get('reviewer_comment')

    client[DB_NAME].photo.update_one({
        "_id": ObjectId(id),
    }, {
        "$push": {
            'reviews': {
                "_id": ObjectId(),
                "reviewer_name": reviewer_name,
                "review_date": review_date,
                "reviewer_comment": reviewer_comment
            }
        }
    })
    return redirect(url_for('details_photo', id=id))

@app.route('/review/<review_id>')
def update_reviews(review_id):
    photo = client[DB_NAME].photo.find_one({
        "reviews._id": ObjectId(review_id)
    })
    id = photo['_id']
    allReviews = client[DB_NAME].photo.find_one({
        'reviews._id': ObjectId(review_id)
    }, {
        'reviews': {
            '$elemMatch': {
                '_id': ObjectId(review_id)
            }
        }
    })

    reviews = allReviews['reviews'][0]

    return render_template('update_reviews.template.html',
                           reviews=reviews,
                           id=id)

@app.route('/review/<review_id>', methods=["POST"])
def process_update_reviews(review_id):
    photo = client[DB_NAME].photo.find_one({
        "reviews._id": ObjectId(review_id)
    })
    id = photo['_id']

    client[DB_NAME].photo.update_one({
        "reviews._id": ObjectId(review_id)
    }, {
        '$set': {
            'reviews.$.reviewer_name': request.form.get('reviewer_name'),
            'reviews.$.review_date': request.form.get('review_date'),
            'reviews.$.reviewer_comment': request.form.get('reviewer_comment')
        }
    })
    return redirect(url_for('details_photo', id=id))

@app.route('/review/<review_id>/delete')
def delete_review(review_id):
    photo = client[DB_NAME].photo.find_one({
        "reviews._id": ObjectId(review_id)
    })
    id = photo['_id']
    review = client[DB_NAME].photo.find_one({
        'reviews._id': ObjectId(review_id)
    }, {
        'reviews': {
            '$elemMatch': {
                '_id': ObjectId(review_id)
            }
        }
    })['reviews'][0]

    return render_template('confirm_delete_review.template.html',
                           review=review,
                           id=id)

@app.route('/review/<review_id>/delete', methods=["POST"])
def process_delete_review(review_id):
    photo = client[DB_NAME].photo.find_one({
        "reviews._id": ObjectId(review_id)
    })
    id = photo['_id']
    client[DB_NAME].photo.update_one({
        'reviews._id': ObjectId(review_id)
    }, {
        "$pull": {
            'reviews': {
                '_id': ObjectId(review_id)
            }
        }
    })
    return redirect(url_for('details_photo', id=id))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)

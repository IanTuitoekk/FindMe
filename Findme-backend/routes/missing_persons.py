# Import necessary modules from Flask and controller
from flask import Blueprint, request, jsonify
from utils.cloudinary_helper import upload_photo
from flask_jwt_extended import jwt_required
from controllers.missing_persons_controller import (
    create_missing_person,
    get_all_missing_persons,
    get_missing_person_by_id,
    update_missing_person,
    delete_missing_person,
)

# Create a Blueprint for missing persons endpoints
missing_persons_bp = Blueprint("missing_persons", __name__, url_prefix="/api/missing-persons")


# Define the POST endpoint to create a missing person report
@missing_persons_bp.route("", methods=["POST"])
def post_missing_person():
    # Accept both form-data and JSON
    if request.content_type and request.content_type.startswith("multipart/form-data"):
        data = request.form.to_dict()
        photo = request.files.get("photo")
        if photo:
            data["photo_url"] = upload_photo(photo)
    else:
        data = request.get_json()
    result = create_missing_person(data)
    return jsonify(result), result.get("status", 201)


# Define the GET endpoint to fetch all missing persons reports
@missing_persons_bp.route("", methods=["GET"])
def list_missing_persons():
    data = get_all_missing_persons()
    return jsonify(
        {
            "success": True,
            "data": data,
            "message": "Missing persons fetched",
        }
    ), 200


# Define the GET endpoint to fetch a single missing person report by ID
@missing_persons_bp.route("/<int:person_id>", methods=["GET"])
def get_missing_person_detail(person_id):
    person = get_missing_person_by_id(person_id)
    if not person:
        return jsonify(
            {
                "success": False,
                "error": "Missing person not found",
            }
        ), 404
    return jsonify(
        {
            "success": True,
            "data": person.to_dict(),
            "message": "Missing person details",
        }
    ), 200


# PUT endpoint to update a missing person report by ID
@missing_persons_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
def put_missing_person(id):
    data = request.get_json()
    result = update_missing_person(id, data)
    return jsonify(result), result.get("status", 200)


# DELETE endpoint to remove a missing person report by ID
@missing_persons_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_missing_person_report(id):
    result = delete_missing_person(id)
    return jsonify(result), result.get("status", 200)

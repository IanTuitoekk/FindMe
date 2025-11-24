#Controller for MissingPerson CRUD operations
from models.missing_person import MissingPerson
from app import db
from sqlalchemy.exc import IntegrityError
from schemas.missing_person_schema import MissingPersonSchema


def create_missing_person(data):
    """
    Create a new missing person report.
    Args:
        data (dict): Incoming JSON data from the request
    Returns:
        dict: Response object with success, data/error, message, and status code
    """
    # Validate incoming data using Marshmallow schema
    # This will check required fields, types, and custom validation
    schema = MissingPersonSchema()
    errors = schema.validate(data)
    if errors:
        # Return validation errors to the client
        return {
            "success": False,
            "error": errors,
            "status": 400
        }
    try:
        # Create a new MissingPerson instance using the provided data
        person = MissingPerson(**data)
        # Add the new person to the database session
        db.session.add(person)
        # Commit the session to save changes to the database
        db.session.commit()
        # Return a success response with the new person's data
        return {
            "success": True,
            "data": person.to_dict(),  # Assumes MissingPerson has a to_dict() method
            "message": "Missing person report created",
            "status": 201
        }
    except IntegrityError as e:
        # Rollback the session if there's a database error (e.g., duplicate case_number)
        db.session.rollback()
        return {
            "success": False,
            "error": "Case number must be unique",
            "status": 409
        }
    except Exception as e:
        # Rollback for any other errors and return a generic error message
        db.session.rollback()
        return {
            "success": False,
            "error": str(e),
            "status": 500
        }


def get_all_missing_persons():
    #Retrieve all missing person reports.
    #list of dictionaries, each representing a missing person report
    persons = MissingPerson.query.all()
    return [person.to_dict() for person in persons]

#function to fetch a missing person by ID
def get_missing_person_by_id(person_id):
    person = MissingPerson.query.get(person_id)
    return person

#function to update missing person
def update_missing_person(id, data):
    person = MissingPerson.query.get(id)
    if not person:
        return {"success": False, "error": "Not found", "status": 404}
    # Validate incoming data for updates; partial=True allows updating only some fields
    schema = MissingPersonSchema(partial=True)
    errors = schema.validate(data)
    if errors:
        # Return validation errors to the client
        return {
            "success": False,
            "error": errors,
            "status": 400
        }
    # Only allow certain fields to be updated
    allowed_fields = ["status", "full_name", "age", "gender", "last_seen_date", "last_seen_location", "contact_name", "contact_phone", "contact_email", "additional_info"]
    for field in data:
        if field in allowed_fields:
            setattr(person, field, data[field])
    db.session.commit()
    return {"success": True, "data": person.to_dict(), "message": "Updated successfully"}

#delete person function
def delete_missing_person(id):
    person = MissingPerson.query.get(id)
    if not person:
        return {"success": False, "error": "Missing person not found", "status": 404}
    try:
        db.session.delete(person)
        db.session.commit()
        return {"success": True, "message": "Missing person deleted", "status": 200}
    except Exception as e:
        db.session.rollback()
        return {"success": False, "error": str(e), "status": 500}

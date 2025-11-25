# routes/missing_persons.py

from flask import Blueprint, request, jsonify
import jwt  # ✅ Use PyJWT to match auth.py
from models.missing_person import MissingPerson
from models.db import db

missing_persons_bp = Blueprint("missing_persons", __name__, url_prefix="/api/missing-persons")
SECRET_KEY = "findme-secret-key-2024"  # ✅ Same secret key as auth.py

def get_user_id_from_token():
    """Extract user_id from JWT token (matches auth.py implementation)"""
    token = request.headers.get('Authorization')
    
    if not token:
        return None
    
    try:
        if token.startswith('Bearer '):
            token = token[7:]
            
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
        
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception:
        return None

# ----------------------------------------
# CREATE REPORT (AUTHENTICATION REQUIRED)
# ----------------------------------------
@missing_persons_bp.route("", methods=["POST"])
def create_missing_person_route():
    try:
        user_id = get_user_id_from_token()
        if not user_id:
            return jsonify({"success": False, "error": "Authentication required"}), 401
            
        data = request.get_json()

        # Required fields validation
        required_fields = ['full_name', 'age', 'gender', 'last_seen_location', 'contact_name', 'contact_phone']
        for field in required_fields:
            if not data.get(field):
                return jsonify({"success": False, "error": f"Missing required field: {field}"}), 400

        data["user_id"] = user_id
        
        person = MissingPerson(**data)
        db.session.add(person)
        db.session.commit()

        return jsonify({
            "success": True,
            "message": "Missing person report created successfully",
            "data": person.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500


# ----------------------------------------
# GET ALL REPORTS
# ----------------------------------------
@missing_persons_bp.route("", methods=["GET"])
def list_all_reports():
    try:
        persons = MissingPerson.query.all()
        return jsonify({
            "success": True,
            "data": [p.to_dict() for p in persons]
        }), 200
    except Exception as e:
        return jsonify({
            "success": True,
            "data": []
        }), 200


# ----------------------------------------
# GET SINGLE REPORT
# ----------------------------------------
@missing_persons_bp.route("/<int:person_id>", methods=["GET"])
def get_single_report(person_id):
    try:
        person = MissingPerson.query.get(person_id)
        if not person:
            return jsonify({"success": False, "error": "Report not found"}), 404

        return jsonify({
            "success": True,
            "data": person.to_dict()
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# ----------------------------------------
# GET MY REPORTS (AUTH REQUIRED)
# ----------------------------------------
@missing_persons_bp.route("/mine", methods=["GET"])
def get_my_reports():
    try:
        user_id = get_user_id_from_token()
        if not user_id:
            return jsonify({"success": False, "error": "Authentication required"}), 401
            
        reports = MissingPerson.query.filter_by(user_id=user_id).all()

        return jsonify({
            "success": True,
            "data": [p.to_dict() for p in reports]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# ----------------------------------------
# UPDATE REPORT (AUTH REQUIRED)
# ----------------------------------------
@missing_persons_bp.route("/<int:person_id>", methods=["PUT"])
def update_report(person_id):
    try:
        user_id = get_user_id_from_token()
        if not user_id:
            return jsonify({"success": False, "error": "Authentication required"}), 401
            
        person = MissingPerson.query.get(person_id)
        
        if not person:
            return jsonify({"success": False, "error": "Report not found"}), 404
            
        # Check if user owns the report
        if person.user_id != user_id:
            return jsonify({"success": False, "error": "Not authorized to update this report"}), 403
        
        data = request.get_json()
        
        # Update allowed fields (prevent changing sensitive fields)
        allowed_fields = [
            'status', 'contact_phone', 'contact_email', 'additional_info',
            'last_seen_location', 'last_seen_wearing', 'distinguishing_features'
        ]
        
        updates_made = False
        for field in allowed_fields:
            if field in data:
                setattr(person, field, data[field])
                updates_made = True
        
        if not updates_made:
            return jsonify({"success": False, "error": "No valid fields to update"}), 400
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Report updated successfully",
            "data": person.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500


# ----------------------------------------
# DELETE REPORT (AUTH REQUIRED)
# ----------------------------------------
@missing_persons_bp.route("/<int:person_id>", methods=["DELETE"])
def delete_report(person_id):
    try:
        user_id = get_user_id_from_token()
        if not user_id:
            return jsonify({"success": False, "error": "Authentication required"}), 401
            
        person = MissingPerson.query.get(person_id)
        
        if not person:
            return jsonify({"success": False, "error": "Report not found"}), 404
            
        # Check if user owns the report
        if person.user_id != user_id:
            return jsonify({"success": False, "error": "Not authorized to delete this report"}), 403
        
        db.session.delete(person)
        db.session.commit()
        
        return jsonify({
            "success": True,
            "message": "Report deleted successfully"
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "error": str(e)}), 500


# ----------------------------------------
# FILTER BY LOCATION
# ----------------------------------------
@missing_persons_bp.route("/location/<string:city>", methods=["GET"])
def filter_by_location(city):
    try:
        persons = MissingPerson.query.filter(
            MissingPerson.last_seen_location.ilike(f'%{city}%')
        ).all()
        
        return jsonify({
            "success": True,
            "data": [p.to_dict() for p in persons],
            "filters": {"location": city}
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# ----------------------------------------
# GET RECENT REPORTS
# ----------------------------------------
@missing_persons_bp.route("/recent", methods=["GET"])
def get_recent_reports():
    try:
        # Get 10 most recent reports
        persons = MissingPerson.query.order_by(MissingPerson.created_at.desc()).limit(10).all()
        
        return jsonify({
            "success": True,
            "data": [p.to_dict() for p in persons]
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# ----------------------------------------
# GET STATISTICS
# ----------------------------------------
@missing_persons_bp.route("/stats", methods=["GET"])
def get_statistics():
    try:
        total_reports = MissingPerson.query.count()
        found_count = MissingPerson.query.filter_by(status='found').count()
        missing_count = MissingPerson.query.filter_by(status='missing').count()
        
        return jsonify({
            "success": True,
            "data": {
                "total_reports": total_reports,
                "found": found_count,
                "missing": missing_count,
                "resolved_rate": round((found_count / total_reports * 100), 2) if total_reports > 0 else 0
            }
        }), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
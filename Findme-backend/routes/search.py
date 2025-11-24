# routes/search.py

from flask import Blueprint, request, jsonify
from models.missing_person import MissingPerson
from models.db import db

search_bp = Blueprint("search", __name__, url_prefix="/api")

# ----------------------------------------
# ADVANCED SEARCH
# ----------------------------------------
@search_bp.route("/search", methods=["GET"])
def advanced_search():
    try:
        # Get query parameters
        name = request.args.get('name', '').strip()
        location = request.args.get('location', '').strip()
        age_min = request.args.get('age_min', type=int)
        age_max = request.args.get('age_max', type=int)
        gender = request.args.get('gender', '').strip()
        status = request.args.get('status', '').strip()
        
        # Start with base query
        query = MissingPerson.query
        
        # Apply filters
        if name:
            query = query.filter(MissingPerson.full_name.ilike(f'%{name}%'))
        
        if location:
            query = query.filter(MissingPerson.last_seen_location.ilike(f'%{location}%'))
        
        if age_min is not None:
            query = query.filter(MissingPerson.age >= age_min)
        
        if age_max is not None:
            query = query.filter(MissingPerson.age <= age_max)
        
        if gender:
            query = query.filter(MissingPerson.gender.ilike(f'%{gender}%'))
        
        if status:
            query = query.filter(MissingPerson.status == status)
        
        # Execute query
        results = query.all()
        
        return jsonify({
            "success": True,
            "data": [person.to_dict() for person in results],
            "filters_applied": {
                "name": name,
                "location": location,
                "age_min": age_min,
                "age_max": age_max,
                "gender": gender,
                "status": status
            },
            "results_count": len(results)
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# ----------------------------------------
# QUICK SEARCH (Search across multiple fields)
# ----------------------------------------
@search_bp.route("/search/quick", methods=["GET"])
def quick_search():
    try:
        search_term = request.args.get('q', '').strip()
        
        if not search_term:
            return jsonify({
                "success": True,
                "data": [],
                "message": "Please provide a search term"
            }), 200
        
        # Search across multiple fields
        results = MissingPerson.query.filter(
            db.or_(
                MissingPerson.full_name.ilike(f'%{search_term}%'),
                MissingPerson.last_seen_location.ilike(f'%{search_term}%'),
                MissingPerson.contact_name.ilike(f'%{search_term}%'),
                MissingPerson.distinguishing_features.ilike(f'%{search_term}%')
            )
        ).all()
        
        return jsonify({
            "success": True,
            "data": [person.to_dict() for person in results],
            "search_term": search_term,
            "results_count": len(results)
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
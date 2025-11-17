from flask import Blueprint, request, jsonify
from controllers.search_controller import SearchController

search_bp = Blueprint('search', __name__, url_prefix='/api')

@search_bp.route('/search', methods=['GET'])
def search_missing_persons():
    """Search missing persons with filters"""
    try:
        results = SearchController.search_missing_persons(request.args.to_dict())
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@search_bp.route('/missing-persons/location/<city>', methods=['GET'])  # Changed county to city
def filter_by_location(county):  
    """Filter by location"""
    try:
        results = SearchController.filter_by_location(county)
        return jsonify({'location': county, 'count': len(results), 'results': results}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@search_bp.route('/missing-persons/recent', methods=['GET'])
def get_recent_reports():
    """Get recent reports (last 7 days)"""
    try:
        days = request.args.get('days', 7, type=int)
        results = SearchController.get_recent_reports(days)
        return jsonify({'days': days, 'count': len(results), 'results': results}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@search_bp.route('/missing-persons/stats', methods=['GET'])
def get_statistics():
    """Get platform statistics"""
    try:
        stats = SearchController.get_statistics()
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
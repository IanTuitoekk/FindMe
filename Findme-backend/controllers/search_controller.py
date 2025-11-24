from models.missing_person import MissingPerson
from datetime import datetime, timedelta

class SearchController:
    @staticmethod
    def search_missing_persons(params):
        """Search and filter missing persons"""
        query = MissingPerson.query
        
        # Apply filters
        if params.get('name'):
            query = query.filter(MissingPerson.full_name.ilike(f"%{params['name']}%"))
        
        if params.get('location'):
            query = query.filter(MissingPerson.last_seen_location.ilike(f"%{params['location']}%"))
        
        if params.get('age_min'):
            query = query.filter(MissingPerson.age >= int(params['age_min']))
        
        if params.get('age_max'):
            query = query.filter(MissingPerson.age <= int(params['age_max']))
        
        if params.get('gender'):
            query = query.filter(MissingPerson.gender.ilike(params['gender']))
        
        if params.get('status'):
            query = query.filter(MissingPerson.status == params['status'])
        
        if params.get('date_from'):
            query = query.filter(MissingPerson.last_seen_date >= datetime.fromisoformat(params['date_from']))
        
        if params.get('date_to'):
            query = query.filter(MissingPerson.last_seen_date <= datetime.fromisoformat(params['date_to']))
        
        # Pagination
        page = int(params.get('page', 1))
        per_page = int(params.get('per_page', 20))
        
        paginated = query.order_by(MissingPerson.last_seen_date.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return {
            'results': [p.to_dict() for p in paginated.items],
            'total': paginated.total,
            'page': page,
            'per_page': per_page,
            'total_pages': paginated.pages
        }
    
    @staticmethod
    def filter_by_location(county):
        """Filter by specific location"""
        results = MissingPerson.query.filter(
            MissingPerson.last_seen_location.ilike(f"%{county}%")
        ).all()
        return [p.to_dict() for p in results]
    
    @staticmethod
    def get_recent_reports(days=7):
        """Get recent reports"""
        cutoff = datetime.utcnow() - timedelta(days=days)
        results = MissingPerson.query.filter(
            MissingPerson.created_at >= cutoff
        ).order_by(MissingPerson.created_at.desc()).all()
        return [p.to_dict() for p in results]
    
    @staticmethod
    def get_statistics():
        """Get platform statistics"""
        return {
            'total_cases': MissingPerson.query.count(),
            'missing': MissingPerson.query.filter_by(status='missing').count(),
            'found': MissingPerson.query.filter_by(status='found').count(),
        }
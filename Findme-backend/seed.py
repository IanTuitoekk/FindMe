from app import create_app, db
from models.missing_person import MissingPerson
from datetime import datetime, timedelta
import random

app = create_app('development')

def seed_database():
    with app.app_context():
        # Clear existing data
        print("🗑️  Clearing existing data...")
        MissingPerson.query.delete()
        db.session.commit()
        
        # Sample data
        first_names = ["John", "Mary", "David", "Alice", "Peter", "Grace", "James", "Sarah", "Michael", "Jane"]
        last_names = ["Doe", "Smith", "Johnson", "Brown", "Kamau", "Wanjiru", "Omondi", "Njeri", "Mwangi", "Otieno"]
        locations = [
            "Nairobi CBD, Kenya",
            "Westlands, Nairobi",
            "Mombasa, Kenya",
            "Kisumu, Kenya",
            "Nakuru, Kenya",
            "Eldoret, Kenya",
            "Thika, Kenya",
            "Ruiru, Kenya",
            "Karen, Nairobi",
            "Kiambu, Kenya"
        ]
        genders = ["Male", "Female"]
        statuses = ["missing", "missing", "missing", "found"]  # More missing than found
        
        test_people = []
        
        # Generate 15 test records
        for i in range(15):
            full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
            age = random.randint(18, 70)
            gender = random.choice(genders)
            status = random.choice(statuses)
            days_ago = random.randint(1, 30)
            
            person = MissingPerson(
                full_name=full_name,
                age=age,
                gender=gender,
                height=f"{random.randint(150, 190)}cm",
                weight=f"{random.randint(50, 90)}kg",
                hair_color=random.choice(["Black", "Brown", "Blonde", "Gray"]),
                eye_color=random.choice(["Brown", "Black", "Blue", "Green"]),
                last_seen_date=datetime.utcnow() - timedelta(days=days_ago),
                last_seen_location=random.choice(locations),
                last_seen_wearing=random.choice([
                    "Blue jeans and white t-shirt",
                    "Red dress",
                    "Black jacket and blue pants",
                    "School uniform",
                    "Green hoodie"
                ]),
                contact_name=f"{random.choice(first_names)} {random.choice(last_names)}",
                contact_phone=f"+2547{random.randint(10000000, 99999999)}",
                contact_email=f"contact{i+1}@example.com",
                status=status,
                case_number=f"MP{str(i+1).zfill(4)}",
                additional_info=f"Last seen {days_ago} days ago. Please contact if you have any information.",
                distinguishing_features=random.choice([
                    "Scar on left cheek",
                    "Tattoo on right arm",
                    "Wears glasses",
                    "Has a birthmark on forehead",
                    "Missing front tooth"
                ])
            )
            test_people.append(person)
        
        # Add all records
        db.session.add_all(test_people)
        db.session.commit()
        
        print(f"✅ Successfully seeded {len(test_people)} records!")
        print("\n📊 Summary:")
        print(f"   Total cases: {len(test_people)}")
        print(f"   Missing: {sum(1 for p in test_people if p.status == 'missing')}")
        print(f"   Found: {sum(1 for p in test_people if p.status == 'found')}")
        
        print("\n📝 Sample records:")
        for person in test_people[:5]:
            print(f"   • {person.full_name} ({person.age}yo {person.gender}) - {person.status} - {person.last_seen_location}")

if __name__ == '__main__':
    seed_database()
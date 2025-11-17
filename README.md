# FindMe - Missing Persons Platform

> Community-driven platform for reporting and tracking missing persons

## 🎯 Project Overview

FindMe is a full-stack web application that enables community members to report and search for missing persons. The platform combines secure authentication, detailed reporting, and advanced search capabilities.

**Tech Stack:**
- **Backend:** Flask (Python), PostgreSQL, JWT Authentication
- **Frontend:** React, TailwindCSS
- **Media Storage:** Cloudinary
- **Database:** PostgreSQL (development & production)

---

## 📋 Table of Contents
1. [Team Roles & Responsibilities](#team-roles--responsibilities)
2. [Database Schema](#database-schema)
3. [API Endpoints](#api-endpoints)
4. [Development Setup](#development-setup)
5. [Git Workflow](#git-workflow)
6. [Testing Guidelines](#testing-guidelines)

---

## 👥 Team Roles & Responsibilities

### 👤 Person 1: Demestrine - Backend Lead & Authentication
**Branch:** `demestrine-dev` → `dev` → `main`

**Responsibilities:**
1. Flask server and project structure setup
2. User authentication system (register/login/logout)
3. JWT token management
4. Password hashing and security (bcrypt)
5. User model and database schema

**Endpoints to Build:**
```
POST   /api/auth/register     - User registration
POST   /api/auth/login        - User login  
GET    /api/auth/me           - Get current user
POST   /api/auth/logout       - User logout
```

**Files You Own:**
```
Findme-backend/
  ├── models/user.py              ✏️ CREATE - User model
  ├── routes/auth.py              ✏️ CREATE - Auth endpoints
  ├── controllers/auth_controller.py  ✏️ CREATE - Auth logic
  └── tests/test_auth.py          ✏️ CREATE - Auth tests
```

**Dependencies to Add:**
```
flask-bcrypt==1.0.1
```

**Setup Instructions:**
```bash
# Create your branch
git checkout dev
git pull origin dev
git checkout -b demestrine-dev

# Create your files
mkdir -p Findme-backend/controllers
touch Findme-backend/models/user.py
touch Findme-backend/routes/auth.py
touch Findme-backend/controllers/auth_controller.py
touch Findme-backend/tests/test_auth.py

# Install your dependencies
pip install flask-bcrypt==1.0.1
pip freeze > requirements.txt
```

---


### 👤 Person 2: Elijah Kamanga - Missing Persons CRUD
**Branch:** `elijah-dev` → `dev` → `main`

**Responsibilities & Achievements:**
- Designed and implemented the `MissingPerson` model with all required fields and relationships.
- Built and tested all CRUD endpoints:
  - `POST /api/missing-persons` (Create report)
  - `GET /api/missing-persons` (List all reports)
  - `GET /api/missing-persons/:id` (Get report by ID)
  - `PUT /api/missing-persons/:id` (Update report/status)
  - `DELETE /api/missing-persons/:id` (Remove report, admin only)
- Integrated JWT authentication for protected routes (create, update, delete).
- Implemented Marshmallow schema for robust data validation (all model fields, custom rules).
- Removed manual required field checks for cleaner validation.
- Integrated Cloudinary for secure photo uploads in missing person reports:
  - Accepts image files via API, uploads to Cloudinary, stores URL in database.
  - API responses now include `photo_url` for each report.
- Automated tests for all endpoints using `pytest` and Qodo:
  - Covers success, validation errors, not found, and auth requirements.
  - Uses in-memory SQLite for test isolation.
- All endpoints tested in Postman and confirmed working.
- Database schema and migrations updated to support new fields (including `photo_url`).

**Files Owned & Updated:**
```
Findme-backend/
  ├── models/missing_person.py        ✅ DONE - Model & serialization
  ├── routes/missing_persons.py       ✅ DONE - CRUD endpoints
  ├── controllers/missing_persons_controller.py  ✅ DONE - Business logic
  ├── schemas/missing_person_schema.py ✅ DONE - Validation
  ├── utils/cloudinary_helper.py      ✅ DONE - Cloudinary integration
  └── tests/test_api.py               ✅ DONE - Automated tests
```

**Key Features Delivered:**
- Full CRUD for missing persons
- JWT-protected endpoints
- Cloudinary photo upload & storage
- Marshmallow validation for all fields
- Automated test suite (pytest/Qodo)
- API response includes image URL
- Database migrations for new fields

**How to Test:**
- Use Postman or frontend to create, update, and fetch reports (with images)
- Run `pytest -q` in `Findme-backend` to verify all tests pass

**Next Steps:**
- Expand tests for edge cases
- Finalize API documentation in README


---

### 👤 Person 3: Ian - Search & Filter System
**Branch:** `ian-dev` → `dev` → `main`

**Responsibilities:**
1. Advanced search functionality
2. Location-based filtering
3. Real-time search results
4. API documentation in README

**Endpoints to Build:**
```
GET    /api/search?name=...&location=...             - Search missing persons
GET    /api/missing-persons/location/:city           - Filter by location
GET    /api/missing-persons/recent                   - Get recent reports (7 days)
GET    /api/missing-persons/stats                    - Platform statistics
```

**Files You Own:**
```
Findme-backend/
  ├── routes/search.py                ✏️ CREATE - Search endpoints
  ├── controllers/search_controller.py ✏️ CREATE - Search logic
  └── tests/test_search.py            ✏️ CREATE - Search tests
```

**Query Parameters to Support:**
- `name` - Name search (partial match, case-insensitive)
- `location` - City/area filter
- `age_min`, `age_max` - Age range
- `gender` - Gender filter
- `status` - Case status (missing/found/closed)
- `page`, `per_page` - Pagination (default: 20 per page)
- `date_from`, `date_to` - Date range

**Dependencies to Add:**
```
# No additional dependencies needed
# Uses existing SQLAlchemy queries
```

**Setup Instructions:**
```bash
# Create your branch
git checkout dev
git pull origin dev
git checkout -b ian-dev

# Create your files
touch Findme-backend/routes/search.py
touch Findme-backend/controllers/search_controller.py
touch Findme-backend/tests/test_search.py

# You'll work with Elijah's MissingPerson model
# Make sure to pull latest dev before starting
```

---

### 👤 Person 4: James - Frontend Lead & Core Pages
**Branch:** `james-dev` → `dev` → `main`

**Responsibilities:**
1. React app setup and routing
2. Homepage and main layout
3. Navigation component
4. Report missing person form
5. Integration with backend APIs

**Pages to Build:**
```
/                - Homepage with search and featured cases
/report          - Report missing person form
/about           - About page
```

**Files You Own:**
```
findme-client/
  ├── src/
  │   ├── pages/
  │   │   ├── Home.jsx              ✏️ CREATE - Homepage
  │   │   ├── ReportForm.jsx        ✏️ CREATE - Report form
  │   │   └── About.jsx             ✏️ CREATE - About page
  │   ├── components/
  │   │   ├── Navbar.jsx            ✏️ CREATE - Navigation with auth
  │   │   ├── Footer.jsx            ✏️ CREATE - Footer
  │   │   ├── SearchBar.jsx         ✏️ CREATE - Search component
  │   │   └── Layout.jsx            ✏️ CREATE - Main layout
  │   ├── services/
  │   │   └── api.js                ✅ EXISTS - Update as needed
  │   └── App.jsx                   ✏️ UPDATE - Add routing
```

**Dependencies to Add:**
```
react-router-dom
axios (already exists)
```

**Setup Instructions:**
```bash
# Create your branch
git checkout dev
git pull origin dev
git checkout -b james-dev

# Navigate to frontend
cd findme-client

# Install dependencies
npm install react-router-dom

# Create folder structure
mkdir -p src/pages src/components src/services

# Create your files
touch src/pages/Home.jsx
touch src/pages/ReportForm.jsx
touch src/pages/About.jsx
touch src/components/Navbar.jsx
touch src/components/Footer.jsx
touch src/components/SearchBar.jsx
touch src/components/Layout.jsx
```

---

### 👤 Person 5: Eva - Frontend Features & UI
**Branch:** `eva-dev` → `dev` → `main`

**Responsibilities:**
1. Search results page
2. Missing person details page
3. Community updates display
4. Responsive design with TailwindCSS

**Pages to Build:**
```
/search          - Search results page
/person/:id      - Individual missing person profile
/updates         - Community updates feed
```

**Files You Own:**
```
findme-client/
  ├── src/
  │   ├── pages/
  │   │   ├── SearchResults.jsx     ✏️ CREATE - Search page
  │   │   ├── PersonDetail.jsx      ✏️ CREATE - Detail page
  │   │   └── Updates.jsx           ✏️ CREATE - Updates feed
  │   ├── components/
  │   │   ├── PersonCard.jsx        ✏️ CREATE - Card for listings
  │   │   ├── SearchFilters.jsx     ✏️ CREATE - Filter sidebar
  │   │   └── UpdateCard.jsx        ✏️ CREATE - Update item
  │   └── index.css                 ✏️ UPDATE - TailwindCSS styles
```

**Dependencies to Add:**
```
# TailwindCSS already configured in vite.config.js
# No additional dependencies needed
```

**Setup Instructions:**
```bash
# Create your branch
git checkout dev
git pull origin dev
git checkout -b eva-dev

# Navigate to frontend
cd findme-client

# Create your files
mkdir -p src/pages src/components
touch src/pages/SearchResults.jsx
touch src/pages/PersonDetail.jsx
touch src/pages/Updates.jsx
touch src/components/PersonCard.jsx
touch src/components/SearchFilters.jsx
touch src/components/UpdateCard.jsx

# Work with James' components (Navbar, Layout)
# Make sure to pull latest dev before starting
```

---

## 🗄️ Database Schema

### **PostgreSQL Configuration**
**Database:** `findme_db`  
**User:** `findme_user`  
**Password:** `grouptwo`  
**Host:** `localhost:5432`

⚠️ **IMPORTANT:** Everyone must use PostgreSQL (no SQLite). Install:
```bash
# Ubuntu/Debian
sudo apt-get install postgresql libpq-dev

# Mac
brew install postgresql
```

### **Tables**

#### `missing_persons` (Person 2)
```sql
id                      SERIAL PRIMARY KEY
full_name               VARCHAR(100) NOT NULL
age                     INTEGER NOT NULL
gender                  VARCHAR(20) NOT NULL
height                  VARCHAR(20)
weight                  VARCHAR(20)
hair_color              VARCHAR(50)
eye_color               VARCHAR(50)
distinguishing_features TEXT
last_seen_date          TIMESTAMP NOT NULL
last_seen_location      VARCHAR(200) NOT NULL
last_seen_wearing       TEXT
contact_name            VARCHAR(100) NOT NULL
contact_phone           VARCHAR(20) NOT NULL
contact_email           VARCHAR(100)
status                  VARCHAR(20) DEFAULT 'missing'
case_number             VARCHAR(50) UNIQUE
additional_info         TEXT
photo_url               VARCHAR(300)
created_at              TIMESTAMP DEFAULT NOW()
updated_at              TIMESTAMP DEFAULT NOW()
```

#### `users` (Person 1)
```sql
id                      SERIAL PRIMARY KEY
username                VARCHAR(80) UNIQUE NOT NULL
email                   VARCHAR(120) UNIQUE NOT NULL
password_hash           VARCHAR(255) NOT NULL
is_admin                BOOLEAN DEFAULT FALSE
created_at              TIMESTAMP DEFAULT NOW()
```

---

## 🔌 API Endpoints Reference

### Base URL
```
Development: http://localhost:5000/api
Production: TBD
```

### Response Format
All responses follow this structure:
```json
{
  "success": true/false,
  "data": { ... },
  "message": "Optional message",
  "error": "Error details (if failed)"
}
```

### Authentication
Protected endpoints require JWT token:
```
Authorization: Bearer <token>
```

### Endpoints Summary

| Method | Endpoint | Auth Required | Owner |
|--------|----------|---------------|-------|
| POST | `/auth/register` | No | Person 1 |
| POST | `/auth/login` | No | Person 1 |
| GET | `/auth/me` | Yes | Person 1 |
| POST | `/missing-persons` | Yes | Person 2 |
| GET | `/missing-persons` | No | Person 2 |
| GET | `/missing-persons/:id` | No | Person 2 |
| PUT | `/missing-persons/:id` | Yes | Person 2 |
| DELETE | `/missing-persons/:id` | Yes (Admin) | Person 2 |
| GET | `/search` | No | Person 3 |
| GET | `/missing-persons/location/:city` | No | Person 3 |
| GET | `/missing-persons/recent` | No | Person 3 |

---

## 🚀 Development Setup

### Backend Setup (All Team Members)

1. **Clone and navigate:**
```bash
git clone https://github.com/muhorocode/FindMe.git
cd FindMe/Findme-backend
```

2. **Create virtual environment:**
```bash
python3 -m venv env
source env/bin/activate  # Mac/Linux
# env\Scripts\activate   # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Setup PostgreSQL database:**
```bash
# Login to PostgreSQL
sudo -u postgres psql

# Create database and user
CREATE DATABASE findme_db;
CREATE USER findme_user WITH PASSWORD 'grouptwo';
GRANT ALL PRIVILEGES ON DATABASE findme_db TO findme_user;
\q
```

5. **Run migrations:**
```bash
flask db upgrade
```

6. **Start server:**
```bash
python app.py
# Server runs on http://localhost:5000
```

7. **Test health endpoint:**
```bash
curl http://localhost:5000/api/health
```

### Frontend Setup (Person 4 & 5)

1. **Navigate to frontend:**
```bash
cd findme-client
```

2. **Install dependencies:**
```bash
npm install
```

3. **Start dev server:**
```bash
npm run dev
# Runs on http://localhost:5173
```

---

## 🌿 Git Workflow

### Branch Structure
```
main (protected - requires 2 approvals)
  ↑
dev (protected - requires 1 approval)
  ↑
feature branches (elijah-dev, person1-dev, etc.)
```

### Workflow Steps

1. **Create feature branch:**
```bash
git checkout dev
git pull origin dev
git checkout -b your-name-dev
```

2. **Make changes and commit:**
```bash
git add .
git commit -m "feat(module): description"
```

3. **Push to your branch:**
```bash
git push origin your-name-dev
```

4. **Create Pull Request:**
- Base: `dev` ← Compare: `your-name-dev`
- Request review from 1 teammate
- Wait for approval before merging

5. **After merge, update your branch:**
```bash
git checkout dev
git pull origin dev
git checkout your-name-dev
git merge dev
```

### Commit Message Format
```
feat(module): add new feature
fix(module): fix bug description
chore(module): update dependencies
docs: update README
test(module): add tests
```

---

## ⚠️ Important Guidelines

### Database
- **ALWAYS use PostgreSQL** - no SQLite in any branch
- **Run migrations** before pushing model changes
- **Never commit** migrations without testing

### Model Changes
- Person 2 owns `MissingPerson` model
- Person 1 owns `User` model
- Coordinate before changing shared fields

### API Contracts
- Document all endpoint changes in this README
- Use consistent response format
- Version breaking changes (e.g., `/api/v2/...`)

### Dependencies
- Add new packages to `requirements.txt` or `package.json`
- Document why dependency is needed
- Check for conflicts before adding

### Before Pushing
```bash
# Backend checklist
python app.py  # Verify server starts
flask db upgrade  # Test migrations
pytest  # Run tests

# Frontend checklist
npm run build  # Verify build works
npm run lint  # Check code style
```

---

## 🧪 Testing Guidelines

### Backend Tests (pytest)
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_missing_persons.py

# Run with coverage
pytest --cov=.
```

### Test Structure
```
tests/
  test_auth.py          - Person 1
  test_missing_persons.py - Person 2
  test_search.py        - Person 3
```

---

## 📞 Communication

### Daily Standups (Async)
Post in team chat:
- What I completed yesterday
- What I'm working on today
- Any blockers

### Conflict Resolution
If you encounter merge conflicts:
1. Don't panic
2. Check this README for "source of truth"
3. Communicate with affected team member
4. Resolve locally, test, then push

### Questions
- Check README first
- Ask in team chat
- Tag relevant person (@person2 for model questions)

---

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [JWT Introduction](https://jwt.io/introduction)

---

## 🚫 Conflict Prevention Guide

### File Ownership Matrix

| File/Folder | Owner | Others Can |
|-------------|-------|-----------|
| `models/user.py` | Demestrine | ❌ Don't touch |
| `models/missing_person.py` | Elijah | ✅ Read only |
| `routes/auth.py` | Demestrine | ❌ Don't touch |
| `routes/missing_persons.py` | Elijah | ❌ Don't touch |
| `routes/search.py` | Ian | ❌ Don't touch |
| `controllers/*_controller.py` | File creator | ❌ Don't touch |
| `app.py` | Shared | ⚠️ Coordinate changes |
| `config.py` | Elijah (done) | ✅ Read only |
| `requirements.txt` | Everyone | ⚠️ Add your deps, don't delete others |
| Frontend `pages/` | James/Eva | ❌ Only owner edits |
| Frontend `components/` | James/Eva | ⚠️ Can reuse, don't modify |

### Communication Rules

**Before Starting Work:**
1. Pull latest `dev` branch
2. Check if your assigned files exist
3. If someone created your file, ping them in chat

**Before Pushing:**
1. Test your code works
2. Check you only modified YOUR files
3. Update this README if you added endpoints/pages

**If You Need to Modify Someone Else's File:**
1. Ask in team chat first
2. Create a separate PR with clear description
3. Tag the file owner as reviewer

### Daily Workflow

**Morning (Before Coding):**
```bash
git checkout dev
git pull origin dev
git checkout your-name-dev
git merge dev  # Get latest changes
```

**Evening (After Coding):**
```bash
# Test your changes
python app.py  # Backend
npm run dev    # Frontend

# Commit and push
git add .
git commit -m "feat(your-module): description"
git push origin your-name-dev

# Create PR: your-name-dev → dev
```

### Emergency: "I Have Conflicts!"

**Don't Panic. Follow these steps:**

1. **Check what's conflicted:**
```bash
git status
```

2. **If it's YOUR file → Keep your version:**
```bash
git checkout --ours path/to/your/file.py
git add path/to/your/file.py
```

3. **If it's a SHARED file (app.py, config.py):**
- Stop and ask in team chat
- Tag the other person who modified it
- Resolve together

4. **If it's SOMEONE ELSE'S file:**
```bash
git checkout --theirs path/to/their/file.py
git add path/to/their/file.py
```

5. **After resolving all conflicts:**
```bash
git commit -m "chore: resolve merge conflicts"
git push origin your-name-dev
```

---

## 📊 Project Timeline

### Week 1 (Nov 14-20)
- ✅ **Elijah**: PostgreSQL setup, MissingPerson model
- 🔄 **Demestrine**: User model, auth endpoints
- 🔄 **James**: React setup, homepage, navbar

### Week 2 (Nov 21-27)
- **Elijah**: CRUD endpoints, Cloudinary integration
- **Ian**: Search and filter endpoints
- **Eva**: Search results page, person detail page

### Week 3 (Nov 28-Dec 4)
- **All**: Testing and bug fixes
- **All**: Integration testing
- **James/Eva**: Final UI polish

---

## 🔄 Changelog

| Date | Author | Change |
|------|--------|--------|
| 2025-11-14 | Elijah | Initial setup: PostgreSQL, MissingPerson model, migrations |
| 2025-11-14 | Elijah | Comprehensive team guide with conflict prevention |
| 2025-11-14 | Demestrine | Auth system placeholder added |

---

## 👥 Team Contact

| Name | Role | GitHub | Slack/Email |
|------|------|--------|-------------|
| Demestrine Awuor | Person 1 (Auth) | @demestrine | TBD |
| Elijah Kamanga | Person 2 (CRUD) | @muhorocode | elijah.kamanga@... |
| Ian Tuitoek | Person 3 (Search) | @ian | TBD |
| James Wachira | Person 4 (Frontend Lead) | @james | TBD |
| Eva Chemngorem | Person 5 (Frontend UI) | @eva | TBD |

---

**Last Updated:** November 14, 2025  
**Maintained by:** All team members (update your section when you make changes) - Missing Persons Reporting Platform

> **Monorepo Architecture**: Full-stack application with Flask backend and React frontend

## Project Structure

```
FindMe/
├── Findme-backend/      # Flask REST API
└── findme-client/       # React + Vite
```

## Tech Stack

### Backend (Flask)
- **Framework**: Flask 3.0.3
- **Database**: SQLAlchemy 2.0.44 + SQLite
- **Migrations**: Alembic 1.13.1
- **Testing**: Pytest 8.4.2
- **CORS**: Flask-CORS 4.0.0

### Frontend (React)
- **Framework**: React 18
- **Build Tool**: Vite 5.x
- **HTTP Client**: Axios

## Getting Started

### Prerequisites
- Python 3.13+
- Node.js 20.x+
- npm

### Backend Setup

```bash
cd Findme-backend

# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```

**Backend runs on**: `http://localhost:5000`

### Frontend Setup

```bash
cd findme-client

# Install dependencies
npm install

# Run development server
npm run dev
```

**Frontend runs on**: `http://localhost:5173`

## Backend Architecture

```
Findme-backend/
├── models/          # Database models (SQLAlchemy)
├── controllers/     # Business logic layer
├── routes/          # API endpoints (Blueprint registration)
├── database/        # SQLite database files
├── tests/           # Unit and integration tests
├── config.py        # Configuration management
└── app.py           # Application entry point
```

### Design Patterns
- **MVC Architecture**: Separation of concerns
- **Blueprint Pattern**: Modular route organization
- **Factory Pattern**: Application configuration

## API Endpoints (Planned)

### Missing Persons

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/missing` | List all missing persons |
| POST | `/api/missing` | Create new report |
| GET | `/api/missing/<id>` | Get specific report |
| PUT | `/api/missing/<id>` | Update report status |
| DELETE | `/api/missing/<id>` | Delete report |

## Testing

### Backend Tests
```bash
cd Findme-backend
pytest
```

### Frontend Tests
```bash
cd findme-client
npm run test
```

## Environment Variables

Create `.env` in `Findme-backend/`:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///database/missing_persons.db
FLASK_ENV=development
```

## Team Collaboration

### Branch Strategy
- `main`: Production-ready code
- `develop`: Integration branch
- `feature/*`: Feature development

## Development Guidelines

### API Design Principles
- RESTful conventions
- JSON response format
- Proper HTTP status codes
- Error handling middleware
- Input validation

## Roadmap

- Project setup and structure
- Database models and migrations
- CRUD API endpoints
- User authentication (JWT)
- Real-time notifications
- Google Maps integration
- SMS alerts
- Admin dashboard
- Mobile responsive design

## Contributors

- Elijah Kamanga
- James Wachira
- Demestrine Awuor
- Eva Chemngorem
- Ian Tuitoek

## License

MIT License

---

**Built by the finders for Phase 4 - Moringa School**

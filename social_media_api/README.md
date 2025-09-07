# Social Media API

A Django REST Framework-based API for a social media platform.

## Setup Instructions

1. Create a virtual environment: `python -m venv env`
2. Activate the environment: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## Authentication Endpoints

### User Registration
- **URL**: `/api/auth/register/`
- **Method**: `POST`
- **Body**:
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "testpass123",
  "bio": "Optional user bio"
}
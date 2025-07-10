# Job Recommendation System

A FastAPI-based backend service for job recommendations that matches user skills with job requirements.

## Requirements

- Python 3.13+

## Features

- User profile management with skills
- Job listing management
- User-job interaction tracking (views and applications)
- Skill-based job recommendations
- Comprehensive error handling and input validation
- Secure database operations

## Setup

1. Ensure you have Python 3.13 installed:
```bash
python3.13 --version
```

2. Create a virtual environment:
```bash
python3.13 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Upgrade pip to the latest version:
```bash
pip install --upgrade pip
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## API Endpoints

### Users
- `POST /users/`: Create a new user
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "skills": ["Python", "FastAPI", "SQL"]
  }
  ```
  Validation:
  - Name: 1-100 characters
  - Email: Valid email format
  - Skills: Non-empty strings, max 50 skills

### Jobs
- `POST /jobs/`: Create a new job listing
  ```json
  {
    "title": "Backend Developer",
    "description": "We are looking for a Python developer...",
    "required_skills": ["Python", "FastAPI", "PostgreSQL"]
  }
  ```
  Validation:
  - Title: 1-200 characters
  - Description: 1-2000 characters
  - Required Skills: Non-empty strings, max 50 skills

### Interactions
- `POST /interactions/`: Log a user-job interaction
  ```json
  {
    "job_id": 1,
    "interaction_type": "view"  // or "apply"
  }
  ```
  Query parameter:
  - user_id: Positive integer

### Recommendations
- `GET /recommendations/{user_id}`: Get top 3 job recommendations for a user
  - Returns jobs sorted by match score (0.0 to 1.0)


## How It Works

The recommendation system works by:
1. Comparing user skills with job required skills
2. Calculating a weighted match score based on:
   - Number of matching skills
   - Previously applied jobs (2x weight for matching skills)
3. Returning the top 3 jobs with the highest match scores

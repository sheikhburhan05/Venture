# Job Recommendation System

A FastAPI-based backend service for job recommendations that matches user skills with job requirements.

## Features

- User profile management with skills
- Job listing management
- User-job interaction tracking (views and applications)
- Skill-based job recommendations

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
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

### Jobs
- `POST /jobs/`: Create a new job listing
  ```json
  {
    "title": "Backend Developer",
    "description": "We are looking for a Python developer...",
    "required_skills": ["Python", "FastAPI", "PostgreSQL"]
  }
  ```

### Interactions
- `POST /interactions/`: Log a user-job interaction
  ```json
  {
    "job_id": 1,
    "interaction_type": "view",  // or "apply"
    "user_id": 1
  }
  ```

### Recommendations
- `GET /recommendations/{user_id}`: Get top 3 job recommendations for a user

## How It Works

The recommendation system works by:
1. Comparing user skills with job required skills
2. Calculating a weighted match score based on the number of matching skills and applied jobs
3. Returning the top 3 jobs with the highest match scores 
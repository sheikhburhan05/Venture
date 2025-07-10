from fastapi import FastAPI
from .database import engine
from .models import Base
from .routes import user_routes, job_routes, interaction_routes, recommendation_routes

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Recommendation System")

# Include routers
app.include_router(user_routes.router)
app.include_router(job_routes.router)
app.include_router(interaction_routes.router)
app.include_router(recommendation_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Recommendation System API"} 
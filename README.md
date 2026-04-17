# hng-api-deployment
# Stage 1 DevOps API

Simple FastAPI application deployed on a VPS using Nginx as a reverse proxy.

## Setup Instructions
1. Clone the repo
2. Create venv: `python -m venv venv`
3. Install: `pip install -r requirements.txt`
4. Run: `uvicorn main:app --reload`

## Endpoints
- GET `/`: Status message
- GET `/health`: Health check
- GET `/me`: Personal details

**Live URL:** 52.90.145.2

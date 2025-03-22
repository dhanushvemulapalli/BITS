from fastapi import APIRouter
from app.api.v1.endpoints import risk_assessment

api_router = APIRouter()
api_router.include_router(risk_assessment.router, prefix="/risk-assessment", tags=["risk-assessment"]) 
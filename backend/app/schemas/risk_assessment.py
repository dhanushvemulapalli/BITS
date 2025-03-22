from pydantic import BaseModel, Field, confloat
from typing import Optional, List, Dict, Any
from .base import BaseSchema
from ..models.risk_assessment import RiskLevel

class RiskAssessmentBase(BaseModel):
    user_id: int
    health_record_id: int
    
    # Risk Scores
    overall_risk_score: confloat(ge=0, le=100)
    risk_level: RiskLevel
    
    # Component Risk Scores
    cardiovascular_risk: Optional[confloat(ge=0, le=100)] = None
    respiratory_risk: Optional[confloat(ge=0, le=100)] = None
    metabolic_risk: Optional[confloat(ge=0, le=100)] = None
    lifestyle_risk: Optional[confloat(ge=0, le=100)] = None
    
    # Predictions
    predicted_health_issues: Optional[List[str]] = None
    risk_factors: Optional[List[str]] = None
    recommendations: Optional[List[str]] = None
    
    # Model Metadata
    model_version: Optional[str] = None
    prediction_confidence: Optional[confloat(ge=0, le=1)] = None

class RiskAssessmentCreate(RiskAssessmentBase):
    pass

class RiskAssessmentUpdate(BaseModel):
    overall_risk_score: Optional[confloat(ge=0, le=100)] = None
    risk_level: Optional[RiskLevel] = None
    cardiovascular_risk: Optional[confloat(ge=0, le=100)] = None
    respiratory_risk: Optional[confloat(ge=0, le=100)] = None
    metabolic_risk: Optional[confloat(ge=0, le=100)] = None
    lifestyle_risk: Optional[confloat(ge=0, le=100)] = None
    predicted_health_issues: Optional[List[str]] = None
    risk_factors: Optional[List[str]] = None
    recommendations: Optional[List[str]] = None
    model_version: Optional[str] = None
    prediction_confidence: Optional[confloat(ge=0, le=1)] = None

class RiskAssessment(RiskAssessmentBase, BaseSchema):
    pass

class RiskAssessmentRequest(BaseModel):
    age: int
    gender: str
    bmi: float
    blood_pressure: float
    cholesterol: float
    smoking_status: bool
    exercise_frequency: int
    diet_quality: str

class RiskAssessmentResponse(BaseModel):
    overall_risk_score: float
    cardiovascular_risk: float
    diabetes_risk: float
    recommendations: List[str] 
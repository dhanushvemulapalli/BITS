from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class RiskAssessmentBase(BaseModel):
    health_data: Dict[str, any] = Field(..., description="Health data used for risk assessment")

class RiskAssessmentCreate(RiskAssessmentBase):
    pass

class RiskAssessmentUpdate(BaseModel):
    health_data: Optional[Dict[str, any]] = None
    recommendations: Optional[List[str]] = None

class RiskAssessmentInDBBase(RiskAssessmentBase):
    id: int
    user_id: int
    overall_risk_score: float
    cardiovascular_risk: float
    diabetes_risk: float
    respiratory_risk: float
    metabolic_risk: float
    lifestyle_risk: float
    recommendations: List[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class RiskAssessmentInDB(RiskAssessmentInDBBase):
    pass

class RiskAssessmentResponse(RiskAssessmentInDBBase):
    pass 
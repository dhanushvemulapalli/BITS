from sqlalchemy import Column, Integer, Float, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel
import enum

class RiskLevel(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"

class RiskAssessment(BaseModel):
    __tablename__ = "risk_assessments"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    health_record_id = Column(Integer, ForeignKey("health_records.id"), nullable=False)
    
    # Risk Scores
    overall_risk_score = Column(Float, nullable=False)  # 0-100
    risk_level = Column(String, nullable=False)  # low, medium, high, very_high
    
    # Component Risk Scores
    cardiovascular_risk = Column(Float)
    respiratory_risk = Column(Float)
    metabolic_risk = Column(Float)
    lifestyle_risk = Column(Float)
    
    # Predictions
    predicted_health_issues = Column(JSON)  # List of predicted health issues
    risk_factors = Column(JSON)  # List of identified risk factors
    recommendations = Column(JSON)  # List of health recommendations
    
    # Model Metadata
    model_version = Column(String)
    prediction_confidence = Column(Float)
    
    # Relationships
    user = relationship("User", back_populates="risk_assessments")
    health_record = relationship("HealthRecord", back_populates="risk_assessments")
    insurance_policies = relationship("InsurancePolicy", back_populates="risk_assessment") 
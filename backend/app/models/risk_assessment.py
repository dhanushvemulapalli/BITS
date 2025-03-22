from sqlalchemy import Column, Integer, Float, String, JSON, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class RiskAssessment(Base):
    __tablename__ = "risk_assessments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    overall_risk_score = Column(Float, nullable=False)
    cardiovascular_risk = Column(Float, nullable=False)
    diabetes_risk = Column(Float, nullable=False)
    respiratory_risk = Column(Float, nullable=False)
    metabolic_risk = Column(Float, nullable=False)
    lifestyle_risk = Column(Float, nullable=False)
    recommendations = Column(JSON, nullable=False)
    health_data = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="risk_assessments") 
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date, JSON
from sqlalchemy.orm import relationship
from .base import BaseModel
import enum

class PolicyType(str, enum.Enum):
    LIFE = "life"
    HEALTH = "health"
    CRITICAL_ILLNESS = "critical_illness"
    DISABILITY = "disability"

class PolicyStatus(str, enum.Enum):
    DRAFT = "draft"
    PENDING = "pending"
    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class InsurancePolicy(BaseModel):
    __tablename__ = "insurance_policies"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    risk_assessment_id = Column(Integer, ForeignKey("risk_assessments.id"), nullable=False)
    provider_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Insurance provider
    
    # Policy Details
    policy_type = Column(String, nullable=False)
    policy_number = Column(String, unique=True, nullable=False)
    status = Column(String, nullable=False, default=PolicyStatus.DRAFT)
    
    # Coverage Details
    coverage_amount = Column(Float, nullable=False)
    premium_amount = Column(Float, nullable=False)
    deductible_amount = Column(Float)
    co_payment_percentage = Column(Float)
    
    # Dates
    start_date = Column(Date)
    end_date = Column(Date)
    renewal_date = Column(Date)
    
    # Policy Features
    benefits = Column(JSON)  # List of covered benefits
    exclusions = Column(JSON)  # List of exclusions
    riders = Column(JSON)  # List of additional riders
    
    # Risk-Based Adjustments
    risk_adjustment_factor = Column(Float)  # Multiplier based on risk assessment
    special_conditions = Column(JSON)  # Any special conditions or requirements
    
    # Relationships
    user = relationship("User", foreign_keys=[user_id], back_populates="insurance_policies")
    provider = relationship("User", foreign_keys=[provider_id])
    risk_assessment = relationship("RiskAssessment", back_populates="insurance_policies") 
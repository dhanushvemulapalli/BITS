from sqlalchemy import Column, String, Enum, Boolean
from sqlalchemy.orm import relationship
import enum
from .base import BaseModel

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    INSURANCE_PROVIDER = "insurance_provider"
    CUSTOMER = "customer"

class User(BaseModel):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.CUSTOMER)
    phone_number = Column(String)
    is_verified = Column(Boolean, default=False)
    
    # Relationships
    health_records = relationship("HealthRecord", back_populates="user")
    risk_assessments = relationship("RiskAssessment", back_populates="user")
    insurance_policies = relationship("InsurancePolicy", back_populates="user") 
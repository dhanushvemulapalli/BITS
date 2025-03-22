from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from .base import BaseModel
from datetime import datetime

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    INSURANCE_PROVIDER = "insurance_provider"
    CUSTOMER = "customer"

class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.CUSTOMER)
    is_verified = Column(Boolean, default=False)
    
    # Relationships
    health_records = relationship("HealthRecord", back_populates="user")
    risk_assessments = relationship("RiskAssessment", back_populates="user")
    insurance_policies = relationship("InsurancePolicy", back_populates="user") 
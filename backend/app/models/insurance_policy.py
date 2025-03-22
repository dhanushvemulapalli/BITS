from sqlalchemy import Column, Integer, Float, String, Date, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class PolicyType(str, enum.Enum):
    HEALTH = "health"
    LIFE = "life"
    CRITICAL_ILLNESS = "critical_illness"
    DISABILITY = "disability"

class PolicyStatus(str, enum.Enum):
    ACTIVE = "active"
    PENDING = "pending"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class InsurancePolicy(Base):
    __tablename__ = "insurance_policies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    policy_type = Column(Enum(PolicyType), nullable=False)
    status = Column(Enum(PolicyStatus), nullable=False, default=PolicyStatus.PENDING)
    coverage_amount = Column(Float, nullable=False)
    premium = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="insurance_policies") 
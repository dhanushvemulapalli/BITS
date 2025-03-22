from pydantic import BaseModel, Field, confloat
from typing import Optional, List, Dict, Any
from datetime import date
from .base import BaseSchema
from ..models.insurance_policy import PolicyType, PolicyStatus

class PolicyBase(BaseModel):
    policy_type: str
    coverage_amount: float
    premium: float
    start_date: date
    end_date: date

class PolicyCreate(PolicyBase):
    pass

class InsurancePolicy(PolicyBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True

class InsurancePolicyBase(BaseModel):
    user_id: int
    risk_assessment_id: int
    provider_id: int
    
    # Policy Details
    policy_type: PolicyType
    policy_number: str
    status: PolicyStatus = PolicyStatus.DRAFT
    
    # Coverage Details
    coverage_amount: confloat(ge=0)
    premium_amount: confloat(ge=0)
    deductible_amount: Optional[confloat(ge=0)] = None
    co_payment_percentage: Optional[confloat(ge=0, le=100)] = None
    
    # Dates
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    renewal_date: Optional[date] = None
    
    # Policy Features
    benefits: Optional[List[str]] = None
    exclusions: Optional[List[str]] = None
    riders: Optional[List[str]] = None
    
    # Risk-Based Adjustments
    risk_adjustment_factor: Optional[confloat(ge=0)] = None
    special_conditions: Optional[List[str]] = None

class InsurancePolicyCreate(InsurancePolicyBase):
    pass

class InsurancePolicyUpdate(BaseModel):
    status: Optional[PolicyStatus] = None
    coverage_amount: Optional[confloat(ge=0)] = None
    premium_amount: Optional[confloat(ge=0)] = None
    deductible_amount: Optional[confloat(ge=0)] = None
    co_payment_percentage: Optional[confloat(ge=0, le=100)] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    renewal_date: Optional[date] = None
    benefits: Optional[List[str]] = None
    exclusions: Optional[List[str]] = None
    riders: Optional[List[str]] = None
    risk_adjustment_factor: Optional[confloat(ge=0)] = None
    special_conditions: Optional[List[str]] = None

class InsurancePolicy(InsurancePolicyBase, BaseSchema):
    pass 
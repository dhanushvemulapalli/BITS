from pydantic import BaseModel, Field, confloat, conint
from typing import Optional, List
from datetime import date
from .base import BaseSchema

class HealthRecordBase(BaseModel):
    date: date
    
    # Basic Health Metrics
    age: Optional[conint(ge=0, le=150)] = None
    height: Optional[confloat(ge=0, le=300)] = None  # cm
    weight: Optional[confloat(ge=0, le=500)] = None  # kg
    bmi: Optional[confloat(ge=0, le=100)] = None
    
    # Vital Signs
    blood_pressure_systolic: Optional[conint(ge=0, le=300)] = None  # mmHg
    blood_pressure_diastolic: Optional[conint(ge=0, le=200)] = None  # mmHg
    heart_rate: Optional[conint(ge=0, le=300)] = None  # bpm
    temperature: Optional[confloat(ge=20, le=45)] = None  # °C
    
    # Lab Results
    cholesterol_total: Optional[confloat(ge=0, le=1000)] = None  # mg/dL
    cholesterol_hdl: Optional[confloat(ge=0, le=200)] = None  # mg/dL
    cholesterol_ldl: Optional[confloat(ge=0, le=500)] = None  # mg/dL
    triglycerides: Optional[confloat(ge=0, le=2000)] = None  # mg/dL
    blood_sugar: Optional[confloat(ge=0, le=500)] = None  # mg/dL
    
    # Lifestyle Factors
    smoking_status: Optional[str] = None  # "never", "former", "current"
    exercise_frequency: Optional[str] = None  # "none", "occasional", "regular", "very_active"
    alcohol_consumption: Optional[str] = None  # "none", "moderate", "heavy"
    diet_type: Optional[str] = None  # "standard", "vegetarian", "vegan", "keto", etc.
    
    # Medical History
    chronic_conditions: Optional[List[str]] = None
    medications: Optional[List[str]] = None
    allergies: Optional[List[str]] = None

class HealthRecordCreate(HealthRecordBase):
    user_id: int

class HealthRecordUpdate(HealthRecordBase):
    pass

class HealthRecord(HealthRecordBase, BaseSchema):
    user_id: int 
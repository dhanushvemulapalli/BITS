from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class HealthRecord(BaseModel):
    __tablename__ = "health_records"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    
    # Basic Health Metrics
    age = Column(Integer)
    height = Column(Float)  # in cm
    weight = Column(Float)  # in kg
    bmi = Column(Float)
    
    # Vital Signs
    blood_pressure_systolic = Column(Integer)  # mmHg
    blood_pressure_diastolic = Column(Integer)  # mmHg
    heart_rate = Column(Integer)  # bpm
    temperature = Column(Float)  # °C
    
    # Lab Results
    cholesterol_total = Column(Float)  # mg/dL
    cholesterol_hdl = Column(Float)  # mg/dL
    cholesterol_ldl = Column(Float)  # mg/dL
    triglycerides = Column(Float)  # mg/dL
    blood_sugar = Column(Float)  # mg/dL
    
    # Lifestyle Factors
    smoking_status = Column(String)  # "never", "former", "current"
    exercise_frequency = Column(String)  # "none", "occasional", "regular", "very_active"
    alcohol_consumption = Column(String)  # "none", "moderate", "heavy"
    diet_type = Column(String)  # "standard", "vegetarian", "vegan", "keto", etc.
    
    # Medical History
    chronic_conditions = Column(String)  # JSON string of conditions
    medications = Column(String)  # JSON string of medications
    allergies = Column(String)  # JSON string of allergies
    
    # Relationships
    user = relationship("User", back_populates="health_records")
    risk_assessments = relationship("RiskAssessment", back_populates="health_record") 
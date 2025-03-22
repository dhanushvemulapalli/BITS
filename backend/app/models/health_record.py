from sqlalchemy import Column, Integer, Float, Date, DateTime, ForeignKey, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class HealthRecord(Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    height = Column(Float)  # in cm
    weight = Column(Float)  # in kg
    systolic_bp = Column(Integer)  # systolic blood pressure
    diastolic_bp = Column(Integer)  # diastolic blood pressure
    heart_rate = Column(Integer)
    cholesterol = Column(Float)
    blood_sugar = Column(Float)
    notes = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="health_records")

    # Basic Health Metrics
    age = Column(Integer)
    bmi = Column(Float)
    
    # Vital Signs
    temperature = Column(Float)  # °C
    
    # Lab Results
    cholesterol_total = Column(Float)  # mg/dL
    cholesterol_hdl = Column(Float)  # mg/dL
    cholesterol_ldl = Column(Float)  # mg/dL
    triglycerides = Column(Float)  # mg/dL
    
    # Lifestyle Factors
    smoking_status = Column(String)  # "never", "former", "current"
    exercise_frequency = Column(String)  # "none", "occasional", "regular", "very_active"
    alcohol_consumption = Column(String)  # "none", "moderate", "heavy"
    diet_type = Column(String)  # "standard", "vegetarian", "vegan", "keto", etc.
    
    # Medical History
    chronic_conditions = Column(String)  # JSON string of conditions
    medications = Column(String)  # JSON string of medications
    allergies = Column(String)  # JSON string of allergies
    
    risk_assessments = relationship("RiskAssessment", back_populates="health_record") 
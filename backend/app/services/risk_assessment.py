from datetime import date
from typing import List, Dict, Any
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os
from app.core.config import settings

class RiskAssessmentService:
    def __init__(self):
        self.model_path = os.path.join(settings.MODEL_PATH, "risk_assessment.joblib")
        self.scaler_path = os.path.join(settings.MODEL_PATH, "scaler.joblib")
        self.model = self._load_model()
        self.scaler = self._load_scaler()

    def _load_model(self) -> RandomForestClassifier:
        if os.path.exists(self.model_path):
            return joblib.load(self.model_path)
        return self._train_new_model()

    def _load_scaler(self) -> StandardScaler:
        if os.path.exists(self.scaler_path):
            return joblib.load(self.scaler_path)
        return StandardScaler()

    def _train_new_model(self) -> RandomForestClassifier:
        # TODO: Implement model training with real data
        return RandomForestClassifier(n_estimators=100, random_state=42)

    def calculate_bmi(self, height: float, weight: float) -> float:
        """Calculate BMI from height (cm) and weight (kg)"""
        height_m = height / 100
        return weight / (height_m * height_m)

    def calculate_cardiovascular_risk(self, data: Dict[str, Any]) -> float:
        """Calculate cardiovascular risk score"""
        # Simplified risk calculation based on common factors
        risk_factors = {
            'bmi': self._normalize_bmi(data.get('bmi', 25)),
            'blood_pressure': self._normalize_blood_pressure(
                data.get('systolic_bp', 120),
                data.get('diastolic_bp', 80)
            ),
            'cholesterol': self._normalize_cholesterol(data.get('cholesterol', 200)),
            'smoking': 1 if data.get('smoking_status') == 'current' else 0,
            'exercise': self._normalize_exercise(data.get('exercise_frequency', 'none'))
        }
        
        weights = {
            'bmi': 0.2,
            'blood_pressure': 0.3,
            'cholesterol': 0.2,
            'smoking': 0.2,
            'exercise': 0.1
        }
        
        return sum(risk_factors[factor] * weights[factor] for factor in risk_factors)

    def calculate_diabetes_risk(self, data: Dict[str, Any]) -> float:
        """Calculate diabetes risk score"""
        risk_factors = {
            'bmi': self._normalize_bmi(data.get('bmi', 25)),
            'blood_sugar': self._normalize_blood_sugar(data.get('blood_sugar', 100)),
            'age': self._normalize_age(data.get('age', 30)),
            'exercise': self._normalize_exercise(data.get('exercise_frequency', 'none'))
        }
        
        weights = {
            'bmi': 0.3,
            'blood_sugar': 0.3,
            'age': 0.2,
            'exercise': 0.2
        }
        
        return sum(risk_factors[factor] * weights[factor] for factor in risk_factors)

    def _normalize_bmi(self, bmi: float) -> float:
        """Normalize BMI to 0-1 range"""
        return min(max((bmi - 18.5) / (30 - 18.5), 0), 1)

    def _normalize_blood_pressure(self, systolic: int, diastolic: int) -> float:
        """Normalize blood pressure to 0-1 range"""
        return min(max((systolic - 90) / (140 - 90), 0), 1)

    def _normalize_cholesterol(self, cholesterol: float) -> float:
        """Normalize cholesterol to 0-1 range"""
        return min(max((cholesterol - 150) / (250 - 150), 0), 1)

    def _normalize_blood_sugar(self, blood_sugar: float) -> float:
        """Normalize blood sugar to 0-1 range"""
        return min(max((blood_sugar - 70) / (126 - 70), 0), 1)

    def _normalize_age(self, age: int) -> float:
        """Normalize age to 0-1 range"""
        return min(max((age - 30) / (60 - 30), 0), 1)

    def _normalize_exercise(self, frequency: str) -> float:
        """Convert exercise frequency to 0-1 range"""
        exercise_map = {
            'none': 1.0,
            'occasional': 0.75,
            'regular': 0.5,
            'very_active': 0.25
        }
        return exercise_map.get(frequency, 0.5)

    def generate_recommendations(self, risk_scores: Dict[str, float]) -> List[str]:
        """Generate personalized health recommendations"""
        recommendations = []
        
        if risk_scores['cardiovascular_risk'] > 0.7:
            recommendations.extend([
                "Schedule a cardiac check-up",
                "Monitor blood pressure daily",
                "Reduce salt intake",
                "Start a regular exercise program"
            ])
        
        if risk_scores['diabetes_risk'] > 0.7:
            recommendations.extend([
                "Monitor blood sugar levels",
                "Consult a nutritionist",
                "Reduce sugar intake",
                "Exercise regularly"
            ])
        
        if risk_scores['metabolic_risk'] > 0.7:
            recommendations.extend([
                "Maintain a balanced diet",
                "Stay hydrated",
                "Get regular sleep",
                "Manage stress levels"
            ])
        
        if risk_scores['lifestyle_risk'] > 0.7:
            recommendations.extend([
                "Quit smoking",
                "Limit alcohol consumption",
                "Practice stress management",
                "Get regular health check-ups"
            ])
        
        return list(set(recommendations))  # Remove duplicates

    def assess_risk(self, health_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform comprehensive health risk assessment"""
        # Calculate individual risk scores
        cardiovascular_risk = self.calculate_cardiovascular_risk(health_data)
        diabetes_risk = self.calculate_diabetes_risk(health_data)
        respiratory_risk = 0.5  # Placeholder
        metabolic_risk = 0.5  # Placeholder
        lifestyle_risk = 0.5  # Placeholder
        
        # Calculate overall risk score
        risk_scores = {
            'cardiovascular_risk': cardiovascular_risk,
            'diabetes_risk': diabetes_risk,
            'respiratory_risk': respiratory_risk,
            'metabolic_risk': metabolic_risk,
            'lifestyle_risk': lifestyle_risk
        }
        
        overall_risk = np.mean(list(risk_scores.values()))
        
        # Generate recommendations
        recommendations = self.generate_recommendations(risk_scores)
        
        return {
            'overall_risk_score': float(overall_risk),
            'cardiovascular_risk': float(cardiovascular_risk),
            'diabetes_risk': float(diabetes_risk),
            'respiratory_risk': float(respiratory_risk),
            'metabolic_risk': float(metabolic_risk),
            'lifestyle_risk': float(lifestyle_risk),
            'recommendations': recommendations
        } 
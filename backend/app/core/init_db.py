from ..core.database import engine
from ..models.base import Base
from ..models.user import User
from ..models.health_record import HealthRecord
from ..models.risk_assessment import RiskAssessment
from ..models.insurance_policy import InsurancePolicy

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Creating database tables...")
    init_db()
    print("Database tables created successfully!") 
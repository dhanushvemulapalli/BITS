from typing import Any, Dict, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.services.risk_assessment import RiskAssessmentService
from app.schemas.risk_assessment import (
    RiskAssessmentCreate,
    RiskAssessmentUpdate,
    RiskAssessmentInDB,
    RiskAssessmentResponse
)
from app.models.risk_assessment import RiskAssessment
from app.models.user import User

router = APIRouter()
risk_service = RiskAssessmentService()

@router.post("/", response_model=RiskAssessmentResponse)
def create_risk_assessment(
    *,
    db: Session = Depends(deps.get_db),
    risk_assessment_in: RiskAssessmentCreate,
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Create new risk assessment for the current user.
    """
    # Perform risk assessment
    risk_scores = risk_service.assess_risk(risk_assessment_in.health_data)
    
    # Create risk assessment record
    risk_assessment = RiskAssessment(
        user_id=current_user.id,
        overall_risk_score=risk_scores['overall_risk_score'],
        cardiovascular_risk=risk_scores['cardiovascular_risk'],
        diabetes_risk=risk_scores['diabetes_risk'],
        respiratory_risk=risk_scores['respiratory_risk'],
        metabolic_risk=risk_scores['metabolic_risk'],
        lifestyle_risk=risk_scores['lifestyle_risk'],
        recommendations=risk_scores['recommendations'],
        health_data=risk_assessment_in.health_data
    )
    
    db.add(risk_assessment)
    db.commit()
    db.refresh(risk_assessment)
    
    return risk_assessment

@router.get("/", response_model=List[RiskAssessmentInDB])
def read_risk_assessments(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Retrieve risk assessments for the current user.
    """
    risk_assessments = db.query(RiskAssessment).filter(
        RiskAssessment.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    
    return risk_assessments

@router.get("/{risk_assessment_id}", response_model=RiskAssessmentInDB)
def read_risk_assessment(
    *,
    db: Session = Depends(deps.get_db),
    risk_assessment_id: int,
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Get specific risk assessment by ID.
    """
    risk_assessment = db.query(RiskAssessment).filter(
        RiskAssessment.id == risk_assessment_id,
        RiskAssessment.user_id == current_user.id
    ).first()
    
    if not risk_assessment:
        raise HTTPException(status_code=404, detail="Risk assessment not found")
    
    return risk_assessment

@router.put("/{risk_assessment_id}", response_model=RiskAssessmentInDB)
def update_risk_assessment(
    *,
    db: Session = Depends(deps.get_db),
    risk_assessment_id: int,
    risk_assessment_in: RiskAssessmentUpdate,
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Update a risk assessment.
    """
    risk_assessment = db.query(RiskAssessment).filter(
        RiskAssessment.id == risk_assessment_id,
        RiskAssessment.user_id == current_user.id
    ).first()
    
    if not risk_assessment:
        raise HTTPException(status_code=404, detail="Risk assessment not found")
    
    # Update fields
    for field, value in risk_assessment_in.dict(exclude_unset=True).items():
        setattr(risk_assessment, field, value)
    
    db.add(risk_assessment)
    db.commit()
    db.refresh(risk_assessment)
    
    return risk_assessment

@router.delete("/{risk_assessment_id}")
def delete_risk_assessment(
    *,
    db: Session = Depends(deps.get_db),
    risk_assessment_id: int,
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    """
    Delete a risk assessment.
    """
    risk_assessment = db.query(RiskAssessment).filter(
        RiskAssessment.id == risk_assessment_id,
        RiskAssessment.user_id == current_user.id
    ).first()
    
    if not risk_assessment:
        raise HTTPException(status_code=404, detail="Risk assessment not found")
    
    db.delete(risk_assessment)
    db.commit()
    
    return {"status": "success"} 
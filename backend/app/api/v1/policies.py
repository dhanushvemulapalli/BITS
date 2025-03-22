from fastapi import APIRouter, Depends
from typing import List
from app.schemas.insurance_policy import InsurancePolicy, PolicyCreate
from app.core.auth import get_current_user
from app.schemas.user import UserResponse

router = APIRouter()

@router.get("/", response_model=List[InsurancePolicy])
async def get_policies(current_user: UserResponse = Depends(get_current_user)):
    # TODO: Implement policy listing
    return []

@router.post("/", response_model=InsurancePolicy)
async def create_policy(
    policy: PolicyCreate,
    current_user: UserResponse = Depends(get_current_user)
):
    # TODO: Implement policy creation
    return InsurancePolicy(
        id=1,
        user_id=current_user.id,
        policy_type=policy.policy_type,
        coverage_amount=policy.coverage_amount,
        premium=policy.premium,
        start_date=policy.start_date,
        end_date=policy.end_date
    ) 
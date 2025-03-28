from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_active: Optional[bool] = True
    is_deleted: Optional[bool] = False 
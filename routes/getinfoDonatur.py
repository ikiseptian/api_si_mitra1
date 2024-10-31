from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.db_connection import get_db1
from ..controller.getinfoDonatur import get_info_donatur_this_month
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

# Response Model
class DonaturResponse(BaseModel):
    # sesuaikan dengan struktur response yang diharapkan
    id_crm: str
    # tambahkan field lainnya
    
    class Config:
        orm_mode = True

@router.get("/my_info_donatur", response_model=DonaturResponse)
async def info_donatur_this_month(
    id_crm: str,
    db: Session = Depends(get_db1)
):
    try:
        result = get_info_donatur_this_month(db, id_crm)
        if not result:
            raise HTTPException(status_code=404, detail="Donatur not found")
        return result
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
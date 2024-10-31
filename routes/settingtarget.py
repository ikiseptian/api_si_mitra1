# routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.db_connection import get_db1
from ..controller.settigtarget import get_transaction_achieve

router = APIRouter()

@router.get("/my_achieve")
async def my_achieve(id_crm: int, waktu: int = 1, growth_persentase: int = 0, db: Session = Depends(get_db1)):
    result = get_transaction_achieve(db, id_crm, waktu, growth_persentase)
    return result

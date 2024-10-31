from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.db_connection import get_db1
from ..controller.getraport import get_raport_zisco

router = APIRouter()

@router.get("/my_raport")
async def my_raport(id_crm: str, waktu: int = 1, db: Session = Depends(get_db1)):
    if not id_crm:
        raise HTTPException(status_code=400, detail="id_crm is required")
    
    raport = get_raport_zisco(db, id_crm, waktu)
    return raport
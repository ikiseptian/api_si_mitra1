from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db_connection import get_db1
from controller.getraportdonatur import get_raport_data

router = APIRouter()

def get_db():
    db = get_db1()
    try:
        yield db
    finally:
        db.close()

@router.get("/donatur_raport")
async def get_raport_zisco_donatur(id_crm: str, waktu: int = 1, db: Session = Depends(get_db1)):
    if not id_crm:
        raise HTTPException(status_code=400, detail="id_crm is required")
    raport_data = get_raport_data(db, id_crm, waktu)
    return raport_data

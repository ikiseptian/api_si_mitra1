from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db_connection import get_db1, get_db2
from app.db_controller import get_campaigns_from_db1, get_campaigns_from_db2

router = APIRouter()

# Route untuk mendapatkan data dari database 1
@router.get("/campaigns/search")
def read_campaigns_db1(db: Session = Depends(get_db1)):
    campaigns = get_campaigns_from_db1(db)
    return {"data": campaigns}

# Route untuk mendapatkan data dari database 2
@router.get("/campaigns/db2")
def read_campaigns_db2(db: Session = Depends(get_db2)):
    campaigns = get_campaigns_from_db2(db)
    return {"data": campaigns}

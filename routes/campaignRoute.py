from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..config.db_connection import get_db1, get_db2
from ..controller.campaignController import (
    get_campaigns_from_db1,
    get_campaigns_from_db2,
    
)

router = APIRouter()

@router.get("/campaigns/search")
def read_campaigns_db1(db: Session = Depends(get_db1)):
    campaigns = get_campaigns_from_db1(db)
    return {"data": campaigns}

@router.get("/campaigns/db2")
def read_campaigns_db2(db: Session = Depends(get_db2)):
    campaigns = get_campaigns_from_db2(db)
    return {"data": campaigns}
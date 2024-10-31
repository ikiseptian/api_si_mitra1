from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.db_connection import get_db1
from ..controller.transaksiController import get_detailed_transactions
import logging

router = APIRouter()

@router.get("/transactions/{id_crm}")
def read_transactions(id_crm: str, db: Session = Depends(get_db1)):
    try:
        logging.info(f"Received id_crm: {id_crm}")  # Logging input
        transactions = get_detailed_transactions(db, id_crm)
        return {"status": True, "data": transactions}
    except ValueError as e:
        logging.error(f"ValueError in read_transactions: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Unexpected error in read_transactions: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


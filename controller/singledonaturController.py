from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.singledonaturModel import SingleDonatur
import logging

def get_single_donatur_info(db: Session, id_donatur: str):
    try:
        single_donatur = db.query(SingleDonatur).filter(SingleDonatur.id_donatur == id_donatur).first()
        if single_donatur is None:
            raise HTTPException(status_code=404, detail="Single Donatur not found")
        return single_donatur
    except Exception as e:
        logging.error(f"Error retrieving single donatur info: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.db_connection import get_db1
from ..controller.singledonaturController import get_single_donatur_info
import logging

router = APIRouter()

@router.get("/singledonatur/{id_donatur}")
def read_single_donatur(id_donatur: str, db: Session = Depends(get_db1)):
    try:
        single_donatur = get_single_donatur_info(db, id_donatur)
        return {
            "id_donatur": single_donatur.id_donatur,
            "donatur": single_donatur.donatur,
            "hp": single_donatur.hp,
            "email": single_donatur.email,
            "aktif": single_donatur.aktif,
            "id_kantor": single_donatur.id_kantor,
            "id_jenis": single_donatur.id_jenis,
            "tgl_lahir": single_donatur.tgl_lahir,
            "status": single_donatur.status,
            "last_transaction": single_donatur.last_transaction,
            "id_profiling": single_donatur.id_profiling,
            "whatsapp": single_donatur.whatsapp,
        }
    except HTTPException as e:
        logging.error(f"HTTP error: {e.detail}")
        raise e
    except Exception as e:
        logging.error(f"Unexpected error in read_single_donatur: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

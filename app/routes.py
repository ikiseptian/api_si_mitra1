import json
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.db_connection import get_db1, get_db2
from app.db_controller import (
    get_campaigns_from_db1,
    get_campaigns_from_db2,
    get_detailed_transactions,
    get_karyawan_by_email,
    get_single_donatur_info
    
)
import logging

router = APIRouter()

@router.get("/campaigns/search")
def read_campaigns_db1(db: Session = Depends(get_db1)):
    campaigns = get_campaigns_from_db1(db)
    return {"data": campaigns}

@router.get("/campaigns/db2")
def read_campaigns_db2(db: Session = Depends(get_db2)):
    campaigns = get_campaigns_from_db2(db)
    return {"data": campaigns}

@router.get("/transactions/{id_crm}")
def read_transactions(id_crm: str, db: Session = Depends(get_db1)):
    try:
        transactions = get_detailed_transactions(db, id_crm)
        return {"status": True, "data": transactions}
    except ValueError as e:
        logging.error(f"ValueError in read_transactions: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Unexpected error in read_transactions: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/zams5/sso")
def get_karyawan_info(email: str, db: Session = Depends(get_db1)):
    try:
        karyawan = get_karyawan_by_email(db, email)
        if karyawan:
            return {
                "status": True,
                "data": {
                    "karyawan": [{
                        "id_karyawan": karyawan.id_karyawan,
                        "karyawan": karyawan.karyawan,
                        "email": karyawan.email,
                        "id_kantor": karyawan.id_kantor,
                        "username": karyawan.username
                    }]
                }
            }
        else:
            raise HTTPException(status_code=404, detail="Karyawan not found")
    except Exception as e:
        logging.error(f"Error in get_karyawan_info: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/singledonatur/{id_donatur}")
def read_single_donatur(id_donatur: str, db: Session = Depends(get_db1)):
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



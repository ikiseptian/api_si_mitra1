from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..config.db_connection import get_db1
from ..controller.karyawanController import get_karyawan_by_email
import logging

router = APIRouter()

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

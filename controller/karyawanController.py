import logging
from sqlalchemy.orm import Session
from sqlalchemy import text

def get_karyawan_by_email(db: Session, email: str):
    try:
        query = text("""
            SELECT id_karyawan, karyawan, email, id_kantor, panggilan AS username
            FROM hcm_karyawan
            WHERE email = :email
        """)
        result = db.execute(query, {"email": email}).first()
        return result
    except Exception as e:
        logging.error(f"Error in get_karyawan_by_email: {str(e)}")
        return None

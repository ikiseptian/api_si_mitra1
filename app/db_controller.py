import logging
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Any

from app.models import SingleDonatur

def get_campaigns_from_db1(db: Session) -> List[Dict[str, Any]]:
    try:
        query = text("""
            SELECT id_campaign, campaign 
            FROM your_table_name
            WHERE active = 1
        """)
        result = db.execute(query)
        return [{"id_campaign": row[0], "campaign": row[1]} for row in result]
    except Exception as e:
        logging.error(f"Error in get_campaigns_from_db1: {str(e)}")
        return []

def get_campaigns_from_db2(db: Session) -> List[Dict[str, Any]]:
    try:
        query = text("""
            SELECT id_campaign, campaign 
            FROM your_second_db_table
            WHERE active = 1
        """)
        result = db.execute(query)
        return [{"id_campaign": row[0], "campaign": row[1]} for row in result]
    except Exception as e:
        logging.error(f"Error in get_campaigns_from_db2: {str(e)}")
        return []

def get_detailed_transactions(db: Session, id_crm: str) -> List[Dict[str, Any]]:
    try:
        query = text("""
            SELECT * FROM transactions_table 
            WHERE id_crm = :id_crm
        """)
        result = db.execute(query, {"id_crm": id_crm})
        return [dict(row) for row in result]
    except Exception as e:
        logging.error(f"Error in get_detailed_transactions: {str(e)}")
        raise

def get_karyawan_by_email(db: Session, email: str):
    try:
        query = text("""
            SELECT id_karyawan, karyawan, email, id_kantor, username
            FROM karyawan_table
            WHERE email = :email
        """)
        result = db.execute(query, {"email": email}).first()
        return result
    except Exception as e:
        logging.error(f"Error in get_karyawan_by_email: {str(e)}")
        return None
    
def get_single_donatur_info(db: Session, id_donatur: str):
    single_donatur = db.query(SingleDonatur).filter(SingleDonatur.id_donatur == id_donatur).first()
    if single_donatur is None:
        raise HTTPException(status_code=404, detail="Single Donatur not found")
    return single_donatur


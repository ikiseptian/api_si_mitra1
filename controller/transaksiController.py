import logging
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Any

def get_detailed_transactions(db: Session, id_crm: str) -> List[Dict[str, Any]]:
    try:
        logging.info(f"Querying transactions for id_crm: {id_crm}")
        query = text("""
            SELECT * FROM corez_transaksi 
            WHERE id_crm = :id_crm
            LIMIT 1
        """)
        
        logging.info("Executing query...")
        result = db.execute(query, {"id_crm": id_crm})
        
        # Ambil satu hasil
        transaction = result.mappings().first()  # Mengambil satu hasil
        
        if transaction is not None:
            transaction_dict = dict(transaction)  # Konversi ke dictionary
            logging.info(f"Formatted Transaction: {transaction_dict}")
            return [transaction_dict]  # Kembalikan dalam list
        else:
            logging.info("No transaction found.")
            return []  # Kembalikan list kosong jika tidak ada hasil
        
    except Exception as e:
        logging.error(f"Error in get_detailed_transactions: {str(e)}")
        raise

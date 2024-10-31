import logging
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List, Dict, Any

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
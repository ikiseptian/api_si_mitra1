from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

# Ubah import ini sesuai dengan struktur folder Anda
from ..config.db_connection import get_db1
from ..controller.getlistdonatur import get_transaction_group_by_donatur_detail

router = APIRouter()

def get_db():
    db = get_db1()
    try:
        yield db
    finally:
        db.close()

@router.get("/transaksi_by_donatur_detail")
def transaksi_by_donatur_detail(id_crm: int, id_donatur: int, page: int = 1, db: Session = Depends(get_db1)):
    transactions, total_count = get_transaction_group_by_donatur_detail(db, id_crm, id_donatur, page)

    total_pages = (total_count // 10) + (1 if total_count % 10 > 0 else 0)

    now = datetime.now()

    return {
        "data": transactions,
        "total": total_count,
        "total_page": total_pages,
        "next_page": page + 1 if page < total_pages else None,
        "previous_page": page - 1 if page > 1 else None,
        "last_page": page == total_pages,
        "url_kuitansi_bulk": f"https://donol9-rz-be-dev3.cnt.id/api/d/downloadIntruksiBayar?id_donatur={id_donatur}&tgl_awal={now.replace(day=1).date()}&tgl_akhir={now.date()}"
    }
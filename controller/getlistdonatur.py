from sqlalchemy.orm import Session
from ..models.getlistdonatur import CorezTransaksiThisMonth1, CorezDonatur, SettingProgram
from datetime import datetime

def get_transaction_group_by_donatur_detail(db: Session, id_crm: int, id_donatur: int, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    now = datetime.now()
    current_month = now.month

    transactions = (
        db.query(CorezTransaksiThisMonth1)
        .join(CorezDonatur, CorezTransaksiThisMonth1.id_donatur == CorezDonatur.id_donatur)
        .join(SettingProgram, CorezTransaksiThisMonth1.id_program == SettingProgram.id_program)
        .filter(
            CorezTransaksiThisMonth1.approved_transaksi == 'y',
            CorezTransaksiThisMonth1.id_crm == id_crm,
            CorezTransaksiThisMonth1.id_donatur == id_donatur,
            CorezDonatur.aktif == 'y',
            CorezTransaksiThisMonth1.tgl_donasi.month == current_month
        )
        .order_by(CorezTransaksiThisMonth1.tgl_donasi.desc())
        .offset(offset)
        .limit(per_page)
        .all()
    )

    total_count = (
        db.query(CorezTransaksiThisMonth1)
        .filter(
            CorezTransaksiThisMonth1.approved_transaksi == 'y',
            CorezTransaksiThisMonth1.id_crm == id_crm,
            CorezTransaksiThisMonth1.id_donatur == id_donatur,
            CorezTransaksiThisMonth1.tgl_donasi.month == current_month
        )
        .count()
    )

    return transactions, total_count

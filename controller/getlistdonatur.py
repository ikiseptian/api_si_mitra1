from sqlalchemy.orm import Session
from sqlalchemy import extract, func
from ..models.getlistdonatur import CorezTransaksiThisMonth1, CorezDonatur, SettingProgram, CorezTransaksi1
from datetime import datetime

def get_transaction_group_by_donatur_detail(db: Session, id_crm: str, id_donatur: str, page: int = 1, per_page: int = 10):
    offset = (page - 1) * per_page
    now = datetime.now()
    current_month = now.month

    # Query untuk data
    transactions = (
        db.query(
            CorezTransaksiThisMonth1.id_transaksi,
            CorezTransaksi1.id_crm,
            CorezTransaksi1.id_donatur,
            CorezTransaksi1.tgl_donasi,
            CorezTransaksi1.id_program,
            CorezDonatur.aktif,
            SettingProgram.program  # Ubah ini dari nama_program menjadi program
        )
        .select_from(CorezTransaksiThisMonth1)
        .join(CorezTransaksi1, CorezTransaksiThisMonth1.id_transaksi == CorezTransaksi1.id_crm)
        .join(CorezDonatur, CorezTransaksi1.id_donatur == CorezDonatur.id_crm)
        .join(SettingProgram, CorezTransaksi1.id_program == SettingProgram.id_program)
        .filter(
            CorezTransaksi1.approved_transaksi == 'y',
            CorezTransaksi1.id_crm == id_crm,
            CorezTransaksi1.id_donatur == id_donatur,
            CorezDonatur.aktif == 'y',
            extract('month', CorezTransaksi1.tgl_donasi) == current_month
        )
        .order_by(CorezTransaksi1.tgl_donasi.desc())
        .offset(offset)
        .limit(per_page)
        .all()
    )

    # Query untuk total count (tidak perlu diubah)
    total_count = (
        db.query(func.count())
        .select_from(CorezTransaksiThisMonth1)
        .join(CorezTransaksi1, CorezTransaksiThisMonth1.id_transaksi == CorezTransaksi1.id_crm)
        .join(CorezDonatur, CorezTransaksi1.id_donatur == CorezDonatur.id_crm)
        .join(SettingProgram, CorezTransaksi1.id_program == SettingProgram.id_program)
        .filter(
            CorezTransaksi1.approved_transaksi == 'y',
            CorezTransaksi1.id_crm == id_crm,
            CorezTransaksi1.id_donatur == id_donatur,
            CorezDonatur.aktif == 'y',
            extract('month', CorezTransaksi1.tgl_donasi) == current_month
        )
        .scalar()
    )

    return transactions, total_count
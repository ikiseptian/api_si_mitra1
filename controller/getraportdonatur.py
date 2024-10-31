from sqlalchemy.orm import Session
from ..models.getraportdonatur import CorezDonatur, CorezTransaksiToday
from sqlalchemy import func

def get_raport_data(db: Session, id_crm: str, waktu: int = None):
    # Hitung total donatur
    donatur_count = db.query(CorezDonatur).filter(
        CorezDonatur.id_crm == id_crm,
        CorezDonatur.aktif != 'n'
    ).count()

    # Hitung jumlah donatur yang berdonasi
    transaction_count = db.query(CorezTransaksiToday).filter(
        CorezTransaksiToday.id_crm == id_crm
    ).distinct(CorezTransaksiToday.id_donatur).count()

    # Inisialisasi data prospek
    prospek_data = {'total_donatur': 0, 'total_prospek': 0}

    # Hitung persentase
    persentase = (transaction_count / donatur_count) * 100 if donatur_count > 0 else 0

    return {
        'donatur': donatur_count,
        'berdonasi': transaction_count,
        'persentase': persentase,
        'terprospek': prospek_data['total_donatur'],
        'jml_prospek': prospek_data['total_prospek']
    }
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.getraport import (
    CorezDonatur1,
    CorezTransaksiToday,
    CorezTransaksiThisMonth,
    CorezTransaksiThisYear,
    CorezTransaksi,
    SettingTarget
)
from datetime import datetime

def get_raport_zisco(db: Session, id_crm: str, waktu: int):
    donaturResult = db.query(CorezDonatur1).filter(
        CorezDonatur1.id_crm == id_crm,
        CorezDonatur1.aktif != 'n',
        CorezDonatur1.id_profiling == 4
    ).first()  # Ambil hasil donatur pertama

    if not donaturResult:
        raise HTTPException(status_code=404, detail="Donatur not found")

    # Switch case untuk memilih model dan tanggal
    if waktu == 1:
        corez_model = CorezTransaksiToday
        tgl = datetime.now().date()
    elif waktu == 2:
        corez_model = CorezTransaksiThisMonth
        tgl = datetime.now().month
    elif waktu == 3:
        corez_model = CorezTransaksiThisYear
        tgl = datetime.now().year
    else:
        corez_model = CorezTransaksi
        tgl = None

    targetResult = db.query(SettingTarget).filter(
        SettingTarget.jenis == 'id_crm',
        SettingTarget.id_jenis == id_crm,
        SettingTarget.tgl_target >= tgl
    ).first()

    transaksiResult = db.query(corez_model).filter(
        corez_model.id_crm == id_crm,
        corez_model.approved_transaksi == 'y',
        corez_model.tgl_donasi == tgl
    ).first()

    donatur_count = db.query(CorezDonatur1).filter(
        CorezDonatur1.id_crm == id_crm,
        CorezDonatur1.aktif != 'n',
        CorezDonatur1.id_profiling == 4
    ).count()  # Menghitung jumlah donatur

    response = {
        'dana': targetResult.total_target if targetResult else None,
        'total_donatur': donatur_count,
        'donatur_baru': donatur_count,
        'total_transaksi': transaksiResult.total_transaksi if transaksiResult else 0
    }

    return response

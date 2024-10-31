# controllers.py
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from models.setting_target import CorezTransaksiToday, CorezTransaksiThisMonth, SettingTarget

def get_transaction_achieve(db: Session, id_crm: int, waktu: int, growth_persentase: int):
    now = datetime.now()
    prospect_query = 0
    target_query = 0
    growth_percentage = None

    # Logic sesuai waktu yang dipilih
    if waktu == 1:
        prospect_result = db.query(CorezTransaksiToday).filter(
            CorezTransaksiToday.approved_transaksi == 'y',
            CorezTransaksiToday.id_crm == id_crm,
            CorezTransaksiToday.tgl_donasi == now.date()
        ).first()

        target_result = db.query(SettingTarget).filter(
            SettingTarget.jenis == 'id_crm',
            SettingTarget.id_jenis == id_crm,
            SettingTarget.tgl_target == now.date()
        ).first()

        prospect_query = prospect_result.transaksi if prospect_result else 0
        target_query = target_result.target if target_result else 0

    # Logic for growth percentage if required
    if growth_persentase == 1 and waktu in [1, 2, 3]:
        last_year = now - timedelta(days=365)
        # Perform year-over-year growth calculation...

    percentage = round((prospect_query / target_query) * 100) if target_query else 0
    return {
        "total": prospect_query,
        "target": target_query,
        "persentase": percentage,
        "growth_persentase": growth_percentage
    }

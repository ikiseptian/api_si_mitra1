from sqlalchemy.orm import Session
from sqlalchemy import func, distinct
from ..models.getInfoDonatur import CorezDonatur5, CorezTransaksiThisMonth2, CorezDafThismonth
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_info_donatur_this_month(db: Session, id_crm: str):
    # Query donatur
    donatur_count = db.query(CorezDonatur5).filter(
        CorezDonatur5.id_crm == id_crm,
        CorezDonatur5.aktif != 'n'
    ).count()
    logger.debug(f"Donatur count: {donatur_count}")

    # Query transaksi
    transaksi_count = db.query(
        func.count(distinct(CorezTransaksiThisMonth2.id_donatur))
    ).filter(
        CorezTransaksiThisMonth2.id_crm == id_crm
    ).scalar() or 0
    logger.debug(f"Transaksi count: {transaksi_count}")

    # Query prospek
    prospek_query = db.query(
        func.count(distinct(CorezDafThismonth.id_muzakki)).label('total_donatur'),
        func.count(CorezDafThismonth.id_muzakki).label('total_prospek')
    ).filter(
        CorezDafThismonth.nia_zisco == id_crm
    ).first()
    total_donatur = prospek_query[0] if prospek_query else 0
    total_prospek = prospek_query[1] if prospek_query else 0
    logger.debug(f"Total Donatur: {total_donatur}, Total Prospek: {total_prospek}")

    # Calculate percentage
    persentase = round((transaksi_count / donatur_count) * 100) if donatur_count != 0 else 0
    logger.debug(f"Persentase: {persentase}")

    # Build and return response
    response = {
        "id_crm": id_crm,
        "donatur": donatur_count,
        "berdonasi": transaksi_count,
        "persentase": str(persentase),
        "terprospek": total_donatur,
        "jml_prospek": total_prospek
    }
    logger.debug(f"Response: {response}")
    return response
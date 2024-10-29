from fastapi import Depends
from app.db_connection import get_db1, get_db2
from sqlalchemy import text 

def get_laporan_beasiswa(
    db1=Depends(get_db1), 
    db2=Depends(get_db2)
):
    perPage = 5
    offset = 0  # Offset ditetapkan ke 0 jika tidak ada pagination

    # Contoh query database 1 (db1) dan db2
    query = text("""
        SELECT laporanid, donatur_id, donatur_nama, id_anak, pm_nama_lengkap, pm_anak_jenjang, semesterid, nama_semester,
               CONCAT('https://ajis.indonesiajuara.org/sinkronisasi_transaksi_corez_ajis/detailLapsem.php?laporanid=',laporanid,'&id_anak=',id_anak,'&semesterid=',semesterid,'&id_donatur=',donatur_id) AS url, 
               donatur.hp, IF(donatur.hp != '', CONCAT('https://api.whatsapp.com/send/?phone=', donatur.hp), 'uncontacted wa') AS url_whatsapp 
        FROM manual_laporan
        JOIN donatur ON manual_laporan.donatur_id = donatur.did
        WHERE manual_laporan.status_terbuat = 1
        ORDER BY manual_laporan.semesterid DESC, manual_laporan.pm_nama_lengkap ASC
        LIMIT :offset, :perPage
    """)

    results = db1.execute(query, {"offset": offset, "perPage": perPage}).fetchall()
    total_data = db1.execute(text("SELECT COUNT(*) FROM manual_laporan WHERE status_terbuat = 1")).scalar()

    # Menghitung total halaman dan navigasi halaman
    total_pages = (total_data + perPage - 1) // perPage
    next_page = None  # Tidak ada navigasi halaman
    previous_page = None  # Tidak ada navigasi halaman

    # Membuat URL XLS
    url_xls = "https://api.rumahzakat.org/zams5/export_to_excel/beasiswa"

    return {
        "results": results,
        "total": total_data,
        "total_pages": total_pages,
        "next_page": next_page,
        "previous_page": previous_page,
        "last_page": total_pages == 1,  # Apakah ini halaman terakhir
        "url_xls": url_xls
    }
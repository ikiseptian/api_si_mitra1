from fastapi import Depends
from config.db_connection import get_db1, get_db2, get_db3
from sqlalchemy import text

def get_laporan_beasiswa(
    db1=Depends(get_db1), 
    db2=Depends(get_db2),
    db3=Depends(get_db3)
):
    perPage = 5
    offset = 0

    try:
        query = text("""
            SELECT 
                manual_laporan.laporanid,
                manual_laporan.donatur_id,
                donatur.nama as donatur_nama,
                manual_laporan.id_anak,
                manual_laporan.pm_nama_lengkap,
                manual_laporan.pm_anak_jenjang,
                manual_laporan.semesterid,
                manual_laporan.nama_semester,
                CONCAT('https://ajis.indonesiajuara.org/sinkronisasi_transaksi_corez_ajis/detailLapsem.php?laporanid=',
                    manual_laporan.laporanid,'&id_anak=',manual_laporan.id_anak,'&semesterid=',
                    manual_laporan.semesterid,'&id_donatur=',manual_laporan.donatur_id) AS url,
                donatur.hp,
                IF(donatur.hp != '', CONCAT('https://api.whatsapp.com/send/?phone=', donatur.hp), '') AS url_whatsapp,
                COALESCE(wa_count.count, '0') as count_wa,
                COALESCE(email_count.count, '0') as count_email
            FROM manual_laporan
            JOIN donatur ON manual_laporan.donatur_id = donatur.did
            LEFT JOIN (
                SELECT laporanid, COUNT(*) as count 
                FROM log_notification 
                WHERE type = 'wa' 
                GROUP BY laporanid
            ) wa_count ON manual_laporan.laporanid = wa_count.laporanid
            LEFT JOIN (
                SELECT laporanid, COUNT(*) as count 
                FROM log_notification 
                WHERE type = 'email' 
                GROUP BY laporanid
            ) email_count ON manual_laporan.laporanid = email_count.laporanid
            WHERE manual_laporan.status_terbuat = 1
            ORDER BY manual_laporan.semesterid DESC, manual_laporan.pm_nama_lengkap ASC
            LIMIT :offset, :perPage
        """)

        result = db3.execute(query, {"offset": offset, "perPage": perPage})
        
        data_list = []
        for row in result:
            data_list.append({
                "laporanid": str(row.laporanid),
                "donatur_id": str(row.donatur_id),
                "donatur_nama": str(row.donatur_nama),
                "id_anak": str(row.id_anak),
                "pm_nama_lengkap": str(row.pm_nama_lengkap),
                "pm_anak_jenjang": str(row.pm_anak_jenjang),
                "semesterid": str(row.semesterid),
                "nama_semester": str(row.nama_semester),
                "url": str(row.url),
                "hp": str(row.hp),
                "url_whatsapp": str(row.url_whatsapp),
                "count_wa": str(row.count_wa),
                "count_email": str(row.count_email)
            })

        return data_list  # Mengembalikan langsung data_list

    except Exception as e:
        print(f"Error in get_laporan_beasiswa: {str(e)}")
        return []
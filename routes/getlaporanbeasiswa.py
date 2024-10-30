from fastapi import APIRouter, Depends
from ..controller.getlaporanbeasiswa import get_laporan_beasiswa

router = APIRouter()

@router.get("/laporan_beasiswa")
def laporan_beasiswa(data=Depends(get_laporan_beasiswa)):
    return {
        "data": [
            {
                "laporanid": data.get('laporanid', ''),
                "donatur_id": data.get('donatur_id', ''),
                "donatur_nama": data.get('donatur_nama', ''),
                "id_anak": data.get('id_anak', ''),
                "pm_nama_lengkap": data.get('pm_nama_lengkap', ''),
                "pm_anak_jenjang": data.get('pm_anak_jenjang', ''),
                "semesterid": data.get('semesterid', ''),
                "nama_semester": data.get('nama_semester', ''),
                "url": data.get('url', ''),
                "hp": data.get('hp', ''),
                "url_whatsapp": data.get('url_whatsapp', ''),
                "count_wa": data.get('count_wa', ''),
                "count_email": data.get('count_email', '')
            }
        ]
    }
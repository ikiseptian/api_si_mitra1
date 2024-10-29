from fastapi import APIRouter, Depends
from getLaporanBeasiswa.db_controller import get_laporan_beasiswa

router = APIRouter()

@router.get("/laporan_beasiswa")
def laporan_beasiswa(data=Depends(get_laporan_beasiswa)):
    return {
        "data": data['results'],
        "total": data['total'],
        "total_page": data['total_pages'],
        "next_page": data['next_page'],
        "previous_page": data['previous_page'],
        "last_page": data['last_page'],
        "url_xls": data['url_xls']
    }

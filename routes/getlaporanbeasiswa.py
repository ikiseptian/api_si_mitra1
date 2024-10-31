from fastapi import APIRouter, Depends
from controller.getlaporanbeasiswa import get_laporan_beasiswa

router = APIRouter()

@router.get("/")
def laporan_beasiswa(data=Depends(get_laporan_beasiswa)):
    return {"data": data}  # Langsung return data tanpa nested dictionary
from fastapi import FastAPI
from .routes.getlaporanbeasiswa import router as laporan_beasiswa_router
from .routes.getraportdonatur import router as raport_donatur_router
from .routes.getraport import router as raport_router
from .routes.getlistdonor import router as donaturbyiddonatur

app = FastAPI()

# Include the routers with specific prefixes for each route
app.include_router(laporan_beasiswa_router, prefix="/laporan_beasiswa")
app.include_router(raport_donatur_router, prefix="/donatur_raport")
app.include_router(raport_router, prefix="/my_raport")
app.include_router(donaturbyiddonatur, prefix="/transaksi_by_donatur_detail")
from fastapi import FastAPI
from app.routes import router as app_campaign_router  # Campaign router
from routes.getlaporanbeasiswa import router as laporan_beasiswa_router  # Laporan beasiswa router
from routes.getraportdonatur import router as raport_donatur_router  # Laporan beasiswa router
from routes.getraport import router as raport_router  # Laporan beasiswa router
from routes.getlistdonor import router as donaturbyiddonatur  # Laporan beasiswa router

app = FastAPI()

# Include the routers with specific prefixes for each route
app.include_router(app_campaign_router, prefix="/campaigns")  # Access via /campaigns endpoint
app.include_router(laporan_beasiswa_router, prefix="/laporan_beasiswa")  # Access via /laporan_beasiswa endpoint
app.include_router(raport_donatur_router, prefix="/donatur_raport")  # Access via /laporan_beasiswa endpoint
app.include_router(raport_router, prefix="/my_raport")  # Access via /laporan_beasiswa endpoint
app.include_router(donaturbyiddonatur, prefix="/transaksi_by_donatur_detail")  # Access via /laporan_beasiswa endpoint

# Run the app with `uvicorn main:app --reload`

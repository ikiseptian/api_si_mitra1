from fastapi import FastAPI
from app.routes import router as campaign_router

app = FastAPI()

# Menambahkan routing ke aplikasi utama
app.include_router(campaign_router)

# Jalankan aplikasi dengan perintah: uvicorn main:app --reload

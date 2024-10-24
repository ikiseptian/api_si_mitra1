from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.db_connection import get_db
from listmenus.db_controller import show_list_menu  # Pastikan path ini benar

app = FastAPI()
router = APIRouter()

@router.get("/list-menu/")
async def get_list_menu(id_campaign: int = None, slug: str = None, db: AsyncSession = Depends(get_db)):
    return await show_list_menu(id_campaign=id_campaign, slug=slug, db=db)

# Menambahkan router ke aplikasi FastAPI
app.include_router(router)

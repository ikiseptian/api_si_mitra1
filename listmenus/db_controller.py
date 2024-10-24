from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Campaign
import json
import datetime
from fastapi import Depends
from app.db_connection import get_db

async def show_list_menu(id_campaign: int = None, slug: str = None, db: AsyncSession = Depends(get_db)):
    # Build query
    query = select(Campaign).where(
        Campaign.id_campaign_parent == 0,

        Campaign.parent == 'y',
        Campaign.expired_date >= datetime.datetime.now()
    ).order_by(Campaign.sort.asc())  # Pastikan atribut 'sort' ada di model

    if id_campaign:
        query = query.where(Campaign.id_campaign == id_campaign)
    elif slug:
        query = query.where(Campaign.slug == slug)
    else:
        query = query.where(Campaign.note.like('%internal%'))

    result = await db.execute(query)
    programs = result.scalars().all()

    # Process notes
    for program in programs:
        if program.note:
            try:
                from xml.etree import ElementTree as ET
                note = ET.fromstring(f"<data>{program.note}</data>")
                program.shake = note.findtext('shake', '')
                program.type = note.findtext('type', '')
                program.href = note.findtext('href', '')
                program.categoryNotShow = note.findtext('categoryNotShow', '')
            except Exception:
                program.shake = ""
                program.type = ""
                program.href = ""
                program.categoryNotShow = ""

    return programs

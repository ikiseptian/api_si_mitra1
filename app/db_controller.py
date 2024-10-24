from sqlalchemy.orm import Session
from app.models import CampaignDB1, CampaignDB2
from datetime import datetime

# Fungsi untuk mengambil data dari database 1
def get_campaigns_from_db1(db: Session):
    current_time = datetime.now()
    return db.query(CampaignDB1).filter(
        CampaignDB1.active == 1,
        CampaignDB1.id_campaign_parent != 0,
        CampaignDB1.show == 1,
        CampaignDB1.parent == 'n',
        CampaignDB1.expired_date >= current_time
    ).all()

# Fungsi untuk mengambil data dari database 2
def get_campaigns_from_db2(db: Session):
    current_time = datetime.now()
    return db.query(CampaignDB2).filter(
        CampaignDB2.active == 1,
        CampaignDB2.id_campaign_parent != 0,
        CampaignDB2.show == 1,
        CampaignDB2.parent == 'n',
        CampaignDB2.expired_date >= current_time
    ).all()

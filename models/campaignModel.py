from sqlalchemy import Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class CampaignDB1(Base):
    __tablename__ = 'setting_campaign'
    __table_args__ = {'extend_existing': True}

    id_campaign = Column(Integer, primary_key=True, index=True)
    id_campaign_parent = Column(Integer)
    campaign = Column(String)
    campaign_en = Column(String)
    icon = Column(String)
    image = Column(String)
    image_en = Column(String)
    slug = Column(String)
    expired_date = Column(DateTime)
    active = Column(Integer)
    show = Column(Integer)
    parent = Column(String)

class CampaignDB2(Base):
    __tablename__ = 'setting_campaign'
    __table_args__ = {'extend_existing': True}

    id_campaign = Column(Integer, primary_key=True, index=True)
    id_campaign_parent = Column(Integer)
    campaign = Column(String)
    campaign_en = Column(String)
    icon = Column(String)
    image = Column(String)
    image_en = Column(String)
    slug = Column(String)
    expired_date = Column(DateTime)
    active = Column(Integer)
    show = Column(Integer)
    parent = Column(String)
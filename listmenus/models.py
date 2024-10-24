from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Campaign(Base):
    __tablename__ = 'campaigns'

    id_campaign = Column(Integer, primary_key=True)
    id_campaign_parent = Column(Integer)
    show = Column(Boolean)
    parent = Column(String)
    expired_date = Column(DateTime)
    note = Column(String)
    sort = Column(Integer)  # Pastikan atribut ini ada

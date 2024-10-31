from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class Karyawan(Base):
    __tablename__ = 'hcm_karyawan'  
    __table_args__ = {'schema': 'zains_rz', 'extend_existing': True}

    id_karyawan = Column(String, primary_key=True)
    karyawan = Column(String)
    email = Column(String, unique=True)
    id_kantor = Column(Integer)
    username = Column("panggilan", String)

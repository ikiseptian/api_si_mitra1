from sqlalchemy import Column, Date, Enum, Integer, String, Float, DateTime, MetaData
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

class CorezTransaksi(Base):
    __tablename__ = 'corez_transaksi'
    __table_args__ = {'schema': 'zains_rz'}

    id_transaksi = Column(String, primary_key=True)
    id_donatur = Column(String)
    id_via_bayar = Column(Integer)
    id_program = Column(String)
    quantity = Column(Integer)
    transaksi = Column(Float)
    tgl_transaksi = Column(DateTime)
    id_kantor_transaksi = Column(Integer)
    id_penghimpunan = Column(Integer)
    id_via_himpun = Column(String)
    id_cara_bayar = Column(String)
    id_crm = Column(String)
    id_claim = Column(String)
    id_position_claim = Column(String)
    approved_transaksi = Column(String)
    keterangan = Column(String)
    user_insert = Column(String)
    tgl_donasi = Column(DateTime)
    
class Karyawan(Base):
    __tablename__ = 'hcm_karyawan'  # Pastikan nama tabel sesuai
    __table_args__ = {'schema': 'zains_rz', 'extend_existing': True}

    id_karyawan = Column(String, primary_key=True)
    karyawan = Column(String)
    email = Column(String, unique=True)
    id_kantor = Column(Integer)
    username = Column("panggilan", String)
    # Hapus kolom username jika tidak ada di tabel
    
class SingleDonatur(Base):
    __tablename__ = 'corez_donatur'

    id_donatur = Column(String(20), primary_key=True, index=True)
    donatur = Column(String(50))
    hp = Column(String(30))
    email = Column(String(100))
    aktif = Column(Enum('y', 'n', 'p', 'u'))
    id_kantor = Column(String(4))
    id_jenis = Column(String(1))
    tgl_lahir = Column(Date)
    status = Column(Enum('Donatur', 'Mitra', 'UPZ', 'Kotak'))
    last_transaction = Column(Date)
    id_profiling = Column(String(1))
    whatsapp = Column(String(30))
    
    
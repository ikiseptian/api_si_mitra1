from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Contoh model untuk tabel donatur
class Donatur(Base):
    __tablename__ = "donatur"

    did = Column(Integer, primary_key=True, index=True)
    donatur_nama = Column(String(255))
    hp = Column(String(15))

    # Relasi ke laporan
    laporan = relationship("ManualLaporan", back_populates="donatur")

# Contoh model untuk tabel manual_laporan
class ManualLaporan(Base):
    __tablename__ = "manual_laporan"

    laporanid = Column(Integer, primary_key=True, index=True)
    donatur_id = Column(Integer, ForeignKey("donatur.did"))
    donatur_nama = Column(String(255))
    id_anak = Column(Integer)
    pm_nama_lengkap = Column(String(255))
    pm_anak_jenjang = Column(String(100))
    semesterid = Column(Integer)
    nama_semester = Column(String(100))
    status_terbuat = Column(Integer)

    # Relasi ke donatur
    donatur = relationship("Donatur", back_populates="laporan")

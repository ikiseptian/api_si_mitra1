from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship, foreign, remote
from app.db_connection import Base

class CorezDonatur1(Base):
    __tablename__ = 'corez_donatur'
    __table_args__ = {'extend_existing': True}

    id_crm = Column(String, primary_key=True, index=True)
    aktif = Column(String)
    id_profiling = Column(Integer)
    last_transaction = Column(Date)

    transactions = relationship(
        'CorezTransaksi',
        primaryjoin="CorezDonatur1.id_crm == foreign(CorezTransaksi.id_crm)",
        back_populates='donatur'
    )

class CorezTransaksi(Base):
    __tablename__ = 'corez_transaksi'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    id_crm = Column(String, index=True)
    approved_transaksi = Column(String)
    tgl_donasi = Column(Date)

    donatur = relationship(
        'CorezDonatur1',
        primaryjoin="foreign(CorezTransaksi.id_crm) == CorezDonatur1.id_crm",
        back_populates='transactions'
    )

class CorezTransaksiToday1(Base):
    __tablename__ = 'corez_transaksi_today'
    __table_args__ = {'extend_existing': True}

    id_crm = Column(String, primary_key=True, index=True)
    id_donatur = Column(String)
    tgl_donasi = Column(Date)
    approved_transaksi = Column(String)

    transaksi = relationship(
        'CorezTransaksi',
        primaryjoin="CorezTransaksiToday1.id_crm == foreign(CorezTransaksi.id_crm)",
        backref='today_transactions',
        viewonly=True
    )

class CorezTransaksiThisMonth(Base):
    __tablename__ = 'corez_transaksi_thismonth'
    __table_args__ = {'extend_existing': True}

    id_crm = Column(String, primary_key=True, index=True)
    id_donatur = Column(String)
    tgl_donasi = Column(Date)

    transaksi = relationship(
        'CorezTransaksi',
        primaryjoin="CorezTransaksiThisMonth.id_crm == foreign(CorezTransaksi.id_crm)",
        backref='this_month_transactions',
        viewonly=True
    )

class CorezTransaksiThisYear(Base):
    __tablename__ = 'corez_transaksi_thisyear'
    __table_args__ = {'extend_existing': True}

    id_crm = Column(String, primary_key=True, index=True)
    id_donatur = Column(String)
    tgl_donasi = Column(Date)

    transaksi = relationship(
        'CorezTransaksi',
        primaryjoin="CorezTransaksiThisYear.id_crm == foreign(CorezTransaksi.id_crm)",
        backref='this_year_transactions',
        viewonly=True
    )

class SettingTarget(Base):
    __tablename__ = 'setting_target'
    __table_args__ = {'extend_existing': True}

    id_target = Column(Integer, primary_key=True, index=True)
    jenis = Column(String)
    id_jenis = Column(String, index=True)
    tgl_target = Column(Date)
    target = Column(Float)
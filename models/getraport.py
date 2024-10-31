from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from config.db_connection import Base

class CorezDonatur1(Base):
    __tablename__ = 'corez_donatur'
    __table_args__ = {'extend_existing': True}

    id_crm = Column(String, primary_key=True, index=True)
    aktif = Column(String)
    id_profiling = Column(Integer)
    last_transaction = Column(Date)

    transactions = relationship('CorezTransaksi', back_populates='donatur')


class CorezTransaksi(Base):
    __tablename__ = 'corez_transaksi'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    id_crm = Column(String, index=True)
    id_donatur = Column(String, ForeignKey('corez_donatur.id_crm'))
    approved_transaksi = Column(String)
    tgl_donasi = Column(Date)

    donatur = relationship('CorezDonatur1', back_populates='transactions')


class CorezTransaksiToday(Base):
    __tablename__ = 'corez_transaksi_today'
    __table_args__ = {'extend_existing': True}

    id_transaksi= Column(Integer, primary_key=True)
    # id_transaksi = Column(Integer)

    @property
    def transaksi(self):
        from sqlalchemy.orm import Session
        session = Session.object_session(self)
        return session.query(CorezTransaksi).filter_by(id=self.id_transaksi).first()

    @property
    def approved_transaksi(self):
        return self.transaksi.approved_transaksi if self.transaksi else None

    @property
    def id_crm(self):
        return self.transaksi.id_crm if self.transaksi else None

    @property
    def tgl_donasi(self):
        return self.transaksi.tgl_donasi if self.transaksi else None


class CorezTransaksiThisMonth(Base):
    __tablename__ = 'corez_transaksi_thismonth'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    id_transaksi = Column(Integer)

    @property
    def transaksi(self):
        from sqlalchemy.orm import Session
        session = Session.object_session(self)
        return session.query(CorezTransaksi).filter_by(id=self.id_transaksi).first()

    @property
    def approved_transaksi(self):
        return self.transaksi.approved_transaksi if self.transaksi else None

    @property
    def id_crm(self):
        return self.transaksi.id_crm if self.transaksi else None

    @property
    def tgl_donasi(self):
        return self.transaksi.tgl_donasi if self.transaksi else None


class CorezTransaksiThisYear(Base):
    __tablename__ = 'corez_transaksi_thisyear'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    id_transaksi = Column(Integer)

    @property
    def transaksi(self):
        from sqlalchemy.orm import Session
        session = Session.object_session(self)
        return session.query(CorezTransaksi).filter_by(id=self.id_transaksi).first()

    @property
    def approved_transaksi(self):
        return self.transaksi.approved_transaksi if self.transaksi else None

    @property
    def id_crm(self):
        return self.transaksi.id_crm if self.transaksi else None

    @property
    def tgl_donasi(self):
        return self.transaksi.tgl_donasi if self.transaksi else None


class SettingTarget(Base):
    __tablename__ = 'setting_target'
    __table_args__ = {'extend_existing': True}

    jenis = Column(String, primary_key=True)
    id_jenis = Column(String, index=True)
    tgl_target = Column(Date)
    target = Column(Float)
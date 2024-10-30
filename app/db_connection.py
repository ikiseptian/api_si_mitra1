from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Membuat objek Base
Base = declarative_base()

# Koneksi ke database 1
DATABASE_URL_1 = "mysql+pymysql://tyo:BismillahAllahuAkbar!@ag.cnt.id:15116/zains_rz"
engine_db1 = create_engine(
    DATABASE_URL_1, 
    pool_size=10, 
    max_overflow=20, 
    pool_timeout=30, 
    pool_recycle=3600
)
SessionLocal_db1 = sessionmaker(autocommit=False, autoflush=False, bind=engine_db1)

# Koneksi ke database 2
DATABASE_URL_2 = "mysql+pymysql://tyo:BismillahAllahuAkbar!@ag.cnt.id:15116/rz_donasi"
engine_db2 = create_engine(
    DATABASE_URL_2, 
    pool_size=10, 
    max_overflow=20, 
    pool_timeout=30, 
    pool_recycle=3600
)
SessionLocal_db2 = sessionmaker(autocommit=False, autoflush=False, bind=engine_db2)

# Koneksi ke database 3
DATABASE_URL_3 = "mysql+pymysql://irvan_vtect:p3rmisi94n_1r4dr1@178.128.63.35:3306/sipc_ijf"
engine_db3 = create_engine(
    DATABASE_URL_3, 
    pool_size=10, 
    max_overflow=20, 
    pool_timeout=30, 
    pool_recycle=3600
)
SessionLocal_db3 = sessionmaker(autocommit=False, autoflush=False, bind=engine_db3)


def get_db1():
    db = SessionLocal_db1()
    try:
        yield db
    finally:
        db.close()

# Dependency untuk mendapatkan session database 2
def get_db2():
    db = SessionLocal_db2()
    try:
        yield db
    finally:
        db.close()

# Dependency untuk mendapatkan session database 3
def get_db3():
    db = SessionLocal_db3()
    try:
        yield db
    finally:
        db.close()

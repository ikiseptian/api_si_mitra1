from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

# Mengaktifkan logging SQLAlchemy
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Koneksi ke database 1 (zains_rz-dev)
DATABASE_URL_1 = "mysql+pymysql://tyo:BismillahAllahuAkbar!@ag.cnt.id:15116/zains_rz"

# Koneksi ke database 2 (rz_donasi-dev)
DATABASE_URL_2 = "mysql+pymysql://tyo:BismillahAllahuAkbar!@ag.cnt.id:15116/rz_donasi"

# Membuat engine dengan pooling untuk database 1
engine_db1 = create_engine(
    DATABASE_URL_1, 
    pool_size=10, 
    max_overflow=20, 
    pool_timeout=30, 
    pool_recycle=3600
)
SessionLocal_db1 = sessionmaker(autocommit=False, autoflush=False, bind=engine_db1)

# Membuat engine dengan pooling untuk database 2
engine_db2 = create_engine(
    DATABASE_URL_2, 
    pool_size=10, 
    max_overflow=20, 
    pool_timeout=30, 
    pool_recycle=3600
)
SessionLocal_db2 = sessionmaker(autocommit=False, autoflush=False, bind=engine_db2)

# Dependency untuk mendapatkan session database 1
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

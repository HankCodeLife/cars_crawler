from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@mysql:3306/cars"


MAX_RETRIES = 10
SLEEP_TIME = 5

for i in range(MAX_RETRIES):
    try:
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL
        )
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        Base = declarative_base()
        print('Mysql connect success')
        break
    except:
        print(f"Failed to connect to Mysql after {MAX_RETRIES} retries, exiting...")
        time.sleep(SLEEP_TIME)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
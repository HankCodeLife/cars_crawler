from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean, JSON

from core.database_mysql import Base

class cars_8891(Base):
    __tablename__ = "cars_8891"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_id = Column(Integer)
    data = Column(JSON)
    
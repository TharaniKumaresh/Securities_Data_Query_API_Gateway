from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class IPOData(Base):
    __tablename__ = "ipo_data"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    subscription_status = Column(String)

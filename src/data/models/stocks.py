from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime, Float

from ..database import db
from ..mixins import CRUDModel

class Stocks(CRUDModel):
    __tablename__ = 'stock'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    firma = Column(String(60), nullable=False, index=False)
    firma_zkratka = Column(String(8), nullable=False, index=True)
    jmenovite_hodnota = Column(Float, nullable=False, index=False)
    posledni_cena = Column(Float, nullable=False,default=False)
    datum_insertu= Column(DateTime)

""" SQLITE DATABASE MODELS """
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):
    """ Table Barang Object """
    __tablename__ = "products"

    id_product = Column("id", String, primary_key=True)
    product = Column("product", String)
    unit = Column("unit", String)
    qty = Column("qty", Integer)

    def __init__(self, id_product, product, unit, qty):
        self.id_product = id_product
        self.product = product
        self.unit = unit
        self.qty = qty

""" SQLITE DATABASE MODELS """
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Barang(Base):
    """ Table Barang Object """
    __tablename__ = "barang"

    id_produk = Column("id", String, primary_key=True)
    produk = Column("produk", String)
    satuan = Column("satuan", String)
    jumlah = Column("jumlah", Integer)

    def __init__(self, id_produk, produk, satuan, jumlah):
        self.id_produk = id_produk
        self.produk = produk
        self.satuan = satuan
        self.jumlah = jumlah

    def __repr__(self):
        return str({
            "id": self.id,
            "produk": self.produk,
            "satuan": self.satuan,
            "jumlah": self.jumlah
        })

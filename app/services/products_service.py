""" Products Table Service """
from nanoid import generate
from app.database.models import Products
from app.database.db import session

async def get_products():
    """ Get all products """
    result = session.query(Products).all()
    return result

async def get_product_by_id(id_product):
    """ Get product by id """
    result = session.query(Products).filter(Products.id_product == id_product).first()
    if not result:
        return {}
    return result

async def create_product(products):
    """ Add product """
    id_product = generate("1234567890", 5)
    add = Products(id_product, products.product, products.unit, products.qty)
    session.add(add)
    session.commit()
    session.refresh(add)
    return add.id_product

async def delete_product_by_id(id_product: str):
    """ Delete product """
    row_to_delete = session.query(Products).get(id_product)
    if row_to_delete:
        session.delete(row_to_delete)
        session.commit()
    
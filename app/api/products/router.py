""" Products API Router """
from fastapi import APIRouter
from app.validator.products_validator import ProductsPayload
import app.services.products_service as service

router = APIRouter()

@router.get("/")
async def get_products():
    """ Get all products """
    items = await service.get_products()
    return items

@router.get("/{id_product}")
async def get_product_by_id(id_product: str):
    """ Get product by id """
    item = await service.get_product_by_id(id_product)
    return item

@router.post("/", status_code=201, response_description="Created")
async def create_product(product: ProductsPayload):
    """ Create product """
    id_product = await service.create_product(product)
    return {"id_product": id_product}

@router.delete("/{id_product}")
async def delete_product_by_id(id_product: str):
    """ Delete product """
    await service.delete_product_by_id(id_product)

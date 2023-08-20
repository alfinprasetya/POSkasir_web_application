""" Products API Routes """
from fastapi import APIRouter
from app.database.dummy import items

router = APIRouter()

@router.get("/")
async def get_products():
    """ Implement your read logic here """
    return items

# @router.get("/{product_id}")
# async def get_product_by_id(product_id: int):
#     """ Implement your read single product logic here """
#     return {"message": f"Read product {product_id}"}
#
# @router.post("/")
# async def create_product():
#     """ Implement your create logic here """
#     return {"message": "Create new product"}
#
# @router.put("/{product_id}")
# async def update_product(product_id: int):
#     """ Implement your update logic here """
#     return {"message": f"Update product {product_id}"}
#
# @router.delete("/{product_id}")
# async def delete_product(product_id: int):
#     """ Implement your delete logic here """
#     return {"message": f"Delete product {product_id}"}#

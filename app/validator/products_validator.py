""" Products Payload Validator """
from pydantic import BaseModel

class ProductsPayload(BaseModel):
    """ Products Payload Schema """
    product: str
    unit: str
    qty: int

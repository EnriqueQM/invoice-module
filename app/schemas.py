from pydantic import BaseModel
from typing import List
from datetime import datetime

# ---------- Product ----------

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

# ---------- Customer ----------

class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        from_attributes = True

# ---------- Invoice ----------

class InvoiceBase(BaseModel):
    customer_id: int
    product_ids: List[int]

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    date: datetime
    customer: Customer
    products: List[Product]

    class Config:
        from_attributes = True
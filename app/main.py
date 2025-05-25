from fastapi import FastAPI
from app.routers import customers, products, invoices

app = FastAPI(title="Invoice API")

app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(invoices.router, prefix="/invoices", tags=["Invoices"])
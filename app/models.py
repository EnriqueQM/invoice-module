from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

# Tabla intermedia entre Invoice y Product (muchos a muchos)
invoice_product_table = Table(
    "invoice_product",
    Base.metadata,
    Column("invoice_id", ForeignKey("invoices.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True),
)

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

    invoices = relationship("Invoice", back_populates="customer")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)


class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    date = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="invoices")
    products = relationship("Product", secondary=invoice_product_table)
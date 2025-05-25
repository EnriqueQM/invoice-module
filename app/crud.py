from sqlalchemy.orm import Session
from app import models, schemas
from app.pdf_generator import generate_invoice_pdf

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_invoice(db: Session, invoice: schemas.InvoiceCreate):
    db_customer = db.query(models.Customer).filter(models.Customer.id == invoice.customer_id).first()
    db_products = db.query(models.Product).filter(models.Product.id.in_(invoice.product_ids)).all()

    db_invoice = models.Invoice(customer=db_customer, products=db_products)
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)

    # Generar PDF
    generate_invoice_pdf(db_invoice)

    return db_invoice
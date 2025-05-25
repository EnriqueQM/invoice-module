from sqlalchemy.orm import Session
from app import models, schemas
from app.pdf_generator import generate_invoice_pdf
from sqlalchemy.orm import joinedload

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
    # Obtener cliente
    db_customer = db.query(models.Customer).filter(models.Customer.id == invoice.customer_id).first()
    if not db_customer:
        raise ValueError(f"Cliente con ID {invoice.customer_id} no existe.")

    # Obtener productos
    db_products = db.query(models.Product).filter(models.Product.id.in_(invoice.product_ids)).all()
    if not db_products:
        raise ValueError("No se encontraron productos con los IDs proporcionados.")

    # Crear factura
    db_invoice = models.Invoice(customer=db_customer, products=db_products)
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)

    # Recargar la factura con relaciones (cliente y productos)
    invoice_full = db.query(models.Invoice).options(
        joinedload(models.Invoice.customer),
        joinedload(models.Invoice.products)
    ).filter(models.Invoice.id == db_invoice.id).first()

    # Generar PDF
    generate_invoice_pdf(invoice_full)

    return invoice_full
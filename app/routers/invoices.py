from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.database import SessionLocal
from app import crud, schemas, models
from app.pdf_generator import generate_invoice_pdf

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Invoice)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    # Crear la factura usando la lógica de negocio
    try:
        new_invoice = crud.create_invoice(db, invoice)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return new_invoice

@router.get("/{invoice_id}", response_model=schemas.Invoice)
def get_invoice(invoice_id: int, db: Session = Depends(get_db)):
    invoice = db.query(models.Invoice).options(
        joinedload(models.Invoice.customer),
        joinedload(models.Invoice.products)
    ).filter(models.Invoice.id == invoice_id).first()

    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    return invoice
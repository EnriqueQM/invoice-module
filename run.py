import typer
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas
from typing import List

app = typer.Typer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.command()
def create_customer(
    name: str = typer.Option(..., help="Nombre del cliente"),
    email: str = typer.Option(..., help="Email del cliente")
):
    db: Session = next(get_db())
    customer = schemas.CustomerCreate(name=name, email=email)
    result = crud.create_customer(db, customer)
    typer.echo(f"✅ Cliente creado: {result.id} - {result.name}")

@app.command()
def create_product(
    name: str = typer.Option(..., help="Nombre del producto"),
    price: float = typer.Option(..., help="Precio del producto")
):
    db: Session = next(get_db())
    product = schemas.ProductCreate(name=name, price=price)
    result = crud.create_product(db, product)
    typer.echo(f"✅ Producto creado: {result.id} - {result.name} - €{result.price:.2f}")

@app.command()
def create_invoice(
    customer_id: int = typer.Option(..., help="ID del cliente"),
    product_ids: str = typer.Option(..., help="IDs de los productos separados por coma (ej: 1,2,3)")
):
    db: Session = next(get_db())
    ids_list = [int(pid.strip()) for pid in product_ids.split(",")]
    invoice_data = schemas.InvoiceCreate(customer_id=customer_id, product_ids=ids_list)
    invoice = crud.create_invoice(db, invoice_data)
    typer.echo(f"✅ Factura {invoice.id} generada y guardada en PDF")

if __name__ == "__main__":
    app()
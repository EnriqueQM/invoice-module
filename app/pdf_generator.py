from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from app.models import Invoice
import os

def generate_invoice_pdf(invoice: Invoice, output_dir="invoices"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"invoice_{invoice.id}.pdf"
    filepath = os.path.join(output_dir, filename)

    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4

    # Encabezado
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 40, "Factura")

    c.setFont("Helvetica", 10)
    c.drawString(30, height - 60, f"Factura ID: {invoice.id}")
    c.drawString(30, height - 75, f"Fecha: {invoice.date.strftime('%Y-%m-%d %H:%M')}")
    c.drawString(30, height - 90, f"Cliente: {invoice.customer.name} ({invoice.customer.email})")

    # Productos
    c.drawString(30, height - 120, "Productos:")
    y = height - 140
    total = 0.0
    for product in invoice.products:
        c.drawString(40, y, f"- {product.name} - €{product.price:.2f}")
        y -= 15
        total += product.price

    # Total
    y -= 10
    c.drawString(30, y, f"Total: €{total:.2f}")

    c.showPage()
    c.save()

    return filepath
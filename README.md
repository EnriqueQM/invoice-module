
# 🧾 Invoice Module – Automated PDF Invoice System

This is a backend project built with FastAPI, Typer, and SQLAlchemy.  
It simulates a real business flow for generating PDF invoices, including customer and product management.

---

## 🚀 Features

- ✅ Create customers and products via API or CLI
- ✅ Generate invoices and export them as PDFs
- ✅ Store invoice records in a real SQL database
- ✅ Expose REST endpoints via FastAPI
- ✅ Interactive Swagger UI
- ✅ Business-ready project structure and logic

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **FastAPI** – API layer
- **Typer** – Command-line interface
- **SQLAlchemy** – ORM & DB models
- **SQLite** – Simple local database (can be replaced by PostgreSQL)
- **ReportLab** – PDF generation engine
- **Uvicorn** – ASGI server

---

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/EnriqueQM/invoice-module.git
cd invoice-module
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
# or
source .venv/bin/activate       # Mac/Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛢️ Initialize the Database

Create the local SQLite database and tables:

```bash
python create_db.py
```

---

## 💻 Run the FastAPI Server

Start the development server:

```bash
uvicorn app.main:app --reload
```

Then visit:

```
http://localhost:8000/docs
```

To interact with the API using Swagger UI.

---

## 🧪 Using the CLI (Optional)

This project includes a CLI powered by Typer. You can:

- Create customers and products
- Generate invoices from the terminal

Example usage:

```bash
python run.py create-customer --name "Alice" --email "alice@example.com"
python run.py create-product --name "Desk" --price 150.00
python run.py create-invoice --customer-id 1 --product-ids "1,2"
```

The PDF will be generated inside the `invoices/` folder.

---

## 📄 Sample Output

PDF invoices are saved to the `/invoices` directory and include:

- Invoice number & date
- Customer name and email
- List of products and prices
- Total amount

---

## 🧠 Business Relevance

This project simulates how real ERP systems (like Odoo) handle invoice generation.  
It showcases backend skills including:

- REST API design
- Database modeling
- Document automation
- Code organization and reusability

---

## 🧰 Future Improvements

- `GET /invoices/{id}/pdf` to download the PDF
- Add authentication (JWT)
- Replace SQLite with PostgreSQL
- Unit and integration tests
- Docker setup for deployment

---

## 👨‍💻 Author

**Enrique Quevedo**  
Backend Developer – Data & AI Enthusiast  
GitHub: [@EnriqueQM](https://github.com/EnriqueQM)

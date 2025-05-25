
# 🛠️ Debug Log – Common Issues & Fixes in the Invoice Module CLI

This file documents the main issues encountered during development of the invoice module CLI, and how each was solved.

---

## 1. `typer.Option(..., multiple=True)` – Not Working

**❌ Error:**
```
TypeError: Option() got an unexpected keyword argument 'multiple'
```

**🧠 Cause:**
Despite having `typer==0.9.0`, there was a compatibility conflict with how `List[int]` was interpreted.

**✅ Fix:**
- Replaced `multiple=True` with a comma-separated string input:
  ```bash
  --product-ids "1,2"
  ```
- Parsed manually inside the command using `split(",")` and `int()`.

---

## 2. `invoice.customer.name` caused `AttributeError`

**❌ Error:**
```
AttributeError: 'NoneType' object has no attribute 'name'
```

**🧠 Cause:**
After calling `db.refresh(db_invoice)`, SQLAlchemy did not automatically load relationships like `customer` or `products`.

**✅ Fix:**
- Performed a second query using `joinedload()` to eagerly load the related objects before generating the PDF.

---

## 3. `sqlite3.OperationalError: no such table: customers`

**❌ Error:**
```
sqlite3.OperationalError: no such table: customers
```

**🧠 Cause:**
The SQLite database (`invoices.db`) did not contain any tables. This happened after the environment was cleaned up and recreated.

**✅ Fix:**
- Ran the database initializer script (`create_db.py`) with:
  ```python
  Base.metadata.create_all(bind=engine)
  ```
- All required tables were created correctly.

---

## 4. `ValueError: Customer with ID 1 does not exist.`

**❌ Error:**
```
ValueError: Customer with ID 1 does not exist.
```

**🧠 Cause:**
The database was empty. The customer and products were not reinserted after the DB reset.

**✅ Fix:**
- Re-ran CLI commands to create a customer and products before generating the invoice.

---

## ✅ Final Result

- Database models are functional.
- CLI creates and validates entities correctly.
- PDF invoices are generated with complete relational data.
- Workflow now simulates real business logic.

from app.models import Base
from app.database import engine

print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Done.")
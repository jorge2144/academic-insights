from backend.database import SessionLocal, engine
from sqlalchemy import inspect

# Crear una sesión para comprobar la conexión
db = SessionLocal()

# Inspeccionar la base de datos
inspector = inspect(engine)
print(f"Tablas en la base de datos: {inspector.get_table_names()}")


    

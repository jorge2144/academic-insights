from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de conexión a la base de datos desde el archivo .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de conexión a la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear sesión local para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base para los modelos
Base = declarative_base()

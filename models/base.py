from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://user:password@localhost:5432/fatura"

# Créer le moteur de la base de données
engine = create_engine(DATABASE_URL)

# Créer une base déclarative pour définir les modèles
Base = declarative_base()

# Créer une fabrique de session pour interagir avec la base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

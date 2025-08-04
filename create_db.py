# Fichier create_db.py
from models.base import Base, engine

print("Création des tables de la base de données...")
Base.metadata.create_all(bind=engine)
print("Tables créées avec succès !")
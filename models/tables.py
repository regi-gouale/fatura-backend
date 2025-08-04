
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.base import Base

# Modèle pour la table 'utilisateurs'
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Définir les relations pour une meilleure navigation
    clients = relationship("Client", back_populates="owner")
    invoices = relationship("Invoice", back_populates="owner")
    expenses = relationship("Expense", back_populates="owner")

# Modèle pour la table 'clients'
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True, nullable=False)
    address = Column(String)
    email = Column(String)
    
    # Clé étrangère vers l'utilisateur
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="clients")

    invoices = relationship("Invoice", back_populates="client")

# Modèle pour la table 'factures'
class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True, nullable=False)
    issue_date = Column(DateTime, default=datetime.now)
    due_date = Column(DateTime, nullable=False)
    status = Column(String, default="Pending")
    total_amount = Column(Float(asdecimal=True), default=0.0)

    # Clés étrangères
    owner_id = Column(Integer, ForeignKey("users.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))

    # Relations
    owner = relationship("User", back_populates="invoices")
    client = relationship("Client", back_populates="invoices")
    invoice_items = relationship("InvoiceItem", back_populates="invoice")

# Modèle pour la table 'articles_facture'
class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    quantity = Column(Integer)
    unit_price = Column(Float(asdecimal=True), default=0.0)

    # Clé étrangère
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    
    # Relation
    invoice = relationship("Invoice", back_populates="invoice_items")

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    amount = Column(Float(asdecimal=True), default=0.0)
    expense_date = Column(DateTime, default=datetime.now)
    category = Column(String, nullable=False)

    # Clé étrangère
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relation
    user = relationship("User", back_populates="expenses")
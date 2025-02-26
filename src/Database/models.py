from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from Database.database import Base

class BD_Acomodacao(Base):
    __tablename__ = "accommodation"
    id_acc = Column(String,primary_key=True)
    status = Column(String)
    id_proprietario = Column(String)
    nome_acomodacao = Column(String)
    tamanho = Column(String)
    cama = Column(String)
    qtde_quartos = Column(Integer)
    qtde_banheiros = Column(Float)
    cod_pais = Column(String)
    cidade = Column(String)
    endereco = Column(String)
    bairro = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    capacidade = Column(Integer)
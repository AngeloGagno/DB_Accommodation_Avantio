# include/db.py
from __future__ import annotations

import os
from pathlib import Path
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

def load_db_string(dotenv_path: str | None = None, env_key: str = "DATABASE_URL") -> str:
    """
    Carrega o .env (se caminho for fornecido) e retorna a URI do banco.
    Lança erro claro se não encontrar.
    """
    if dotenv_path:
        load_dotenv(dotenv_path=dotenv_path, override=True)
    else:
         load_dotenv(override=True)

    db_url = os.getenv(env_key)
    if not db_url or not isinstance(db_url, str):
        raise RuntimeError(
            f"Variável {env_key} ausente. "
            "Defina-a no ambiente ou passe um dotenv_path absoluto."
        )
    return db_url

def get_engine(db_url: str | None = None, dotenv_path: str | None = None):
    """
    Cria o engine sob demanda. Se db_url não vier, tenta do .env.
    """
    if not db_url:
        db_url = load_db_string(dotenv_path=dotenv_path)
    # Parâmetros seguros para produção
    return create_engine(db_url, pool_pre_ping=True, future=True)

def get_session(db_url: str | None = None, dotenv_path: str | None = None):
    """
    Retorna uma Session aberta; o chamador é responsável por fechar.
    Prefira usar session_scope().
    """
    engine = get_engine(db_url=db_url, dotenv_path=dotenv_path)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
    return SessionLocal()

@contextmanager
def session_scope(db_url: str | None = None, dotenv_path: str | None = None):
    """
    Context manager: abre, faz commit/rollback e fecha a sessão.
    Uso:
        with session_scope(db_url) as s:
            s.add(obj)
    """
    engine = get_engine(db_url=db_url, dotenv_path=dotenv_path)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

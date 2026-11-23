import os
from pathlib import Path
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

caminho_env = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(caminho_env)

db = SQLAlchemy()


def conectar_banco(app):
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError("DATABASE_URL não foi configurada no .env")

    if database_url.startswith("postgresql://"):
        database_url = database_url.replace(
            "postgresql://",
            "postgresql+psycopg://",
            1
        )
    elif database_url.startswith("postgres://"):
        database_url = database_url.replace(
            "postgres://",
            "postgresql+psycopg://",
            1
        )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)


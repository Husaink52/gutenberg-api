from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Update the password and user if needed
DATABASE_URL = "mysql+pymysql://root:Husain%402004@localhost:3306/gutenberg"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

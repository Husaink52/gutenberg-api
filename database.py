from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Update the password and user if needed
DATABASE_URL = "mysql://root:vtuflswOKSDWDZkVytNDeqSEQWpgEWEV@interchange.proxy.rlwy.net:23585/railway"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

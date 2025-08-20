from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create engine and base
engine = create_engine("sqlite:///company.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

import argparse
import uvicorn
import os
from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from dotenv import load_dotenv
from app.routes import api_router
from app.models import Base
from app.database import initialize_db

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the FastAPI application")
    
    # Add a command-line argument to specify the mode (e.g., "test" or "production")
    parser.add_argument("--mode", help="Specify the application mode (production or test)")
    
    args = parser.parse_args()
    mode = args.mode
    env_file = f".env.{mode}"

    if not os.path.exists(env_file):
        raise Exception(f"Error: .env file for mode '{mode}' does not exist.")
    else:
        load_dotenv(env_file)
        url = URL.create(
            database="postgres",
            drivername="postgresql+psycopg2",
            host=os.getenv("DB_HOST"),
            username=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            port="5432",
        )
        engine = initialize_db(url)

        if(mode == "test"):
            # Base.metadata.drop_all(bind=engine)
            Base.metadata.create_all(bind=engine)

    uvicorn.run(app, host="0.0.0.0", port=8000)

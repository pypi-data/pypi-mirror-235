import os
import typer
from pathlib import Path
from dotenv import load_dotenv

import sys
sys.path.append('.')

load_dotenv('.env')

class DBSettings:
	
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_DB_NAME  = os.environ.get("MYSQL_DB_NAME")
    MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DB_NAME}"


class Config:
    
    APP_NAME = "sigan"
    APP_DIR = typer.get_app_dir(APP_NAME)
    APP_DIR_PATH = Path(APP_DIR)
    APP_CACHE_PATH = Path(APP_DIR) / "team_id_cache.json"
    

configs = Config()
settings = DBSettings()
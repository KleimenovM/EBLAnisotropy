# /config/settings.py
# Configuration settings for the project

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
CATALOG_DIR = DATA_DIR / "catalog_files"

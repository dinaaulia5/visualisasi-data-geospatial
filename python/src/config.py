from pathlib import Path

# Root folder python/
BASE_DIR = Path(__file__).resolve().parent.parent

# Folder data
DATA_DIR = BASE_DIR / "data"

# Raw dataset
RAW_DATA_PATH = DATA_DIR / "raw" / "covid_19_indonesia_time_series_all.csv"

# GeoJSON
GEOJSON_PATH = DATA_DIR / "geojson" / "indonesia.geojson"

# Output
OUTPUT_DIR = BASE_DIR / "output"

# 22 nya pake koordinat
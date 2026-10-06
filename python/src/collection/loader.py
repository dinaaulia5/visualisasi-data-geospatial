from pathlib import Path
import pandas as pd
import json

BASE_DIR = Path(__file__).resolve().parents[2]

DATASET_PATH = BASE_DIR / "dataset" / "covid_19_indonesia_time_series_all.csv"
GEOJSON_PATH = BASE_DIR / "geojson" / "id.json"

def load_dataset():
    """_
    Membaca dataset COVID Indonesia
    """
    
    df = pd.read_csv(DATASET_PATH)
    print("Dataset berhasil di muat")
    print(f"jumlah data {len(df)}")
    
    return df

def load_geojson():
    """
    Membaca file Geojson Indonesia
    """
    
    with open(GEOJSON_PATH, "r", encoding="utf-8") as file:
        geojson = json.load(file)
        
    print("GeoJSON berhasil dimuat")
    
    return geojson
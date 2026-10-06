from src.collection.loader import load_dataset
from src.cleaning.cleaner import clean_dataset
from src.transformation.transformer import transform_dataset
from src.analysis.analytics import analyze_dataset
from src.export.exporter import export_json


df = load_dataset()

df = clean_dataset(df)

transformed = transform_dataset(df)

result = analyze_dataset(transformed)

export_json("summary.json", result)

print("\nSemua file berhasil dibuat.")
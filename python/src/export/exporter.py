import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


def export_json(filename, data):
    """
    Export dictionary/list menjadi JSON.
    """

    file_path = OUTPUT_DIR / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"{filename} berhasil dibuat")
import pandas as pd


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Membersihkan dataset COVID-19 Indonesia.
    """

    print("=" * 60)
    print("DATA CLEANING")
    print("=" * 60)

    # =====================================================
    # 1. Missing Value
    # =====================================================

    print("\n[1] Missing Value")
    print(df.isnull().sum())

    # =====================================================
    # 2. Duplicate
    # =====================================================

    print("\n[2] Duplicate Data")
    print(df.duplicated().sum())

    # Hapus duplicate
    df = df.drop_duplicates()

    # =====================================================
    # 3. Konversi Tanggal
    # =====================================================

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    # =====================================================
    # 4. Konversi Kolom Numerik
    # =====================================================

    numeric_columns = [
        "New Cases",
        "New Deaths",
        "New Recovered",
        "Total Cases",
        "Total Deaths",
        "Total Recovered"
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # =====================================================
    # 5. Hapus Baris yang Date atau Location-nya kosong
    # =====================================================

    required_columns = []

    if "Date" in df.columns:
        required_columns.append("Date")

    if "Location" in df.columns:
        required_columns.append("Location")

    if required_columns:
        df = df.dropna(subset=required_columns)

    print("\nCleaning selesai.")

    return df
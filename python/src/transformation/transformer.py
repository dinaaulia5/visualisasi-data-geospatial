import pandas as pd

def transform_dataset(df: pd.DataFrame):
    """
    Trnasfomrasi dataset agar siap dianalisis.
    """
    
    print("=" * 60)
    print("DATA TRANSFORMATION")
    print("=" * 60)
    
    # Pisakan data nasional dan provinsi
    indonesia_df = df[df["Location"] == "Indonesia"].copy()
    
    province_df = df[df["Location Level"] == "Province"].copy()

    print(f"Data Nasional : {len(indonesia_df)}")
    print(f"Data Provinsi : {len(province_df)}")

    return {
        "indonesia": indonesia_df,
        "province": province_df
    }
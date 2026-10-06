import pandas as pd 

def analyze_dataset(data):
    """
    Melakukan Analisis dataset COVID-19 Indonesia
    """
    
    print("=" * 60)
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 60)
    
    indonesia = data["indonesia"]
    province = data["province"]
    
    # Ringkasan Naional
    latest = indonesia.sort_values("Date").iloc[-1]
    
    summary = {
        "date": latest["Date"].strftime("%Y-%m-%d"),
        "total_cases": int(latest["Total Cases"]),
        "total_deaths": int(latest["Total Deaths"]),
        "total_recovered": int(latest["Total Recovered"]),
        "total_active": int(latest["Total Active Cases"])
    }

    print("\nSummary Indonesia")
    print(summary)

    return {
        "summary": summary
    }
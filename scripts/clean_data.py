# clean_data.py
# Script to clean and preprocess the AI job dataset.

import pandas as pd

RAW_FILE = "data/ai_job_dataset_cleaned.csv"
CLEAN_FILE = "data/ai_jobs_prepared.csv"

def clean_dataset():
    df = pd.read_csv(RAW_FILE)
    df = df.drop(columns=["salary_currency", "company_location", "company_size", "company_name"], errors="ignore")
    df["required_skills"] = df["required_skills"].fillna("Not specified")
    df["education_required"] = df["education_required"].fillna("Not specified")
    df["industry"] = df["industry"].fillna("Unknown")
    df["posting_date"] = pd.to_datetime(df["posting_date"], errors="coerce")
    df["application_deadline"] = pd.to_datetime(df["application_deadline"], errors="coerce", dayfirst=True)
    df = df[df["salary_usd"] > 0]
    exp_map = {"EN": "Entry", "MI": "Mid", "SE": "Senior", "EX": "Executive"}
    df["experience_level"] = df["experience_level"].map(exp_map).fillna(df["experience_level"])
    df.to_csv(CLEAN_FILE, index=False)
    print(f"✅ Cleaned dataset saved to {CLEAN_FILE}")

if __name__ == "__main__":
    clean_dataset()

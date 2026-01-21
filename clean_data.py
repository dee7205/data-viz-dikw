import pandas as pd
import os

def clean_data():
    input_path = 'dataset/women_in_software_engineering_stats.csv'
    output_path = 'dataset/cleaned_women_stats.csv'
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    print(f"Reading {input_path}...")
    df = pd.read_csv(input_path)

    # Convert last_updated to datetime
    print("Converting dates...")
    df['last_updated'] = pd.to_datetime(df['last_updated'], format='%m/%d/%Y', errors='coerce')
    
    # Add year column
    df['year'] = df['last_updated'].dt.year

    # Drop 'team' column as per user request
    print("Dropping 'team' column...")
    df = df.drop(columns=['team'], errors='ignore')

    # Feature Engineering
    print("Engineering features...")
    
    # 1. num_male_eng
    df['num_male_eng'] = df['num_eng'] - df['num_female_eng']
    
    # 2. company_size_group
    def categorize_size(size):
        if size <= 20:
            return 'Small'
        elif size <= 100:
            return 'Medium'
        else:
            return 'Large'
            
    df['company_size_group'] = df['num_eng'].apply(categorize_size)
    
    # 3. days_since_baseline
    min_date = df['last_updated'].min()
    df['days_since_baseline'] = (df['last_updated'] - min_date).dt.days

    # Sanitize company names (strip whitespace)
    print("Sanitizing text...")
    df['company'] = df['company'].str.strip()
    
    # Save cleaned data
    print(f"Saving to {output_path}...")
    df.to_csv(output_path, index=False)
    
    # Verification stats
    print("\n--- Verification ---")
    print(f"Original shape: {pd.read_csv(input_path).shape}")
    print(f"Cleaned shape: {df.shape}")
    print(f"Missing last_updated: {df['last_updated'].isnull().sum()}")
    print(f"Unique years: {df['year'].unique()}")
    print(f"Columns: {list(df.columns)}")

if __name__ == "__main__":
    clean_data()

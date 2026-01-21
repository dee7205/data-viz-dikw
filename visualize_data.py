import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualize_data():
    input_path = 'dataset/cleaned_women_stats.csv'
    output_dir = 'visualizations'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Reading {input_path}...")
    df = pd.read_csv(input_path)

    # Set style
    sns.set_theme(style="whitegrid")

    # 1. Distribution of Female Engineer Percentage
    print("Generating distribution plot...")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['percent_female_eng'], kde=True, bins=20)
    plt.title('Distribution of Female Engineer Percentage across Companies')
    plt.xlabel('Percentage of Female Engineers')
    plt.ylabel('Count')
    plt.savefig(f'{output_dir}/dist_female_eng.png')
    plt.close()

    # 2. Top 10 Companies by Female Engineer Percentage (min 20 engineers)
    print("Generating top 10 companies plot...")
    df_filtered = df[df['num_eng'] > 20].sort_values('percent_female_eng', ascending=False).head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(data=df_filtered, x='percent_female_eng', y='company', palette='viridis')
    plt.title('Top 10 Companies by Female Engineer Percentage (min 20 engineers)')
    plt.xlabel('Percentage of Female Engineers')
    plt.ylabel('Company')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/top_10_female_eng.png')
    plt.close()

    # 3. Scatter Plot: Team Size vs. Female Percentage
    print("Generating scatter plot...")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='num_eng', y='percent_female_eng', alpha=0.6)
    plt.title('Engineering Team Size vs. Female Representation')
    plt.xlabel('Number of Engineers')
    plt.ylabel('Percentage of Female Engineers')
    plt.xscale('log') # Log scale for better visibility of skewed size data
    plt.savefig(f'{output_dir}/size_vs_percent.png')
    plt.close()

    # 4. Trend Over Years
    print("Generating trend plot...")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='year', y='percent_female_eng')
    plt.title('Female Engineer Percentage Over Years')
    plt.xlabel('Year')
    plt.ylabel('Percentage of Female Engineers')
    plt.savefig(f'{output_dir}/trend_over_years.png')
    plt.close()

    # Filter out 'ALL' aggregate for top 10 lists
    df_companies = df[df['company'] != 'ALL']

    # 5. Top 10 Companies by Number of Engineers
    print("Generating top 10 by number of engineers...")
    df_top_eng = df_companies.sort_values('num_eng', ascending=False).head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(data=df_top_eng, x='num_eng', y='company', palette='magma')
    plt.title('Top 10 Companies by Total Number of Engineers')
    plt.xlabel('Number of Engineers')
    plt.ylabel('Company')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/top_10_num_eng.png')
    plt.close()

    # 6. Top 10 Companies by Number of Female Engineers
    print("Generating top 10 by number of female engineers...")
    df_top_female = df_companies.sort_values('num_female_eng', ascending=False).head(10)
    plt.figure(figsize=(12, 8))
    sns.barplot(data=df_top_female, x='num_female_eng', y='company', palette='coolwarm')
    plt.title('Top 10 Companies by Number of Female Engineers')
    plt.xlabel('Number of Female Engineers')
    plt.ylabel('Company')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/top_10_num_female_eng.png')
    plt.close()

    # 7. Gender Gap Aggregate
    print("Generating gender gap plot...")
    total_eng = df['num_eng'].sum()
    total_female = df['num_female_eng'].sum()
    total_male = df['num_male_eng'].sum()
    
    plt.figure(figsize=(7, 7))
    plt.pie([total_male, total_female], labels=['Male', 'Female'], autopct='%1.1f%%', colors=['skyblue', 'lightpink'], startangle=90)
    plt.title(f'Overall Gender Gap (Total: {total_eng} Engineers)')
    plt.savefig(f'{output_dir}/gender_gap_aggregate.png')
    plt.close()

    # 8. Representation by Company Size
    print("Generating representation by company size...")
    plt.figure(figsize=(10, 6))
    order = ['Small', 'Medium', 'Large']
    sns.barplot(data=df, x='company_size_group', y='percent_female_eng', order=order, palette='pastel')
    plt.title('Average Female Engineer Percentage by Company Size')
    plt.xlabel('Company Size Group')
    plt.ylabel('Average % Female Engineers')
    plt.savefig(f'{output_dir}/rep_by_company_size.png')
    plt.close()

    print(f"All visualizations saved to {output_dir}/")

if __name__ == "__main__":
    visualize_data()

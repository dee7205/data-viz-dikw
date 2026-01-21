<div align="center">

# 👩‍💻 Women in Tech: A DIKW Data Analysis Project

A Data Visualization project

<br />

</div>

# 📖 Overview
The Women in Tech Data Analysis Project is a technical study conducted by Gigawin, Dave Shanna Marie E. for the course Data Visualization Activity 1.

Unlike standard reports that simply list statistics, this project utilizes the Data-Information-Knowledge-Wisdom (DIKW) framework to move from raw data points to high-level organizational wisdom. By processing global engineering datasets, we identify critical trends in gender representation, specifically focusing on how company size affects the ability to maintain a diverse workforce.

📊 1. DATA (The Foundation)

Dataset Source: Women in Tech Dataset (Kaggle).


Raw Content: 251 raw CSV rows featuring company names, update timestamps, and unorganized counts of total and female engineers.


Initial State: Unrefined records with missing "N/A" values and inconsistent date formats that required systematic cleaning.

🗂️ 2. INFORMATION (Organized Context)

Total Sample: A structured population of 31,934 engineers.


Gender Breakdown: 25,962 (81.3%) male engineers and 5,972 (18.7%) female engineers.


Market Leaders: Identification of volume-leading firms like Wells Fargo, employing over 5,000 engineers.

🧠 3. KNOWLEDGE (Patterns & Trends)

The Inverse Size Rule: Small companies lead with ~24% average female representation, while large firms trail at 13%.


Scaling Agility: Evidence suggests smaller, younger firms are more agile in diverse hiring, whereas maintaining balance becomes harder as teams scale rapidly.


Alternative Success: Public-sector organizations like the City of Los Angeles IT Agency outperform private-sector giants in female talent density.

💡 4. WISDOM (Strategic Action)
For Job Seekers & Professionals:


Prioritize Small-to-Mid Firms: Small firms offer nearly double the female representation percentage of large corporations.


Look Beyond Volume: Absolute headcount is not a proxy for diversity; evaluate internal ratios before applying.

For Industry Leaders & Recruiters:


Study Small-Scale Agility: Identify and replicate the recruitment models used by high-performing small firms.


Formalize Diversity Scaling: Implement specific protocols to prevent diversity "drift" during periods of rapid growth.

# 🛠️ Tech Stack
Programming Language: Python 3.x

Data Manipulation: Pandas

Visualization Libraries: Matplotlib, Seaborn

Development Environment: VS Code / Jupyter

⚙️ Installation & Setup
1. Clone the Repository
```
git clone https://github.com/your-username/women-in-tech-dikw.git
cd women-in-tech-dikw
```
2. Setup Data Files
Ensure the raw dataset is placed in the ```dataset/``` folder as women_in_software_engineering_stats.csv.

3. Run Cleaning & Visualization
```
python clean_data.py
python visualize_data.py
```
# 📂 Project Structure

/dataset
  ├── women_in_software_engineering_stats.csv  <-- Raw Data
  └── cleaned_women_stats.csv                  <-- Cleaned Output
/visualizations
  ├── rep_by_company_size.png                  <-- Figure 1 [cite: 58]
  ├── gender_gap_aggregate.png                 <-- Figure 2 [cite: 64]
  ├── top_10_num_eng.png                       <-- Figure 3 [cite: 82]
  └── top_10_num_female_eng.png                <-- Figure 4 [cite: 101]
clean_data.py                                  <-- ETL Logic
visualize_data.py                              <-- Chart Logic

# Women in Tech: A DIKW Data Analysis Project
This repository contains a comprehensive analysis of gender representation within the technology industry. Using the Data-Information-Knowledge-Wisdom (DIKW) framework, this project transforms raw employment statistics into actionable strategic insights.

🚀 Project Overview
The goal of this project is to analyze the relationship between company size and gender diversity in engineering roles. By processing a dataset of over 31,000 engineers, we identify key patterns in how diversity scales (or fails to scale) within the tech ecosystem.

📊 The DIKW Workflow
1. Data (The Foundation)
The project began with the Women in Tech Dataset from Kaggle, consisting of 251 raw CSV rows.


Raw State: Initially unorganized with missing "N/A" values and inconsistent date formats.

Processing: I developed clean_data.py to sanitize text, handle nulls, and engineer new features like company_size_group.

2. Information (Organized Context)
By cleaning the data, we extracted structural context answering the "Who" and "How Many":


Total Population: 31,934 Engineers.


Gender Split: 81.3% Male vs. 18.7% Female.


Industry Leaders: Identified Wells Fargo and ThoughtWorks as the highest-volume employers.

3. Knowledge (Patterns & Trends)
Analyzing the information revealed significant correlations between organizational structure and diversity:


Inverse Relationship: As shown in Figure 1, smaller companies maintain significantly higher female representation (~24%) compared to large firms (~13%).


Scaling Challenges: Data suggests that maintaining gender balance becomes increasingly difficult as teams scale rapidly.


Sector Performance: Public-sector organizations often outperform private tech giants in female-talent density.

4. Wisdom (Strategic Action)
The final layer provides actionable recommendations based on the discovered patterns:


For Job Seekers: Prioritize small-to-mid firms for better representation ratios.


For Recruiters: Study the "Small Company Agility" model to prevent diversity drift during rapid scaling.

🛠️ Tech Stack & Structure
Language: Python 3.10+

Libraries: pandas, matplotlib, seaborn

Structure:

dataset/: Contains raw and cleaned CSV files.

visualizations/: Generated PNG charts for the DIKW layers.

src/: Python scripts for automated ETL and visualization.

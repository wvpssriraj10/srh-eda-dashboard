# 🧡 SRH IPL Cricket Stats Dashboard (EDA Project)

A detailed data analysis project focused on **Sunrisers Hyderabad (SRH)**, using ball-by-ball data from the **Indian Premier League (IPL)**. This project extracts meaningful insights from raw cricket data using Python, Pandas, Matplotlib, and Seaborn.

---

## 🎯 Objective

To perform **exploratory data analysis (EDA)** on Sunrisers Hyderabad’s IPL performance across seasons — focusing on:

- Top batsmen and bowlers
- Year-wise team performance
- Wickets by dismissal type
- Opponent-wise matchups
- Economy & strike metrics

---

## 🗂️ Dataset

| Source        | Cricsheet IPL Data |
|---------------|--------------------|
| Type          | Ball-by-ball delivery-level data (CSV) |
| Scope         | 2008–2025 IPL seasons |
| Filtered For  | Matches involving Sunrisers Hyderabad (SRH) |

---

## ⚙️ Tech Stack

| Tool             | Purpose                         |
|------------------|----------------------------------|
| Python           | Data analysis & scripting        |
| Pandas           | Data manipulation                |
| Matplotlib       | Plotting graphs                  |
| Seaborn          | Statistical visualizations       |
| Jupyter / VS Code| Development environment          |

---

##📊 Key Analyses

🧡 Top 10 SRH Batsmen (by Runs)  
![Top 10 SRH Batsmen](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/top_5_batsmen.png)

🎯 Top 10 SRH Bowlers (by Wickets)  
![Top 10 SRH Bowlers](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/Figure_2.png)

📅 SRH Year-wise Total Wickets  
![Year-wise Wickets](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/Figure_3.png)

🔢 SRH Total Runs by Season  
![Total Runs by Season](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/Figure_9.png)

🤝 Top 10 SRH Batting Partnerships  
![Top Partnerships](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/Figure_8.png)

🎯 SRH Bowling vs Opponent Teams  
![Wickets by Opponent](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/Figure_5.png)

🔁 SRH Batting & Bowling vs Opponent Teams  
![Combined Batting & Bowling](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/Figure_6.png)

💥 Top 10 SRH Batsmen - Fours and Sixes  
![Most 4s and 6s](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/Figure_7.png)

💸 Top 10 Most Economical SRH Bowlers  
![Economical Bowlers](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/Figure_4.png)

---

## 📝 Summary Report

A summarized PDF version of this project is available:

📄 [SRH_EDA_Visual_Summary.pdf](https://github.com/wvpssriraj10/srh-eda-dashboard/raw/main/SRH_EDA_Visual_Summary.pdf)

---

## 🧰 How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/wvpssriraj10/srh-eda-dashboard.git
cd srh-eda-dashboard

# Step 2: Create virtual environment (optional)
python -m venv .venv
.venv\Scripts\activate  # For Windows

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the analysis
python srh_eda.py

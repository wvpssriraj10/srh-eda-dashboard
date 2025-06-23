# 🧡 SRH IPL Cricket Stats Dashboard (EDA Project)

A detailed data analysis project focused on **Sunrisers Hyderabad (SRH)**, using ball-by-ball data from the Indian Premier League (IPL). This project extracts meaningful insights from raw cricket data using **Python, Pandas, Matplotlib, and Seaborn**.

---

## 🎯 Objective

To perform exploratory data analysis (EDA) on Sunrisers Hyderabad’s IPL performance across seasons — focusing on:
- Top batsmen and bowlers
- Year-wise team performance
- Wickets by dismissal type
- Opponent-wise matchups
- Economy & strike metrics

---

## 🗂️ Dataset

- Source: [Cricsheet IPL Data](https://cricsheet.org/)
- Type: Ball-by-ball delivery-level data in CSV format
- Scope: 2008–2025 IPL seasons, filtered for matches involving SRH

---

## ⚙️ Tech Stack

| Tool           | Purpose                      |
|----------------|------------------------------|
| Python         | Data analysis & scripting    |
| Pandas         | Data manipulation            |
| Matplotlib     | Plotting graphs              |
| Seaborn        | Statistical visualizations   |
| Jupyter/VS Code| Development environment      |

---

## 📊 Key Analyses

### 🧡 Top 10 SRH Batsmen (by Runs)
![Top Batsmen](Top%2010%20SRH%20batsmens.png)

### 🎯 Top 10 SRH Bowlers (by Wickets)
![Top Bowlers](top%2010%20SRH%20bowlers.png)

### 📅 SRH Year-wise Total Wickets
![Year-wise Wickets](SRH%20year%20wise%20total%20wickets.png)

### 🔢 SRH Total Runs by Season
![Total Runs by Season](SRH%20total%20runs%20by%20season.png)

### 🤝 Top 10 SRH Batting Partnerships
![Partnerships](Top%2010%20SRH%20Batting%20Partnerships.png)

### 🎯 SRH Bowling vs Opponent Teams
![Wickets by Opponent](Total%20wickets%20taken%20by%20SRH%20bowlers%20against%20each%20team.png)

### 🔁 SRH Batting & Bowling vs Opponent Teams
![Combined](SRH%20batting%20and%20bowling%20vs%20opponent.png)

### 💥 Top 10 SRH Batsmen - Fours and Sixes
![4s and 6s](Top%2010%20SRH%20batsmen-%204's%20and%206's.png)

### 💸 Top 10 Most Economical SRH Bowlers
![Economy](Top%2010%20SRH%20most%20economical%20bowlers.png)

---

## 📝 Summary Report

A brief PDF version of this project is available:
- 📄 [`srh_eda_summary.pdf`](srh_eda_summary.pdf)

---

## 🧰 How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/wvpssriraj10/srh-eda-dashboard.git
cd srh-eda-dashboard

# Step 2: Create virtual environment (optional)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the analysis
python srh_eda.py

# 🧡 SRH IPL Cricket Stats Dashboard (EDA Project)

A detailed data analysis project focused on **Sunrisers Hyderabad** (SRH), using ball-by-ball data from the Indian Premier League (IPL). This project extracts meaningful insights from raw cricket data using Python, Pandas, Matplotlib, and Seaborn.

---

## 📌 Objective

To perform exploratory data analysis (EDA) on Sunrisers Hyderabad's IPL performance across seasons — focusing on player stats, match outcomes, and season-wise trends.

---

## 🧩 Dataset

- Source: [Cricsheet](https://cricsheet.org/)
- Format: CSV (processed from raw JSON)
- Scope: IPL matches involving Sunrisers Hyderabad (2013–2025)
- Key columns: `striker`, `bowler`, `runs_off_bat`, `player_dismissed`, `season`, `match_id`, etc.

---

## 📊 Key Visualizations

- 🔝 **Top 10 SRH Batsmen** by total runs
- 🎯 **Top 10 SRH Bowlers** by total wickets
- 📅 **Wickets per Season**
- 🧹 **Dismissal Type Breakdown**
- ⚖️ **Economy Rates** of SRH bowlers
- 🆚 **Performance vs Opponent Teams**
- 🚀 **4s and 6s Analysis**
- 🤝 **Top Batting Partnerships**
- 📈 **Total Runs by Season**
- ⚔️ **Combined Batting & Bowling vs Opponents**

All plots use team-based color palettes for clear visual distinction.

---

## ⚙️ Tech Stack

- `Python 3.x`
- `Pandas`
- `Matplotlib`
- `Seaborn`
- `NumPy`

---

## 🧼 Features

- Cleaned and standardized team names
- Custom color palettes per IPL franchise
- Readable, labeled, and publication-ready plots
- Modular and extensible code for new teams/years

---

## 🧠 Insights

- Warner, Dhawan, and Williamson lead SRH batting charts.
- Bhuvneshwar Kumar is SRH's most successful bowler.
- SRH’s bowling has been consistently strong across seasons.
- SRH has shown varied performance against different teams (e.g., more wickets vs MI, fewer vs CSK).

---

## 📁 How to Run

```bash
git clone https://github.com/your-username/srh-eda-dashboard.git
cd srh-eda-dashboard
pip install -r requirements.txt
python srh_eda.py

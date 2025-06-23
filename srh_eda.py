import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import seaborn as sns

# Team color palette mapping
team_colors = {
    'Sunrisers Hyderabad': ["#FF6F00", "#FF8F00", "#FFA000", "#FFB300",],
    'Chennai Super Kings': ["#FFF200", "#F1C40F", "#F39C12"],
    'Royal Challengers Bengaluru': ["#DA1818", "#000000"],
    'Mumbai Indians': ["#045093", "#0078D7"],
    'Kolkata Knight Riders': ["#3B215F", "#FDB913"],
    'Delhi Capitals': ["#17449B", "#D71920"],
    'Rajasthan Royals': ["#E41B89", "#2B2A29"],
    'Punjab Kings': ["#D71920", "#B2B2B2"],
    'Gujarat Titans': ["#0C2340", "#A5ACAF"],
    'Lucknow Super Giants': ["#F2A900", "#004C93"],
    'Rising Pune Supergiants': ["#5A2C83", "#FFB81C"],
    'Pune Warriors': ["#00B8F1", "#003366"],
    'Deccan Chargers': ["#A6D608", "#000000"]
}

# Load the SRH data
df = pd.read_csv('srh_data.csv', low_memory=False)
team_name_fixes = {              # Standardize team names     
    'Royal Challengers Bangalore': 'Royal Challengers Bengaluru',
    'Rising Pune Supergiant': 'Rising Pune Supergiants',
    'Delhi Daredevils': 'Delhi Capitals'
}
# Apply fixes
df['batting_team'] = df['batting_team'].replace(team_name_fixes)
df['bowling_team'] = df['bowling_team'].replace(team_name_fixes)

print("🔸 Columns:", df.columns)
print("🔸 Matches SRH involved in:", df['match_id'].nunique())

# 1. Top 10 SRH Batsmen
top_batsmen_df = df[df['batting_team'] == 'Sunrisers Hyderabad'].groupby('striker', as_index=False)['runs_off_bat'].sum()
top_batsmen_df = top_batsmen_df.sort_values(by='runs_off_bat', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_batsmen_df, x='runs_off_bat', y='striker', hue='striker', dodge=False, palette=team_colors['Sunrisers Hyderabad'])
plt.legend([],[], frameon=False)
for i in range(len(top_batsmen_df)):
    runs = top_batsmen_df['runs_off_bat'].iloc[i]
    plt.text(runs + 20, i, str(runs), va='center', fontweight='bold', color='black')
plt.title("Top 10 SRH Batsmen (by Runs)")
plt.xlabel("Runs")
plt.ylabel("Batsman")
plt.tight_layout()
plt.show()

# 2. Top 10 SRH Bowlers by Wickets
bowling_df = df[df['bowling_team'] == 'Sunrisers Hyderabad']
wickets = bowling_df[bowling_df['player_dismissed'].notna()]
top_bowlers = wickets['bowler'].value_counts().head(10)

print("\n🎯 Top 10 SRH Bowlers by Wickets:\n", top_bowlers)

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=top_bowlers.values, y=top_bowlers.index, palette='Blues_r')
for i, v in enumerate(top_bowlers.values):
    ax.text(v + 1, i, str(v), color='black', va='center', fontweight='bold')
plt.xlim(0, top_bowlers.values[0] + 10)
plt.title('Top 10 SRH Bowlers by Wickets (Cricsheet Data)')
plt.xlabel("Wickets")
plt.ylabel("Bowler")
plt.tight_layout()
plt.show()



#year-wise analysis of SRH wickets

bowling_df = df[df['bowling_team'] == 'Sunrisers Hyderabad'] # Filter for SRH bowling team
wickets = bowling_df[bowling_df['player_dismissed'].notna()] # Filter only deliveries where a dismissal occurred
wickets_by_year = wickets.groupby('season')['player_dismissed'].count() # Count wickets by season

print("\n📅 SRH Year-wise Total Wickets:\n", wickets_by_year)

# Plotting
plt.figure(figsize=(10, 5))
ax = sns.lineplot(x=wickets_by_year.index, y=wickets_by_year.values, marker='o', color='blue')
for x, y in zip(wickets_by_year.index, wickets_by_year.values):
    ax.text(x, y + 1.5, str(y), ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.title('SRH Year-wise Total Wickets ')
plt.xlabel("Season")
plt.ylabel("Wickets Taken")
plt.grid(True)
plt.tight_layout()
plt.show()

#types of dismissals by SRH bowlers

bowling_df = df[df['bowling_team'] == 'Sunrisers Hyderabad']
dismissals = bowling_df[bowling_df['player_dismissed'].notna()]
dismissal_counts = dismissals['wicket_type'].value_counts() # Count types of dismissal

print("\n🧹 Dismissal Type Breakdown:\n", dismissal_counts)

#Plotting the dismissal types

plt.figure(figsize=(10, 6))
dismissal_counts_sorted = dismissal_counts.sort_values(ascending=False)

ax = sns.barplot(x=dismissal_counts_sorted.values,
                 y=dismissal_counts_sorted.index,
                palette='Oranges_r')  

for i, v in enumerate(dismissal_counts_sorted.values):
    ax.text(v + 1, i, str(v), color='black', va='center', fontweight='bold')

plt.title('SRH Dismissal Types')
plt.xlabel("Wicket Count")
plt.ylabel("Dismissal Type")
plt.tight_layout()
plt.close()

# Top 10 Economical SRH Bowlers
srh_bowling = df[df['bowling_team'] == 'Sunrisers Hyderabad']

bowler_stats = srh_bowling.groupby('bowler').agg({     #grouping by bowler
    'ball': 'count',
    'runs_off_bat': 'sum',
    'extras': 'sum'
}).reset_index()

bowler_stats['total_runs'] = bowler_stats['runs_off_bat'] + bowler_stats['extras']  # Total runs conceded (runs + extras)
bowler_stats = bowler_stats[bowler_stats['ball'] >= 100] # Filter bowlers with min 100 balls
bowler_stats['economy'] = bowler_stats['total_runs'] / (bowler_stats['ball'] / 6) #economy rate
top_economical = bowler_stats.sort_values('economy').head(10) #sorting by economy rate

print("\n⚖️ Top 10 Economical SRH Bowlers:\n", top_economical[['bowler', 'ball', 'total_runs', 'economy']])

# plotting
plt.figure(figsize=(9, 6))
ax = sns.barplot(x='economy', y='bowler', data=top_economical, palette='Greens_r')
for i, (eco, bowler) in enumerate(zip(top_economical['economy'], top_economical['bowler'])):
    ax.text(eco + 0.05, i, f"{eco:.2f}", va='center', fontweight='bold')

plt.title('Top 10 Most Economical SRH Bowlers (min 100 balls)')
plt.xlabel('Economy Rate (Runs per Over)')
plt.ylabel('Bowler')
plt.tight_layout()
plt.show()

# SRH’s Bowling Performance vs Opponent Teams
opponent_wickets = df[(df['bowling_team'] == 'Sunrisers Hyderabad') & (df['player_dismissed'].notna())]
team_wickets = opponent_wickets.groupby('batting_team').size().sort_values(ascending=False)

print("\n🆚 SRH Wickets Taken vs Opponent Teams:\n", team_wickets)

# Assign each bar its respective team color
colors = [team_colors.get(team, ["#808080"])[0] for team in team_wickets.index]

plt.figure(figsize=(10, 6))
ax = sns.barplot(x=team_wickets.values, y=team_wickets.index, palette=colors)

for i, v in enumerate(team_wickets.values):
    ax.text(v + 2, i, str(v), va='center', fontweight='bold')

plt.title("Total Wickets Taken by SRH vs Opponent Teams")
plt.xlabel("Wickets Taken")
plt.ylabel("Opponent Team")
plt.tight_layout()
plt.show()



# Combined Batting & Bowling vs Opponent Teams
batting_df = df[df['batting_team'] == 'Sunrisers Hyderabad']
batting_vs_team = batting_df.groupby('bowling_team')['runs_off_bat'].sum()

bowling_df = df[(df['bowling_team'] == 'Sunrisers Hyderabad') & (df['player_dismissed'].notna())]
wickets_vs_team = bowling_df.groupby('batting_team').size()

combined = pd.DataFrame({
    'Runs Scored': batting_vs_team,
    'Wickets Taken': wickets_vs_team
}).fillna(0).astype(int)
combined = combined.sort_values('Runs Scored', ascending=False)

teams = combined.index
x = np.arange(len(teams))
bar_width = 0.4
bar_colors = [team_colors.get(team, ["#808080"])[0] for team in teams]

plt.figure(figsize=(12, 6))
plt.bar(x - bar_width/2, combined['Runs Scored'], width=bar_width, label='Runs Scored', color=bar_colors)
plt.bar(x + bar_width/2, combined['Wickets Taken'], width=bar_width, label='Wickets Taken', color='steelblue')

for i in range(len(teams)):
    plt.text(x[i] - bar_width/2, combined['Runs Scored'].iloc[i] + 5,
             str(combined['Runs Scored'].iloc[i]), ha='center', va='bottom', fontweight='bold')
    plt.text(x[i] + bar_width/2, combined['Wickets Taken'].iloc[i] + 2,
             str(combined['Wickets Taken'].iloc[i]), ha='center', va='bottom', fontweight='bold')

plt.xticks(x, teams, rotation=45)
plt.xlabel("Opponent Team")
plt.ylabel("Runs / Wickets")
plt.title("SRH Batting & Bowling vs Opponent Teams")
plt.legend()
plt.tight_layout()
plt.show()



# Most 4s and 6s by SRH batsmen

batting_df = df[df['batting_team'] == 'Sunrisers Hyderabad']

# Count 4s and 6s
fours = batting_df[batting_df['runs_off_bat'] == 4].groupby('striker').size()
sixes = batting_df[batting_df['runs_off_bat'] == 6].groupby('striker').size()

boundaries_df = pd.DataFrame({'4s': fours, '6s': sixes}).fillna(0).astype(int)
boundaries_df['Total'] = boundaries_df['4s'] + boundaries_df['6s']
top_boundaries = boundaries_df.sort_values('Total', ascending=False).head(10)

#Plotting
plt.figure(figsize=(12, 6))
x = np.arange(len(top_boundaries))
width = 0.35

plt.bar(x - width/2, top_boundaries['4s'], width=width, label='4s', color='orange')
plt.bar(x + width/2, top_boundaries['6s'], width=width, label='6s', color='crimson')

for i in range(len(top_boundaries)):
    plt.text(x[i] - width/2, top_boundaries['4s'].iloc[i] + 1, str(top_boundaries['4s'].iloc[i]),
             ha='center', va='bottom', fontweight='bold')
    plt.text(x[i] + width/2, top_boundaries['6s'].iloc[i] + 1, str(top_boundaries['6s'].iloc[i]),
             ha='center', va='bottom', fontweight='bold')

plt.xticks(x, top_boundaries.index, rotation=45)
plt.title("Top 10 SRH Batsmen - Most 4s and 6s")
plt.xlabel("Batsman")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()
plt.show()


#top srh partnerships


batting_df = df[df['batting_team'] == 'Sunrisers Hyderabad']

batting_df['pair'] = batting_df.apply( # Create a combined key for striker + non-striker
    lambda row: tuple(sorted([row['striker'], row['non_striker']])), axis=1)

partnerships = batting_df.groupby(['match_id', 'pair'])['runs_off_bat'].sum().reset_index() # Group by match and pair
top_partnerships = partnerships.groupby('pair')['runs_off_bat'].sum().sort_values(ascending=False).head(10) # Group again to get total partnerships (across matches)
top_partnerships = top_partnerships.reset_index() # Convert to readable format
top_partnerships['pair'] = top_partnerships['pair'].apply(lambda x: f"{x[0]} & {x[1]}")

print("\n🤝 Top 10 SRH Batting Partnerships (Total Runs Across Matches):\n")
print(top_partnerships)

#Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='runs_off_bat', y='pair', data=top_partnerships, palette='YlOrBr')

for i, v in enumerate(top_partnerships['runs_off_bat']):
    plt.text(v + 5, i, str(v), va='center', fontweight='bold')

plt.title("Top 10 SRH Batting Partnerships (Combined Across Matches)")
plt.xlabel("Total Runs Together")
plt.ylabel("Batting Pair")
plt.tight_layout()
plt.show()


#SRH Total Runs by Season

df['season'] = df['season'].astype(str).str.strip()

srh_batting_df = df[df['batting_team'] == 'Sunrisers Hyderabad']

season_total = srh_batting_df.groupby('season')['runs_off_bat'].sum().sort_index()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(season_total.index, season_total.values, marker='o', color='orange', linewidth=2)

for i, val in enumerate(season_total.values):
    plt.text(season_total.index[i], val + 40, str(val), ha='center', fontsize=9, fontweight='bold')

plt.title("SRH Total Runs by Season", fontsize=14)
plt.xlabel("Season")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

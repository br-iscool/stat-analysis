import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
try:
    df = pd.read_csv("england-premier-league-2018-to-2019.csv")
except FileNotFoundError:
    print(f"Error: file not found.")
    exit()

# Get total goals and sort
home_goals = df.groupby("HomeTeam")["FTHG"].sum()
away_goals = df.groupby("AwayTeam")["FTAG"].sum()
teams = sorted(set(home_goals.index) | set(away_goals.index))

# Calculate percentages
home_goals_percentage = []
away_goals_percentage = []

for team in teams:
    home = home_goals.get(team, 0)
    away = away_goals.get(team, 0)
    total = home + away
    
    home_goals_percentage.append((home / total) * 100)
    away_goals_percentage.append((away / total) * 100)

# Plot bar graph
plt.figure(figsize=(12, 6), layout="constrained")

plt.bar(teams, home_goals_percentage, color="orange", alpha=0.7, label="Home Goals (%)")
plt.bar(teams, away_goals_percentage, color="blue", alpha=0.5, label="Away Goals (%)", bottom=home_goals_percentage)

plt.xlabel("Teams")
plt.ylabel("Percentage of Goals (%)")
plt.title("Percentage of Home Goals vs. Away Goals (EPL 2018/19)")
plt.legend()
plt.xticks(rotation=45)

plt.show()

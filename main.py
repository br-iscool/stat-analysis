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

# Get list of total goals
home_goals_list = []
for team in teams:
    home_goals_list.append(home_goals.get(team, 0))
home_goals = home_goals_list

away_goals_list = []
for team in teams:
    away_goals_list.append(away_goals.get(team, 0))
away_goals = away_goals_list

# Plot bar graph
plt.figure(figsize=(12, 6))

plt.bar(teams, home_goals, color="orange", alpha=0.7, label="Home Goals")
plt.bar(teams, away_goals, color="blue", alpha=0.5, label="Away Goals", bottom=home_goals)

plt.xlabel("Teams")
plt.ylabel("Total Goals")
plt.title("Home Goals vs. Away Goals (EPL 2018/19)")
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


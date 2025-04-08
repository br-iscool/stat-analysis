import matplotlib.pyplot as plt
import pandas as pd

try:
    df = pd.read_csv("ufc/ufc-master.csv")
except FileNotFoundError:
    print("Error: File not found")
    exit()
    
finishes = df["Finish"].str.upper().str.strip()

ko_finishes = df[finishes.str.contains("KO", na=False)].dropna(subset=["FinishRound"])
ko_finishes["FinishRound"] = pd.to_numeric(ko_finishes["FinishRound"]).dropna().astype(int)

total_kos = ko_finishes["FinishRound"].value_counts()

plt.figure(figsize=(10, 6), layout="constrained")
plt.bar(total_kos.index, total_kos.values, color="tomato")
plt.xlabel("Round")
plt.ylabel("Number of KOs / TKOs")
plt.title("Average Number of KOs / TKOs per Round (Mid-2010 - Present)")
plt.show()
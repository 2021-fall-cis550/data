import pandas as pd
from collections import defaultdict

df = pd.read_csv("~/Downloads/players.txt")

# does playerID -> retroID?
my_dict1 = defaultdict(set)
for indx, row in df.iterrows():
    my_dict1[row["playerID"]].add(row["retroID"])

for k, v in my_dict1.items():
    if len(v) != 1:
        print(f"{k}:= {v}")

# does retroID -> playerID?
my_dict2 = defaultdict(set)
for indx, row in df.iterrows():
    my_dict2[row["retroID"]].add(row["playerID"])

for k, v in my_dict2.items():
    if len(v) != 1:
        print(f"{k}:= {v}")

# none of playerID and retroID match

my_dict3 = dict()
for indx, row in df.iterrows():
    my_dict3[row["playerID"]] = row["retroID"]

import pandas as pd
from collections import defaultdict as dict

df = pd.read_csv("~/Downloads/teams.txt")

print("# does teamIDretro -> teamID?")
my_dict1 = dict(set)
for indx, row in df.iterrows():
    my_dict1[row["teamIDretro"]].add(row["teamID"])

for k, v in my_dict1.items():
    if len(v) != 1:
        print(f"{k}:= {v}")

print("# does teamID -> teamIDretro?")
my_dict2 = dict(set)
for indx, row in df.iterrows():
    my_dict2[row["teamID"]].add(row["teamIDretro"])

for k, v in my_dict2.items():
    if len(v) != 1:
        print(f"{k}:= {v}")

# # does teamID -> name?
# my_dict3 = dict(set)
# for indx, row in df.iterrows():
#     my_dict3[row["teamID"]].add(row["name"])
#
# for k, v in my_dict3.items():
#     if len(v) != 1:
#         print(f"{k}:= {v}")

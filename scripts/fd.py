from collections import defaultdict as ddict
import pandas as pd

# Helper functions for functional dependencies.

# Print violation of functional dependencies.
def print_fd(deps, key, dep):
    print(key, dep, sep="\t")
    for k, v in deps.items():
        if len(v) > 1:
            print(f"{k}:=\t{v}")

# Extract the functional dependencies from the dataframe.
def fd(pdf, key, dep):
    dets = ddict(set)
    pdf.apply(lambda x: dets[x[key]].add(x[dep]), axis=1)
    print_fd(dets, key, dep)
    return dets

# Replace based on functional dependencies.
def replace_fd(pdf, index, key, rmap):
    if pdf.loc[index, key] in rmap:
        pdf.loc[index, key] = rmap[pdf.loc[index, key]]

def load_fd_rMap(fd_file):
    df = pd.read_csv(fd_file)
    k1, k2 = tuple(df.keys())
    rMap = {
        row[k1]: row[k2] for _, row in df.iterrows()
    }
    return k1, k2, rMap
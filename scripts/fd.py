from collections import defaultdict as ddict
import pandas as pd

# Helper functions for functional dependencies.

def print_fd(deps, key, dep):
    """
    Print violation of functional dependencies.

    :param deps: The functional dependencies as a dictionary of sets.
    """
    print(key, dep, sep="\t")
    for k, v in deps.items():
        if len(v) > 1:
            print(f"{k}:=\t{v}")

# Extract the functional dependencies from the dataframe.
def fd(pdf, key, dep):
    """
    Is the functional dependency key -> dep satisfied?

    If staisfied the print out is empty,
    otherwise the violation is printed.
    """
    dets = ddict(set)
    pdf.apply(lambda x: dets[x[key]].add(x[dep]), axis=1)
    print_fd(dets, key, dep)
    return dets

# Replace based on functional dependencies.
def replace_fd(pdf, index, key, rmap):
    """
    Replace a column corresponding to key with the value in rmap.

    Example:
    >>> # Replace all occurrences of 1 with "a" and 2 with "b" in the column A.
    >>> for index in df.index:
    ...     replace_fd(df, index, "A", {1: "a", 2: "b"})
    """
    if pdf.loc[index, key] in rmap:
        pdf.loc[index, key] = rmap[pdf.loc[index, key]]

def load_fd_rMap(fd_file):
    """
    Load the functional dependencies from the file.

    Example:
    >>> # Load the functional dependencies playerID -> ID.
    >>> fd_rMap = load_fd_rMap("playerID.csv")
    >>> # Replace playerID with ID.
    >>> for index in df.index:
    ...     replace_fd(df, index, "playerID", fd_rMap)
    """
    df = pd.read_csv(fd_file)
    k1, k2 = tuple(df.keys())
    rMap = {
        row[k1]: row[k2] for _, row in df.iterrows()
    }
    return k1, k2, rMap
"""
Vendor seaborn's example datasets into csv_data/ as plain CSV files.

Why: seaborn's sns.load_dataset() downloads from GitHub at call time. That
requires a live internet connection and can break if the upstream repository
moves. Saving local copies makes the course materials reproducible, and lets
collaborators work with the data offline.

Run once from the course repo:

    python csv_data/fetch_seaborn_datasets.py

Add dataset names to DATASETS as the course needs them. The full list of
available names is printed by seaborn.get_dataset_names().
"""

import os
import seaborn as sns

DATASETS = [
    "titanic",    # Modules 1-2 homework: nominal/ordinal/ratio, plus missing data
    "diamonds",   # Module 2: clean ordinal scales (cut, clarity)
    "penguins",   # Module 2 lecture notes
    "mpg",        # spare: interval trap (model_year), nominal origin
    "tips",       # spare: small and tidy
]

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    for name in DATASETS:
        out = os.path.join(HERE, name + ".csv")
        if os.path.exists(out):
            print("skip (already present):", os.path.basename(out))
            continue
        try:
            df = sns.load_dataset(name)
        except Exception as exc:
            print("FAILED", name, "->", exc)
            continue
        df.to_csv(out, index=False)
        print("saved {:<14} {:>6} rows x {:>2} cols".format(
            os.path.basename(out), df.shape[0], df.shape[1]))


if __name__ == "__main__":
    main()

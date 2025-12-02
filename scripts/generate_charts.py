
import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_DIR = "data"
CHART_DIR = "charts"

os.makedirs(CHART_DIR, exist_ok=True)

def generate_chart(subject_file):
    subject_name = subject_file.replace(".csv", "")
    path = os.path.join(DATA_DIR, subject_file)

    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["score"], marker='o')
    plt.title(f"{subject_name.capitalize()} Score Trend")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    out_path = os.path.join(CHART_DIR, f"{subject_name}.png")
    plt.savefig(out_path)
    plt.close()

    print(f"Generated {out_path}")

def main():
    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            generate_chart(file)

if __name__ == "__main__":
    main()

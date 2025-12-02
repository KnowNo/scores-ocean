import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_DIR = "data"
CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)

def generate_chart(subject_file):
    subject_name = subject_file.replace(".csv", "")
    path = os.path.join(DATA_DIR, subject_file)

    if os.path.getsize(path) == 0:
        print(f"⚠️ Skip {subject_file} (empty file)")
        return

    df = pd.read_csv(path)
    if df.empty or "score" not in df.columns:
        print(f"⚠️ Skip {subject_file} (no data)")
        return

    plt.figure(figsize=(10, 5))

    # 主科目线
    plt.plot(df["date"], df["score"], marker="o", label=subject_name)

    # 平均分红色虚线
    if "Average" in df.columns:
        plt.plot(df["date"], df["Average"], linestyle="--", marker="x", color="red", label="Average")

    plt.title(f"{subject_name.capitalize()} Score Trend with Average")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.grid(True)
    plt.xticks(rotation=30)
    plt.legend()
    plt.tight_layout()

    plt.savefig(os.path.join(CHART_DIR, f"{subject_name}.png"))
    plt.close()

    print(f"✅ Generated {subject_name}.png")

def main():
    for file in os.listdir(DATA_DIR):
        if file.endswith(".csv"):
            generate_chart(file)

if __name__ == "__main__":
    main()

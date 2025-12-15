import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. LOAD JSON DATA
# -----------------------------
with open("meta_analysis_data.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# -----------------------------
# 2. CLEAN DATA
# -----------------------------
# Keep only rows with valid contaminant, value, and target
df = df.dropna(subset=["value of contaminant", "target value"])

# Convert numeric columns
df["value of contaminant"] = pd.to_numeric(df["value of contaminant"], errors="coerce")
df["target value"] = pd.to_numeric(df["target value"], errors="coerce")

df = df.dropna(subset=["value of contaminant", "target value"])

# -----------------------------
# 3. COMPUTE EFFECT SIZE (RQ)
# -----------------------------
df["RQ"] = df["value of contaminant"] / df["target value"]

# Log-transform for meta-analysis stability
df["log_RQ"] = np.log(df["RQ"])

# -----------------------------
# 4. META-ANALYSIS BY CONTAMINANT
# -----------------------------
results = (
    df.groupby("contaminant of concern (inorganic)")["log_RQ"]
    .agg(["mean", "std", "count"])
    .reset_index()
)

results["effect_size"] = np.exp(results["mean"])  # back-transform
results["ci_lower"] = np.exp(results["mean"] - 1.96 * (results["std"] / np.sqrt(results["count"])))
results["ci_upper"] = np.exp(results["mean"] + 1.96 * (results["std"] / np.sqrt(results["count"])))

print("\n=== META-ANALYSIS RESULTS ===")
print(results)

# -----------------------------
# 5. FOREST PLOT
# -----------------------------
plt.figure(figsize=(8, 12))

y_pos = range(len(results))

plt.errorbar(
    results["effect_size"],
    y_pos,
    xerr=[results["effect_size"] - results["ci_lower"],
          results["ci_upper"] - results["effect_size"]],
    fmt="o"
)

plt.yticks(y_pos, results["contaminant of concern (inorganic)"])
plt.xlabel("Risk Quotient (RQ) — Meta-Analytic Effect Size")
plt.title("Meta-analysis of Ecological Risk of Contaminants")
plt.grid(True)

plt.show()

# -----------------------------
# 6. SAVE OUTPUT
# -----------------------------
results.to_csv("meta_analysis_results.csv", index=False)

print("\nSaved results to meta_analysis_results.csv")


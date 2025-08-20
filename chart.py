import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic seasonal revenue data
np.random.seed(42)
months = pd.date_range(start="2023-01-01", periods=12, freq="M").strftime("%b")
revenue = (
    50000
    + 10000 * np.sin(np.linspace(0, 2 * np.pi, 12))  # seasonal pattern
    + np.random.normal(0, 3000, 12)  # random variation
)

data = pd.DataFrame({"Month": months, "Revenue": revenue})

# Create lineplot
plt.figure(figsize=(8, 8), dpi=64)  # ensures 512x512 pixels
sns.lineplot(data=data, x="Month", y="Revenue", marker="o", linewidth=2.5, color="teal")

# Add titles and labels
plt.title("Seasonal Revenue Trends (Synthetic Data)", fontsize=16, pad=20)
plt.xlabel("Month")
plt.ylabel("Revenue (USD)")
plt.xticks(rotation=45)

# Save chart as EXACT 512x512 PNG
plt.savefig("chart.png", dpi=64, bbox_inches=None, pad_inches=0)
plt.close()

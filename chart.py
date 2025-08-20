import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set professional Seaborn style and context
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Generate realistic synthetic data for customer engagement
# Assumptions:
# - Rows: Days of the week
# - Columns: Hours of the day (0-23)
# - Values: Engagement score (0-100) representing relative activity
np.random.seed(42)
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
hours = [f"{h:02d}:00" for h in range(24)]

# Base pattern: higher engagement during working hours and evening peaks on weekends
base = np.zeros((7, 24))
for i in range(7):
    for h in range(24):
        # daytime activity
        day_factor = 20 + 50 * np.exp(-((h - 14) ** 2) / 40)
        # morning bump
        morning = 15 * np.exp(-((h - 9) ** 2) / 6)
        # weekend lift
        weekend = 1.3 if i >= 5 else 1.0
        base[i, h] = (day_factor + morning) * weekend

# Add variety per day and noise to simulate realistic variation
day_offsets = np.array([0.9, 1.0, 1.0, 1.05, 1.15, 1.25, 1.2])[:, None]
noise = np.random.normal(loc=0.0, scale=6.0, size=base.shape)
engagement = np.clip(base * day_offsets + noise, 0, 100)

# Convert to DataFrame
df = pd.DataFrame(engagement, index=days, columns=hours)

# Create heatmap
plt.figure(figsize=(8, 8))  # This combined with dpi=64 will create 512x512 PNG

cmap = sns.color_palette("rocket_r", as_cmap=True)
sns.heatmap(df, cmap=cmap, linewidths=0.5, linecolor="#ffffff",
            cbar_kws={"label": "Engagement Score"}, fmt=".0f")

plt.title("Customer Engagement by Day and Hour", pad=16, fontsize=16)
plt.ylabel("Day of Week")
plt.xlabel("Hour of Day")

# Enhance axis label readability
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)

# Save at 512x512 pixels: figsize(8,8) with dpi=64 -> 8*64=512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

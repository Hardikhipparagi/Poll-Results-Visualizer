import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Synthetic dataset
data = {
    "Timestamp": pd.date_range("2024-04-01", periods=20, freq="h"),  # lowercase h
    "Age Group": np.random.choice(["18-24", "25-34", "35-44"], 20),
    "Gender": np.random.choice(["Male", "Female"], 20),
    "Preferred Tool": np.random.choice(["Python", "R", "Excel"], 20),
    "Satisfaction (1-5)": np.random.randint(1, 6, 20),
    "Feedback": np.random.choice(["Great tool!", "Needs improvement", "Very useful"], 20)
}
df = pd.DataFrame(data)

# Save cleaned dataset
df.to_csv("data/cleaned_poll_data.csv", index=False)

# Analysis
tool_counts = df['Preferred Tool'].value_counts(normalize=True) * 100
print("Tool Preference (%):\n", tool_counts)

# Visualization
plt.figure(figsize=(6,4))
sns.countplot(x='Preferred Tool', data=df, palette='Set2', hue=None, legend=False)  # fixed
plt.title("Tool Preference")
plt.show()

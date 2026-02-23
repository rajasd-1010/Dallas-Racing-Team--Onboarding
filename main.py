import pandas as pd
import matplotlib.pyplot as plt

# 1. load data
df = pd.read_csv('data.csv')

# 2. find and remove dead sensor columns (Analog Input columns only)

analog_cols = [col for col in df.columns if 'Analog Input' in col]
dead_cols = [col for col in analog_cols if df[col].nunique() == 1]
df = df.drop(columns=dead_cols)
print(f"Removed {len(dead_cols)} dead sensor(s): {dead_cols}")

# 3. graph RPM and TPS
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))

ax1.plot(df['RPM'], color='red')
ax1.set_title('RPM Over Time')
ax1.set_ylabel('RPM')

ax2.plot(df['TPS'], color='blue')
ax2.set_title('TPS Over Time')
ax2.set_ylabel('TPS')

plt.tight_layout()
plt.savefig('output.png')  # saves the graph as an image
plt.show()

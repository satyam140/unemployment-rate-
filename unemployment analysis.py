import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('unemployment.csv')

# Clean column names (remove extra spaces and rename for easier access)
df.columns = df.columns.str.strip()
df = df.loc[:, ~df.columns.duplicated()]  # Remove duplicate 'Region' if present

# Rename long column names for convenience
df.rename(columns={
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Participation_Rate'
}, inplace=True)

# Print column names to debug
print("Available columns:", df.columns.tolist())

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Show basic info
print("Dataset Overview:")
print(df.head())

print("\nData Summary:")
print(df.describe())

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Unemployment trend over time (overall)
plt.figure(figsize=(10, 5))
sns.lineplot(x='Date', y='Unemployment_Rate', data=df)
plt.title("Unemployment Rate Over Time (Overall)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Region-wise unemployment trend
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Unemployment_Rate', hue='Region', data=df)
plt.title("Unemployment Rate Over Time by Region")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.legend(title='Region')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Average unemployment per region
avg_unemployment = df.groupby('Region')['Unemployment_Rate'].mean().sort_values()

plt.figure(figsize=(10, 5))
sns.barplot(x=avg_unemployment.index, y=avg_unemployment.values, palette='viridis')
plt.title("Average Unemployment Rate by Region")
plt.ylabel("Average Rate (%)")
plt.xlabel("Region")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory (update path)
os.chdir("Practical 10")  

print(os.getcwd())  # Verify location
print(os.listdir())  # Check if 'dalys-rate-from-all-causes.csv' exists

# Load data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")


print(dalys_data.head(5))  

# Get dataframe info (column types, non-null counts)
dalys_data.info()  

# Summary statistics
print(dalys_data.describe())  

# Select specific cells with iloc (row 0, column 3)
print(dalys_data.iloc[0, 3])  

# Show years for first 10 rows (column index 2)
print(dalys_data.iloc[0:10, 2])  

# Boolean indexing for 1990 data
is_1990 = dalys_data['Year'] == 1990
print(dalys_data.loc[is_1990, 'DALYs'])  

# Extract UK and France data
uk = dalys_data[dalys_data['Entity'] == 'United Kingdom']
france = dalys_data[dalys_data['Entity'] == 'France']

# Compare mean DALYs
uk_mean = uk['DALYs'].mean()
fr_mean = france['DALYs'].mean()
print(f"UK mean DALYs: {uk_mean}, France: {fr_mean}")
print("The UK mean is larger than the French mean")

uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']
print(uk_data.head())  # Verify the filtered data
plt.figure(figsize=(10, 6))  # Set figure size

# Plot UK DALYs
plt.plot(uk_data['Year'], uk_data['DALYs'], 
         marker='s',          # Square markers
         linestyle='--',      # Dashed line
         color='royalblue',   # Line color
         label='UK DALYs')

# Customize the plot
plt.title('DALYs in the United Kingdom (1990–2019)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('DALYs per 100,000', fontsize=12)
plt.xticks(uk_data['Year'], rotation=45)  # Rotate x-axis labels
plt.grid(True, linestyle=':', alpha=0.5)  # Add dotted gridlines
plt.legend()

# Save the plot
plt.savefig('uk_dalys.png', dpi=300, bbox_inches='tight')  # High-resolution output
plt.show()  # Display the plot

# Group data by Year and calculate mean DALYs globally
global_dalys = dalys_data.groupby('Year')['DALYs'].mean().reset_index()
print(global_dalys.head())  # Check aggregated data
plt.figure(figsize=(10, 6))  # Set figure size
plt.plot(global_dalys['Year'], global_dalys['DALYs'], 
         marker='o',  # Add markers to data points
         linestyle='-',  # Solid line
         color='green',  # Line color
         label='Global Mean DALYs')

# Customize the plot
plt.title('Global DALYs Over Time (1990–2019)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('DALYs per 100,000', fontsize=12)
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.grid(True, linestyle='--', alpha=0.6)  # Add gridlines
plt.legend()  # Show legend

# Save the plot as a PNG file
plt.savefig('global_dalys.png', dpi=300, bbox_inches='tight')  # High-resolution output
plt.show()  # Display the plot
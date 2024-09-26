# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Iris dataset
file_path = r"C:\Users\PC\Downloads\archive\iris.csv"  # Update this to your file path
df = pd.read_csv(file_path)

# Step 2: Basic Exploratory Data Analysis (EDA)
print("First 7 rows of the dataset:")
print(df.head(7))  # Display 7 rows

print("\nSummary statistics of the dataset:")
print(df.describe())

# Step 3: Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Step 4: Scatter plot of Sepal Length vs Sepal Width
plt.figure(figsize=(8, 6))
plt.scatter(df['SepalLengthCm'], df['SepalWidthCm'], color='blue', alpha=0.7)
plt.xlabel('Sepal Length (cm)', fontsize=12)
plt.ylabel('Sepal Width (cm)', fontsize=12)
plt.title('Scatter Plot of Sepal Length vs Sepal Width', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Step 5: Count plot of different species
plt.figure(figsize=(8, 6))
df['Species'].value_counts().plot(kind='bar', color='purple', alpha=0.7)
plt.title('Count of Different Iris Species', fontsize=14)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
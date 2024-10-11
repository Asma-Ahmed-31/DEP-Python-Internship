# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\PC\OneDrive\Desktop\student-por.csv"
data = pd.read_csv(file_path)

# Preview the dataset
print(data.head())

# Check available columns in the dataset
print(data.columns)

# 1. Bar Plot - Count of students by sex (gender)
plt.figure(figsize=(6, 4))
sns.countplot(x='sex', data=data)  # Changed 'gender' to 'sex'
plt.title('Count of Students by Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()

# ---------------------------------------
# 2. Pie Chart - Distribution of family support (famsup) instead of 'lunch'
# ---------------------------------------
famsup_counts = data['famsup'].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(famsup_counts, labels=famsup_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
plt.title('Distribution of Family Support')
plt.show()

# ---------------------------------------
# 3. Dot Plot - Math scores by gender
# ---------------------------------------
plt.figure(figsize=(8, 4))
sns.stripplot(x='sex', y='G3', data=data, jitter=True, palette='Set1')  # Use final grades (G3) as a proxy for math scores
plt.title('Distribution of Final Grades by Gender')
plt.xlabel('Gender')
plt.ylabel('Final Grade (G3)')
plt.show()

# ---------------------------------------
# 4. Bar Plot - Parental level of education distribution
# ---------------------------------------
plt.figure(figsize=(10, 6))
sns.countplot(y='Medu', data=data, palette='muted')  # Using 'Medu' for mother's education level
plt.title('Distribution of Mother\'s Education Level')
plt.xlabel('Count')
plt.ylabel('Mother\'s Education Level')
plt.show()

# ---------------------------------------
# 5. Bar Plot - Test preparation course completion rate
# ---------------------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='schoolsup', data=data, palette='Set2')  # Use 'schoolsup' (school support) as a substitute for test prep
plt.title('School Support Completion')
plt.xlabel('School Support')
plt.ylabel('Count')
plt.show()


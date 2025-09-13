import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("dark_background")

df = pd.read_csv(r"C:\Users\USER\OneDrive\New folder\2019_nC0v_20200121_20200126 - SUMMARY.csv")

print("Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Columns and data types:\n", df.dtypes)

for col in df.columns:
    print(f"Unique values in {col}: {df[col].nunique()}")

cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    print(f"\nValue counts for {col}:\n", df[col].value_counts())

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_cols:
    plt.figure(figsize=(6, 3))
    sns.histplot(df[col].dropna(), kde=True, color="steelblue")
    plt.title(f'Distribution of {col}')
    plt.show()

for col in num_cols:
    plt.figure(figsize=(6, 3))
    sns.boxplot(x=df[col].dropna(), color="tomato")
    plt.title(f'Boxplot of {col}')
    plt.show()

for col in cat_cols:
    plt.figure(figsize=(6, 3))
    sns.countplot(data=df, x=col, color="seagreen")
    plt.title(f'Countplot of {col}')
    plt.xticks(rotation=45)
    plt.show()

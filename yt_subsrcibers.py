import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("dark_background")
youtube_red = "#FF0000"
youtube_gray = "#AAAAAA"
youtube_white = "#FFFFFF"

df = pd.read_csv(r"C:\Users\USER\OneDrive\New folder\New folder\netflx\topSubscribed.csv")

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
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Reds", cbar_kws={'label': 'Correlation'})
plt.title("📊 YouTube Channel Metrics Correlation", color=youtube_white, fontsize=14)
plt.show()

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    plt.figure(figsize=(6, 3))
    sns.histplot(df[col].dropna(), kde=True, color=youtube_red)
    plt.title(f'📈 Distribution of {col}', color=youtube_white, fontsize=12)
    plt.xlabel(col, color=youtube_gray)
    plt.ylabel("Frequency", color=youtube_gray)
    plt.show()

for col in num_cols:
    plt.figure(figsize=(6, 3))
    sns.boxplot(x=df[col].dropna(), color=youtube_red)
    plt.title(f'🎬 Spread of {col}', color=youtube_white, fontsize=12)
    plt.xlabel(col, color=youtube_gray)
    plt.show()

for col in cat_cols:
    plt.figure(figsize=(6, 3))
    sns.countplot(data=df, x=col, color=youtube_red)
    plt.title(f'🔥 Content Count by {col}', color=youtube_white, fontsize=12)
    plt.xlabel(col, color=youtube_gray)
    plt.ylabel("Count", color=youtube_gray)
    plt.xticks(rotation=45, color=youtube_white)
    plt.yticks(color=youtube_white)
    plt.show()

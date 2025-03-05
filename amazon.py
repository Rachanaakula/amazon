import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load Amazon product data from a CSV or JSON file."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or JSON.")

def basic_analysis(df):
    """Perform basic analysis on the dataset."""
    print("Dataset Overview:\n", df.head())
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nStatistical Summary:\n", df.describe())

def plot_price_distribution(df):
    """Visualize the price distribution of products."""
    plt.figure(figsize=(10, 5))
    sns.histplot(df['price'], bins=50, kde=True)
    plt.title("Price Distribution of Products")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.show()

def plot_rating_distribution(df):
    """Visualize the rating distribution of products."""
    plt.figure(figsize=(10, 5))
    sns.countplot(x='rating', data=df, palette='viridis')
    plt.title("Product Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.show()

def analyze_reviews(df):
    """Analyze product reviews and their correlation with ratings."""
    print("Average Reviews per Rating:\n", df.groupby('rating')['reviews'].mean())
    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=df['reviews'], y=df['rating'])
    plt.title("Reviews vs Ratings")
    plt.xlabel("Number of Reviews")
    plt.ylabel("Rating")
    plt.show()

def main():
    file_path = input("Enter the path to the dataset (CSV/JSON): ")
    df = load_data(file_path)
    basic_analysis(df)
    plot_price_distribution(df)
    plot_rating_distribution(df)
    analyze_reviews(df)

if __name__ == "__main__":
    main()

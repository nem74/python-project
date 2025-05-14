import requests
import pandas as pd
import matplotlib.pyplot as plt

# API Endpoint
API_URL = "https://disease.sh/v3/covid-19/countries"

# Fetch global COVID-19 data by country
def fetch_covid_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        print("Failed to fetch data:", response.status_code)
        return None

# Display top countries by cases
def display_top_countries(df, n=10):
    top_countries = df[['country', 'cases', 'deaths', 'recovered']].sort_values(by='cases', ascending=False).head(n)
    print(f"\nTop {n} Countries by Confirmed Cases:")
    print(top_countries.to_string(index=False))

# Plot a bar chart of top countries by active cases
def plot_top_active_cases(df, n=10):
    top = df[['country', 'active']].sort_values(by='active', ascending=False).head(n)
    plt.figure(figsize=(10, 6))
    plt.bar(top['country'], top['active'], color='orange')
    plt.title(f"Top {n} Countries by Active COVID-19 Cases")
    plt.xlabel("Country")
    plt.ylabel("Active Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function
def main():
    print("🌍 COVID-19 Global Data Tracker")
    df = fetch_covid_data()
    if df is not None:
        display_top_countries(df)
        plot_top_active_cases(df)

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Main program to load the dataset, filter data, and display a graph for a specific country.
    """

    path = "life_expectancy_years.csv"

    dataset = load(path)
    if dataset is None:
        print("Failed to load the dataset.")
        return

    country_column = "country"
    if country_column not in dataset.columns:
        print(f"Error: The dataset does not contain a '{country_column}' column.")
        return

    country_name = "Spain"

    country_data = dataset[dataset[country_column] == country_name]
    if country_data.empty:
        print(f"Error: No data found for the country '{country_name}'.")
        return

    years = country_data.columns[1:]
    life_expectancy = country_data.iloc[0, 1:].values.astype(float)

    plt.figure(figsize=(10, 6))
    plt.plot(years, life_expectancy, marker="", label=f"Life Expectancy in {country_name}")

    plt.title(f"{country_name} Life expectancy Projections", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Life Expectancy", fontsize=12)
    plt.xticks(years[::40])
    plt.legend()
    plt.grid(False)

    plt.show()


if __name__ == "__main__":
    main()
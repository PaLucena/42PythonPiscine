from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Main program to load the dataset, filter data, and compare population of two countries.
    """
    dataset = load("population_total.csv")
    if dataset is None:
        print("Failed to load the dataset.")
        return

    country_column = "country"
    if country_column not in dataset.columns:
        print(f"Error: The dataset does not contain a '{country_column}' column.")
        return

    campus_country = "Spain"
    other_country = "France"
    campus_data = dataset[dataset[country_column] == campus_country]
    other_data = dataset[dataset[country_column] == other_country]

    if campus_data.empty or other_data.empty:
        print(f"Error: Data not found for '{campus_country}' or '{other_country}'.")
        return

    years = [str(year) for year in range(1800, 2051)]
    campus_population = campus_data[years].iloc[0].apply(lambda x: float(x.replace('M', ''))).values
    other_population = other_data[years].iloc[0].apply(lambda x: float(x.replace('M', ''))).values

    plt.figure(figsize=(12, 8))
    plt.plot(years, campus_population, marker="", label=campus_country)
    plt.plot(years, other_population, marker="", label=other_country)

    plt.title(f"Population Projections", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Population", fontsize=14)

    plt.xticks(years[::40])

    plt.legend()
    plt.grid(False)

    # Mostrar el gráfico
    plt.show()


if __name__ == "__main__":
    main()
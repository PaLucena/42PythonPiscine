from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    """
    Main program to load datasets and plot life expectancy against GDP per capita for 1900.
    """
    income_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_expectancy_path = "life_expectancy_years.csv"

    income_data = load(income_path)
    life_expectancy_data = load(life_expectancy_path)

    if income_data is None or life_expectancy_data is None:
        print("Failed to load one or both datasets.")
        return

    year = "1900"
    if year not in income_data.columns or year not in life_expectancy_data.columns:
        print(f"Error: Year {year} not found in one or both datasets.")
        return

    income_data = income_data.set_index("country")
    life_expectancy_data = life_expectancy_data.set_index("country")

    merged_data = pd.merge(income_data[[year]], life_expectancy_data[[year]],
                           left_index=True, right_index=True, suffixes=("_income", "_life_expectancy"))

    merged_data["GDP per Capita"] = merged_data["GDP per Capita"].apply(
        lambda x: float(str(x).replace('M', '').replace('K', '')) * (1000 if 'K' in str(x) else 1)
    )
    merged_data["Life Expectancy"] = merged_data["Life Expectancy"].astype(float)


    merged_data = merged_data.dropna()
    merged_data["GDP per Capita"] = merged_data["GDP per Capita"].apply(lambda x: float(x.replace('M', '').replace('K', '')) * (1000 if 'K' in x else 1))
    merged_data["Life Expectancy"] = merged_data["Life Expectancy"].astype(float)

    plt.figure(figsize=(12, 8))
    plt.scatter(merged_data["GDP per Capita"], merged_data["Life Expectancy"], color="blue", alpha=0.6, label="Countries")

    plt.title(f"Life Expectancy vs GDP per Capita (Year {year})", fontsize=16)
    plt.xlabel("GDP per Capita (PPP, Inflation Adjusted)", fontsize=14)
    plt.ylabel("Life Expectancy (Years)", fontsize=14)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()

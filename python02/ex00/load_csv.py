import pandas as pd
from typing import Union


def load(path: str) -> Union[pd.DataFrame, None]:
    """
    Load a dataset from the specified path,
    returning its dimensions and handling errors.

    Args:
        path (str): Path to the dataset file.

    Returns:
        Union[pd.DataFrame, None]: Loaded dataset as a DataFrame, or None.
    """
    try:
        dataset = pd.read_csv(path)

        print(f"Loading dataset of dimensions {dataset.shape}")

        return dataset
    except FileNotFoundError:
        print("Error: The file was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or has invalid data.")
    except pd.errors.ParserError:
        print("Error: The file format is incorrect or unreadable.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


def main():
	load("life_expectancy_years.csv")


if __name__ == "__main__":
    main()

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("'Family' must be a list")

    try:
        family_array = np.array(family, dtype=object)
    except Exception as e:
        raise ValueError(f"Error while converting list ti array: {e}")

    if family_array.ndim != 2:
        raise ValueError("'Family' must be a 2D list (matrix)")

    print(f"My shape is: {family_array.shape}")

    truncated_array = family_array[start:end, :]

    print(f"My new shape is: {truncated_array.shape}")

    return truncated_array.tolist()


def main():
    family = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    print(slice_me(family, 1, 3))


if __name__ == "__main__":
    main()
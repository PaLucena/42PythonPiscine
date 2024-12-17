import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[float]:
    """
    Calculates BMI (Body Mass Index) of each height-weight value.
    :param weights: weights list (int/float)
    :param heights: heights list (int/float)
    :return: BMI values list (float)
    """
    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)

    if height_array.shape != weight_array.shape:
        raise ValueError("Height & weight lists must have same size")
    if np.any(height_array <= 0):
        raise ValueError("Height must be more than 0")

    bmi = weight_array / (height_array ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if BMI limits are higher than a given value
    :param bmi_values: BMI values list (int/float)
    :param limit: Limit value (int o float)
    :return: Bools list
    """
    if not isinstance(limit, int):
        raise TypeError("El límite debe ser un número entero.")

    bmi_array = np.array(bmi, dtype=float)
    result = bmi_array > limit
    return result.tolist()


def main():
    """
    Checks use of both functions above
    """
    height = [1.75, 1.8, 1.6]
    weight = [70, 80, 50]

    bmi = give_bmi(height, weight)
    print("BMI:", bmi)  # Expected result: [22.86, 24.69, 19.53] (rounded)

    result = apply_limit(bmi, 23)
    print("Above limit:", result)  # Expected result: [False, True, False]


if __name__ == "__main__":
    main()

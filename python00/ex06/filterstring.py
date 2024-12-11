import sys
from ft_filter import ft_filter


def contains_special_chas(str):
    """
        Checks str passed as argument for special characters (not allowed)
    """
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
                  0123456789 ")
    return any(char not in allowed for char in str)


def check_length(str) -> bool:
    """
        Checks length
    """
    for n in sys.argv[2]:
        if not n.isdigit():
            raise AssertionError("the arguments are bad")
    min = int(sys.argv[2])

    return (True if len(str) > min else False)


def main():
    """
        Receives a string(s) and an integer(n) and outputs the numbers of words
        in s that are longer than n characters
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        elif contains_special_chas(sys.argv[1]):
            raise AssertionError("the arguments are bad")
        print(list(ft_filter(check_length, sys.argv[1].split())))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()

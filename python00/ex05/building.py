import sys


def prompt_user() -> str:
    """
        Prompt user for an argument if one has not been provided
    """
    return_str = input("Hola?\n")
    return (return_str)


def main():
    """
        Counts every character, upper and lower case letter,
        punctuation marks, spaces and digits
    """


    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        prompt = sys.argv[1] if len(sys.argv) == 2 else prompt_user()

        upper_count = sum(1 for c in prompt if c.isupper())
        lower_count = sum(1 for c in prompt if c.islower())
        punct_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`´{|}~"
        punct_count = sum(1 for c in prompt if c in punct_chars)
        spaces_count = sum(1 for c in prompt if c == ' ')
        digit_count = sum(1 for c in prompt if c.isdigit())

        print(f"The text contains {len(prompt)} characters:")
        print(f"{upper_count} upper letters")
        print(f"{lower_count} lower letters")
        print(f"{punct_count} punctuation marks")
        print(f"{spaces_count} spaces")
        print(f"{digit_count} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()

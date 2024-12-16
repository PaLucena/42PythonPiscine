import sys


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        
    except AssertionError as e:
        print(f"AssertionError: {e}")
    str.isalnum()
    if any(char not in allowed for char in str):
        raise AssertionError("the arguments are bad")

if __name__ == "__main__":
    main()

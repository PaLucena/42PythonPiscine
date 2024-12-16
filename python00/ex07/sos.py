import sys


def main():
    morse_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '/'
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        str = sys.argv[1].upper()
        for c in str:
            if not (c.isalnum() or c == ' '):
                raise AssertionError("the arguments are bad")
        morseStr = ' '.join(morse_code[c] for c in str)
        print(morseStr)
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()

"""
Contains methods that translate morse code into english through varying mediums.
"""


def morse_text_to_english_text(code: str) -> str:
    """
    Translates morse code text to English text.

    Parameter code: morse code str to be translated. Must be of type str and formatted like "--- ...
    --- / --- ... ---". Letters separated by " ", words separated by ' / '


    For debugging purposes within outside implementations, unsupported morse code chars will not throw an error and
    will instead add a '#' to the output string and print an error message before continuing execution.
    """
    morse_code_dict_reversed = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '/': ' ',
        '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
        '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
        '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
        '.-..-.': '"', '...-..-': '$', '.--.-.': '@',
        # You can add more Morse code characters as needed.
    }

    if type(code) != str:
        raise TypeError("Input must be of type str")

    # Split input code into list of 'char' strings
    code_split = code.split(' ')

    english_text = ""

    # Translate each 'char' and append to output string.
    err_count = 1
    for char in code_split:
        try:
            english_text += morse_code_dict_reversed[char]
        except KeyError:
            print("Invalid char " + str(err_count) + ": \"" + char + "\"")
            english_text += "#"
            err_count += 1

    return english_text


def english_text_to_morse_text(english_text: str) -> str:
    """
    Translates english text to morse code text.

    Parameter english_text: English text str to be translated.
    Ex: "HI BOB" will return ".... ../-... --- -.../

    For debugging purposes within outside implementations, unsupported english letters will not throw an error and
    will instead add a '#' to the output string and print an error message before continuing execution.
    """

    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
        ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    }

    if type(english_text) != str:
        raise TypeError("Input must be of type str")

    english_text = english_text.upper()

    # Split this up so that there are no spaces before and after '/'

    code = ""
    err_count = 1

    # Translate each 'char' and append to output string.
    for char in english_text:
        try:
            code += (morse_code_dict[char] + " ")
        except KeyError:
            print("Invalid char " + str(err_count) + ": \"" + char + "\"")
            english_text += "# "
            err_count += 1

    code = code.rstrip(' ')
    return code

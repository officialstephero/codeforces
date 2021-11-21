MORSE_CODE =  {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
     '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
     '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
     '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
     '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
     '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
     '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
     '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
     '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
     '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
     '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'
     }


def decodeBits(bits):
    bits = bits.strip("0")
    unit = 0
    for bit in bits:
        if bit != "0":
            unit += 1
        else:
            break
    # unit now might be 1 unit or 3 units
    count = 1
    for i in range(1, len(bits)):
        if bits[i] == bits[i - 1]:
            count += 1
        else:
            if count < unit:
                unit = count
                count = 1
            else:
                count = 1
    morse_code = ""

    words = bits.split("0" * 7 * unit)
    for word in words:
        characters = word.split("0" * 3 * unit)
        for character in characters:
            signs = character.split("0" * unit)
            for sign in signs:
                if sign == "1" * 3 * unit:
                    morse_code += "-"
                else:
                    morse_code += "."
            morse_code += " "
        morse_code += "   "
    return morse_code


def decodeMorse(morse_code):
    morse_code.strip()
    result = ""
    characters = morse_code.split(" ")
    for character in characters:
        if character != "":
            result += MORSE_CODE[character]
        else:
            result += " "
    return ' '.join(result.split())



m2 = '11001100110011000000110000001' \
     '11111001100111111001111110000' \
     '00000000001100111111001111110' \
     '01111110000001100110011111100' \
     '00001111110011001100000011'
print(decodeBits(m2))

morse_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    "?": "..--..",
    "!": "-.-.--",
    ".": ".-.-.-",
    ",": "--..--",
    ";": "-.-.-.",
    ":": "---...",
    "+": ".-.-.",
    "-": "-....-",
    "/": "-..-.",
    "=": "-...-",
    " ": "\n"
}

c = input('Enter Word: ').lower()

for i in str(c):
  if str(i) != morse_dict[str(i)]:
    print(f"character {i} does not exist")
  else:
    print(morse_dict[str(i)])

"""This program counts the number of vowels in a string."""
def count_vowels(string:str) -> int:
    contador = 0
    contador += string.lower().count("a")
    contador += string.lower().count("e")
    contador += string.lower().count("i")
    contador += string.lower().count("o")
    contador += string.lower().count("u")

    return contador

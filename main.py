from deep_translator import GoogleTranslator
import colorama

print(colorama.Fore.BLUE + """
    Welcome on my translator
"""+ colorama.Style.RESET_ALL)

l_text : str = input("Choose the language of the text : ")
text : str = input("Texte a traduire : ")

translator = GoogleTranslator(source="auto", target=l_text).translate(text)
print(colorama.Fore.GREEN + "\n" + translator + "\n" + colorama.Style.RESET_ALL)
from deep_translator import GoogleTranslator
import colorama

print(colorama.Fore.BLUE + """
████████╗██████╗  █████╗ ███╗   ██╗███████╗██╗      █████╗ ████████╗ ██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
   ██║   ██████╔╝███████║██╔██╗ ██║███████╗██║     ███████║   ██║   ██║   ██║██████╔╝       ██║   ██║   ██║██║   ██║██║     
   ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗       ██║   ██║   ██║██║   ██║██║     
   ██║   ██║  ██║██║  ██║██║ ╚████║███████║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝""")

l_text : str = input("Choose the language of the text : " + colorama.Style.RESET_ALL)
text : str = input(colorama.Fore.BLUE + "Text to translate : " + colorama.Style.RESET_ALL)

translator = GoogleTranslator(source="auto", target=l_text).translate(text)
print(colorama.Fore.GREEN + "\n" + translator + "\n\n\n" + colorama.Style.RESET_ALL)

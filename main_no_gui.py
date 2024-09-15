from deep_translator import GoogleTranslator
import colorama

print(colorama.Fore.BLUE + """
 _  _  _       _                                           ______            _                _                                                   _                       
| || || |     | |                                         / __   |      _   | |              | |               _       _                         | |      _               
| || || | ____| | ____ ___  ____   ____     ___  ____    | | //| |_   _| |_ | | _   ____ ____| | _   ___   ___| |_    | |_   ____ ____ ____   ___| | ____| |_  ___   ____ 
| ||_|| |/ _  ) |/ ___) _ \|    \ / _  )   / _ \|  _ \   | |// | ( \ / )  _)| || \ / _  ) _  | || \ / _ \ /___)  _)   |  _) / ___) _  |  _ \ /___) |/ _  |  _)/ _ \ / ___)
| |___| ( (/ /| ( (__| |_| | | | ( (/ /   | |_| | | | |  |  /__| |) X (| |__| | | ( (/ ( ( | | | | | |_| |___ | |__   | |__| |  ( ( | | | | |___ | ( ( | | |_| |_| | |    
 \______|\____)_|\____)___/|_|_|_|\____)   \___/|_| |_|   \_____/(_/ \_)\___)_| |_|\____)_|| |_| |_|\___/(___/ \___)   \___)_|   \_||_|_| |_(___/|_|\_||_|\___)___/|_|    
                                                                                       (_____|                                                                                                                                                                                                                                                                   
""")

l_text : str = input("Choose the language of the text : " + colorama.Style.RESET_ALL)
text : str = input(colorama.Fore.BLUE + "Text to translate : " + colorama.Style.RESET_ALL)

translator = GoogleTranslator(source="auto", target=l_text).translate(text)
print(colorama.Fore.GREEN + "\n" + translator + "\n\n\n" + colorama.Style.RESET_ALL)
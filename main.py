from deep_translator import GoogleTranslator
from customtkinter import *
from PIL import Image
import colorama

# print(colorama.Fore.BLUE + """
#     Welcome on my translator
# """+ colorama.Style.RESET_ALL)

# l_text : str = input("Choose the language of the text : ")
# text : str = input("Texte a traduire : ")

# translator = GoogleTranslator(source="auto", target=l_text).translate(text)
# print(colorama.Fore.GREEN + "\n" + translator + "\n" + colorama.Style.RESET_ALL)

app = CTk()
app.title("Translator - |by 0xtheghost|")
app.iconbitmap('')
app.geometry("500x400")
theme : str = "dark"

set_appearance_mode(theme)
icon_translate = Image.open(f'images/translate_for_{theme}.png')

label = CTkLabel(master=app, text="Welcome on my translator", font=("Arial", 25),text_color="#32b878")
btn = CTkButton(master=app, text="Translate", corner_radius=12, fg_color="transparent",
                hover_color="#40ad79", border_color="#2e855b",
                border_width=2, image=CTkImage(dark_image=icon_translate, light_image=icon_translate, size=(20,20)))

label.place(relx=.5, rely=.1, anchor="n")
btn.place(relx=.5, rely=.5, anchor="center")
app.mainloop()
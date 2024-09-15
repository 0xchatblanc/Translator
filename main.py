from deep_translator import GoogleTranslator
from customtkinter import *
from PIL import Image

# list_langue = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

app = CTk()
app.geometry("1000x800")
app.title("Translator - |by 0xtheghost|")
set_appearance_mode("dark")
app.resizable(width=True, height=True)
app.minsize(width=900, height=600)

icon_translate = Image.open('images/translate_for_dark.png')
icon_arrow = Image.open('images/right-arrow.png')

def click_translate():
    language = boxselect.get()
    text_to_translate = boxtext.get("1.0", END)  # Pour récupérer tout le texte
    translation = GoogleTranslator(source="auto", target=language).translate(text_to_translate)

    # Pour modifier le texte dans un CTkTextbox désactivé
    boxresult.configure(state="normal")  # Activer la modification
    boxresult.delete("1.0", END)  # Supprimer l'ancien contenu
    boxresult.insert("1.0", translation)  # Insérer la traduction
    boxresult.configure(state="disabled")  # Désactiver à nouveau


label = CTkLabel(master=app, 
                 text="Translator 0x", 
                 font=("Arial", 30),
                 text_color="#32b878")
label.place(relx=.5, rely=.2, anchor="n")

img_arrow = CTkLabel(master=app, 
                     text="", 
                     image=CTkImage(dark_image=icon_arrow, size=(20,20)))
img_arrow.place(relx=.5, rely=.5, anchor="center")

boxtext = CTkTextbox(master=app, 
                     wrap="word",
                     width=400, 
                     height=150,
                     fg_color="#2d3036", 
                     corner_radius=15, 
                     activate_scrollbars=True)
boxtext.place(relx=.25, rely=.5, anchor="center")

boxresult = CTkTextbox(master=app, 
                     wrap="word",
                     width=400, 
                     height=150,
                     fg_color="#2d3036", 
                     corner_radius=15, 
                     activate_scrollbars=True)
boxresult.place(relx=.75, rely=.5, anchor="center")
boxresult.configure(state="disabled")

boxselect = CTkComboBox(master=app, 
                        width=200, 
                        height=50,
                        corner_radius=15,
                        border_width=0,
                        fg_color="#2d3036",
                        button_color="#32456b",
                        button_hover_color="#141a26",
                        dropdown_fg_color="#212121",
                        dropdown_hover_color="#2d3036",
                        font=("Arial", 15),
                        dropdown_font=("Arial", 15),
                        values=['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'assamese', 'aymara', 'azerbaijani', 'bambara', 'basque', 'belarusian', 'bengali', 'bhojpuri', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dhivehi', 'dogri', 'dutch', 'english', 'esperanto', 'estonian', 'ewe', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'guarani', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'ilocano', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'kinyarwanda', 'konkani', 'korean', 'krio', 'kurdish (kurmanji)', 'kurdish (sorani)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lingala', 'lithuanian', 'luganda', 'luxembourgish', 'macedonian', 'maithili', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'meiteilon (manipuri)', 'mizo', 'mongolian', 'myanmar', 'nepali', 'norwegian', 'odia (oriya)', 'oromo', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'quechua', 'romanian', 'russian', 'samoan', 'sanskrit', 'scots gaelic', 'sepedi', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'tatar', 'telugu', 'thai', 'tigrinya', 'tsonga', 'turkish', 'turkmen', 'twi', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'],
                        )
boxselect.place(relx=.5, rely=.7, anchor="center")

btn = CTkButton(master=app, 
                text="Translate", 
                width=200, 
                height=50, 
                corner_radius=12, 
                fg_color="transparent",
                hover_color="#40ad79", 
                border_color="#2e855b",
                border_width=2, 
                image=CTkImage(dark_image=icon_translate,size=(20,20)),
                command=click_translate)
btn.place(relx=.5, rely=.9, anchor="s")

app.mainloop()
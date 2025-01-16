# Translator Tool 🈵🌐  
**Translator Tool** is a powerful Python-based GUI and CLI application designed for quick and efficient translations using the Google Translator API. The tool provides both a **Graphical User Interface (GUI)** for an intuitive user experience and a **Command-Line Interface (CLI)** for lightweight and fast translation needs.

---

## ✨ Features  

### GUI Application  
- 🌍 **Language Selection**: Choose from a wide range of languages via a dropdown menu.  
- 📜 **Text Translation**: Input text in one language and translate it to another instantly.  
- 🎨 **Modern Design**: Built with **CustomTkinter**, featuring a dark theme and sleek design.  
- 🖼️ **Image Integration**: Includes icons for buttons and labels for a polished look.  

### CLI Application  
- ⚡ **Fast Translation**: Translate text directly in the terminal.  
- 🔤 **Auto Language Detection**: Detects the source language automatically.  
- 🎨 **Colorized Interface**: Uses **Colorama** to highlight text and make the CLI visually appealing.  

---

## 🚀 Installation  

### Prerequisites  
Ensure you have **Python 3.8+** installed on your system.  

### Install Dependencies  
Run the following command to install the required Python packages:  
```bash  
pip install deep-translator customtkinter pillow colorama  
```  

---

## 🖥️ Usage  

### GUI Mode  
1. Run the `Translator` GUI application:  
   ```bash  
   python translator_gui.py  
   ```  
2. Input your text in the left textbox.  
3. Select the target language from the dropdown menu.  
4. Click **Translate** to see the result in the right textbox.  

### CLI Mode  
1. Run the CLI translator script:  
   ```bash  
   python translator_cli.py  
   ```  
2. Enter the desired target language (e.g., `fr` for French, `es` for Spanish).  
3. Input the text to translate.  
4. View the translated output directly in the terminal.  

---

## 🛠️ Example  

### GUI Example  
1. Enter text in the **left textbox** (e.g., "Hello, how are you?").  
2. Select the **target language** (e.g., "French").  
3. The translated text ("Bonjour, comment ça va ?") will appear in the **right textbox**.  

### CLI Example  
**Input**:  
```  
Choose the language of the text: fr  
Text to translate: Hello, how are you?  
```  
**Output**:  
```  
Bonjour, comment ça va ?  
```  

---

## 🗂️ Project Structure  

```
translator-tool/  
├── translator_gui.py        # Main GUI script  
├── translator_cli.py        # Main CLI script  
├── images/                  # Icons for GUI
│   ├── translate_for_light.png 
│   ├── translate_for_dark.png  
│   └── right-arrow.png  
└── requirements.txt         # Python dependencies  
```  

---

## 🌟 Supported Languages  

The tool supports over **100 languages**, including:  
- English (`en`), French (`fr`), Spanish (`es`), German (`de`), Chinese Simplified (`zh-CN`), Arabic (`ar`), Japanese (`ja`), and more.  

A complete list of languages is available in the code as `list_langue`.  

---

## ✨ Future Enhancements  
- 📃 **Text-to-Speech Support**: Add a feature to read the translated text aloud.  
- 📁 **File Translation**: Support for translating text files.  
- 🖥️ **Desktop Packaging**: Package the GUI application into a standalone desktop app.  

---

## 🤝 Contributing  

Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a new branch for your feature:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add feature"  
   ```  
4. Push to your branch:  
   ```bash  
   git push origin feature-name  
   ```  
5. Open a pull request.  

---

## 📄 License  

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for more details.  

---

## 🙏 Acknowledgments  

- Translation powered by [GoogleTranslator](https://pypi.org/project/deep-translator/).  
- GUI design with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter).  
- CLI color enhancements with [Colorama](https://pypi.org/project/colorama/).  

---

**Created with ❤️ by 0xchatblanc.** 😊  

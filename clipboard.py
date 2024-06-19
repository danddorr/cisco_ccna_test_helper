import pyperclip

def get_clipboard_content():
    clipboard_content = pyperclip.paste()
    
    return clipboard_content

def set_clipboard_content(content):
    pyperclip.copy(content)
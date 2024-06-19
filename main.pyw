from pynput.keyboard import Key, Listener
from clipboard import get_clipboard_content, set_clipboard_content
from scrape_answers import get_answers, get_soup
import time, json

soup = get_soup()
file_answers = {}

def on_release(key):

    if key==Key.space or key==Key.ctrl_r:
        with open("answer_log.json", "w+") as file:
            clipboard_content = get_clipboard_content()
            answers = get_answers(soup, clipboard_content)

            for i in answers:
                set_clipboard_content(i)
                time.sleep(0.3)

            if clipboard_content in file_answers:
                return

            file_answers[clipboard_content] = answers
            json.dump(file_answers, file, indent=4)
    
    if key == Key.esc:
        exit()
    
with Listener(on_release=on_release) as listener:
    listener.join()

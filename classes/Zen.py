import pyautogui
import pytesseract
import os
import threading
from pytesseract import Output
from time import sleep
from dotenv import load_dotenv

class Zen(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        load_dotenv()
        self.target_word = 'zen'
        pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD')

    def run(self):
        # TODO: Add a while true here...
        words = self.get_window_words()
        coords = self.find_word_coordinates(words)
        if not coords:
            print('Zen not found...')
            return
        self.pick_up(coords[0], coords[1]);
        

    def get_window_words(self):
        im = pyautogui.screenshot()
        return pytesseract.image_to_data(im, output_type=Output.DICT)

    def find_word_coordinates(self, words):
        found_coords_screen = None
        n_items = len(words['text'])
        for i in range(n_items):
            current_word = words['text'][i].strip().lower()
            
            if self.target_word.lower() in current_word:
                x = words['left'][i] + 5
                y = words['top'][i] + 5
                found_coords_screen = (x, y)
                break
        return found_coords_screen

    def pick_up(self, x, y):
        pyautogui.keyDown('alt')
        sleep(0.5)
        pyautogui.click(x=x, y=y)
        sleep(0.5)
        pyautogui.keyUp('alt')

        # Show the item names again
        pyautogui.press('alt')

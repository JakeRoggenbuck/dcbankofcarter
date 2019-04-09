from pynput.keyboard import Key,Controller
from time import sleep
k = Controller()
k.type('set FLASK_ENV=development')
k.press(Key.enter)
k.release(Key.enter)
k.type('set FLASK_APP=flask_app.py')
k.press(Key.enter)
k.release(Key.enter)
k.type('flask run')
k.press(Key.enter)
k.release(Key.enter)

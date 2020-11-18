import pyautogui
import webbrowser
import time

url = 'https://translate.google.com.br'
webbrowser.open_new(url)

pyautogui.moveTo(257,286)
pyautogui.click()
time.sleep(1)
pyautogui.write('Fala rapaziada', interval=0.3)

pyautogui.moveTo(116,387)
pyautogui.click()
time.sleep(8)

url = 'https://www.youtube.com/watch?v=UF8IQXvFKfs'
webbrowser.open_new(url)



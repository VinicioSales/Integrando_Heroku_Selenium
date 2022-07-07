from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip
from tkinter import *
from PySimpleGUI import PySimpleGUI as sg
from openpyxl import Workbook, load_workbook
import os

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.google.com/")

navegador.maximize_window()
time.sleep(5)


variavel = previsao = navegador.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a').text
print(variavel)




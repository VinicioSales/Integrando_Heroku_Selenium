from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")

#servico = Service(ChromeDriverManager().install())
#navegador = webdriver.Chrome(service=servico)
navegador = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

navegador.get("https://www.google.com/")

navegador.maximize_window()
time.sleep(5)


variavel = previsao = navegador.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a').text
print(variavel)



 
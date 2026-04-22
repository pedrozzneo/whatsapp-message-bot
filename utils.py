from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from PIL import Image
import io
import win32clipboard

def search(filter, driver):
    try:
        print("im on search")
        
        try:
            close_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="End icon button"]')))
            close_btn.click()
        except:
            print("nothing to reset")
   
        # Find and select the search field 
        search_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Pesquisar ou começar uma nova conversa"]')))
        search_field.click()
        print(f"\n clicked")
    
        # Clear the search field and type the filter
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        search_field.send_keys(Keys.BACKSPACE + filter) 
        print(f"\n Pesquisa por {filter}")
    except:
        print(f"\n ❌ Pesquisa por {filter}")
        raise

def scroll_inside_div_js(driver, scroll_amount):
    try:
        # Find the div element that will be scrolled
        div_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "pane-side")))

        # scroll
        driver.execute_script("arguments[0].scrollTop += arguments[1];",div_element,scroll_amount)
    except:
        print("❌ scrolled down")

def imageToClipboard(folder_path):
    # Lista todos os arquivos da pasta
    files = os.listdir(folder_path)

    # Filtra apenas arquivos de imagem
    images = [f for f in files]

    if not images:
        print("Nenhuma imagem encontrada na pasta!")
        return

    # Pega a primeira imagem da lista
    image_path = os.path.join(folder_path, images[0])

    # Abre e converte para BMP/DIB
    img = Image.open(image_path)
    output = io.BytesIO()
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    # Copia para a área de transferência
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

    print(f"Imagem '{images[0]}' copiada para a área de transferência!")
    time.sleep(5)

    
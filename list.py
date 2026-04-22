from selenium.webdriver.common.by import By
import utils
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def message(driver, addedContacts, profile):
    # Path to get the images from
    clipboardPath = fr"C:\Users\pedro\Documents\Code\whatsapp\images\{profile}"
    
    contador = 0
    while addedContacts != [] and contador < 30:
        time.sleep(10)
        try:
            # Get the first contact in the list
            contact = addedContacts.pop(0)

            success = False
            while not success:
                try:
                    utils.search(contact, driver)
                    success = True
                    time.sleep(10)
                except:
                    continue

            groupCount = 0

            try:
                groupCount += 1
                print(f"\ncollecting contacts from group {groupCount} ... \n")

                group = WebDriverWait(driver, 30).until(
                    EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='x10l6tqk xh8yej3 x1g42fcv']"))
                )
                contactsAmount = len(group)

            except Exception as e:
                print(f"unable to find a group of contacts {str(e)}")

            for i in range(contactsAmount):
                try:
                    # Get the name of the contact
                    name = group[i].text.split('\n')[0].strip()
                    print(name)
                except:
                    print("messaging failed")

            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//span[@title="{name}"]')))
            print(element)

            # go up to the clickable container
            clickable = element.find_element(By.XPATH, './ancestor::div[@role="button"]')
            print(clickable)
            clickable.click()

            time.sleep(random.randint(5, 10))

            # Make the input field empty
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()

            # Copy the image
            utils.imageToClipboard(clipboardPath)

            # Paste it
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            time.sleep(random.randint(3, 6))

            # Send it
            try:
                # Portuguese
                send_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Enviar']"))
                )
            except:
                # English
                send_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Send"]'))
                )

            send_button.click()
            time.sleep(10)

            #Remove contact from list
            with open(f"lists/{profile}/addedContacts.txt", "w") as addedContactsFile:
                for i in range(len(addedContacts)):
                    addedContactsFile.write(addedContacts[i] + '\n')
            
            contador += 1
            print(f"Mensagem para {contact} - {contador} bem sucedida, {len(addedContacts)} restantes")
        except:
            print(f"❌ Erro ao enviar mensagem para {contact}")
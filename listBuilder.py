from selenium.webdriver.common.by import By
import utils
import time
import driver as d
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def build(profile):
    # Set chrome driver and open whatsapp
    driver = d.set(profile)
    driver.get("https://web.whatsapp.com")
    time.sleep(5)

    # Filter "lista" contacts until it's successfull
    success = False
    while not success:
        try:
            utils.search("fibra", driver)
            success = True
            time.sleep(5)
        except:
            continue

    addedContacts = []
    removedContacts = []
    errors = []
    equalNames = []
    groupCount = 0

    end = False
    while not end:
        try:
            groupCount += 1
            print(f"\ncollecting contacts from group {groupCount} ... \n")

            group = WebDriverWait(driver, 30).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='x10l6tqk xh8yej3 x1g42fcv']"))
            )
            contactsAmount = len(group)

        except Exception as e:
            print(f"unable to find a group of contacts {str(e)}")
            errors.append("unable to find a group of contacts")
        
        for i in range(contactsAmount):
            try:
                # Get the name of the contact
                name = group[i].text.split('\n')[0].strip()

                # Stop condition
                if name.lower() == "messages" or name.lower() == "mensagens":
                    end = True
                    print("MESSAGES found, stop looking for other contacts")
                    break

                # Check if the contact should not be added
                if "excluir" in name.lower() or "mec med" in name.lower() or name.lower() == "contacts" or name.lower() == "chats" or name.lower() == "conversas" or "fibra" not in name.lower() or "mec med" in name.lower() or "problema" in name.lower():
                    print(f"{i} - skipping contact: {name}")
                    removedContacts.append(name)
                    continue
            
                # Add the contact to the array only if its new
                if name not in addedContacts:
                    addedContacts.append(name)    
                    print(f" {i} - {name} added")
                else:
                    equalNames.append(name)
                    print(f" {i} - {name} already on list")
            except:
                print("messaging failed")

        # Quit the loop
        if end:
            print("End of contacts reached.")
            break

        # Scroll down to the next group of contacts
        try:
            distance = group[1].location['y']  - group[0].location['y']
            if groupCount == 1:
                scroll_amount = distance * (contactsAmount + 7)
            else:
                scroll_amount = distance * (contactsAmount) 
            utils.scroll_inside_div_js(driver, scroll_amount)
        except:
            print("scrolling failed")

        # Wait for the DOM to make this instance stale, giving room for the new one
        try:
            WebDriverWait(driver, 30).until(EC.staleness_of(group[0]))
            print("Old group become stale, looking for new one...")
        except:
            print("staleness failed")

    addedContacts.reverse()
    
    with open(f"lists/{profile}/addedContacts.txt", "w", encoding="utf-8") as addedContactsFile:
        for i in range(len(addedContacts)):
            addedContactsFile.write(addedContacts[i] + '\n')

build("flavia")
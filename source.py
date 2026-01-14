import driver as d
import utils
import list
import time
from datetime import datetime

def main(profile):
    # Set chrome driver and open whatsapp
    driver = d.set(profile)
    driver.get("https://web.whatsapp.com")
    time.sleep(30)

    # Filter "lista" contacts until it's successfull
    success = False
    while not success:
        try:
            utils.search("fibra", driver)
            success = True
            time.sleep(53)
        except:
            continue

    # Build all the lists
    addedContacts, removedContacts, errors, equalNames= list.build(driver)

main("thiago")
main("pedro")
main("flavia")
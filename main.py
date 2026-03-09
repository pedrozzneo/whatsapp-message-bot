import time
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

    # Build the list until "contacts"
    addedContacts, removedContacts, errors, equalNames= list.build(driver)

    # Build the rest of list
    oldContacts, removedContacts, errors, equalNames = list.buildOld(driver, addedContacts)

    # Print the lists
    utils.show(oldContacts, removedContacts, errors, equalNames)

    # Message each contact
    list.message(driver, oldContacts, profile)
    driver.quit()

# Each profile runs in a different time of the day
while True:
    agora = datetime.now()
    if agora.hour == 8 and agora.minute == 0:
        main("thiago")
    elif agora.hour >= 15 and agora.hour == 0:
        main("thiago")
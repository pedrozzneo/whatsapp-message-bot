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

    # Build all the lists
    addedContacts, removedContacts, errors, equalNames= list.build(driver)

    # Reverse the list to start with the oldest
    addedContacts.reverse()
    utils.show(addedContacts, removedContacts, errors, equalNames)

    # Message each contact
    list.message(driver, addedContacts, profile)
    driver.quit()

# Each profile runs in a different time of the day
while True:
    agora = datetime.now()
    if agora.hour == 3 and agora.minute <= 60:
        main("thiago")
    # elif agora.hour >= 7 and agora.hour <= 8:
    #     main("thiago")
    # elif agora.hour >= 15 and agora.hour <= 16:
    #     main("flavia")
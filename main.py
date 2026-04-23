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
    # time.sleep(5)

    with open(f"lists/{profile}/addedContacts.txt", "r", encoding="utf-8") as addedContactsFile:
        contacts = addedContactsFile.read().split("\n")

    # Message each contact
    list.message(driver, contacts, profile)
    driver.quit()


# main("flavia")
main("pedro")
# Each profile runs in a different time of the day
# while True:
#     agora = datetime.now()
#     if agora.hour == 7:
#         main("thiago")
#     time.sleep(25)
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

    with open(f"lists/{profile}/addedContacts.txt", "r", encoding="utf-8") as addedContactsFile:
        contacts = addedContactsFile.read().split("\n")

    # Message each contact
    list.message(driver, contacts, profile)
    driver.quit()

# Each profile runs in a different time of the day
weekDayTime = [[9, 0], [9, 10],[9, 20],[9, 30],[9, 40]]
while True:
    agora = datetime.now()
    dayCombo = weekDayTime[agora.weekday()]
    hour = dayCombo[0]
    minute = dayCombo[1]

    if agora.hour == hour and agora.minute == minute:
        main("thiago")
        main("pedro")
        main("flavia")

    time.sleep(20)
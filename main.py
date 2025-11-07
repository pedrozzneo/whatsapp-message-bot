import time
import driver as d
import utils
import list
import time
from datetime import datetime

#Espera dar 08:00 para iniciar a aplicação
# while True:
#     agora = datetime.now()
#     if agora.hour >= 7 and agora.hour <= 16:
#         break
#     time.sleep(60)  

profile = "thiago"
# profile = "pedro"
# profile = "flavia"

# Set chrome driver and open whatsapp
driver = d.set(profile)
driver.get("https://web.whatsapp.com")
time.sleep(140)

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

# Print them
utils.show(addedContacts, removedContacts, errors, equalNames)

# Start with a specific contact
addedContacts = list.filter(addedContacts, profile)
utils.show(addedContacts, removedContacts, errors, equalNames)

# Message each contact
list.message(driver, addedContacts, profile)  

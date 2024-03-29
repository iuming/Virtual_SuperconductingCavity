import epics
import random
import time

while True:
    random_value = random.gauss(0, 5)  
    epics.caput("DEL_F_Microphonics", random_value)
#     time.sleep(1e-10)

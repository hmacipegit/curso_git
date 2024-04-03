from time import sleep
import random

opt = ["Buena presentacion", "Buena presentación, jefe", "Mucho mejor que la del icm"]
while True:
    print(opt[random.randint(0,2)])
    sleep(2)
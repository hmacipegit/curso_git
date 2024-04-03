from time import sleep
from random import randint

opt = ["Buena presentacion", "Buena presentación, jefe", "Mucho mejor que la del icm"]
while True:
    affirmation = randint(0,2)
    print(opt[affirmation])
    sleep(3)
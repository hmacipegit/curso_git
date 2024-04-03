from time import sleep
from random import randint

opt = ["Buena presentacion", "Buena presentación, jefe", "Mucho mejor que la del icm", "Mucho mejor que la del icm"]
print("Buena presentación")
sleep(3)
while True:
    affirmation = randint(0,3)
    print(opt[affirmation])
    sleep(3)
import os
import random
for root, dirs, files in os.walk('.'):
    for name in files:
        a = random.randint(0, 100)
        if a < 66:
            os.remove(name)
import modulePage1

print(modulePage1.person["name"])

for x , y in modulePage1.person.items():
    print(x , y)

import modulePage2 as m2

print(m2.person["name"])

for x , y in m2.person.items():
    print(x , y)

from modulePage3 import language

obj = language("Python", "Guido Van Rossum", 1991)
obj.infos()
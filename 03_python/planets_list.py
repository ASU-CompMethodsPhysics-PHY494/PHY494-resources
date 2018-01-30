# install https://github.com/phalt/swapi-python

import swapi
planets = swapi.get_all('planets')

records = []
for p in planets.iter():
    if p.name == "unknown":
        continue
    try:
        diameter = int(p.diameter)
    except ValueError:
        diameter = p.diameter
    else:
        if diameter == 0:
            diameter = u"unknown"

    records.append((p.name.replace(' ', '_'),
                    diameter,
                    p.terrain.replace(' ', '').replace(',', '/')))

with open("planets.dat", "w") as output:
    for name, diameter, terrain in records:
        output.write("{0:15s}  {1:9}  {2}\n".format(name, diameter, terrain))


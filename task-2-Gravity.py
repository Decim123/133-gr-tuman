import math
import requests
import json

Grav = 6.6743 * math.pow(10, -11)
m1 = 5.976 * math.pow(10, 24)
m2 = float(input("Масса в кг? (без 10 в степени)     ")) * math.pow(10,int(input("степень 10?    ")))
issm = 42 * math.pow(10, 7)
iss = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
isst = json.dumps(iss.json())
altitude = iss.json()['altitude']
distance = int(input("Расстояние в км?    ")) * 1000

def f(x,y,z):
    return Grav * (x * y / math.pow(z, 2))

print("Взаимное притяжение от земли до космического тела ≈", f(m1,m2,distance))
print("Взаимное притяжение от земли до МКС(в данный момент) ≈", f(m1,issm,altitude))

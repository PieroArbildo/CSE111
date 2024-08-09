import math
"""list = [
    ["#1 Picnic"],
    [6.83],
    [10.16],
    ["#1 tall", 7.78, 11.91],
    ["#2", 8.73, 11.59],
    ["#2.5", 10.32, 11.91],
    ["#3 Cylinder", 10.79, 17.78],
    ["#5",13.02,14.29],
    ["#6Z",5.40,8.89],
    ["#8Z short",6.83,7.62],
    ["#10",15.72,17.78],
    ["#211",6.83,12.38],
    ["#300",7.62,11.27],
    ["#303",8.10,11.11]
]


def main():
    return "a"

def compute_volume():
    return"b"

def compute_surface_area():
    return "c"

for lista_exterior in arreglo:
    for elemento in lista_exterior:
        print(elemento)

"""
"""
datos_latas = {
    "#1 Picnic": {"Radius": 6.83, "Height": 10.16, "Cost per Can": 0.28},
    "#1 Tall": {"Radius": 7.78, "Height": 11.91, "Cost per Can": 0.43},
    "#2": {"Radius": 8.73, "Height": 11.59, "Cost per Can": 0.45},
    "#2.5": {"Radius": 10.32, "Height": 11.91, "Cost per Can": 0.61},
    "#3 Cylinder": {"Radius": 10.79, "Height": 17.78, "Cost per Can": 0.86},
    "#5": {"Radius": 13.02, "Height": 14.29, "Cost per Can": 0.83},
    "#6Z": {"Radius": 5.40, "Height": 8.89, "Cost per Can": 0.22},
    "#8Z short": {"Radius": 6.83, "Height": 7.62, "Cost per Can": 0.26},
    "#10": {"Radius": 15.72, "Height": 17.78, "Cost per Can": 1.53},
    "#211": {"Radius": 6.83, "Height": 12.38, "Cost per Can": 0.34},
    "#300": {"Radius": 7.62, "Height": 11.27, "Cost per Can": 0.38},
    "#303": {"Radius": 8.10, "Height": 11.11, "Cost per Can": 0.42}
}
"""
# Imprimir el diccionario
#print(datos_latas)

def compute_volume(radius,height):
    return (math.pi * float(radius) ** 2) * float(height)


print(compute_volume(6.83,10.16))


def compute_surface_area(radius,height):
   # return (2*math.pi * float(radius))*(float(radius)+float(height))
    return 2 * math.pi * radius * (radius + height)
        
#surface_area = 2π radius (radius + height)
print(compute_surface_area(6.83,10.16))
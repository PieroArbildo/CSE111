import math

def main():
    #print(storage_efficiency(compute_volume(6.83,10.16),compute_surface_area(6.83,10.16)))
    data_cans = [
    {'name':'#1 Picnic','radius': 6.83, 'height': 10.16, 'cost_per_can': 0.28},
    {'name':'#1 Tall','radius': 7.78, 'height': 11.91, 'cost_per_can': 0.43},
    {'name':'#2','radius': 8.73, 'height': 11.59, 'cost_per_can': 0.45},
    {'name':'#2.5','radius': 10.32, 'height': 11.91, 'cost_per_can': 0.61},
    {'name':'#3 Cylinder','radius': 10.79, 'height': 17.78, 'cost_per_can': 0.86},
    {'name':'#5','radius': 13.02, 'height': 14.29, 'cost_per_can': 0.83},
    {'name':'#6Z','radius': 5.40, 'height': 8.89, 'cost_per_can': 0.22},
    {'name':'#8Z short','radius': 6.83, 'height': 7.62, 'cost_per_can': 0.26},
    {'name':'#10','radius': 15.72, 'height': 17.78, 'cost_per_can': 1.53},
    {'name':'#211','radius': 6.83, 'height': 12.38, 'cost_per_can': 0.34},
    {'name':'#300','radius': 7.62, 'height': 11.27, 'cost_per_can': 0.38},
    {'name':'#303','radius': 8.10, 'height': 11.11, 'cost_per_can': 0.42},
    ]

    for can in data_cans:
        #print(f"Name: {lata['name']}, Radius: {lata['radius']}, Height: {lata['height']}, Cost per Can: {lata['cost_per_can']}")
        print(can['name'],storage_efficiency(compute_volume(can['radius'],can['height']),compute_surface_area(can['radius'],can['height'])))

def storage_efficiency(volume,surface_area):
    return round(volume/surface_area,2)

def compute_volume(radius,height):
    return math.pi * float(radius)**2 * float(height)


def compute_surface_area(radius,height):
    return 2*math.pi * float(radius) * (float(radius) + float(height))

main()



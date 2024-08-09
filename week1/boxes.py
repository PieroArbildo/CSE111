import math

def calc_boxes():
    number_items = int(input("Enter the number of items:"))
    items_per_box = int(input("Enter the number of items per box:"))
    boxes = math.ceil(number_items/items_per_box)
    print(f"For {number_items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.") 

calc_boxes()

import csv

def main():
    KEY_COLUMN_INDEX=0
    productos_dict = read_dictionary('products.csv',KEY_COLUMN_INDEX)
    print("All Products")
    print(productos_dict)

    request_dict = read_dictionary('request.csv',KEY_COLUMN_INDEX)
    print("Requested Items")
    
    for key2, value2 in request_dict.items():
        if key2 in productos_dict:
            value1 = productos_dict[key2]
            print(value1[1], value2[1], value1[2])
    

def read_dictionary(filename, key_column_index):
    dictionary={}

    with open(filename,'rt') as csv_products:
        reader = csv.reader(csv_products)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary
        

if __name__ == "__main__":
    main()
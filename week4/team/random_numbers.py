import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    append_random_numbers(numbers,3)
    print(f"numbers {numbers}")


def append_random_numbers(numbers_list,quantity=1):

    for _ in range(quantity):
        number_ramdom = round(random.uniform(0.0,1.0),1)
        numbers_list.append(number_ramdom)
        
  
if __name__ == "__main__":
    main()

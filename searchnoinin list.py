# Program to search for a number in a list
def search_number(lst, num):
    for item in lst:
        if item == num:
            print(f"{num} found in the list.")
            break
    else:
        print(f"{num} not found in the list.")

# Example usage
numbers = [2, 4, 6, 8, 10]
search_number(numbers, 6)  # Number found
search_number(numbers, 3)  # Number not found

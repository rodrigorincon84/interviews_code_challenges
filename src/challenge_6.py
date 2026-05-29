# Given an array, return the average
# If the array contains no numeric elements, return None

def all_numbers(array_):
    all_numbers_ = True
    for e in array_:
        if type(e) != int:
            all_numbers_ = False
            break
    return all_numbers_

def sum_array(array_):
    return array_[0] if len(array_) == 1 else array_[0] + sum_array(array_[1:])

if __name__ == '__main__':
    array = [3, 6, "9"]
    average = None
    if all_numbers(array):
        s = sum_array(array)
        print(f"Sum is {s}")
        average = s / len(array)
    print(f"Average is: {average}")


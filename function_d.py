def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    big_num = 0

    for num in numbers:
        if num > big_num:
            big_num = num
    
    return big_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))

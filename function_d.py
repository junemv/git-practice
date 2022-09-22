def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    big_num = 0

    for num in numbers:
        if num > big_num:
            big_num = num
    
    return big_num

>>>>>>> 752c8a09c3073018640ca393f80a3d895f9feca6

if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))

a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [0, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
a3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a4 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nOdds output:\n")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add necessary print statement to output only the odd values (hint, best if shown as a single line)
    # Date: 9/23/23, UCID: sb2648
    # This code filters out the odd values from an array and prints out the odd values array.
    odd_values = [i for i in arr if i % 2 != 0]  # List comprehension to filter out odd values.
    print(odd_values)   # Prints out odd values.
    
print("Problem 1")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value
    # Date: 9/24/23, UCID: sb2648
    # Iterating over the given list and checks if it is an element of integer or float type.
    # If it is a negative number, then it is converted to positve number using abs() function.
    # If it is a string, then it is first coverted to inteter value then it is coverted to a positive number and typecasted back to string type.
    positive_values = []
    for i in arr:
        if isinstance(i, (int, float)):
            positive_values.append(abs(i))
        elif isinstance(i, str) :
            positive_values.append(str(abs(int(i))))
        else:
            positive_values.append(i)
    
    for positive_value in positive_values:
        print(f"Value: {positive_value} , Type: {type(positive_value)}")

print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)
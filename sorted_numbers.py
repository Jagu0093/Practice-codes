def list_to_integer(digit_list):
    """Converts a list of digits to a single integer."""
    if not digit_list:  # Handle empty list case
        return 0  # Or raise an exception if an empty list is invalid input

    num_str = "".join(map(str, digit_list)) #Convert the list of integers to list of string then join them together
    return int(num_str)
number = 1308821
digits = str(number)
p_sorted_asc = list_to_integer(sorted(digits, reverse=True))
p_sorted_desc = list_to_integer(sorted(digits))
#num_list = [int(i) for i in p_sorted]

print(p_sorted_asc-p_sorted_desc)

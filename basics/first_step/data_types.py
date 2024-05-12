# var = input("Enter a data_type with first letter in capitals and full name: ")
# data_types = {'Integer' : 4 , 'Float' : 4, 'Long': 8, 'Double': 8 , 'Character': 1} 
# if var in data_types:
#     print(data_types[var])

# alternative way - this code printing 408 bytes as size.

import sys

data_type_name = input("Enter the data type name (e.g., int, float, str): ")

try:
    data_type = eval(data_type_name)
    size_in_bytes = sys.getsizeof(data_type)
    print(f"The size of {data_type_name} is {size_in_bytes} bytes.")
except (NameError, TypeError):
    print(f"Invalid data type name: {data_type_name}")    
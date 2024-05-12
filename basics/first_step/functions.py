# #code 1
# def my_sum(*args):
#   """This function sums an arbitrary number of arguments."""
#   result = 0
#   # Check if args is a list and unpack its elements
#   if isinstance(args, list):
#     for num in args:
#       result += num
#       # Modify the element inside the loop (demonstration)
#       num *= 2  # This modification will not affect the original list
 
#   else:
#     # Handle other types of arguments passed to *args
#     for num in args:
#       result += num
#   return result,args

# # Call the function with a list
# numbers = [1, 2, 3, 4, 5]
# total = my_sum(*numbers)  # Unpack the list elements using * 
# print(total[1]) # output: (1, 2, 3, 4, 5)- prints the tuple and there is no change in it.

# print(f"Original list (before modification): {numbers}")  #  list before modification [1, 2, 3, 4, 5]
# print(f"Sum (inside function): {total[0]}")  # Print the sum inside the function

# # Modify the original list after the function call
# numbers[0] = 100

# print(f"Original list (after modification): {numbers}") # output : [100, 2, 3, 4, 5]

# #---------------------------------------------------------------------------------
# #code 2
# def my_sum(numbers):  # Take the list directly as an argument (no need for *args)
#   """This function sums an arbitrary number of arguments (modifies the list)."""
#   result = 0
#   for i in range(len(numbers)):  # Use indexing to modify the original list
#     numbers[i] *= 2  # Modify the element at the current index
#     result += numbers[i]
#   return result

# # Call the function with a list
# numbers = [1, 2, 3, 4, 5]

# # Print the original list before the function call
# print(f"Original list (before function call): {numbers}") # output : [1, 2, 3, 4, 5]

# total = my_sum(numbers)  # Pass the list directly

# # Print the sum (inside function is not necessary here)
# # print(f"Sum (inside function): {total}")  # Uncomment if you want to see the sum inside the function

# # Print the list after the function call (shows the modification)
# print(f"Original list (after function call): {numbers}") # output: [2, 4, 6, 8, 10]

# #-------------------------------------------------------------------------------------------------------
# #code3
def modify_list_using_args(*args):
  args[0] = "Changed!"
    # Function takes arguments as a tuple using *args
  """This function demonstrates pass by reference with a list using *args."""
  # Since we use *args, the list elements are treated as individual arguments
  # Modify the first element (modifying the original list)

# Create a shopping list
shopping_list = ["apples", "bread", "milk"]

# Print the list before the function call
print(f"Shopping list (before): {shopping_list}")  # Output: ["apples", "bread", "milk"]

# Call the function, passing the list unpacked using *
modify_list_using_args(*shopping_list)

# Print the list after the function call
print(f"Shopping list (after): {shopping_list}")  # Output: ["Changed!", "bread", "milk"]

""" So what this code promised to do ( third code) it can't do ,args contains a tuple only and it's
immutable so we can't change like args[0]= 'amit', it's wrong, it throws error - TypeError: 'tuple' object does 
not support item assignment """

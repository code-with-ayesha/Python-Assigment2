# 10. **Get last element**
#     Fill out the function `get_last_element(lst)` which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# 11. **Get a List**
#     Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

#     Here's a sample run (user input is in blue):

#     ```
#     Enter a value: 1
#     Enter a value: 2
#     Enter a value: 3
#     Enter a value:
#     Here's the list: ['1', '2', '3']
#    ```

# **Get last element**
def get_last_element(lst):
    # Print the last element of the list
    print(lst[-1])

    # **Get a List**
def get_list_from_user():
    # Initialize an empty list to store user inputs
    user_list = []

    while True:
        # Ask the user to enter a value
        value = input("Enter a value: ")
        
        # Break the loop if the user presses Enter without typing anything
        if value == "":
            break
        
        # Add the value to the list
        user_list.append(value)
    
    # Print the list after exiting the loop
    print("Here's the list:", user_list)


# Example usage
get_list_from_user()



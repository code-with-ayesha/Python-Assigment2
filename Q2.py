# . **Agreement Boot**

#    Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also \_\_\_!" (the blank should be filled in with the user-inputted animal, of course).

#    Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

#    ```
#    What's your favorite animal? cow

#    My favorite animal is also cow!

#  ask athe user for their favourite animal
fav_animal= input("what's your favourite animal?")

#  Respond with the same animal
print(f"my favourite animal is also {fav_animal}")
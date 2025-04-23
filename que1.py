def reverse():
    user_input=input("Enter a string: ")
    reverse=''.join(reversed(user_input))
    return reverse
result=reverse()
print(f"The reverse is {result}")
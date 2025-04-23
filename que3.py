def palindrom():
    palindrome_number=input("Enter a string: ")
    string=''.join(reversed(palindrome_number))
    print(string)
    if string==palindrome_number:
        print("It is the palindrome")
    else: 
        print("No, it is not a palindrome")
palindrom()

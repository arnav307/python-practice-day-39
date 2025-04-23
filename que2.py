def vowels():
    count=0
    vowels=["a","e","i","o","u"]
    user=input("Enter a string you like :")
    for i in user:
        if i in vowels:
            count+=1
    return count
            
result=vowels()
print(f"There are {result}.")
user_input = input("enter a word ")

while user_input.isdigit():
    print("Enter a word instead")
    user_input = input("Enter a word ")
else: 
    print(user_input)

#resource: https://pynative.com/python-check-user-input-is-number-or-string/
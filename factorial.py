'''find factyorial of any number'''
factorial=1
user_input=int(input("Please enter positive discrete number whose factorial you want to know"))
user_input1=user_input
while (user_input !=1):
    factorial=int(user_input)*int(factorial)
    user_input =(user_input -1)


print("factorial of",user_input1,"is",factorial)



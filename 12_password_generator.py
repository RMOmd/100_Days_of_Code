import random
print("Welcome to the PasswordGenerator")
letters = ['q', 'w', 'e', 'r', 't' ,'y' ,'u' ,'i' ,'o', 'p', 'a', 's', 'd','f' ,'g' ,'h' ,'j' ,'k' ,'l' ,'z' ,'x' ,'c' ,'v' ,'b' ,'n', 'm', 'Q', 'W', 'E', 'R','T' ,'Y' ,'U' ,'I' ,'O' ,'P', 'A', 'S', 'D' ,'F', 'G', 'H', 'J', 'K', 'L', 'Z','X', 'C', 'V', 'B', 'N', 'M']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']
nr_letters = int(input(f"How many letters would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

'''
# Easy method
u_pass = ""
for i in range(1, nr_letters + 1):
    u_pass += random.choice(letters)
for i  in range(1, nr_numbers + 1):
    u_pass += random.choice(numbers)
for i in range(1, nr_symbols + 1):
    u_pass += random.choice(symbols)
print(u_pass)
'''

# Hard level
u_pass = []
for i in range(1, nr_letters + 1):
    u_pass += random.choice(letters)
for i  in range(1, nr_numbers + 1):
    u_pass += random.choice(numbers)
for i in range(1, nr_symbols + 1):
    u_pass += random.choice(symbols)
random.shuffle(u_pass)
password = ""
for char in u_pass:
    password += char
    
print(f"Your password is: {password}")
    

import secrets
import string

rand_ascii = string.ascii_letters
rand_up = string.ascii_uppercase
rand_down = string.ascii_lowercase
rand_digits = string.digits
rand_punch = string.punctuation

rand_total = rand_up + rand_punch + rand_ascii + rand_digits + rand_down

password = ''
pass_len = int(input("Enter the length of the password : "))
for i in range(pass_len):
    password += ''.join(secrets.choice(rand_total))

print("Your random password : " + str(password))
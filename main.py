
import secrets
import string

def password_gen(password_length):

    characters = string.ascii_letters + string.digits
    secure_password = ''.join(secrets.choice(characters) for i in range(password_length))
    return secure_password

def main():

    chosen_length = int(input("Enter the number of digits for password:"))
    print("Secure Password Generated: ", password_gen(chosen_length))

main()

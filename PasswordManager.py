from cryptography.fernet import Fernet
'''
def generate_key():
    key = Fernet.generate_key()
    with open('Encrypter.key','wb') as encrypter:
        encrypter.write(key)
        
generate_key()
'''

def load_key():
    with open('Encrypter.key','rb') as f:
        key = f.read()
    return key

def add_password():
    username = input('Enter Username: ')
    pass_word = input('Enter password: ')
    with open('Passwords.txt', 'a') as file:
        file.write(username
                   + ' | '
                   + encryption.encrypt(pass_word.encode()).decode()
                   + '\n')

def view_passwords():
    with open('Passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("Username: " + user + ", Password: " + encryption.decrypt(passw.encode()).decode())


choice = input('Would you like to start the program? (yes/no): '.lower())
key = load_key()
encryption = Fernet(key)
if choice == 'yes':
    while True:
        option = input('''\nSelect option by number:-
1: Add new
2: View passwords
3: Quit
Option: ''')
        if option == '1':
            add_password()
        elif option == '2':
            view_passwords()
        elif option == '3':
            print('Quitting program....')
            break
else:
    print('Thank You!')
    print('Quitting program....')
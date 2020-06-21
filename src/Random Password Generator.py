import random
import string
# I am using a 10000 word csv list for passwords
import csv 
import os


choice = ''

# input for while loop
while choice != '3':
    choice = input('''What would you like to do today?:
    Generate Random Password (1)
    Random Word Password (2)
    exit (3)
    ''')

    if choice == '1':
        answer = int(input('How many characters do you want in your password?: '))
        print()

        # function includes pythons list of upper and lower case of the alphabet
        # I also put in random characters to also add to the for loop
        def randomPass(length = answer):
            characters_numbers = string.ascii_letters + string.digits + '!@#$%^&*()_+'
            return ''.join(random.choice(characters_numbers) for num in range(length))

        print('Here is your password: ' + randomPass())
        print()

    elif choice == '2':
        word_amount = int(input('How many random words would you like?: '))
        password_words = []
        final_password = ''

        # opens the csv file and appends them to a list
        word_list_path = os.path.join(os.path.dirname(__file__), '10000Words.csv')
        for i in range(0, word_amount):
            with open(word_list_path) as f:
                reader = csv.reader(f)
                password_words.append(random.choice(list(reader)))
                # puts the words that were randomly chosen into one big string
                final_password = ("".join(["".join(x) for x in password_words]))
                

        print()
        print (final_password)
        print()
print()
print('Goodbye')

# thanks for checking it out
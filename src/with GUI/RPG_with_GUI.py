from Password_GeneratorUI import *
import sys
import random
import string
# I am using a 10000 word csv list for passwords
import csv 
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

class App(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.generate_password.clicked.connect(self.randomPass)
    
    def randomPass(self, length):
        #combobox list in the application
        choice = self.word_or_char_password.currentText()
        if choice == 'Random Character Password':
            #reads the value of the counter in the app
            #max of 24
            length = self.amount.value()
            characters_numbers = string.ascii_letters + string.digits + '!@#$%^&*()_+'
            characters_numbers = ''.join(random.choice(characters_numbers) for num in range(int(length)))
            #writing the passwords to the text box
            self.textBrowser.setText(characters_numbers)
        
        elif choice == 'Random Word Password':
            password_words = []
            final_password = ''

            # opens the csv file and appends them to a list
            word_list_path = os.path.join(os.path.dirname(__file__), '10000Words.csv')
            #reads the value of the counter in the app
            #max of 24
            length = self.amount.value()
            for i in range(0, length):
                with open(word_list_path) as f:
                    reader = csv.reader(f)
                    password_words.append(random.choice(list(reader)))
                    # puts the words that were randomly chosen into one big string
                    final_password = ("".join(["".join(x) for x in password_words]))
                    #writing the passwords to the text box
                    self.textBrowser.setText(final_password)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = App(MainWindow)

MainWindow.show()
app.exec_()
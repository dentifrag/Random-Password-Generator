


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 391)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generate_password = QtWidgets.QPushButton(self.centralwidget)
        self.generate_password.setGeometry(QtCore.QRect(80, 220, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.generate_password.setFont(font)
        self.generate_password.setObjectName("generate_password")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 150, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.word_or_char_password = QtWidgets.QComboBox(self.centralwidget)
        self.word_or_char_password.setGeometry(QtCore.QRect(160, 100, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.word_or_char_password.setFont(font)
        self.word_or_char_password.setObjectName("word_or_char_password")
        self.word_or_char_password.addItem("")
        self.word_or_char_password.addItem("")
        self.amount = QtWidgets.QSpinBox(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(240, 180, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.amount.setFont(font)
        self.amount.setMaximum(24)
        self.amount.setObjectName("amount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(300, 220, 161, 71))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.generate_password.setText(_translate("MainWindow", "Generate Password"))
        self.label.setText(_translate("MainWindow", "Number of Characters/Words in Password"))
        self.word_or_char_password.setItemText(0, _translate("MainWindow", "Random Character Password"))
        self.word_or_char_password.setItemText(1, _translate("MainWindow", "Random Word Password"))
        self.label_2.setText(_translate("MainWindow", "What would you like to do today?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

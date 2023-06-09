# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalguiredo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelInput = QtWidgets.QLabel(self.centralwidget)
        self.labelInput.setGeometry(QtCore.QRect(20, 40, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.labelInput.setFont(font)
        self.labelInput.setObjectName("labelInput")
        self.leInput = QtWidgets.QLineEdit(self.centralwidget)
        self.leInput.setGeometry(QtCore.QRect(20, 90, 481, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(True)
        self.leInput.setFont(font)
        self.leInput.setObjectName("leInput")
        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelOutput.setGeometry(QtCore.QRect(10, 380, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.labelOutput.setFont(font)
        self.labelOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOutput.setObjectName("labelOutput")
        self.radio_add = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_add.setGeometry(QtCore.QRect(20, 140, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.radio_add.setFont(font)
        self.radio_add.setObjectName("radio_add")
        self.radio_subtract = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_subtract.setGeometry(QtCore.QRect(260, 140, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.radio_subtract.setFont(font)
        self.radio_subtract.setObjectName("radio_subtract")
        self.radio_multiply = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_multiply.setGeometry(QtCore.QRect(20, 220, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.radio_multiply.setFont(font)
        self.radio_multiply.setObjectName("radio_multiply")
        self.radio_divide = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_divide.setGeometry(QtCore.QRect(260, 220, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(26)
        self.radio_divide.setFont(font)
        self.radio_divide.setObjectName("radio_divide")
        self.button_calc = QtWidgets.QPushButton(self.centralwidget)
        self.button_calc.setGeometry(QtCore.QRect(60, 310, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.button_calc.setFont(font)
        self.button_calc.setObjectName("button_calc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.radio_add.setChecked(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "List Calculator"))
        self.labelInput.setText(_translate("MainWindow", "Input any amount of #\'s seperated by one space each:"))
        self.labelOutput.setText(_translate("MainWindow", "--------------------"))
        self.radio_add.setText(_translate("MainWindow", "Add All"))
        self.radio_subtract.setText(_translate("MainWindow", "Subtract All"))
        self.radio_multiply.setText(_translate("MainWindow", "Multiply All"))
        self.radio_divide.setText(_translate("MainWindow", "Divide All"))
        self.button_calc.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

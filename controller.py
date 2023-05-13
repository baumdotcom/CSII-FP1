from PyQt5.QtWidgets import *
from finalguiredo import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_calc.clicked.connect(lambda: self.calc())

    def calc(self):
        values = []
        total = 0
        try:
            values = self.leInput.text().split()
            values = [float(a) for a in values]

            if self.radio_add.isChecked():
                total = sum(values)
            elif self.radio_subtract.isChecked():
                total = values[0]
                for i in values:
                    if i == 0:
                        continue
                    else:
                        total -= i
            elif self.radio_multiply.isChecked():
                total = 1

                for i in values:
                    total *= i
            elif self.radio_divide.isChecked():
                total = values[0]
                if 0 in values:
                    raise ZeroDivisionError
                else:
                    for i in values[1:]:
                        total /= i

            self.labelOutput.setText(str(total))
        except TypeError:
            self.labelOutput.setText("Numbas only pretty please")
        except ZeroDivisionError:
            self.labelOutput.setText("Can't divide by zero!")


#Part 1 Final Project by Sam Baumert

from controller import *

def main():
    app = QApplication([])
    MainWindow = Controller()
    MainWindow.show()
    app.exec()

if __name__ == '__main__':
    main()

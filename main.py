#no need to install anything
import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import Qt
# just change the name
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # the way app working
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        # khai bao nut an
        self.uic.Button_cancel.clicked.connect(self.close)
        self.uic.Button_login.clicked.connect(self.login)
        self.uic.Button_logout.clicked.connect(self.logout)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            print("press enter")
            self.login()
        else:
            super().keyPressEvent(event)

    def login(self):
        ID = self.uic.screen_id.text()
        password = self.uic.screen_password.text()
        print("ID: ", ID)
        print("password: ", password)
        if ID == "user" and password == "1":
            self.uic.stackedWidget.setCurrentWidget(self.uic.page_2)
        elif ID != "user":
            QMessageBox.information(self, "hello", "your ID is wrong")
        elif password != "1":
            QMessageBox.information(self, "hello", "your password is wrong")
        else:
            QMessageBox.information(self, "hello", "your password or ID are wrong")

    def logout(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_1)
        self.uic.screen_password.setText("")

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
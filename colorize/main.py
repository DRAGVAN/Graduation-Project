import sys, os
# if hasattr(sys, 'frozen'):
#     os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot
# from ui_LoginWindow import Ui_LoginWindow
# from ui_AlertDialog import Ui_AlertDialog
from loginWindow import QLoginWindow
from userWindow import QUserWindow
from signupWindow import QSignupWindow
from changePasswordWindow import QChangePasswordWindow
import sys


def user_window(str):
    login.close()
    login.ui.passwordLineEdit.clear()
    user.show()
    user.username = str

def user2log_window():
    user.close()
    login.show()

def sign_window():
    login.close()
    login.ui.passwordLineEdit.clear()
    signup.show()

def sign2log_window():
    signup.close()
    login.show()

def change2login_window():
    change.close()
    login.show()

def user2change_window(str):
    user.close()
    change.show()
    change.username = str

def change2user_window():
    change.close()
    user.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = QLoginWindow()
    signup = QSignupWindow()
    change = QChangePasswordWindow()
    user = QUserWindow()

    login.show()

    login.login_signal.connect(user_window)
    login.signup_signal.connect(sign_window)
    signup.signup_signal.connect(sign2log_window)
    change.change2login_signal.connect(change2login_window)
    change.change2user_signal.connect(change2user_window)
    user.user2change_signal.connect(user2change_window)
    user.user2log_signal.connect(user2log_window)

    sys.exit(app.exec_())
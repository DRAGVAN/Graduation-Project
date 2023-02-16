import sys, os
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from ui_LoginWindow import Ui_LoginWindow
# from ui_AlertDialog import Ui_AlertDialog
# from ui_UserWindow import Ui_UserWindow


import sys

class QLoginWindow(QWidget):
    login_signal = pyqtSignal(str)
    signup_signal = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.on_btnLogin_clicked)
        self.ui.btnSignup.clicked.connect(self.on_btnSignup_clicked)
        self.ui.btnForgot.clicked.connect(self.on_btnForgot_clicked)
        # self.setFixedSize(300, 200)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap('./colorize/background/login/back.jpg')))
        self.setPalette(palette)

    @pyqtSlot()
    def on_btnLogin_clicked(self):
        username = self.ui.usernameLineEdit.text()
        passwd = self.ui.passwordLineEdit.text()

        if(username == "" or passwd == ""):
            return
        
        try:
            f = open("colorize/userdata/register", 'r')
            user=eval(f.read())
            f.close()
        except:
            f = open("colorize/userdata/register", 'w')
            f.write("{'root': 'password'}")
            print('write')
            f.close()

        # user = {'root': 'password'}
        reply = QMessageBox(self)

        log_error_dialog = QDialog(self)
        if username not in user:
            reply.question(self, 'alert', "unername not exist!", QMessageBox.Yes)
            # diagUi = Ui_AlertDialog("unername not exist!")
            # diagUi.setupUi(log_error_dialog)
            # log_error_dialog.show()
            # print('username not exist')
        elif passwd != user[username]:
            reply.question(self, 'alert', "password error!", QMessageBox.Yes)
            # diagUi = Ui_AlertDialog("password error!")
            # diagUi.setupUi(log_error_dialog)
            # log_error_dialog.show()
            # print('pwd error')
        else:
            self.login_signal.emit(username)
            # userWindow = QUserWindow(self)
            # userWindow.logout_signal.connect(self.show_again)
            # userWindow.show()
            # self.hide()
            # print('success')

    def on_btnSignup_clicked(self):
        self.signup_signal.emit("sign up")

    def on_btnForgot_clicked(self):
        QMessageBox.question(self, "alert", "please contact QQ: 666666", QMessageBox.Yes)

    # def show_again(self):
    #     self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = QLoginWindow()
    login.show()
    sys.exit(app.exec_())
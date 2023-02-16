from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from ui_AlertDialog import Ui_AlertDialog
from ui_UserWindow import Ui_UserWindow
from ui_SignupWindow import Ui_SignupWindow
from loginWindow import QLoginWindow
from userWindow import QUserWindow
import sys

class QSignupWindow(QWidget):
    signup_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignupWindow()
        self.ui.setupUi(self)
        self.ui.btnSignup.clicked.connect(self.on_btnSignup_clicked)
        self.ui.btnCancle.clicked.connect(self.on_btnCancle_clicked)
        # self.setFixedSize(250, 250)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap('./background/sign/sign.jpg')))
        self.setPalette(palette)

    @pyqtSlot()

    def on_btnSignup_clicked(self):
        # reply = QMessageBox(self)
        username = self.ui.usernameLineEdit.text()
        passwd = self.ui.passwordLineEdit.text()
        passwdConfirm = self.ui.confirmLineEdit.text()
        if(username == "" or passwd == ""):
            # log_error_dialog = QDialog(self)
            # diagUi = Ui_AlertDialog("both username and passwd")
            # diagUi.setupUi(log_error_dialog)
            # log_error_dialog.show()
            return
        if passwd != passwdConfirm:
            QMessageBox.question(self, 'alert', "The two passwords you entered were inconsistent, please try again", QMessageBox.Yes)
        elif ' ' in passwd or ' ' in username:
            QMessageBox.question(self, 'alert', "Username and password cannot have spaces.", QMessageBox.Yes)
        else:
            try:
                f = open('userdata/register', 'r')
                user = eval(f.read())
                f.close()
            except:
                f = open('userdata/register', 'w')
                f.write("{'root': 'passwd'}")
                f.close
                user = {'root': 'passwd'}
            if username in user:
                QMessageBox.question(self, 'alert', "This username already exists.", QMessageBox.Yes)
            else:
                user[username] = passwd
                QMessageBox.question(self, 'alert', "Register successfully, please log in again.", QMessageBox.Yes)
                f = open('userdata/register', 'w')
                f.write(str(user))
                f.close()
                self.signup_signal.emit("sign up success")
                # self.hide()


    def on_btnCancle_clicked(self):
        self.signup_signal.emit("sign up cancled")
        # self.hide()
        


        
        # try:
        #     f = open("/userdata/register.txt", 'r')
        #     user=eval(f.read())
        #     f.close()
        # except:
        # f = open("user.txt", 'w')
        # f.write("{'root': 'password'}")
        # f.close
        # user = {'root': 'password'}

        # if username not in user:
        #     print('username not exist')
        # elif passwd != user[username]:
        #     print('pwd error')
        # else:
        #     userWindow = QUserWindow(self)
        #     userWindow.show()
        #     self.hide()
        #     print('success')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign = QSignupWindow()
    sign.show()
    sys.exit(app.exec_())
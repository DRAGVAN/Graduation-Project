from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from ui_AlertDialog import Ui_AlertDialog
from ui_UserWindow import Ui_UserWindow
from ui_ChangePasswordWindow import Ui_ChangePasswordWindow
from loginWindow import QLoginWindow
from userWindow import QUserWindow
import sys

class QChangePasswordWindow(QWidget):
    change2login_signal = pyqtSignal(str)
    change2user_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ChangePasswordWindow()
        self.ui.setupUi(self)
        self.ui.btnConfirm.clicked.connect(self.on_btnConfirm_clicked)
        self.ui.btnCancle.clicked.connect(self.on_btnCancle_clicked)
        # self.setFixedSize(250, 250)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap('background/sign/sign.jpg')))
        self.setPalette(palette)

        self.username = ''

    @pyqtSlot()

    def on_btnConfirm_clicked(self):
        # reply = QMessageBox(self)
        old = self.ui.oldPasswordLineEdit.text()
        new = self.ui.newPasswordLineEdit.text()
        confirm = self.ui.confirmLineEdit.text()

        if(old == "" or new == "" or confirm == ""):
            return

        if new != confirm:
            QMessageBox.question(self, 'alert', "The two passwords you entered were inconsistent, please try again", QMessageBox.Yes)
        elif ' ' in new:
            QMessageBox.question(self, 'alert', "password cannot have spaces.", QMessageBox.Yes)
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
            if user[self.username] == old:
                if new == old:
                    QMessageBox.question(self, 'error', "The new password cannot be the same as the old password, please try  again", QMessageBox.Yes)
                else:
                    user[self.username] = new
                    QMessageBox.question(self, 'success', "change password successfully, please log in again.", QMessageBox.Yes)
                    f = open('userdata/register', 'w')
                    f.write(str(user))
                    f.close
                    self.change2login_signal.emit("sign up success")
                # self.hide()
            else:
                QMessageBox.question(self, 'error', "The old password that you typed is wrong, please try  again", QMessageBox.Yes)



    def on_btnCancle_clicked(self):
        self.change2user_signal.emit("change password cancled")
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
    sign = QChangePasswordWindow()
    sign.show()
    sys.exit(app.exec_())
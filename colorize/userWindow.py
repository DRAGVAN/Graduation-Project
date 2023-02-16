import sys, cv2
import numpy as np
import os

from PyQt5.QtWidgets import (QApplication, QMessageBox, QMainWindow, QDialog, QFileDialog, QGraphicsScene, QDesktopWidget, QWidget)
from PyQt5.QtCore import pyqtSlot, QDir, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtGui import QPalette, QBrush, QPixmap

# from process import Login
from ui_UserWindow import Ui_UserWindow
from ui_AlertDialog import Ui_AlertDialog

class QUserWindow(QMainWindow):
    user2log_signal = pyqtSignal(str)
    user2change_signal = pyqtSignal(str)
    # dialog = QDialog()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UserWindow()
        self.ui.setupUi(self)

        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap('background/user/user2.jpg')))
        self.setPalette(palette)

        self.ui.actionadd_dataset.triggered.connect(self.open_dataset)
        self.ui.actiondelete_dataset.triggered.connect(self.delete_dataset)
        self.ui.actionlog_out.triggered.connect(self.log_out)
        self.ui.actionswitch_account.triggered.connect(self.switch_account)
        self.ui.actionchange_password.triggered.connect(self.change_password)
        self.ui.actioninstructions.triggered.connect(self.show_instructions)
        self.ui.actioncontact_administrator.triggered.connect(self.contact_administrator)
        self.ui.actionreport_error.triggered.connect(self.report_error)
        self.ui.actionprocessed.triggered.connect(self.processed)
        self.ui.actionunprocessed.triggered.connect(self.unprocessed)
        self.ui.actionmanage_information.triggered.connect(self.manage_information)
        self.ui.menuExit.menuAction().triggered.connect(self.out)

        self.ui.btnOpenPic.clicked.connect(self.on_btnOpenPic_clicked)
        self.ui.btnClearPic.clicked.connect(self.on_btnClearPic_clicked)
        self.ui.btnMethod_1.clicked.connect(self.on_btnMethod_1_clicked)
        self.ui.btnMethod_2.clicked.connect(self.on_btnMethod_2_clicked)
        self.ui.btnMethod_3.clicked.connect(self.on_btnMethod_3_clicked)
        self.ui.btnSavePic.clicked.connect(self.on_btnSavePic_clicked)

        self.unProcessedScene = QGraphicsScene()
        self.processedScene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.unProcessedScene)
        self.ui.graphicsView_2.setScene(self.processedScene)

        self.filename = ""
        self.processedFlag = False

        self.username = ''

        # self.setCenter()
        self.move(320, 160)

    def setCenter(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        width = (screen.width() - size.width()) / 2
        height = (screen.height() - size.height()) / 2
        print(width)
        print(height)
        # self.move((screen.width() - size.width()) / 2,  (screen.height() - size.height()) / 2)
        # self.move(width, height)
    def displayImageToView2(self, method, ckpt):

        with open('method_images/' + str(method) + '.jpg', 'rb') as f:
            img = f.read()
        with open("CycleGAN/datasets/apple2orange/testB/1.jpg", 'wb') as f:
            f.write(img)

        with open(self.filename, 'rb') as f:
            img = f.read()
        with open("CycleGAN/datasets/apple2orange/testA/1.jpg", 'wb') as f:
            f.write(img)
        os.system("python CycleGAN/test.py --dataroot CycleGAN\\datasets\\apple2orange --name " + ckpt + " --model cycle_gan --gpu_ids -1")
        img = cv2.imread("results/" + ckpt + "/test_latest/images/1_fake_B.png")
        with open("results/l2g/test_latest/images/1_fake_B.png", 'rb') as f:
            self.img_b = f.read()
        cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        y, x = img.shape[:-1]
        frame = QImage(cvimg, x, y, QImage.Format_RGB888)
        self.processedScene.clear()
        self.pix = QPixmap.fromImage(frame)
        self.processedScene.addPixmap(self.pix)
        # login = Login(self.filename, method) 
        # self.img_b = login.process()
        self.processedFlag = True
        # img_np = np.frombuffer(self.img_b, np.uint8)
        # img = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)
        # cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # y, x = img.shape[:-1]
        # frame = QImage(cvimg, x, y, QImage.Format_RGB888)
        # self.processedScene.clear()
        # self.pix = QPixmap.fromImage(frame)
        # self.processedScene.addPixmap(self.pix)

    @pyqtSlot()
    def open_dataset(self):
        curPath = QDir.currentPath() + "//dataset"
        QFileDialog.getOpenFileName(self, "choose a file to open", curPath)

    def delete_dataset(self):
        curPath = QDir.currentPath() + "//dataset"
        QFileDialog.getOpenFileName(self,"Select a file and right click to delete", curPath)

    def log_out(self):
        self.user2log_signal.emit("log_out")

    def switch_account(self):
        self.user2log_signal.emit("switch_account")

    def change_password(self):
        self.user2change_signal.emit(self.username)

    def show_instructions(self):
        QMessageBox.question(self, 'instruction', "        1.click open to select the picture,\n\
        2.click the method1~method3 button to color the picture in three different ways,\n\
        3.click the clear button to clear the left and right pictures at the same time,\n\
        4.Once the image is processed, you can click the Save button to save the processed image.", QMessageBox.Yes)
        # dialog = QDialog(self)
        # diagUi = Ui_AlertDialog("Click open to select the picture, \
        #                         click the method1~method3 button to color the picture in three different ways, \
        #                         click the clear button to clear the left and right pictures at the same time")
        # diagUi.setupUi(dialog)
        # dialog.show()
    def contact_administrator(self):
        QMessageBox.question(self, 'contact means', "QQ: 666666", QMessageBox.Yes)
        # dialog = QDialog(self)
        # diagUi = Ui_AlertDialog("QQ:666666")
        # diagUi.setupUi(dialog)
        # dialog.show()
    def report_error(self):
        QMessageBox.question(self, 'Thanks for your feedback', "please contact the administrator", QMessageBox.Yes)

    def manage_information(self):
        print('none')

    def processed(self):
        curPath = QDir.currentPath() + "/saved"
        QFileDialog.getOpenFileName(self, "processed", curPath)

    def unprocessed(self):
        curPath = QDir.currentPath() + "/dataset"
        QFileDialog.getOpenFileName(self, "unprocessed", curPath)

    def out(self):
        self.close()

    def on_btnOpenPic_clicked(self):
        curPath = QDir.currentPath() + "/dataset"
        dlgTitle = "choose a picture"
        filt = "picture files(*.jpg *.jpeg *.png)"
        filename, filtUsed = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
        if(filename == ""): return
        print('open success')
        self.filename = filename
        if(self.processedFlag == True):
            self.processedScene.clear()
            self.processedFlag = False
        img = cv2.imread(self.filename)
        cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        y, x = img.shape[:-1]
        frame = QImage(cvimg, x, y, QImage.Format_RGB888)
        self.unProcessedScene.clear()
        self.pix = QPixmap.fromImage(frame)
        self.unProcessedScene.addPixmap(self.pix)

    def on_btnClearPic_clicked(self):
        if(self.filename == ""): return
        print('clear success')
        self.filename = ""
        self.unProcessedScene.clear()
        if(self.processedFlag == True):
            self.processedScene.clear()


    def on_btnMethod_1_clicked(self):
        if(self.filename == ""): 
            print('file name is null')
            return
        # print(self.filename)

        self.displayImageToView2('1', 'l2g')
        print("method 1 success")

    def on_btnMethod_2_clicked(self):
        if(self.filename == ""): return
        self.displayImageToView2('2', 'l2y')
        print("method 2 success")

    def on_btnMethod_3_clicked(self):
        if(self.filename == ""): return
        self.displayImageToView2('3', 'l2b')
        print("method 3 success")
        
    def on_btnSavePic_clicked(self):
        if(self.filename == "" or self.processedFlag == False): return
        filename = self.filename.split('/')[-1]
        curPath = QDir.currentPath() + "/saved/" + filename
        print(curPath)
        dlgTitle = "choose a path"
        filt = "*.jpg;; *.jpeg;; *.png"
        savedFileName, filtUsed = QFileDialog.getSaveFileName(self, dlgTitle, curPath, filt)
        if(savedFileName == ""): return

        print('saved success')
        # reply = QMessageBox(self)
        QMessageBox.question(self, 'alert', "saved success", QMessageBox.Yes)
        # saved_diag = QDialog(self)
        # diagUi = Ui_AlertDialog("Saved Success")
        # diagUi.setupUi(saved_diag)
        # saved_diag.show()
        # cv2.imwrite(savedFileName, )
        with open(savedFileName, 'wb') as f:
            f.write(self.img_b)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QUserWindow()
    main.show()
    print(main.width())
    print(main.height())
    sys.exit(app.exec_())
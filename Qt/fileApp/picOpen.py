import sys, cv2
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QInputDialog, QGraphicsScene)
from PyQt5.QtCore import Qt, pyqtSlot, QDir, QTime
from PyQt5.QtGui import QPalette, QColor, QFont, QImage, QPixmap
from picUI import Ui_Dialog

class QmyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_btnOpen_clicked)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.show()

    @pyqtSlot()
    def on_btnOpen_clicked(self):
        curPath = QDir.currentPath()
        dlgTitle = "choose a picture"
        filt = "all files(*.*);;text files(*.txt);;picture files(*.jpg *.gif *.png)"
        filename, filtUsed = QFileDialog.getOpenFileName(self, dlgTitle, curPath, filt)
        img = cv2.imread(filename)
        cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        y, x = img.shape[:-1]
        frame = QImage(cvimg, x, y, QImage.Format_RGB888)
        self.scene.clear()
        self.pix = QPixmap.fromImage(frame)
        self.scene.addPixmap(self.pix)
        self.scene.add

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QmyDialog()
    main.show()
    sys.exit(app.exec_())
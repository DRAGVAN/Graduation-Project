# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userWindow/userWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        # UserWindow.resize(569, 381)
        self.centralWidget = QtWidgets.QWidget(UserWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnMethod_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnMethod_1.setIconSize(QtCore.QSize(14, 14))
        self.btnMethod_1.setObjectName("btnMethod_1")
        self.gridLayout.addWidget(self.btnMethod_1, 0, 0, 1, 1)
        self.btnMethod_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnMethod_2.setIconSize(QtCore.QSize(128, 14))
        self.btnMethod_2.setObjectName("btnMethod_2")
        self.gridLayout.addWidget(self.btnMethod_2, 0, 1, 1, 1)
        self.btnMethod_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnMethod_3.setObjectName("btnMethod_3")
        self.gridLayout.addWidget(self.btnMethod_3, 0, 2, 1, 1)

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_2.setMinimumWidth(260)
        self.graphicsView_2.setMinimumWidth(260)
        self.graphicsView_2.setStyleSheet("background: transparent;border:1px solid ")

        self.gridLayout.addWidget(self.graphicsView_2, 1, 0, 1, 3)
        self.btnSavePic = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSavePic.setObjectName("btnSavePic")
        self.gridLayout.addWidget(self.btnSavePic, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnOpenPic = QtWidgets.QPushButton(self.groupBox)
        self.btnOpenPic.setObjectName("btnOpenPic")
        self.gridLayout_2.addWidget(self.btnOpenPic, 0, 1, 1, 1)
        # self.btnOpenPic.setStyleSheet("background: transparent;border:1px solid")

        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox)
        self.graphicsView.setMinimumWidth(260)
        self.graphicsView.setMinimumHeight(260)
        self.graphicsView.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setStyleSheet("background: transparent;border:1px solid ")

        self.gridLayout_2.addWidget(self.graphicsView, 1, 0, 1, 3)
        self.btnClearPic = QtWidgets.QPushButton(self.groupBox)
        self.btnClearPic.setIconSize(QtCore.QSize(14, 14))
        self.btnClearPic.setObjectName("btnClearPic")
        self.gridLayout_2.addWidget(self.btnClearPic, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        UserWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(UserWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 569, 19))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuview_dataset = QtWidgets.QMenu(self.menuFile)
        self.menuview_dataset.setObjectName("menuview_dataset")
        self.menulog_out = QtWidgets.QMenu(self.menuBar)
        self.menulog_out.setObjectName("menulog_out")
        self.menuhelp = QtWidgets.QMenu(self.menuBar)
        self.menuhelp.setObjectName("menuhelp")
        self.menuExit = QtWidgets.QMenu(self.menuBar)
        self.menuExit.setObjectName("menuExit")
        UserWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(UserWindow)
        self.statusBar.setObjectName("statusBar")
        UserWindow.setStatusBar(self.statusBar)
        self.actionadd_dataset = QtWidgets.QAction(UserWindow)
        self.actionadd_dataset.setObjectName("actionadd_dataset")
        self.actiondelete_dataset = QtWidgets.QAction(UserWindow)
        self.actiondelete_dataset.setObjectName("actiondelete_dataset")
        self.actionlog_out = QtWidgets.QAction(UserWindow)
        self.actionlog_out.setObjectName("actionlog_out")
        self.actionswitch_account = QtWidgets.QAction(UserWindow)
        self.actionswitch_account.setObjectName("actionswitch_account")
        self.actionchange_password = QtWidgets.QAction(UserWindow)
        self.actionchange_password.setObjectName("actionchange_password")
        self.actioninstructions = QtWidgets.QAction(UserWindow)
        self.actioninstructions.setObjectName("actioninstructions")
        self.actioncontact_administrator = QtWidgets.QAction(UserWindow)
        self.actioncontact_administrator.setObjectName("actioncontact_administrator")
        self.actionreport_error = QtWidgets.QAction(UserWindow)
        self.actionreport_error.setObjectName("actionreport_error")
        self.actionprocessed = QtWidgets.QAction(UserWindow)
        self.actionprocessed.setObjectName("actionprocessed")
        self.actionunprocessed = QtWidgets.QAction(UserWindow)
        self.actionunprocessed.setObjectName("actionunprocessed")
        self.actionmanage_information = QtWidgets.QAction(UserWindow)
        self.actionmanage_information.setObjectName("actionmanage_information")
        self.menuview_dataset.addAction(self.actionprocessed)
        self.menuview_dataset.addAction(self.actionunprocessed)
        self.menuFile.addAction(self.menuview_dataset.menuAction())
        self.menuFile.addAction(self.actionadd_dataset)
        self.menuFile.addAction(self.actiondelete_dataset)
        self.menulog_out.addAction(self.actionmanage_information)
        self.menulog_out.addAction(self.actionswitch_account)
        self.menulog_out.addAction(self.actionchange_password)
        self.menulog_out.addAction(self.actionlog_out)
        self.menuhelp.addAction(self.actioninstructions)
        self.menuhelp.addAction(self.actioncontact_administrator)
        self.menuhelp.addAction(self.actionreport_error)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menulog_out.menuAction())
        self.menuBar.addAction(self.menuhelp.menuAction())
        self.menuBar.addAction(self.menuExit.menuAction())

        self.retranslateUi(UserWindow)
        # QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "colorize"))
        self.groupBox_2.setTitle(_translate("UserWindow", "processed"))
        self.btnMethod_1.setText(_translate("UserWindow", "method 1"))
        self.btnMethod_2.setText(_translate("UserWindow", "method 2"))
        self.btnMethod_3.setText(_translate("UserWindow", "method 3"))
        self.btnSavePic.setText(_translate("UserWindow", "save picture"))
        self.groupBox.setTitle(_translate("UserWindow", "unprocessed"))
        self.btnOpenPic.setText(_translate("UserWindow", "open picture"))
        self.btnClearPic.setText(_translate("UserWindow", "clear picture"))
        self.menuFile.setTitle(_translate("UserWindow", "File"))
        self.menuview_dataset.setTitle(_translate("UserWindow", "view dataset"))
        self.menulog_out.setTitle(_translate("UserWindow", "Account"))
        self.menuhelp.setTitle(_translate("UserWindow", "Help"))
        self.menuExit.setTitle(_translate("UserWindow", "Exit"))
        self.actionadd_dataset.setText(_translate("UserWindow", "add dataset"))
        self.actiondelete_dataset.setText(_translate("UserWindow", "delete dataset"))
        self.actionlog_out.setText(_translate("UserWindow", "log out"))
        self.actionswitch_account.setText(_translate("UserWindow", "switch account"))
        self.actionchange_password.setText(_translate("UserWindow", "change password"))
        self.actioninstructions.setText(_translate("UserWindow", "instructions"))
        self.actioncontact_administrator.setText(_translate("UserWindow", "contact administrator"))
        self.actionreport_error.setText(_translate("UserWindow", "report error"))
        self.actionprocessed.setText(_translate("UserWindow", "processed"))
        self.actionunprocessed.setText(_translate("UserWindow", "unprocessed"))
        self.actionmanage_information.setText(_translate("UserWindow", "manage information"))
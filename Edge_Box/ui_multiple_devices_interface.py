# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\multiple_devices_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_send_multiple_device_config(object):
    def setupUi(self, send_multiple_device_config):
        send_multiple_device_config.setObjectName("send_multiple_device_config")
        send_multiple_device_config.resize(719, 435)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/addixo_X_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        send_multiple_device_config.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(send_multiple_device_config)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        self.upload_multiple_config = QtWidgets.QPushButton(send_multiple_device_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_multiple_config.sizePolicy().hasHeightForWidth())
        self.upload_multiple_config.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.upload_multiple_config.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-restauration-de-base-de-données-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload_multiple_config.setIcon(icon1)
        self.upload_multiple_config.setObjectName("upload_multiple_config")
        self.gridLayout.addWidget(self.upload_multiple_config, 5, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(send_multiple_device_config)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)
        self.cancel_multi_send_button = QtWidgets.QPushButton(send_multiple_device_config)
        self.cancel_multi_send_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_multi_send_button.sizePolicy().hasHeightForWidth())
        self.cancel_multi_send_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel_multi_send_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-supprimer-la-base-de-données-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_multi_send_button.setIcon(icon2)
        self.cancel_multi_send_button.setObjectName("cancel_multi_send_button")
        self.gridLayout.addWidget(self.cancel_multi_send_button, 6, 0, 1, 1)
        self.multiple_device_config_table = QtWidgets.QTableWidget(send_multiple_device_config)
        self.multiple_device_config_table.setObjectName("multiple_device_config_table")
        self.multiple_device_config_table.setColumnCount(5)
        self.multiple_device_config_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.multiple_device_config_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.multiple_device_config_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.multiple_device_config_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.multiple_device_config_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.multiple_device_config_table.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.multiple_device_config_table, 1, 0, 1, 1)
        self.multi_send_status = QtWidgets.QLabel(send_multiple_device_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multi_send_status.sizePolicy().hasHeightForWidth())
        self.multi_send_status.setSizePolicy(sizePolicy)
        self.multi_send_status.setMinimumSize(QtCore.QSize(30, 0))
        self.multi_send_status.setStyleSheet("QLabel {color : red; }")
        self.multi_send_status.setText("")
        self.multi_send_status.setObjectName("multi_send_status")
        self.gridLayout.addWidget(self.multi_send_status, 0, 0, 1, 1)

        self.retranslateUi(send_multiple_device_config)
        QtCore.QMetaObject.connectSlotsByName(send_multiple_device_config)

    def retranslateUi(self, send_multiple_device_config):
        _translate = QtCore.QCoreApplication.translate
        send_multiple_device_config.setWindowTitle(_translate("send_multiple_device_config", "Frame"))
        self.upload_multiple_config.setText(_translate("send_multiple_device_config", "Upload To EdgeBox"))
        self.cancel_multi_send_button.setText(_translate("send_multiple_device_config", "Cancel"))
        item = self.multiple_device_config_table.horizontalHeaderItem(0)
        item.setText(_translate("send_multiple_device_config", "Send"))
        item = self.multiple_device_config_table.horizontalHeaderItem(1)
        item.setText(_translate("send_multiple_device_config", "Nom"))
        item = self.multiple_device_config_table.horizontalHeaderItem(2)
        item.setText(_translate("send_multiple_device_config", "Adresse Ip"))
        item = self.multiple_device_config_table.horizontalHeaderItem(3)
        item.setText(_translate("send_multiple_device_config", "Port"))
        item = self.multiple_device_config_table.horizontalHeaderItem(4)
        item.setText(_translate("send_multiple_device_config", "Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    send_multiple_device_config = QtWidgets.QFrame()
    ui = Ui_send_multiple_device_config()
    ui.setupUi(send_multiple_device_config)
    send_multiple_device_config.show()
    sys.exit(app.exec_())
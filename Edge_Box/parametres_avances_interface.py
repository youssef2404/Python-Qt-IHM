# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\parametres_avances.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_paramtres_avances(object):
    def setupUi(self, paramtres_avances):
        paramtres_avances.setObjectName("paramtres_avances")
        paramtres_avances.resize(492, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-automatique-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        paramtres_avances.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(paramtres_avances)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ignore_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignore_list.sizePolicy().hasHeightForWidth())
        self.ignore_list.setSizePolicy(sizePolicy)
        self.ignore_list.setObjectName("ignore_list")
        self.gridLayout.addWidget(self.ignore_list, 4, 3, 1, 1)
        self.source_path = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_path.sizePolicy().hasHeightForWidth())
        self.source_path.setSizePolicy(sizePolicy)
        self.source_path.setObjectName("source_path")
        self.gridLayout.addWidget(self.source_path, 1, 3, 1, 1)
        self.destination_path = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.destination_path.sizePolicy().hasHeightForWidth())
        self.destination_path.setSizePolicy(sizePolicy)
        self.destination_path.setObjectName("destination_path")
        self.gridLayout.addWidget(self.destination_path, 2, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 9, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.browse_for_source_path = QtWidgets.QToolButton(self.centralwidget)
        self.browse_for_source_path.setObjectName("browse_for_source_path")
        self.gridLayout.addWidget(self.browse_for_source_path, 1, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.add_element_to_ignore_list = QtWidgets.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_element_to_ignore_list.setIcon(icon1)
        self.add_element_to_ignore_list.setObjectName("add_element_to_ignore_list")
        self.gridLayout.addWidget(self.add_element_to_ignore_list, 4, 4, 1, 1)
        self.cancel_advanced_configuration_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_advanced_configuration_button.sizePolicy().hasHeightForWidth())
        self.cancel_advanced_configuration_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel_advanced_configuration_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-annuler-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_advanced_configuration_button.setIcon(icon2)
        self.cancel_advanced_configuration_button.setObjectName("cancel_advanced_configuration_button")
        self.gridLayout.addWidget(self.cancel_advanced_configuration_button, 5, 2, 1, 1)
        self.save_advanced_configuration_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_advanced_configuration_button.sizePolicy().hasHeightForWidth())
        self.save_advanced_configuration_button.setSizePolicy(sizePolicy)
        self.save_advanced_configuration_button.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_advanced_configuration_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-coche-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_advanced_configuration_button.setIcon(icon3)
        self.save_advanced_configuration_button.setObjectName("save_advanced_configuration_button")
        self.gridLayout.addWidget(self.save_advanced_configuration_button, 5, 3, 1, 1)
        paramtres_avances.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(paramtres_avances)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 26))
        self.menubar.setObjectName("menubar")
        paramtres_avances.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(paramtres_avances)
        self.statusbar.setObjectName("statusbar")
        paramtres_avances.setStatusBar(self.statusbar)

        self.retranslateUi(paramtres_avances)
        QtCore.QMetaObject.connectSlotsByName(paramtres_avances)

    def retranslateUi(self, paramtres_avances):
        _translate = QtCore.QCoreApplication.translate
        paramtres_avances.setWindowTitle(_translate("paramtres_avances", "Paramétres avancés"))
        self.label_2.setText(_translate("paramtres_avances", "Source path :"))
        self.label_4.setText(_translate("paramtres_avances", "Ignore list :"))
        self.browse_for_source_path.setText(_translate("paramtres_avances", "..."))
        self.label_3.setText(_translate("paramtres_avances", "Destination path :"))
        self.add_element_to_ignore_list.setText(_translate("paramtres_avances", "..."))
        self.cancel_advanced_configuration_button.setText(_translate("paramtres_avances", "Annuler"))
        self.save_advanced_configuration_button.setText(_translate("paramtres_avances", "Enregistrer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    paramtres_avances = QtWidgets.QMainWindow()
    ui = Ui_paramtres_avances()
    ui.setupUi(paramtres_avances)
    paramtres_avances.show()
    sys.exit(app.exec_())

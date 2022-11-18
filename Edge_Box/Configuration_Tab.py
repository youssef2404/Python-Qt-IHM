import os
import sys
import traceback
from multiprocessing.resource_sharer import stop

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtGui import QPixmap
from pythonping import ping
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Logger import Logger
from parametres_avances_interface import Ui_paramtres_avances
import logging

from send_files_to_device import connect_to_device


class Configuration_Tab:

    def __init__(self, tabwid):
        self.tab = QtWidgets.QWidget()
        self.tabWidget = tabwid
        self.advanced = QtWidgets.QMainWindow()
        self.advanced_config = Ui_paramtres_avances()
        self.advanced_config.setupUi(self.advanced)

    def create_new_tab(self, clicked_item, device_id, main_user):
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.show_hide_password = QtWidgets.QCheckBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_hide_password.sizePolicy().hasHeightForWidth())
        self.show_hide_password.setSizePolicy(sizePolicy)
        self.show_hide_password.setObjectName("show_hide_password")
        self.gridLayout.addWidget(self.show_hide_password, 8, 2, 1, 1)
        self.Device_Name = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Device_Name.sizePolicy().hasHeightForWidth())
        self.Device_Name.setSizePolicy(sizePolicy)
        self.Device_Name.setObjectName("Device_Name")
        self.gridLayout.addWidget(self.Device_Name, 4, 1, 1, 1)
        self.IP_adress = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_adress.sizePolicy().hasHeightForWidth())
        self.IP_adress.setSizePolicy(sizePolicy)
        self.IP_adress.setObjectName("IP_adress")
        self.gridLayout.addWidget(self.IP_adress, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.show_advanced_parameters_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_advanced_parameters_button.sizePolicy().hasHeightForWidth())
        self.show_advanced_parameters_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_advanced_parameters_button.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-automatique-16.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.show_advanced_parameters_button.setIcon(icon)
        self.show_advanced_parameters_button.setObjectName("show_advanced_parameters_button")
        self.gridLayout.addWidget(self.show_advanced_parameters_button, 9, 3, 1, 1)
        self.Ping_buttton = QtWidgets.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-tour-de-radio-16.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.Ping_buttton.setIcon(icon1)
        self.Ping_buttton.setObjectName("Ping_buttton")
        self.gridLayout.addWidget(self.Ping_buttton, 5, 2, 1, 1)
        self.Device_port_number = QtWidgets.QSpinBox(self.tab)
        self.Device_port_number.setObjectName("Device_port_number")
        self.gridLayout.addWidget(self.Device_port_number, 6, 1, 1, 1)
        self.password = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 8, 1, 1, 1)
        self.cancel_modify_device_interface_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_modify_device_interface_button.sizePolicy().hasHeightForWidth())
        self.cancel_modify_device_interface_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancel_modify_device_interface_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-annuler-16.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.cancel_modify_device_interface_button.setIcon(icon2)
        self.cancel_modify_device_interface_button.setObjectName("cancel_modify_device_interface_button")
        self.gridLayout.addWidget(self.cancel_modify_device_interface_button, 9, 0, 1, 1)
        self.save_device_button = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_device_button.sizePolicy().hasHeightForWidth())
        self.save_device_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_device_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-coche-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_device_button.setIcon(icon3)
        self.save_device_button.setObjectName("save_device_button")
        self.gridLayout.addWidget(self.save_device_button, 9, 1, 1, 1)
        self.download_from_edgebox_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_from_edgebox_button.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-dossier-des-téléchargements-16.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_from_edgebox_button.setIcon(icon4)
        self.download_from_edgebox_button.setObjectName("download_from_edgebox_button")
        self.gridLayout.addWidget(self.download_from_edgebox_button, 11, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 10, 0, 1, 4)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 4)
        self.update_device_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update_device_button.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-envoi-de-courriel-16.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.update_device_button.setIcon(icon5)
        self.update_device_button.setObjectName("update_device_button")
        self.gridLayout.addWidget(self.update_device_button, 11, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.label_6.setStyleSheet("")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(".\\ui_files\\../icons/addixo-st gris - fond-transparent (1).png"))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.Cancel_upload = QtWidgets.QPushButton(self.tab)
        self.Cancel_upload.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Cancel_upload.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\ui_files\\../icons/icons8-supprimer-la-propriété-16.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.Cancel_upload.setIcon(icon6)
        self.Cancel_upload.setObjectName("Cancel_upload")
        self.gridLayout.addWidget(self.Cancel_upload, 12, 3, 1, 1)
        self.upload_state = QtWidgets.QLabel(self.tab)
        self.upload_state.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_state.sizePolicy().hasHeightForWidth())
        self.upload_state.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.upload_state.setFont(font)
        self.upload_state.setStyleSheet("QLabel {color : red; }")
        self.upload_state.setText("")
        self.upload_state.setObjectName("upload_state")
        self.gridLayout.addWidget(self.upload_state, 12, 1, 1, 1)
        self.tabWidget.addTab(self.tab, clicked_item.text(0))
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow", "Numéro de port :"))
        self.label_4.setText(_translate("MainWindow", "Nom d\'utilisateur :"))
        self.label_5.setText(_translate("MainWindow", "Mot de passe :"))
        self.label.setText(_translate("MainWindow", "Adresse IP:"))
        self.show_hide_password.setText(_translate("MainWindow", "Show"))
        self.label_2.setText(_translate("MainWindow", "Nom du périphérique :"))
        self.show_advanced_parameters_button.setText(_translate("MainWindow", "Paramètres avancés"))
        self.Ping_buttton.setText(_translate("MainWindow", "Test"))
        self.cancel_modify_device_interface_button.setText(_translate("MainWindow", "Annuler"))
        self.save_device_button.setText(_translate("MainWindow", "Enregistrer"))
        self.download_from_edgebox_button.setText(_translate("MainWindow", "Download From EdgeBox"))
        self.update_device_button.setText(_translate("MainWindow", "Upload To EdgeBox"))
        self.Cancel_upload.setText(_translate("MainWindow", "Cancel upload"))
        self.message_box = QMessageBox()
        self.logger = Logger(log_file_directory="Logging")
        self.tab_devices_buttons(device_id=device_id, main_user=main_user)
        self.cancel = False

    def tab_devices_buttons(self, device_id, main_user):
        try:
            self.show_hide_password.toggled.connect(lambda: self.show_hide_password_checkbox())
            self.save_device_button.clicked.connect(lambda: self.get_device_configuration_fromTab(device_id=device_id, main_user=main_user))
            self.cancel_modify_device_interface_button.clicked.connect(lambda: self.tab_cancel_button(device_id=device_id, main_user=main_user))
            self.show_advanced_parameters_button.clicked.connect(lambda: self.open_advanced_configuration_interface(device_id=device_id, main_user=main_user))
            self.Ping_buttton.clicked.connect(lambda: self.test_ping())
            self.update_device_button.clicked.connect(lambda: self.send_update_files_to_device(device_id, main_user))
            self.Cancel_upload.clicked.connect(lambda: self.Cancel_update_device())
            self.download_from_edgebox_button.clicked.connect(lambda: self.get_files_from_device(main_user, device_id))
        except Exception:
            traceback.print_exc()

    def Disable_advanced_mode(self):
        self.password.setEnabled(False)
        self.username.setEnabled(False)
        self.IP_adress.setEnabled(False)
        self.Device_port_number.setEnabled(False)
        self.Device_Name.setEnabled(False)
        self.save_device_button.setEnabled(False)
        self.cancel_modify_device_interface_button.setEnabled(False)

    def Enable_advanced_mode(self):
        self.password.setEnabled(True)
        self.username.setEnabled(True)
        self.IP_adress.setEnabled(True)
        self.Device_port_number.setEnabled(True)
        self.Device_Name.setEnabled(True)
        self.save_device_button.setEnabled(True)
        self.cancel_modify_device_interface_button.setEnabled(True)

    def test_ping(self):
        try:
            ip_adress = self.IP_adress.text()
            ping_response = ping(ip_adress, count=1)
            if ping_response.success():
                self.message_box.about(QtWidgets.QWidget(), "Ping Test", "Success test")
            else:
                self.message_box.about(QtWidgets.QWidget(), "Ping Test", "Device not accessable")
        except Exception as exception:
            self.logger.error_logger(exception)

    def show_hide_password_checkbox(self):
        try:
            if self.show_hide_password.isChecked():
                self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            else:
                self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        except Exception as exception:
            logging.exception(exception)

    def get_device_configuration_fromTab(self, device_id, main_user):
        try:
            username = self.username.text()
            password = self.password.text()
            IP_adress = self.IP_adress.text()
            port_number = self.Device_port_number.text()
            device_name = self.Device_Name.text()
            tab_index = self.tabWidget.currentIndex()
            existance_of_device_name = main_user.verify_if_device_name_exits(device_name, device_id)
            if existance_of_device_name is None:
                self.tabWidget.setTabText(tab_index, device_name)
                main_user.add_device_configuration(username, password, port_number, IP_adress, device_name, id_device=device_id)
            else:
                self.message_box.about(QtWidgets.QWidget(), "Attention", "Device Name exists")
                main_user.set_configuration_in_tab(device_id)

        except Exception as exception:
            logging.exception(exception)

    def show_device_configuration_on_double_click(self, username, password, IP_adress, port_number, device_name):
        try:
            self.username.setText(username)
            self.password.setText(password)
            self.IP_adress.setText(IP_adress)
            self.Device_port_number.setValue(port_number)
            self.Device_Name.setText(device_name)
        except Exception as exception:
            logging.exception(exception)

    def tab_cancel_button(self, device_id, main_user):
        try:
            main_user.set_configuration_in_tab(id_device=device_id)
        except Exception as exception:
            logging.exception(exception)

    def open_advanced_configuration_interface(self, device_id, main_user):
        try:
            self.advanced.show()
            self.advanced_config.browse_for_source_path.clicked.connect(lambda: self.select_src_path())
            self.advanced_config.save_advanced_configuration_button.clicked.connect(lambda: self.save_advanced_parameters(device_id=device_id, main_user=main_user))
            self.advanced_config.cancel_advanced_configuration_button.clicked.connect(lambda: self.cancel_advanced_parameters_button(device_id, main_user))
            self.advanced_config.add_element_to_ignore_list.clicked.connect(lambda: self.add_element_to_ignorelist())
            self.advanced_config.ignore_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.advanced_config.ignore_list.customContextMenuRequested.connect(lambda: self.ignore_list_right_click())
            self.advanced_config.source_path.textChanged.connect(self.src_path_not_empty)
            self.advanced_config.ignore_list.setEnabled(False)
            self.advanced_config.add_element_to_ignore_list.setEnabled(False)
            main_user.get_advanced_parameters(id_device=device_id)
        except Exception as exception:
            logging.exception(exception)

    def src_path_not_empty(self, text):
        try:
            if text:
                self.advanced_config.ignore_list.setEnabled(True)
                self.advanced_config.add_element_to_ignore_list.setEnabled(True)
            else:
                self.advanced_config.ignore_list.setEnabled(False)
                self.advanced_config.add_element_to_ignore_list.setEnabled(False)
        except Exception as exception:
            logging.exception(exception)

    def select_src_path(self):
        try:
            src_folder = QFileDialog.getExistingDirectory(QtWidgets.QWidget(), "Select Directory")
            self.advanced_config.source_path.setText(src_folder)
        except Exception as exception:
            logging.exception(exception)

    def get_destination_path(self):
        try:
            destination_path = self.advanced_config.destination_path.text()
            return destination_path
        except Exception as exception:
            logging.exception(exception)

    def save_advanced_parameters(self, device_id, main_user):
        try:
            selected_ignore_list = []
            src_path = self.advanced_config.source_path.text()
            dest_path = self.get_destination_path()
            for ignore_list_elements in range(self.advanced_config.ignore_list.count()):
                selected_ignore_list.append(self.advanced_config.ignore_list.item(ignore_list_elements).text())
            main_user.add_advanced_parameters(src_path, dest_path, device_id)
            main_user.add_ignore_list_element(device_id, selected_ignore_list)
        except Exception as exception:
            logging.exception(exception)

    def show_advanced_parameters(self, src_path, dest_path, ignore_list):
        try:
            self.advanced_config.source_path.setText(src_path)
            self.advanced_config.destination_path.setText(dest_path)
            self.advanced_config.ignore_list.clear()
            for ignore_list_element in range(0, len(ignore_list)):
                self.advanced_config.ignore_list.addItem(ignore_list[ignore_list_element])
        except Exception as exception:
            logging.exception(exception)

    def cancel_advanced_parameters_button(self, device_id, main_user):
        try:
            self.advanced_config.ignore_list.clear()
            main_user.get_advanced_parameters(device_id)
        except Exception as exception:
            logging.exception(exception)

    def add_element_to_ignorelist(self):
        try:
            names = QFileDialog.getOpenFileNames(parent=QtWidgets.QWidget(),
                                                caption="open File", directory=self.advanced_config.source_path.text(),
                                                filter="ALL Files (*.*)")
            for name in names[0]:
                relative_name = name.replace(self.advanced_config.source_path.text()+"/", "")
                self.advanced_config.ignore_list.addItem(relative_name)
        except Exception as exception:
            logging.exception(exception)

    def ignore_list_right_click(self):
        try:
            right_click_menu = QtWidgets.QMenu()
            action_1 = right_click_menu.addAction("Add Files")
            action_2 = right_click_menu.addAction("Delete File")
            selected_action = right_click_menu.exec_(self.advanced_config.ignore_list.mapToGlobal(QtCore.QPoint()))
            if selected_action == action_1:
                self.add_element_to_ignorelist()
            elif selected_action == action_2:
                self.delete_file_from_ignore_list()
        except Exception as exception:
            logging.exception(exception)

    def delete_file_from_ignore_list(self):
        try:
            selected_file = self.advanced_config.ignore_list.currentRow()
            self.advanced_config.ignore_list.takeItem(selected_file)
        except Exception as exception:
            logging.exception(exception)

    def send_update_files_to_device(self, device_id, main_user):
        self.update_device_button.setEnabled(False)
        device_name = self.Device_Name.text()
        self.upload_state.setText("Connecting to "+device_name+"...")
        QtTest.QTest.qWait(3000)
        username = self.username.text()
        password = self.password.text()
        IP_adress = self.IP_adress.text()
        port_number = self.Device_port_number.text()
        advanced_parameters = main_user.get_advanced_parameters_to_send(device_id)
        device_sender = connect_to_device(ip_adress=IP_adress, username=username, password=password, port=port_number)
        self.Cancel_upload.setEnabled(True)
        if advanced_parameters[0] != "" and advanced_parameters[1] != "":
            verify_existance_of_folder = os.path.isdir(advanced_parameters[0])
            if verify_existance_of_folder and not self.cancel:
                folder_content = os.listdir(advanced_parameters[0])
                folder_content_to_send = self.delete_folders_from_list(folder_content, advanced_parameters[0])
                filtered_list = self.filter_files_list_before_send(folder_content_to_send, advanced_parameters[2])
                verify_connection = device_sender.startconnection()
                if verify_connection and not self.cancel:
                    self.upload_state.setText("Sending to temp folder ...")
                    QtTest.QTest.qWait(7000)
                    self.Cancel_upload.setEnabled(False)
                    send_verify = device_sender.send_files_to_device(source_path=advanced_parameters[0], list_to_send=filtered_list)
                    if send_verify and not self.cancel:
                        self.upload_state.setText("Updating ...")
                        QtTest.QTest.qWait(2000)
                        copy_from_temp_to_destination = device_sender.copy_from_tempfile_to_destination(advanced_parameters[1])
                        if copy_from_temp_to_destination:
                            self.upload_state.setText("")
                            self.message_box.about(QtWidgets.QWidget(), "Connection", "device was updated successfully")
                        else:
                            self.upload_state.setText("")
                            self.message_box.about(QtWidgets.QWidget(), "Error", "Check destination path")
                    else:
                        if self.cancel:
                            device_sender.cancel_updating()
                            self.upload_state.setText("")
                            self.message_box.about(QtWidgets.QWidget(), "Connection", "Update Canceled")
                        else:
                            self.upload_state.setText("")
                            self.message_box.about(QtWidgets.QWidget(), "Connection", "Check destination path")
                else:
                    if self.cancel:
                        device_sender.cancel_updating()
                        self.upload_state.setText("")
                        self.message_box.about(QtWidgets.QWidget(), "Connection", "Update Canceled")
                    else:
                        self.upload_state.setText("")
                        self.message_box.about(QtWidgets.QWidget(), "Connection", "Failed device connection")
            else:
                if self.cancel:
                    device_sender.cancel_updating()
                    self.upload_state.setText("")
                    self.message_box.about(QtWidgets.QWidget(), "Connection", "Update Canceled")
                else:
                    self.upload_state.setText("")
                    self.message_box.about(QtWidgets.QWidget(), "Problem", "Folder does not exist ")
        else:
            self.upload_state.setText("")
            self.message_box.about(QtWidgets.QWidget(), "Problem", "you should select source or destination folder")
        self.Cancel_upload.setEnabled(False)
        self.update_device_button.setEnabled(True)
        self.cancel = False

    def delete_folders_from_list(self, folder_content, path):
        list_to_return = []
        for content in range(len(folder_content)):
            if os.path.isfile(os.path.join(path, folder_content[content])):
                list_to_return.append(folder_content[content])
        return list_to_return

    def filter_files_list_before_send(self, folder_content, ignore_list):
        for ignore_list_element in range(len(ignore_list)):
            if ignore_list[ignore_list_element] in folder_content:
                folder_content.remove(ignore_list[ignore_list_element])
        return folder_content

    def get_files_from_device(self, main_user, device_id):
        self.download_from_edgebox_button.setEnabled(False)
        username = self.username.text()
        password = self.password.text()
        IP_adress = self.IP_adress.text()
        port_number = self.Device_port_number.text()
        advanced_parameters = main_user.get_advanced_parameters_to_send(device_id)
        if advanced_parameters[1] != "":
            device_getter = connect_to_device(ip_adress=IP_adress, username=username, password=password,
                                              port=port_number)
            verify_connection = device_getter.startconnection()
            if verify_connection:
                get_files_verif = device_getter.get_files_from_device(advanced_parameters[1])
                if get_files_verif:
                    self.message_box.about(QtWidgets.QWidget(), "Connection", "data downloaded successfully")
                else:
                    self.message_box.about(QtWidgets.QWidget(), "Connection", "No Files in selected folder")
            else:
                self.message_box.about(QtWidgets.QWidget(), "Connection", "Failed device connection")
        else:
            self.message_box.about(QtWidgets.QWidget(), "Problem", "you should select destination folder")
        self.download_from_edgebox_button.setEnabled(True)

    def Cancel_update_device(self):
        self.cancel = True
        self.Cancel_upload.setEnabled(False)
        self.upload_state.setText("Cancel ...")




































# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Project.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import threading
from PyQt5 import QtCore, QtWidgets, QtGui, QtTest
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt, QCoreApplication, QTimer
from Configuration_Tab import Configuration_Tab
from Item_Organisation import Item_Organisation
from Logger import Logger
from Tab_Organisation import Tab_Organisation
from multi_send_organisation import multi_send_organisation
from send_files_to_device import connect_to_device
from ui_create_project_interface import Ui_Create_Project_Interface
from ui_main_window import Ui_MainWindow
from Device import Device
import sip
import sys
import json

from ui_multiple_devices_interface import Ui_send_multiple_device_config
from ui_splash_screen import Ui_Frame


class main_user_interface(threading.Thread):

    def __init__(self):
        super(main_user_interface, self).__init__()
        self.ui = None
        self.loading_complete = False
        self.device_name_counter = 0
        self.device_list = []
        self.items_list = []
        self.tabs_list = []
        self.multi_send_list = []
        self.advanced_mode_state = False
        self.projectname = "New_Project"
        self.logger = Logger(log_file_directory="Logging")

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        self.splash = QtWidgets.QFrame()
        self.splash_screen = Ui_Frame()
        self.splash_screen.setupUi(self.splash)
        self.splash.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.splash.show()
        QtTest.QTest.qWait(5000)
        self.splash.close()
        MainWindow.show()
        self.buttons_configuration()
        self.loading_complete = True
        sys.exit(app.exec_())

    def buttons_configuration(self):
        try:
            self.ui.advanced_mode.setCheckable(True)
            self.ui.advanced_mode.triggered.connect(self.check_advanced_mode_status)
            self.ui.Create_Project.triggered.connect(lambda: self.open_create_project_window())
            self.ui.Save_Project.triggered.connect(lambda: self.save_project())
            self.ui.Exit.triggered.connect(lambda: self.exit_from_project())
            self.ui.Create_new_project_acceuil.clicked.connect(lambda: self.open_create_project_window())
            self.ui.load_project_acceuil.clicked.connect(lambda: self.read_json_file())
            self.ui.Project_Devices_Tree.itemDoubleClicked.connect(lambda: self.show_selected_device_configuration())
            self.ui.Project_Devices_Tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.ui.Project_Devices_Tree.customContextMenuRequested.connect(self.menuContextTree)
            self.ui.Save_Project.setIcon(QIcon("icons/icons8-sauvegarder-16.png"))
            self.ui.Create_Project.setIcon(QIcon("icons/icons8-plus-16.png"))
            self.ui.advanced_mode.setIcon(QIcon("icons/icons8-outils-administratifs-16.png"))
            self.ui.Exit.setIcon(QIcon("icons/icons8-connexion-16.png"))
            self.ui.actionModify_Project.setIcon(QIcon("icons/icons8-modifier-la-propriété-16.png"))
            self.ui.actionModify_Project.triggered.connect(lambda: self.open_create_project_window())
            self.ui.Version.setIcon(QIcon("icons/icons8-poser-une-question-16.png"))
            self.ui.actionSend_Multiple.setIcon(QIcon("icons/icons8-choix-multiple-16.png"))
            self.ui.actionSend_Multiple.triggered.connect(lambda: self.open_send_multiple_interface())
            tabs = self.ui.tabWidget
            tabs.tabCloseRequested.connect(self.close_tab)
        except Exception as exception:
            print(exception)
           # self.logger.error(exception, exc_info=True)

    def check_advanced_mode_status(self, state):
        try:
            if state:
                for tab in self.tabs_list:
                    self.new_tab = tab.tab
                    self.new_tab.Enable_advanced_mode()
            else:
                for tab in self.tabs_list:
                    self.new_tab = tab.tab
                    self.new_tab.Disable_advanced_mode()
            self.advanced_mode_state = state
        except Exception as exception:
            self.logger.error(exception, exc_info=True)

    def close_tab(self, index_of_closed_tab):
        closed_tab_name = self.ui.tabWidget.tabText(index_of_closed_tab)
        self.ui.tabWidget.removeTab(index_of_closed_tab)
        self.remove_tab_from_tablist(tab_name=closed_tab_name)

    def remove_tab_from_tablist(self, tab_name):
        item_match = list(filter(lambda item_cursor: item_cursor.item.text(0) == tab_name, self.items_list))
        for item_cursor in item_match:
            id_device = self.get_device_by_item(item=item_cursor.item)
            for tab in self.tabs_list:
                if tab.device_id == id_device:
                    self.tabs_list.remove(tab)

    def add_tree_project(self, project_name):
        self.ui.Project_Devices_Tree.headerItem().setText(0, project_name)

    def add_tree_device(self, device_name):
        _translate = QtCore.QCoreApplication.translate
        item = QtWidgets.QTreeWidgetItem(self.ui.Project_Devices_Tree)
        item.setData(0, Qt.DisplayRole, device_name)
        device_id = self.create_new_device()
        items = Item_Organisation(item, device_id)
        self.items_list.append(items)
        self.ui.Project_Devices_Tree.addTopLevelItem(item)

    def open_create_project_window(self):
        self.Create = QtWidgets.QFrame()
        self.create_project_window = Ui_Create_Project_Interface()
        self.create_project_window.setupUi(self.Create)
        self.Create.setWindowTitle("Create Project")
        self.Create.show()
        self.create_project_window.Save_ProjectName.clicked.connect(lambda: self.save_project_name())
        self.create_project_window.Save_ProjectName.clicked.connect(lambda: self.Create.close())
        self.create_project_window.Quit_CreateProject_Interface.clicked.connect(lambda: self.Create.close())

    #right_click_on_QtreeWidget(items_list)
    def menuContextTree(self, point):
        right_click_menu = QtWidgets.QMenu()
        action_1 = right_click_menu.addAction("Add New Device")
        action_2 = right_click_menu.addAction("Delete Device")
        act = right_click_menu.exec_(self.ui.Project_Devices_Tree.mapToGlobal(point))
        if act == action_1:
            self.add_tree_device("New_device_" + str(self.device_name_counter))
            self.device_name_counter += 1
        elif act == action_2:
            self.delete_device()

    def save_project_name(self):
        self.projectname = self.create_project_window.Project_Name_field.text()
        self.add_tree_project(project_name=self.projectname)
        self.remove_specefic_tab(tab_name="Acceuil")

    def show_selected_device_configuration(self):
            double_clicked_item = self.ui.Project_Devices_Tree.currentItem()
            id_device = self.get_device_by_item(double_clicked_item)
            existance_of_tab = self.verify_existance_of_tab(double_clicked_item.text(0))
            if existance_of_tab is None:
                self.new_tab = Configuration_Tab(self.ui.tabWidget)
                self.new_tab.create_new_tab(double_clicked_item, id_device, main_user_interface)
                tab_device = Tab_Organisation(self.new_tab, id_device)
                self.tabs_list.append(tab_device)
                current_tab_index = self.ui.tabWidget.currentIndex()
                self.ui.tabWidget.setCurrentIndex(current_tab_index+1)
                self.get_device_configuration_from_list(id_device)
                if self.advanced_mode_state:
                    self.new_tab.Enable_advanced_mode()
                else:
                    self.new_tab.Disable_advanced_mode()
            else:
                self.ui.tabWidget.setCurrentIndex(existance_of_tab)

    def add_device_configuration(self, username, password, port_number, IP_adress, device_name, id_device):
        item = self.get_item_by_device(id_device)
        item.setData(0, Qt.DisplayRole, device_name)
        device_match = list(filter(lambda device: device.id == id_device, self.device_list))
        for device in device_match:
            device.username = username
            device.password = password
            device.port_number = port_number
            device.IP_adress = IP_adress
            device.device_name = device_name

    def create_new_device(self):
        new_device = Device()
        self.device_list.append(new_device)
        return new_device.id

    def get_device_configuration_from_list(self, id_device):
        device_match = list(filter(lambda device: device.id == id_device, self.device_list))
        for device in device_match:
            self.new_tab.show_device_configuration_on_double_click(device.username, device.password, device.IP_adress,
                                                                   int(device.port_number), device.device_name)

    def set_configuration_in_tab(self, id_device):
        self.new_tab = self.get_tab_by_device(id_device)
        device_match = list(filter(lambda device: device.id == id_device, self.device_list))
        for device in device_match:
            self.new_tab.show_device_configuration_on_double_click(device.username, device.password, device.IP_adress, int(device.port_number), device.device_name)

    def get_device_by_item(self, item):
        for item_cursor in self.items_list:
            if item_cursor.item == item:
                return item_cursor.device_id

    def get_item_by_device(self, id_device):
        for item in self.items_list:
            if item.device_id == id_device:
                return item.item

    def get_tab_by_device(self, id_device):
        for tab in self.tabs_list:
            if tab.device_id == id_device:
                return tab.tab

    def delete_device(self):
        selected_item = self.ui.Project_Devices_Tree.currentItem()
        id_device = self.get_device_by_item(selected_item)
        for device in self.device_list:
            if device.id == id_device:
                self.device_list.remove(device)
                break
        tab = selected_item.text(0)
        self.remove_specefic_tab(tab_name=tab)
        self.remove_tab_from_tablist(tab_name=tab)
        sip.delete(selected_item)
        self.delete_item_from_items_list(id_device=id_device)

    def delete_item_from_items_list(self, id_device):
        for item_cur in self.items_list:
            if item_cur.device_id == id_device:
                self.items_list.remove(item_cur)
                break

    def verify_existance_of_tab(self, tab_name):
        tab_position = None
        for tab in range(0, self.ui.tabWidget.count()+1):
            if tab_name == self.ui.tabWidget.tabText(tab):
                tab_position = tab
        return tab_position

    def remove_specefic_tab(self, tab_name):
        for tab in range(0, self.ui.tabWidget.count()+1):
            if tab_name == self.ui.tabWidget.tabText(tab):
                self.ui.tabWidget.removeTab(tab)

    def save_project(self):
        filename = self.open_save_dialog()
        if filename[0] != "":
            with open(filename[0], 'w') as f:
                project = [{"Project_Name": self.projectname, "Version": "0.0.1", "Device": []}]
                for device in self.device_list:
                    project[0]["Device"].append({"Id": device.id, "Device_name": device.device_name, "IP_Adress": device.IP_adress, "Port_number": device.port_number, "Username": device.username, "Password": device.password, "src_path": device.src_path, "dest_path": device.dest_path, "ignore_list": device.ignore_list})
                json.dump(project, f, indent=4)

    def open_save_dialog(self):
        filename = QFileDialog.getSaveFileName(QtWidgets.QWidget(), "Save Project", str(self.projectname), "Json File(*.json)")
        return filename

    def load_project_dialog(self):
        filename = QFileDialog.getOpenFileName(QtWidgets.QWidget(), "open File", "", "Json File (*.json)")
        return filename

    def read_json_file(self):
        filename = self.load_project_dialog()
        if filename[0] != "":
            jsonfile = open(filename[0], 'r')
            data = jsonfile.read()
            obj = json.loads(data)
            self.projectname = obj[0]['Project_Name']
            self.add_tree_project(project_name=obj[0]['Project_Name'])
            for devices in range(len(obj[0]['Device'])):
                new_device = Device()
                self.device_list.append(new_device)
            for devices in range(len(obj[0]['Device'])):
                self.add_tree_device_onload(obj[0]['Device'][devices]['Device_name'], devices+1)
            for devices in range(len(obj[0]['Device'])):
                self.add_device_configuration(str(obj[0]['Device'][devices]['Username']), str(obj[0]['Device'][devices]['Password']), int(obj[0]['Device'][devices]['Port_number']), str(obj[0]['Device'][devices]['IP_Adress']), str(obj[0]['Device'][devices]['Device_name']), devices+1)
                self.add_advanced_parameters(obj[0]['Device'][devices]['src_path'], obj[0]['Device'][devices]['dest_path'], devices+1)
                self.add_ignore_list_element(devices+1, obj[0]['Device'][devices]['ignore_list'])
            self.remove_specefic_tab(tab_name="Acceuil")

    def add_tree_device_onload(self, device_name, device_id):
        _translate = QtCore.QCoreApplication.translate
        item = QtWidgets.QTreeWidgetItem(self.ui.Project_Devices_Tree)
        item.setData(0, Qt.DisplayRole, device_name)
        items = Item_Organisation(item, device_id)
        self.items_list.append(items)
        self.ui.Project_Devices_Tree.addTopLevelItem(item)

    def add_advanced_parameters(self, src_path, dest_path, device_id):
        device_match = list(filter(lambda device: device.id == device_id, self.device_list))
        for device in device_match:
            device.src_path = src_path
            device.dest_path = dest_path

    def get_advanced_parameters(self, id_device):
        self.new_tab = self.get_tab_by_device(id_device)
        for device in self.device_list:
            if device.id == id_device:
                self.new_tab.show_advanced_parameters(device.src_path, device.dest_path, device.ignore_list)
                break

    def add_ignore_list_element(self, id_device, selected_list):
        for device in self.device_list:
            if device.id == id_device:
                device.ignore_list.clear()
                for selected_element in range(0, len(selected_list)):
                    if len(device.ignore_list) != 0:
                        if selected_list[selected_element] in device.ignore_list:
                            print("ignore list element existe")
                        else:
                            device.ignore_list.append(selected_list[selected_element])
                    else:
                        device.ignore_list.append(selected_list[selected_element])

    def delete_file_from_ignorelist(self, filename, device_id):
        for device in self.device_list:
            if device.id == device_id:
                for ignore_list_element in range(0, len(device.ignore_list)):
                    if device.ignore_list[ignore_list_element] == filename:
                        device.ignore_list.pop(ignore_list_element)
                        break

    def exit_from_project(self):
        save_before_exit_dialog = QMessageBox()
        save_before_exit_dialog.setWindowTitle("Exit")
        save_before_exit_dialog.setText("Do you want to save the project ?")
        save_before_exit_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        save_before_exit_dialog.setIcon(QMessageBox.Question)
        clicked_button = save_before_exit_dialog.exec()
        if clicked_button == QMessageBox.Yes:
            self.save_project()
            sys.exit(QtWidgets.QApplication(sys.argv).exec_())
        elif clicked_button == QMessageBox.No:
            sys.exit(QtWidgets.QApplication(sys.argv).exec_())

    def verify_if_device_name_exits(self, device_name, device_id):
        device_match = list(filter(lambda device: device.device_name == device_name and device.id != device_id, self.device_list))
        for device in device_match:
            return device.id

    def get_advanced_parameters_to_send(self, id_device):
        for device in self.device_list:
            if device.id == id_device:
                return device.src_path, device.dest_path, device.ignore_list

    def open_send_multiple_interface(self):
        self.multi_send_list = []
        self.cancel_multi_send = False
        self.send_multiple_device_config = QtWidgets.QFrame()
        self.muliple_send_interface = Ui_send_multiple_device_config()
        self.muliple_send_interface.setupUi(self.send_multiple_device_config)
        self.send_multiple_device_config.setWindowTitle("Multiple Upload")
        self.show_config_on_send_mulitple_interface()
        self.send_multiple_device_config.show()
        self.muliple_send_interface.upload_multiple_config.clicked.connect(lambda: self.multiple_upload())
        self.muliple_send_interface.multiple_device_config_table.cellChanged.connect(self.oncellchanged)
        self.muliple_send_interface.cancel_multi_send_button.clicked.connect(lambda: self.cancel_multi_send_config())

    def show_config_on_send_mulitple_interface(self):
        self.muliple_send_interface.progressBar.setVisible(False)
        self.muliple_send_interface.multiple_device_config_table.setRowCount(len(self.device_list))
        for table_lines in range(len(self.device_list)):
            multi_send_table_checkbox = QTableWidgetItem()
            multi_send_table_checkbox.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            multi_send_table_checkbox.setCheckState(Qt.CheckState.Unchecked)
            self.muliple_send_interface.multiple_device_config_table.setItem(table_lines, 0, multi_send_table_checkbox)
        for device in self.device_list:
            table_item = QTableWidgetItem()
            table_item.setText(device.device_name)
            table_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.muliple_send_interface.multiple_device_config_table.setItem(device.id-1, 1, table_item)
        for device in self.device_list:
            table_item = QTableWidgetItem()
            table_item.setText(device.IP_adress)
            table_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.muliple_send_interface.multiple_device_config_table.setItem(device.id-1, 2, table_item)
        for device in self.device_list:
            table_item = QTableWidgetItem()
            table_item.setText(str(device.port_number))
            table_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.muliple_send_interface.multiple_device_config_table.setItem(device.id - 1, 3, table_item)
        for table_row in range(0, len(self.device_list)):
            table_item = QTableWidgetItem()
            table_item.setText("")
            table_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            self.muliple_send_interface.multiple_device_config_table.setItem(table_row, 4, table_item)
        self.check_if_device_have_all_configuration_parameteres()

    def oncellchanged(self, row, column):
        item = self.muliple_send_interface.multiple_device_config_table.item(row, column)
        boxcheck = item.checkState()
        if boxcheck == Qt.CheckState.Checked and column == 0:
            device_name = self.muliple_send_interface.multiple_device_config_table.item(row, 1).text()
            device_in_multi_send = multi_send_organisation(device_name, row)
            self.multi_send_list.append(device_in_multi_send)
        elif boxcheck == Qt.CheckState.Unchecked and column == 0:
            device_name = self.muliple_send_interface.multiple_device_config_table.item(row, 1).text()
            device_match = list(filter(lambda device: device.device_name == device_name, self.multi_send_list))
            for device in device_match:
                self.multi_send_list.remove(device)

    def multiple_upload(self):
        if len(self.multi_send_list):
            self.muliple_send_interface.upload_multiple_config.setEnabled(False)
            self.muliple_send_interface.cancel_multi_send_button.setEnabled(True)
            self.muliple_send_interface.progressBar.setVisible(True)
            self.muliple_send_interface.progressBar.setValue(70)
            for to_send in self.multi_send_list:
                for device in self.device_list:
                    if to_send.device_name == device.device_name:
                        self.muliple_send_interface.multi_send_status.setText("Connecting to "+to_send.device_name+"...")
                        QtTest.QTest.qWait(2000)
                        connect_to_send = connect_to_device(ip_adress=device.IP_adress, username=device.username, password=device.password, port=device.port_number)
                        verify_connection = connect_to_send.startconnection()
                        if verify_connection and not self.cancel_multi_send:
                            self.muliple_send_interface.progressBar.setValue(80)
                            advanced_parameters = self.get_advanced_parameters_to_send(device.id)
                            if advanced_parameters[0] != "" and advanced_parameters[1] != "":
                                verify_existance_of_folder = os.path.isdir(advanced_parameters[0])
                                if verify_existance_of_folder and not self.cancel_multi_send:
                                    folder_content = os.listdir(advanced_parameters[0])
                                    folder_content_to_send = self.delete_folders_from_list(folder_content, advanced_parameters[0])
                                    filtered_list = self.filter_list_before_send(folder_content_to_send, advanced_parameters[2])
                                    self.muliple_send_interface.multi_send_status.setText("Sending to temp folder of "+to_send.device_name+"...")
                                    QtTest.QTest.qWait(4000)
                                    send_verify = connect_to_send.send_files_to_device(
                                                                       source_path=advanced_parameters[0],
                                                                       list_to_send=filtered_list)
                                    if send_verify and not self.cancel_multi_send:
                                        self.muliple_send_interface.multi_send_status.setText("Updating " + to_send.device_name + "...")
                                        QtTest.QTest.qWait(2000)
                                        copy_from_temp_to_destination = connect_to_send.copy_from_tempfile_to_destination(advanced_parameters[1])
                                        self.muliple_send_interface.progressBar.setValue(90)
                                        if copy_from_temp_to_destination:
                                            item = self.muliple_send_interface.multiple_device_config_table.item(to_send.device_row, 4)
                                            item.setText("ok")
                                        else:
                                            item = self.muliple_send_interface.multiple_device_config_table.item(to_send.device_row, 4)
                                            item.setText("Error")
                                            No_device_checked_dialog = QMessageBox()
                                            No_device_checked_dialog.about(QtWidgets.QWidget(), "Send Multiple",
                                                                       "Check destination path of "+device.device_name)
                                    else:
                                        if not send_verify and not self.cancel_multi_send:
                                            Error_dialog = QMessageBox()
                                            Error_dialog.about(QtWidgets.QWidget(), "Send Multiple",
                                                               "Check advanced Config")
                                        else:
                                            self.delete_temp_file(ip_adress=device.IP_adress, username=device.username,
                                                                  password=device.password, port=device.port_number)
                                            self.muliple_send_interface.multi_send_status.setText("")
                                            self.muliple_send_interface.cancel_multi_send_button.setEnabled(False)
                                            self.muliple_send_interface.upload_multiple_config.setEnabled(True)
                                            self.cancel_multi_send = False
                                            self.show_config_on_send_mulitple_interface()
                                            return 0
                                else:
                                    if not verify_existance_of_folder and not self.cancel_multi_send:
                                        Error_dialog = QMessageBox()
                                        Error_dialog.about(QtWidgets.QWidget(), "Send Multiple", "Check existance of folder ")
                                    else:
                                        self.delete_temp_file(ip_adress=device.IP_adress, username=device.username,
                                                              password=device.password, port=device.port_number)
                                        self.muliple_send_interface.multi_send_status.setText("")
                                        self.muliple_send_interface.cancel_multi_send_button.setEnabled(False)
                                        self.muliple_send_interface.upload_multiple_config.setEnabled(True)
                                        self.cancel_multi_send = False
                                        self.show_config_on_send_mulitple_interface()
                                        return 0
                        else:
                            if not verify_connection and not self.cancel_multi_send:
                                item = self.muliple_send_interface.multiple_device_config_table.item(to_send.device_row,4)
                                item.setText("Failed Connection")
                            else:
                                self.delete_temp_file(ip_adress=device.IP_adress, username=device.username, password=device.password, port=device.port_number)
                                self.muliple_send_interface.multi_send_status.setText("")
                                self.muliple_send_interface.cancel_multi_send_button.setEnabled(False)
                                self.muliple_send_interface.progressBar.setValue(0)
                                self.muliple_send_interface.upload_multiple_config.setEnabled(True)
                                self.cancel_multi_send = False
                                self.show_config_on_send_mulitple_interface()
                                return 0
            self.muliple_send_interface.multi_send_status.setText("")
            self.muliple_send_interface.cancel_multi_send_button.setEnabled(False)
            self.muliple_send_interface.progressBar.setValue(100)
            self.muliple_send_interface.upload_multiple_config.setEnabled(True)
        else:
            No_device_checked_dialog = QMessageBox()
            No_device_checked_dialog.about(QtWidgets.QWidget(), "Send Multiple", "No device checked !!")

    def delete_folders_from_list(self, folder_content, path):
        list_to_return = []
        for content in range(len(folder_content)):
            if os.path.isfile(os.path.join(path, folder_content[content])):
                list_to_return.append(folder_content[content])
        return list_to_return

    def check_if_device_have_all_configuration_parameteres(self):
        for device in self.device_list:
            advanced_parameters = self.get_advanced_parameters_to_send(device.id)
            if advanced_parameters[0] != "" and advanced_parameters[1] != "":
                verify_existance_of_folder = os.path.isdir(advanced_parameters[0])
                if not verify_existance_of_folder:
                    self.muliple_send_interface.multiple_device_config_table.item(device.id-1, 0).setFlags(Qt.ItemFlag.NoItemFlags)
                    item = self.muliple_send_interface.multiple_device_config_table.item(device.id-1, 4)
                    item.setText("Error (folder) ")
            else:
                self.muliple_send_interface.multiple_device_config_table.item(device.id-1, 0).setFlags(Qt.ItemFlag.NoItemFlags)
                item = self.muliple_send_interface.multiple_device_config_table.item(device.id - 1, 4)
                item.setText("Error (Paths)")

    def filter_list_before_send(self, folder_content, ignore_list):
        for ignore_list_element in range(len(ignore_list)):
            if ignore_list[ignore_list_element] in folder_content:
                folder_content.remove(ignore_list[ignore_list_element])
        return folder_content

    def cancel_multi_send_config(self):
        self.cancel_multi_send = True
        for table_row in range(len(self.multi_send_list)):
            item = self.muliple_send_interface.multiple_device_config_table.item(table_row, 4)
            if item.text() != "ok":
                item.setText("Canceled")

    def delete_temp_file(self, ip_adress, username, password, port):
        delete_temp_file = connect_to_device(ip_adress=ip_adress, username=username, password=password, port=port)
        verify_connection = delete_temp_file.startconnection()
        if verify_connection:
            delete_temp_file.cancel_updating()


if __name__ == '__main__':
    main_user_interface = main_user_interface()
    main_user_interface.start()








import os
import socket
import paramiko
from PyQt5.QtWidgets import QFileDialog
from paramiko.ssh_exception import BadHostKeyException, AuthenticationException, SSHException
from scp import SCPClient, SCPException
from PyQt5 import QtWidgets

class connect_to_device():
    def __init__(self, ip_adress, username, password, port):
        self.device_ip = ip_adress
        self.username = username
        self.password = password
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def startconnection(self):
        try:
            self.ssh.connect(hostname=self.device_ip, username=self.username, password=self.password, port=self.port)
            return True
        except (BadHostKeyException, AuthenticationException,
                SSHException, socket.error) as exception:
            print(exception)
            return False

    def send_files_to_device(self, source_path, list_to_send):
        try:
            for list_element in range(len(list_to_send)):
                destination_path = "/home/pi/temp_file"
                create_directory_command = "mkdir "+destination_path+"/"
                stdin, stdout, stderr = self.ssh.exec_command(create_directory_command)
                srcfile = source_path+"/"+list_to_send[list_element]
                destinationfile = destination_path+"/"+list_to_send[list_element]
                with SCPClient(self.ssh.get_transport()) as scp:
                    scp.put(srcfile, remote_path=destinationfile)
            return True
        except (SCPException, SSHException, BadHostKeyException, AuthenticationException, SSHException, socket.error):
            return False

    def copy_from_tempfile_to_destination(self, destination_path):
        try:
            backup_folder_path = "/home/pi/backup"
            create_backup_folder_command = "mkdir " + backup_folder_path + "/"
            stdin, stdout, stderr = self.ssh.exec_command(create_backup_folder_command)
            copy_from_destination_path_to_backup = "cp -RT " + destination_path + " " + backup_folder_path
            stdin, stdout, stderr = self.ssh.exec_command(copy_from_destination_path_to_backup)
            copy_from_temp_path_to_backup = "cp -RT /home/pi/temp_file " + backup_folder_path
            stdin, stdout, stderr = self.ssh.exec_command(copy_from_temp_path_to_backup)
            delete_old_folder = "rm -r " + destination_path
            stdin, stdout, stderr = self.ssh.exec_command(delete_old_folder)
            command = "mv /home/pi/backup " + destination_path
            stdin, stdout, stderr = self.ssh.exec_command(command)
            if "cannot move" in str(stderr.read()):
                delete_temp_file_if_exist = "rm -r /home/pi/temp_file"
                stdin, stdout, stderr = self.ssh.exec_command(delete_temp_file_if_exist)
                delete_backup_file_if_exist = "rm -r /home/pi/backup"
                stdin, stdout, stderr = self.ssh.exec_command(delete_backup_file_if_exist)
                self.ssh.close()
                return False
            delete_temp_file_if_exist = "rm -r /home/pi/temp_file"
            stdin, stdout, stderr = self.ssh.exec_command(delete_temp_file_if_exist)
            delete_backup_file_if_exist = "rm -r /home/pi/backup"
            stdin, stdout, stderr = self.ssh.exec_command(delete_backup_file_if_exist)
            self.ssh.close()
            return True
        except (SCPException, SSHException, BadHostKeyException, AuthenticationException, SSHException, socket.error):
            return False

    def cancel_updating(self):
        try:
            command = "rm -r /home/pi/temp_file "
            stdin, stdout, stderr = self.ssh.exec_command(command)
            delete_backup_file_if_exist = "rm -r /home/pi/backup"
            stdin, stdout, stderr = self.ssh.exec_command(delete_backup_file_if_exist)
            self.ssh.close()
            return True
        except (BadHostKeyException, AuthenticationException, SSHException, socket.error):
            return False

    def get_files_from_device(self, destination_folder):
        destination_path = destination_folder+"/*.*"
        save_folder = str(QFileDialog.getExistingDirectory(QtWidgets.QWidget(), "Select Directory"))
        while save_folder == "":
            save_folder = str(QFileDialog.getExistingDirectory(QtWidgets.QWidget(), "Select Directory"))
        try:
            with SCPClient(self.ssh.get_transport(), sanitize=lambda x: x) as scp:
                scp.get(destination_path, save_folder)
            return True
        except SCPException:
            return False












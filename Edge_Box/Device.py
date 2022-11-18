import itertools




class Device:
    count = 0

    def __init__(self):
        self.id = self.incr()
        self.password = ""
        self.device_name = ""
        self.username = ""
        self.password = ""
        self.IP_adress = ""
        self.port_number = 0
        self.src_path = ""
        self.dest_path = ""
        self.ignore_list = []

    def set_device_configuration(self, IP_adress, port_number, username, password, device_name):
        self.IP_adress = IP_adress
        self.port_number = port_number
        self.username = username
        self.password = password
        self.device_name = device_name



    @classmethod
    def incr(cls):
        cls.count += 1
        return cls.count


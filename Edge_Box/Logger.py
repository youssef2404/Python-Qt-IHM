import logging
import logging.handlers as handlers
import time
import traceback
from pathlib import Path
import os
import sys


class Logger(logging.Logger):
    def __init__(self, log_file_directory="", log_file_name="main-SF-Log.log", log_level="ERROR", is_printing=False):
        super(Logger, self).__init__(name=log_file_name, level=log_level)
        self.log_file_directory = log_file_directory
        self.log_file_name = log_file_name
        path_delimiter = '/'
        self.log_file_path = path_delimiter.join(
            self.log_file_directory.split(path_delimiter) +
            self.log_file_name.split(path_delimiter))

        self.log_level = log_level.upper()
        self.is_printing = is_printing

        absolute_log_file_directory = "/".join(self.log_file_path.split("/")[:-1])

        if not Path(absolute_log_file_directory).exists():

            os.mkdir(absolute_log_file_directory)

        handler = logging.handlers.RotatingFileHandler(self.log_file_path,
                                                       maxBytes=100*(1024**2),
                                                       backupCount=5,
                                                       encoding='utf-8')

        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        self.addHandler(handler)

        self.setLevel(self.log_level)

    def info_logger(self, message):
        try:
            self.info(message)
            if self.isEnabledFor(20) and self.is_printing:
                print(message)
        except Exception:
            self.error(traceback.format_exc())

    def debug_logger(self, message):
        try:
            self.debug(message)
            if self.isEnabledFor(10) and self.is_printing:
                print(message)
        except Exception:
            self.error(traceback.format_exc())

    def error_logger(self, message):

        try:
            self.error(message)
            if self.isEnabledFor(40) and self.is_printing:
                print(message)

        except Exception:
            self.error(traceback.format_exc())

    def set_log_level_logger(self, log_level: str):
        try:
            self.setLevel(log_level.upper())
            self.log_level = log_level.upper()

        except Exception:
            exception_message = traceback.format_exc()
            print(exception_message)
            self.error(exception_message)
            self.setLevel(self.log_level)


if __name__ == '__main__':
    """testing logger"""

    if getattr(sys, 'frozen', False):
        execution_root = os.path.dirname(sys.executable)
    else:
        execution_root = os.path.dirname(__file__)

    logger = Logger(log_file_directory=execution_root+"/log1", log_file_name="main-SF-Log.log", log_level="INFO"
                    , is_printing=True)
    file_path = Path(logger.log_file_path)
    i = 0
    while True:
        i += 1
        logger.info_logger(f" logging iteration {i} ")
        time.sleep(1)





import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def WaitForElementPresence(self, text):
        wait = WebDriverWait(self.driver, 8).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

    def getLogger(self):
        logNmae = inspect.stack()[1][3]  # displays called file name istesd of this parent calss file
        # logging object created.Name parameter captures name of test that is being run
        logger = logging.getLogger(logNmae)

        # Defining format of log. %()s is c language used to print
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        # File handlier defines the file to be created
        fileHandle = logging.FileHandler('../logfile..log')
        # file handler faormat is set by passing formater object as parameter
        fileHandle.setFormatter(formatter)
        # logger is linked with file to be printed and format using filehandler object
        logger.addHandler(fileHandle)

        # logger level defines from what level logs will be printed debug<info<warning<error<critical. if level is error only error and critical will be printed
        logger.setLevel(logging.DEBUG)
        return logger

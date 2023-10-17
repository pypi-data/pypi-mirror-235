"""
This module handles web automation to monitor court availability.
"""
import logging
import re
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Optional

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .court import Court
from .singleton import SingletonInstance
from .xpaths import *

URL = "https://www.thetennisplay.com"
TIMEOUT = 10


class Driver(SingletonInstance):
    """Singleton instance for handling web automation"""

    def __init__(
        self,
        headless: Optional[bool] = True,
        logger: Optional[logging.Logger] = logging.getLogger(__name__),
    ) -> None:
        """Initialize chromedriver and basic setup"""
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        self.logger = logger

        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        self.logger.info("Initializing chrome...")
        self.driver = webdriver.Chrome(options=options)
        self.logger.info("Heading to the website")
        self.driver.get(URL)

    def login(self, username: str, password: str):
        """Login with given credentials"""

        self.logger.info("Starting to sign in with given credentials")
        self.logger.debug("Waiting the button to login with email to be clickable")
        btn_login_with_email = WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, LOGIN_WITH_EMAIL_BUTTON_XPATH))
        )
        btn_login_with_email.click()
        self.logger.debug("Clicked the button to login with email")
        self.logger.debug("Waiting until login button to be clickable")
        WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, LOGIN_BUTTON_XPATH)))
        self.logger.debug("Login button is now clickable")
        self.logger.debug("Filling out username")
        self.driver.find_element(By.XPATH, USERNAME_INPUT_XPATH).send_keys(username)
        self.logger.debug("Filling out password")
        self.driver.find_element(By.XPATH, PASSWORD_INPUT_XPATH).send_keys(password)
        self.logger.debug("Click Login!")
        self.driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()
        self.logger.info("Waiting until reservation button on sidebar to clickable")
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, RESERVE_BUTTON_XPATH)))
        self.logger.info("Reservation button is now clickable")

    def close_modal(self):
        """Close modal if exists"""
        try:
            self.logger.debug("Finding any opened modal")
            modal_close_btn = WebDriverWait(self.driver, TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, MODAL_CLOSE_BUTTON_XPATH))
            )
            self.logger.info("Modal has been found! Now closing...")
            modal_close_btn.click()
        except TimeoutError:
            self.logger.info("Modal has not been found! Skipping...")

    def pick_court(self, court: Court):
        """Pick court on modal appears"""
        self.logger.info("Heading to the reservation page")
        self.driver.get(URL + "/schedule-booking")
        self.logger.info(f"Picking a court: {court}")
        court_btn = WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, Court.to_xpath(court)))
        )
        court_btn.click()
        self.close_modal()

    def refresh_page(self):
        """Refresh page then close modal"""
        self.driver.refresh()
        self.close_modal()

    def refresh_available_courts(self):
        """Click refresh data button"""
        self.logger.debug("Waiting a refresh button to be clickable")
        refresh_btn = WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, REFRESH_DATA_BUTTON_XPATH))
        )
        self.logger.info("Refreshing data")
        refresh_btn.click()

    def get_current_date(self):
        """Get selected date on form"""
        date = self.driver.find_element(By.CLASS_NAME, "day__month_btn").text
        try:
            day = self.driver.find_element(By.CLASS_NAME, "selected").text
        except NoSuchElementException:
            day = "1"
        return datetime.strptime(date + day, "%Y년 %m월%d")

    def pick_date(self, target: str) -> bool:
        """Navigate date with forms"""
        target_time = datetime.strptime(target, "%Y-%m-%d")
        while diff := (target_time.replace(day=1) - self.get_current_date().replace(day=1)).days != 0:
            WebDriverWait(self.driver, TIMEOUT).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "next" if diff > 0 else "prev"))
            ).click()

        day_btn = self.driver.find_element(By.XPATH, f'//span[text()="{target_time.day}"]')
        classes = day_btn.get_attribute("class")
        if classes is None:
            return False
        clickable = classes.find("disabled") == -1
        if clickable:
            day_btn.click()
        return clickable

    def parse_courts(self) -> Dict[str, List[int]]:
        """Parse available courts"""
        result = defaultdict(list)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        divs = soup.find_all("div")
        for div in divs:
            child_divs = div.find_all("div")
            if len(child_divs) != 2:
                continue
            if re.match(r"^\d+ 시", child_divs[0].text) and child_divs[1].text.startswith("코트 "):
                result[child_divs[1].text].append(int(child_divs[0].text.split()[0]))
        return result

    def __del__(self):
        self.driver.quit()

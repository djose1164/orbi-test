from time import sleep
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from data.login_repository import LoginRepository

from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver, wait) -> None:
        super().__init__(driver, wait)
        self.url = "https://orbi.edu.do/orbi/"
        self.locators = None

    def go_to_login_page(self):
        self.go_to_page(self.url)

    def make_login_pass(self, username, password):
        self.driver.save_screenshot("results/login_intro.png")
        usernameField = self.driver.find_element(By.ID, LoginRepository.USERNAME_FIELD)
        usernameField.send_keys(username)
        
        passwordField = self.driver.find_element(By.ID, LoginRepository.PASSWORD_FIELD)
        passwordField.send_keys(password)

        elem = self.driver.find_element(By.ID, LoginRepository.LOGIN_BTN)
        elem.click()

        self.driver.save_screenshot("results/login_success.png")

    def make_login_fails(self, username: str, password: str):
        self.driver.save_screenshot("results/login_intro.png")
        usernameField = self.driver.find_element(By.ID, LoginRepository.USERNAME_FIELD)
        usernameField.send_keys(username)
        
        passwordField = self.driver.find_element(By.ID, LoginRepository.PASSWORD_FIELD)
        passwordField.send_keys(password)

        elem = self.driver.find_element(By.ID, LoginRepository.LOGIN_BTN)
        elem.click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "mensajeLogin")))

        self.driver.save_screenshot("results/login_fail.png")

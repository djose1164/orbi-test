from time import sleep
from data.academy_repository import AcademyRepository
from data.login_repository import LoginRepository
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class AccountPage(BasePage):
    def __init__(self, driver, wait) -> None:
        super().__init__(driver, wait)
        self.login = LoginPage(driver, wait)
        self.account_url = "https://orbi.edu.do/orbi/caja/planpagoacuerdo/estadoCuenta"
        self.payment_url = "https://orbi.edu.do/orbi/servicio/pagoenlinea"
        self.url = "https://orbi.edu.do/orbi/seguridad/usuario/inicio"

    def go_to_account_page(self):
        self.login.go_to_login_page()
        self.login.make_login_pass(LoginRepository.USERNAME, LoginRepository.PASSWORD)
        # self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "/orbi/seguridad/usuario/inicio")))

        self.go_to_page(self.url)

    def make_a_query_to_balance(self):
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@href='#' and text()='MI MENÚ']")))
        self.wait.until(EC.element_to_be_clickable((By.ID, "drpduRolUsuario")))
        self.driver.find_element(By.XPATH, "//select[@name='drpdRolUsuario']").click()
        opt = self.driver.find_element(
            By.XPATH, "//select[@name='drpdRolUsuario']/option[text()='Estudiante']"
        )
        opt.click()
        sleep(10)
        self.driver.find_element(
            By.XPATH, "//select[@name='drpdRolUsuario']"
        ).send_keys(Keys.ENTER)
        sleep(10)
        self.go_to_page(self.account_url)
        self.driver.save_screenshot("results/account_balance.png")

    def make_a_payment(self):
        self.go_to_page(self.payment_url)
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@value='Pagos Tecnólogo']")
            )
        )
        self.driver.find_element(By.XPATH, "//input[@value='Pagos Tecnólogo']").click()
        sleep(15)
        self.driver.save_screenshot("results/account_payment.png")

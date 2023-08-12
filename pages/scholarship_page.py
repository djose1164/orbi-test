from time import sleep
from data.academy_repository import AcademyRepository
from data.login_repository import LoginRepository
from data.scholarship_repo import ScholarshipLocator
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class SchorlarshipPage(BasePage):
    def __init__(self, driver, wait) -> None:
        super().__init__(driver, wait)
        self.login = LoginPage(driver, wait)
        self.url = "https://orbi.edu.do/orbi/seguridad/usuario/inicio"
        self.scholarship_requests_url = "https://orbi.edu.do/orbi/beca/beca/verSolicitudBeca"

    def go_to_scholarship_page(self):
        self.login.go_to_login_page()
        self.login.make_login_pass(LoginRepository.USERNAME, LoginRepository.PASSWORD)
        self.go_to_page(self.url)

    def make_a_scholarship_request(self):
        self.wait.until(EC.element_to_be_clickable(ScholarshipLocator.MENU_BUTTON))
        self.driver.find_element(*ScholarshipLocator.MENU_BUTTON).click()

        self.wait.until(EC.element_to_be_clickable(ScholarshipLocator.REQUEST_SCHOLARSHIP_BUTTON))
        self.driver.find_element(*ScholarshipLocator.REQUEST_SCHOLARSHIP_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(ScholarshipLocator.SCHOLARSHIP_POPUP))
        self.driver.save_screenshot("results/request_scholarship.png")

    def make_a_see_scholarship_requests(self):
        #self.wait.until(EC.element_to_be_clickable(ScholarshipLocator.SEE_REQUEST_SCHOLARSHIP_BUTTON))
        self.go_to_page(self.scholarship_requests_url)
        self.driver.save_screenshot("results/see_request_scholarship.png")
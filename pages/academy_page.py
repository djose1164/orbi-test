from time import sleep
from data.academy_repository import AcademyRepository
from data.login_repository import LoginRepository
from pages.base_page import BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

class AcademyPage(BasePage):
    def __init__(self, driver, wait) -> None:
        super().__init__(driver, wait)
        self.login = LoginPage(driver, wait)
        self.url = "https://orbi.edu.do/orbi/academico/inscripcion/detalleSeleccion"

    def go_to_query_inscrption(self):
        self.login.go_to_login_page()
        self.login.make_login_pass(LoginRepository.USERNAME, LoginRepository.PASSWORD)
        self.go_to_page(self.url)

    def make_an_inscription_listing(self):
        self.driver.save_screenshot("results/academy_listing.png")
    
    def make_an_exportation_to_pdf(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "titulo")))
        self.driver.save_screenshot("results/academy_intro.png")
        export_btn = self.driver.find_element(By.CLASS_NAME, AcademyRepository.EXPORT_BUTTON)
        export_btn.click()

        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        
        self.driver.save_screenshot("results/academy_export.png")

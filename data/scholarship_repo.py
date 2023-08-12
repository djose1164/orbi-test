from selenium.webdriver.common.by import By

class ScholarshipLocator:
    SCHOLARSHIP_BUTTON = "//li[@id='mBeca']/a[@class='fcGris']"
    REQUEST_SCHOLARSHIP_BUTTON = (By.XPATH, "//li[a[text() = 'Solicitud Beca ']]")
    MENU_BUTTON = (By.XPATH, "//li[@class='selected']/a[text() = 'MI MENÚ ']")
    SEE_REQUEST_SCHOLARSHIP_BUTTON = (By.XPATH, "//li[a[contains(text(), 'Ver Solicitud Beca')]]")
    SCHOLARSHIP_POPUP = (By.XPATH, "//div[@id='window_0']")
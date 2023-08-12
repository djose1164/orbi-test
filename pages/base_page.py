class BasePage:
    def __init__(self, driver, wait=None) -> None:
        self.driver = driver
        self.wait = wait

    def go_to_page(self, url: str):
        self.driver.get(url)

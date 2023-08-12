from time import sleep
import pytest

from selenium.webdriver.common.by import By

from data.login_repository import LoginRepository
from pages.login_page import LoginPage
from tests.base_test import BaseTest

@pytest.mark.skip()
class TestLoginPage(BaseTest):
    @pytest.fixture
    def load_page(self):
        self.page = LoginPage(self.driver, self.wait)
        self.page.go_to_login_page()

    def test_valid_credentials(self, load_page):
        self.page.make_login_pass(LoginRepository.USERNAME, LoginRepository.PASSWORD)

    def test_invalid_credentials(self, load_page):
        self.page.make_login_fails(
            LoginRepository.INVALID_USERNAME, LoginRepository.PASSWORD
        )

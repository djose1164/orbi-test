import pytest
from pages.account_page import AccountPage


from tests.base_test import BaseTest

@pytest.mark.skip()
class TestAccountPage(BaseTest):
    @pytest.fixture
    def account_login_fixture(self):
        self.page = AccountPage(self.driver, self.wait)
        self.page.go_to_account_page()

    
    def test_query_to_balance(self, account_login_fixture):
        self.page.make_a_query_to_balance()

    def test_pay_button(self, account_login_fixture):
        self.page.make_a_payment()

import pytest
from pages.account_page import AccountPage

from tests.base_test import BaseTest

@pytest.mark.skip()
class TestAcademyPage(BaseTest):
    @pytest.fixture
    def login_fixture(self):
        self.page = AccountPage(self.driver, self.wait)
        self.page.go_to_account_page()

    def test_inscription_listing(self, login_fixture):
        self.page.make_an_inscription_listing()

    def test_export_inscription(self, login_fixture):
        self.page.make_an_exportation_to_pdf()

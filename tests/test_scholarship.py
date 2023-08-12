import pytest
from pages.account_page import AccountPage
from pages.scholarship_page import SchorlarshipPage


from tests.base_test import BaseTest


class TestScholarshipPage(BaseTest):
    @pytest.fixture
    def scholarship_login_fixture(self):
        self.page = SchorlarshipPage(self.driver, self.wait)
        self.page.go_to_scholarship_page()

    
    def test_schorlarship_request(self, scholarship_login_fixture):
        self.page.make_a_scholarship_request()
    
    @pytest.mark.skip()
    def test_see_scholarship_requests(self, scholarship_login_fixture):
        self.page.make_a_see_scholarship_requests()


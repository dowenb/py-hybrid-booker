# tests_phb.py
from assertpy import assert_that
from base_test_case import BaseTestCase
import rbp_sdk as booker
from parameterized import parameterized

class HybridTestCase(BaseTestCase):

    def test_room_booking(self):
        self.open(booker._url('/'))
        for i in range(4):
            self.click('#next')
        self.click('#closeModal')
        self.send_keys('#username', 'admin')
        self.send_keys('#password', 'password')
        self.click('#doLogin')
        self.find_element('#roomNumber101')
        self.find_element('#roomNumber201')
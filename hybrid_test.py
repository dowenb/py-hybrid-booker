# tests_phb.py
from assertpy import assert_that
from base_test_case import BaseTestCase
import rbp_sdk as booker

class HybridTestCase(BaseTestCase):

    def test_room_booking(self):
        #Testing the API has setup the pre-requisite data correctly
        rooms = booker.get_rooms()
        assert_that(rooms).is_not_empty()
        for room in rooms:
            roomNumber = room['roomNumber']
            assert_that(roomNumber).is_greater_than(199)
            assert_that(roomNumber).is_less_than(210)

        self.open(booker._url('/'))
        for i in range(4):
            self.click('#next')
        self.click('#closeModal')
        self.send_keys('#username', 'admin')
        self.send_keys('#password', 'password')
        self.click('#doLogin')
        for i in range (200, 209):
            value = '#roomNumber' + str(i)
            self.assert_element(value)
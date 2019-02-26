from seleniumbase import BaseCase
import rbp_sdk as booker

class BaseTestCase(BaseCase):

    bookings = {}
    
    def setupTestBookings(self):
        testdata_bookings = {}
        for i in range(10):
            testdata_bookings['booking'+str(i)] = booker.create_booking(
                booker.generate_booking()
            ).json()
        return testdata_bookings

    def remove_all_rooms(self):
        rooms = booker.get_rooms()
        if rooms:
            for room in rooms:
                id = str(room['roomid'])
                booker.remove_room(id)

    def setUp(self):
        super(BaseTestCase, self).setUp()
        # Add custom setUp code for your tests AFTER the super().setUp()
        self.remove_all_rooms()
        global bookings
        bookings = self.setupTestBookings() #setup test data

    def tearDown(self):
        # Add custom tearDown code for your tests BEFORE the super().tearDown()
        self.remove_all_rooms()
        super(BaseTestCase, self).tearDown()
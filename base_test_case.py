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

    def tearDownBookings(self):
        global bookings
        try:
            for booking in bookings:
                booker.remove_booking(booking['id'])
        except:
            pass

    def setUp(self):
        super(BaseTestCase, self).setUp()
        # Add custom setUp code for your tests AFTER the super().setUp()
        global bookings
        bookings = self.setupTestBookings() #setup test data

    def tearDown(self):
        # Add custom tearDown code for your tests BEFORE the super().tearDown()
        self.tearDownBookings()
        super(BaseTestCase, self).tearDown()
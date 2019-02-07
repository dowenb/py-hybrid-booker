from seleniumbase import BaseCase
import rbp_sdk as booker

class BaseTestCase(BaseCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        # Add custom setUp code for your tests AFTER the super().setUp()

    def tearDown(self):
        # Add custom tearDown code for your tests BEFORE the super().tearDown()
        super(BaseTestCase, self).tearDown()

    def setupTestBookings(self):
        testdata_bookings = {}
        for i in range(10):
            testdata_bookings['booking'+str(i)] = booker.create_booking(
                booker.generate_booking()
            ).json()
        return testdata_bookings
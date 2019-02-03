#tests_phb.py
from assertpy import assert_that
import rbp_sdk as rb
print(
    rb.get_bookings(rb.get_auth, 1).text
)
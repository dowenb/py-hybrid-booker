#tests_phb.py
from assertpy import assert_that
import rbp_sdk as booker
print(
    booker.create_booking(
        booker.get_auth(), 
        booker.generate_booking()
    ).json()
)
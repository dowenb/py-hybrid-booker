# phb.py Py Hybrid Booker common functions
import requests


def _url(path):
    return(
        'https://automationintesting.online/' + path
    )


def get_auth(username='admin', password='password'):
    return(
        requests.post(_url('/auth/login'),
                      json={
            "username": username,
            "password": password
        }
        ).json()['token']
    )


def get_bookings(auth_token, roomid):
    return(
        requests.get(
            _url('/booking/'),
            params={"roomid": roomid}
        )
    )


def create_booking(auth_token, booking):
    return(
        requests.post(
            _url('/booking/'),
            json=booking,
            cookies={
                "token" : auth_token
            }
        )
    )

def create_room(auth_token, room):
    return(
        requests.post(
            _url('/room/'),
            json=room,
            cookies={
                "token" : auth_token
            }
        )
    )


def generate_booking():
    room = create_room(get_auth(), generate_room())
    roomid = room.json()['roomid']
    return(
        {"roomid": roomid,
        "firstname": "James",
        "lastname": "Bond",
        "totalprice": "100",
        "depositpaid": "true",
        "bookingdates": {
            "checkin": "2019-02-03", 
            "checkout": "2019-02-04"
            }
        }
    )
    # TODO make random
    # TODO Ensure to use a real roomid

def generate_room():
    return(
        {
            "roomNumber": "102",
            "type": "Single",
            "beds": "1",
            "accessible": "false",
            "details": "fridge"
        }
    )
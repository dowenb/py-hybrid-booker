# phb.py Py Hybrid Booker common functions
import requests, random

roomNumber = 200

def _url(path):
    return(
        'https://automationintesting.online' + path
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

def get_bookings(roomid, auth_token = get_auth()):
    return(
        requests.get(
            _url('/booking/'),
            params={"roomid": roomid}
        )
    )

def create_booking(booking, auth_token = get_auth()):
    return(
        requests.post(
            _url('/booking/'),
            json=booking,
            cookies={
                "token" : auth_token
            }
        )
    )

def create_room(room, auth_token = get_auth()):
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
    room = create_room(generate_room())
    roomid = room.json()['roomid']
    firstname = random.choice(['Jane', 'James', 'Dave', 'Sally', 'Ben', 'Nick'])
    lastname = random.choice(['Smith', 'Jones', 'Tylor', 'Tinker'])
    totalprice = random.choice(['50', '150', '200', '225', '350'])
    depositpaid = random.choice(['true', 'false'])
    checkin = random.choice(['2019-01-01', '2019-01-05', '2019-01-07', '2019-01-11'])
    checkout = random.choice(['2019-02-01', '2019-02-05', '2019-02-07', '2019-02-11'])
    
    return(
        {"roomid": roomid,
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin, 
            "checkout": checkout
            }
        }
    )

def generate_room():
    global roomNumber
    roomNumber += 1
    type = random.choice(['Single', 'Double', 'King', 'Super King', 'Queen'])
    beds = random.choice(['1', '2', '3', '4'])
    accessible = random.choice(['true', 'false'])
    details = random.choice(['Fridge', 'Netflix', 'Free WiFi'])

    return(
        {
            "roomNumber": roomNumber,
            "type": type,
            "beds": beds,
            "accessible": accessible,
            "details": details
        }
    )

def get_rooms():
    return(
        requests.get(_url('/room')).json()
    )
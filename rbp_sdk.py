#phb.py Py Hybrid Booker common functions
import requests

def _url(path):
    return(
        'https://automationintesting.online/' + path
    )

def get_auth(username = 'admin', password = 'password'):
    return(
        requests.post(_url('/auth/login'),
        json={
            "username" : username,
            "password" : password
            }
        ).json()['token']
    )

def get_bookings(auth_token, roomid):
    return(
        requests.get(
            _url('/booking/'),
            params={"roomid" : roomid}
        )
    )
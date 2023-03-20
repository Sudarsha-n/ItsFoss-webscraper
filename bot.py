import requests

def bot_send(message):
    url = "channel-link"
    auth = {
        'authorization' : 'authorization-token'
    }
    message = {
        'content' : message
    }
    requests.post(url, headers=auth, data=message)
import send
from notify_user import notify_user

while True:
    c = send.send()
    if c != 0:
        notify_user(c)
        

